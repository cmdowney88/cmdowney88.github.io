"""
Build LaTeX CV from cv_data.yaml.

Usage:
    python build_cv.py                          # default: exclude internal-informal
    python build_cv.py --exclude-tags undergrad  # also exclude undergrad items
    python build_cv.py --exclude-tags none       # include everything
    python build_cv.py --output my_cv.tex        # custom output filename
"""

import argparse
import re
from collections import OrderedDict
from pathlib import Path

import yaml


# ============================================================
# LaTeX helpers
# ============================================================

LATEX_SPECIAL = {
    "&": r"\&",
    "%": r"\%",
    "#": r"\#",
    "_": r"\_",
    "~": r"\textasciitilde{}",
}

# Characters we should NOT escape when they appear inside LaTeX commands
LATEX_CMD_PATTERN = re.compile(r"\\[a-zA-Z]+\{[^}]*\}")


def tex_escape(text: str) -> str:
    """Escape special LaTeX characters, but leave backslash commands alone."""
    if not text:
        return ""
    text = str(text)
    # Protect existing LaTeX commands by replacing them with placeholders
    commands = []
    def _save_cmd(match):
        commands.append(match.group(0))
        return f"__CMD{len(commands) - 1}__"
    protected = LATEX_CMD_PATTERN.sub(_save_cmd, text)

    for char, replacement in LATEX_SPECIAL.items():
        protected = protected.replace(char, replacement)

    # Restore commands
    for i, cmd in enumerate(commands):
        protected = protected.replace(f"__CMD{i}__", cmd)
    return protected


def bold_name(authors: str, name: str = "C.M. Downey") -> str:
    """Bold the author's name in an author string."""
    return authors.replace(name, rf"\textbf{{{name}}}")


def make_href(url: str, text: str) -> str:
    return rf"\href{{{url}}}{{{text}}}"


def extract_year(date_str: str) -> str:
    """Pull the year from a date string like 'November 2024' or '2025'."""
    match = re.search(r"\b((?:19|20)\d{2})\b", str(date_str))
    return match.group(1) if match else str(date_str)


def date_to_short(date_str: str) -> str:
    """Convert 'September 2019 - June 2020' to '2019--2020', etc."""
    date_str = str(date_str)
    if " - " in date_str:
        parts = date_str.split(" - ")
        left_raw = parts[0].strip()
        right_raw = parts[1].strip()

        if right_raw.lower() == "present":
            left_year = extract_year(left_raw)
            return f"{left_year}--present"

        left_year = extract_year(left_raw)
        right_year = extract_year(right_raw)

        # If one side has no year (e.g. "January - March 2024"),
        # both months are in the same year
        if left_year == left_raw and right_year != right_raw:
            return right_year
        if right_year == right_raw and left_year != left_raw:
            return left_year

        if left_year == right_year:
            return left_year
        return f"{left_year}--{right_year}"
    return extract_year(date_str)


def should_include(item: dict, exclude_tags: set[str]) -> bool:
    """Check whether an item should be included given excluded tags."""
    if not exclude_tags:
        return True
    item_tags = set(item.get("tags", []))
    return not item_tags.intersection(exclude_tags)


# ============================================================
# Semester sorting for teaching
# ============================================================

SEMESTER_ORDER = {"winter": 0, "spring": 1, "summer": 2, "fall": 3}


def semester_sort_key(semester: str) -> tuple[int, int]:
    """Return a sortable key for 'Fall 2024' style strings (descending)."""
    parts = semester.strip().split()
    season = parts[0].lower()
    year = int(parts[1])
    return (-year, -SEMESTER_ORDER.get(season, 0))


def build_semester_rows(
    courses: list[dict],
    role_type: str,
) -> list[dict]:
    """
    Invert course-centric YAML into semester-centric rows.
    Returns list of {semester, course, institution, note} dicts, sorted.
    """
    rows = []
    for course_entry in courses:
        course_name = course_entry["course"]
        institution = course_entry.get("institution", "")
        # Shorten institution names for the tabular
        inst_short = institution.replace("University of Washington", "UW").replace(
            "University of Rochester", "UR"
        )
        details = course_entry.get("details", [])
        role = course_entry.get("role", "")
        note = ""
        if details:
            note = details[0]
        elif role:
            note = role.lower()

        for semester in course_entry.get("semesters", []):
            rows.append(
                {
                    "semester": semester,
                    "course": f"{inst_short} {course_name}",
                    "note": note,
                }
            )

    rows.sort(key=lambda r: semester_sort_key(r["semester"]))
    return rows


def render_teaching_tabular(rows: list[dict]) -> str:
    """Render semester-grouped teaching rows as a LaTeX tabular."""
    lines = [
        r"\begin{tabular}{@{}p{6.5em}p{\dimexpr\textwidth-7.5em\relax}@{}}"
    ]
    prev_semester = None
    for i, row in enumerate(rows):
        semester_label = row["semester"] if row["semester"] != prev_semester else ""
        # Pad semester column to align nicely in source
        semester_col = semester_label.ljust(11) if semester_label else " " * 11

        course_text = row["course"]
        if row["note"]:
            note_text = tex_escape(row["note"])
            # Put note in italics on same line in parens, or below
            course_text += rf" \textit{{({note_text})}}"

        line = f"    {semester_col} & {course_text} \\\\"
        # Add vertical spacing between semester groups
        if semester_label and prev_semester is not None:
            # Replace the \\ on the previous line with \\[0.4em]
            lines[-1] = lines[-1].rstrip("\\\\") + "\\\\[0.4em]"
        lines.append(line)

        prev_semester = row["semester"]

    lines.append(r"\end{tabular}")
    return "\n".join(lines)


# ============================================================
# Guest lecture helpers
# ============================================================

def _format_guest_lecture_detail(entry: dict) -> str:
    """Build the detail line from structured guest lecture fields."""
    parts = []
    if "course" in entry:
        parts.append(entry["course"])
    if "institution" in entry:
        parts.append(entry["institution"])
    if "instructor" in entry:
        parts.append(f"instructed by {entry['instructor']}")
    return ", ".join(parts)


def build_guest_lecture_rows(lectures: list[dict]) -> list[dict]:
    """Flatten guest lectures into date-sorted rows."""
    rows = []
    for lecture in lectures:
        title = lecture["title"]
        if "instances" in lecture:
            for inst in lecture["instances"]:
                rows.append(
                    {
                        "date": inst["date"],
                        "title": title,
                        "detail": _format_guest_lecture_detail(inst),
                    }
                )
        elif "dates" in lecture:
            detail = _format_guest_lecture_detail(lecture)
            for date in lecture["dates"]:
                rows.append({"date": date, "title": title, "detail": detail})
        else:
            rows.append(
                {
                    "date": lecture.get("date", ""),
                    "title": title,
                    "detail": _format_guest_lecture_detail(lecture),
                }
            )
    # Sort by date descending (extract year + month)
    rows.sort(key=lambda r: _date_sort_key(str(r["date"])), reverse=True)
    return rows


def _talk_sort_key(talk: dict) -> tuple[int, int]:
    """Sort key for a talk entry. Uses most recent instance date for multi-instance."""
    if "instances" in talk:
        return max(_date_sort_key(str(inst["date"])) for inst in talk["instances"])
    return _date_sort_key(str(talk.get("date", "")))


def _date_sort_key(date_str: str) -> tuple[int, int]:
    """Parse 'May 22 2024' or 'January 27 2020' into (year, month) for sorting."""
    months = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    }
    parts = date_str.strip().split()
    year = int(parts[-1])
    month = months.get(parts[0][:3].lower(), 0) if len(parts) > 1 else 0
    return (year, month)


def format_guest_lecture_date(date_str: str) -> str:
    """Shorten 'May 22 2024' to 'May 2024', 'January 27 2020' to 'Jan 2020'."""
    short_months = {
        "january": "Jan", "february": "Feb", "march": "Mar", "april": "Apr",
        "may": "May", "june": "Jun", "july": "Jul", "august": "Aug",
        "september": "Sep", "october": "Oct", "november": "Nov", "december": "Dec",
    }
    parts = str(date_str).strip().split()
    if len(parts) >= 2:
        month_word = parts[0].lower()
        month_short = short_months.get(month_word, parts[0])
        year = parts[-1]
        return f"{month_short} {year}"
    return str(date_str)


def render_guest_lectures_tabular(rows: list[dict]) -> str:
    """Render guest lectures as a LaTeX tabular."""
    lines = [
        r"\begin{tabular}{@{}p{6.5em}p{\dimexpr\textwidth-7.5em\relax}@{}}"
    ]
    for i, row in enumerate(rows):
        date_label = format_guest_lecture_date(row["date"]).ljust(11)
        title_line = f"    {date_label} & ``{tex_escape(row['title'])}'' \\\\"
        lines.append(title_line)
        if row["detail"]:
            detail_line = (
                f"    {' ' * 11} & \\hspace{{1em}}\\textit{{{tex_escape(row['detail'])}}} \\\\"
            )
            lines.append(detail_line)
        # Spacing between entries
        if i < len(rows) - 1:
            lines[-1] = lines[-1].rstrip("\\\\") + "\\\\[0.4em]"

    lines.append(r"\end{tabular}")
    return "\n".join(lines)


# ============================================================
# Section renderers
# ============================================================

def render_header(data: dict) -> str:
    name = data["name"]
    title = data["title"]
    departments = data.get("departments", [])
    affiliation = data["affiliation"]
    email = data["email"]
    links = data.get("links", {})
    labels = data.get("link_labels", {})

    dept_line = "~~$\\cdot$~~".join(
        [f"Department of {departments[0]}"]
        + [
            f"Goergen Institute for Data Science \\& AI"
            if d == "Data Science"
            else f"Department of {d}"
            for d in departments[1:]
        ]
    )

    link_parts = []
    for key in links:
        url = links[key]
        label = labels.get(key, url)
        link_parts.append(make_href(url, label))
    link_line = "~~$\\cdot$~~%\n    ".join(link_parts)

    return rf"""% === Header ===
\begin{{center}}
    {{\LARGE\bfseries\scshape {name}}}\\[0.4em]
    {title}\\
    {dept_line}\\
    {affiliation}\\[0.2em]
    {make_href(f'mailto:{email}', rf'\nolinkurl{{{email}}}')}\\[0.2em]
    {link_line}
\end{{center}}"""


def render_education(data: dict) -> str:
    lines = ["% === Education ===", r"\section{Education}", r"\begin{cvlist}"]
    for entry in data["education"]:
        dates = date_to_short(entry["dates"])
        institution = tex_escape(entry["institution"])
        lines.append(f"    \\cventry{{{institution}}}{{{dates}}}")

        # Parse degree into bold level + field
        degree_str = entry["degree"]
        # Split on first space after the degree level abbreviation
        for prefix in ["Ph.D.", "B.S.", "M.S.", "B.A.", "M.A."]:
            if degree_str.startswith(prefix):
                field = degree_str[len(prefix):].strip()
                lines.append(
                    f"    \\cvdetail{{\\textbf{{{prefix}}} {tex_escape(field)}}}"
                )
                break
        else:
            lines.append(f"    \\cvdetail{{\\textbf{{{tex_escape(degree_str)}}}}}")

        for detail in entry.get("details", []):
            lines.append(f"    \\cvdetail{{{tex_escape(detail)}}}")
        lines.append("")

    # Remove trailing blank line
    if lines[-1] == "":
        lines.pop()
    lines.append(r"\end{cvlist}")
    return "\n".join(lines)


SUMMER_MONTHS = {"june", "july", "august", "september"}


def employment_date_display(date_str: str) -> str:
    """
    Convert employment date ranges to display form.
    'June - September 2022' -> 'Summer 2022'
    'July 2024 - Present' -> '2024--present'
    'September 2018 - June 2024' -> '2018--2024'
    """
    date_str = str(date_str)
    if " - " not in date_str:
        return extract_year(date_str)

    left_raw, right_raw = [s.strip() for s in date_str.split(" - ")]

    # Check for "Month - Month Year" pattern (internships)
    left_parts = left_raw.split()
    right_parts = right_raw.split()
    if (
        len(left_parts) == 1
        and len(right_parts) == 2
        and left_parts[0].lower() in SUMMER_MONTHS
        and right_parts[0].lower() in SUMMER_MONTHS
    ):
        return f"Summer {right_parts[1]}"

    return date_to_short(date_str)


def render_employment(data: dict) -> str:
    lines = ["% === Employment ===", r"\section{Employment}", r"\begin{cvlist}"]
    for entry in data["employment"]:
        # Extract short employer name (before parenthetical or "Department")
        employer_raw = entry["employer"]
        employer_short = employer_raw.split(" (")[0].split(" Department")[0]
        dates = employment_date_display(entry["dates"])
        position = entry["position"]

        # Build detail line with position and any parenthetical from employer
        detail = position
        paren_match = re.search(r"\(([^)]+)\)", employer_raw)
        if paren_match:
            detail += f", {paren_match.group(1)}"

        lines.append(f"    \\cventry{{{tex_escape(employer_short)}}}{{{dates}}}")
        lines.append(f"    \\cvdetail{{{tex_escape(detail)}}}")
        lines.append("")

    if lines[-1] == "":
        lines.pop()
    lines.append(r"\end{cvlist}")
    return "\n".join(lines)


def render_honors(data: dict, exclude_tags: set[str]) -> str:
    lines = [
        "% === Honors & Awards ===",
        r"\section{Honors \& Awards}",
        r"\begin{cvlist}",
    ]
    for entry in data["honors"]:
        if not should_include(entry, exclude_tags):
            continue
        title = tex_escape(entry["title"])
        dates = date_to_short(entry["dates"])
        source = tex_escape(entry.get("source", ""))

        lines.append(f"    \\cventry{{{title}}}{{{dates}}}")
        if source:
            detail_parts = [source]
            details = entry.get("details", [])
            # Append first detail to source line if it's short context
            for d in details:
                detail_parts.append(tex_escape(d))
            lines.append(f"    \\cvdetail{{{'; '.join(detail_parts)}}}")
        lines.append("")

    if lines[-1] == "":
        lines.pop()
    lines.append(r"\end{cvlist}")
    return "\n".join(lines)


def render_publication(pub: dict) -> str:
    """Render a single publication entry."""
    year = pub["year"]
    title = tex_escape(pub["title"])
    authors = bold_name(pub["authors"])
    venue = tex_escape(pub["venue"])
    status = pub.get("status", "")
    note = pub.get("note", "")
    links = pub.get("links", {})

    # Link the title to the first available URL
    # Priority: acl_anthology > repository > openreview > arxiv
    link_url = None
    for key in ["acl_anthology", "repository", "openreview", "arxiv"]:
        if key in links:
            link_url = links[key]
            break
    if link_url:
        title_display = make_href(link_url, title)
    else:
        title_display = title

    # Add "To appear:" prefix if applicable
    if status == "to appear":
        venue = f"To appear: {venue}"

    line = f"    \\pub{{{year}}}{{{title_display}}}{{{authors}}}{{" f"{venue}}}"

    if note:
        line += f"\n    \\\\ \\hspace*{{0.5em}}\\textbf{{{tex_escape(note)}}}"

    return line


def render_publications(data: dict) -> str:
    pubs = data["publications"]
    lines = ["% === Publications ===", r"\section{Publications}"]

    # Peer-reviewed
    if pubs.get("peer_reviewed"):
        lines.extend([r"\subsection{Peer-Reviewed}", r"\begin{cvlist}"])
        for pub in pubs["peer_reviewed"]:
            lines.append(render_publication(pub))
            lines.append("")
        if lines[-1] == "":
            lines.pop()
        lines.append(r"\end{cvlist}")

    # Dissertation / Other
    if pubs.get("other"):
        lines.extend(["", r"\subsection{Dissertation}", r"\begin{cvlist}"])
        for pub in pubs["other"]:
            lines.append(render_publication(pub))
        lines.append(r"\end{cvlist}")

    # Pre-prints
    if pubs.get("preprints"):
        lines.extend(["", r"\subsection{Pre-prints}", r"\begin{cvlist}"])
        for pub in pubs["preprints"]:
            lines.append(render_publication(pub))
        lines.append(r"\end{cvlist}")

    return "\n".join(lines)


def render_talks(data: dict, exclude_tags: set[str]) -> str:
    talks = data["talks"]
    lines = ["% === Talks ===", r"\section{Talks}"]

    # Refereed
    if talks.get("refereed"):
        lines.extend([r"\subsection{Refereed}", r"\begin{cvlist}"])
        for talk in talks["refereed"]:
            if not should_include(talk, exclude_tags):
                continue
            title = tex_escape(talk["title"])
            year = extract_year(talk["date"])
            venue = tex_escape(talk["venue"])
            fmt = talk.get("format", "")
            venue_display = f"{venue} ({fmt})" if fmt else venue
            lines.append(f"    \\cventry{{{title}}}{{{year}}}")
            lines.append(f"    \\cvdetail{{{venue_display}}}")
            lines.append("")
        if lines[-1] == "":
            lines.pop()
        lines.append(r"\end{cvlist}")

    # Invited (sorted by most recent date, descending)
    if talks.get("invited"):
        invited = [t for t in talks["invited"] if should_include(t, exclude_tags)]
        invited.sort(key=_talk_sort_key, reverse=True)
        lines.extend(["", r"\subsection{Invited}", r"\begin{cvlist}"])
        for talk in invited:
            title = tex_escape(talk["title"])
            talk_links = talk.get("links", {})
            if "event" in talk_links:
                title = make_href(talk_links["event"], title)

            if "instances" in talk:
                # Multi-instance talk: title with sublist of venues
                lines.append(f"    \\cventry{{{title}}}{{}}")
                lines.append(r"    \begin{sublist}")
                for inst in talk["instances"]:
                    venue = tex_escape(inst["venue"])
                    year = extract_year(inst["date"])
                    lines.append(
                        f"        \\item {venue} \\hfill {year}"
                    )
                lines.append(r"    \end{sublist}")
            else:
                year = extract_year(talk["date"])
                venue = tex_escape(talk.get("venue", ""))
                lines.append(f"    \\cventry{{{title}}}{{{year}}}")
                if venue:
                    lines.append(f"    \\cvdetail{{{venue}}}")
            lines.append("")
        if lines[-1] == "":
            lines.pop()
        lines.append(r"\end{cvlist}")

    return "\n".join(lines)


def render_teaching(data: dict) -> str:
    teaching = data["teaching"]
    lines = [
        "% === Teaching ===",
        "% Teaching uses a semester-grouped layout: date on the left, courses on the right.",
        "% Multiple courses in the same semester share a single date label.",
        r"\section{Teaching}",
    ]

    # Instructor
    if teaching.get("instructor"):
        instructor_rows = build_semester_rows(teaching["instructor"], "instructor")
        lines.append("")
        lines.append(r"\subsection{Instructor}")
        lines.append(render_teaching_tabular(instructor_rows))

    # Teaching Assistant
    if teaching.get("teaching_assistant"):
        ta_rows = build_semester_rows(teaching["teaching_assistant"], "ta")
        lines.append("")
        lines.append(r"\subsection{Teaching Assistant}")
        lines.append(render_teaching_tabular(ta_rows))

    # Guest Lectures
    if teaching.get("guest_lectures"):
        gl_rows = build_guest_lecture_rows(teaching["guest_lectures"])
        lines.append("")
        lines.append(r"\subsection{Guest Lectures}")
        lines.append(render_guest_lectures_tabular(gl_rows))

    return "\n".join(lines)


def render_service(data: dict, exclude_tags: set[str]) -> str:
    lines = ["% === Service ===", r"\section{Service}", r"\begin{cvlist}"]

    # Group consecutive same-title entries (like AmericasNLP across years)
    service_items = [s for s in data["service"] if should_include(s, exclude_tags)]
    merged = merge_service_entries(service_items)

    for entry in merged:
        title = tex_escape(entry["title"])
        dates = entry["dates_display"]
        role = tex_escape(entry.get("role", ""))
        lines.append(f"    \\cventry{{{title}}}{{{dates}}}")
        detail_parts = [role] if role else []
        for d in entry.get("details", []):
            detail_parts.append(tex_escape(d))
        if detail_parts:
            lines.append(f"    \\cvdetail{{{'; '.join(detail_parts)}}}")
        lines.append("")

    if lines[-1] == "":
        lines.pop()
    lines.append(r"\end{cvlist}")
    return "\n".join(lines)


def merge_service_entries(items: list[dict]) -> list[dict]:
    """Merge consecutive service entries with the same title and role into one."""
    merged = []
    for item in items:
        title = item["title"]
        role = item.get("role", "")
        dates_str = str(item["dates"])

        if (
            merged
            and merged[-1]["title"] == title
            and merged[-1].get("role", "") == role
        ):
            merged[-1]["dates_display"] += f", {dates_str}"
        else:
            merged.append(
                {
                    **item,
                    "dates_display": dates_str,
                }
            )
    return merged


# ============================================================
# Preamble (static LaTeX header)
# ============================================================

PREAMBLE = r"""% Auto-generated from cv_data.yaml by build_cv.py
% Do not edit this file directly; edit cv_data.yaml instead.

\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage{libertinus}
\usepackage[margin=0.85in]{geometry}
\usepackage[dvipsnames]{xcolor}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{etoolbox}
\usepackage{titlesec}

% === Color configuration ===
% Change this to add color to section headers (e.g., MidnightBlue, NavyBlue)
\newcommand{\sectioncolor}{black}

% === Hyperlink styling ===
\hypersetup{
    colorlinks=true,
    linkcolor=MidnightBlue,
    urlcolor=MidnightBlue,
}

% === Section header formatting ===
\titleformat{\section}
    {\large\bfseries\scshape\color{\sectioncolor}}
    {}{0em}{}
    [\vspace{-0.6em}\textcolor{\sectioncolor}{\rule{\textwidth}{0.4pt}}]
\titlespacing{\section}{0pt}{1.2em}{0.5em}

\titleformat{\subsection}
    {\normalsize\bfseries}
    {}{0em}{}
\titlespacing{\subsection}{0pt}{0.8em}{0.3em}

% === List formatting ===
\newlist{cvlist}{description}{1}
\setlist[cvlist]{
    labelwidth=0pt,
    labelsep=0pt,
    leftmargin=0pt,
    parsep=0.4em,
    itemsep=0.6em,
}
% Prevent page breaks within a single cvlist item
\BeforeBeginEnvironment{cvlist}{\interlinepenalty=10000}
\AfterEndEnvironment{cvlist}{\interlinepenalty=0}

\newlist{sublist}{itemize}{1}
\setlist[sublist]{
    label={},
    leftmargin=1em,
    itemsep=0pt,
    parsep=0pt,
    topsep=0.2em,
}

% === Entry commands ===
\newcommand{\cventry}[2]{%
    \item[\phantom{.}] \parbox[t]{\dimexpr\textwidth-6em\relax}{\textbf{#1}} \hfill #2%
}
\newcommand{\cvdetail}[1]{%
    \\ \hspace*{0.5em}#1%
}
\newcommand{\pub}[4]{%
    \item[\phantom{.}] #1.\enspace #2.\enspace #3.\enspace \textit{#4}.%
}

% === Suppress page numbers ===
\pagestyle{empty}
"""


# ============================================================
# Main
# ============================================================

def build_cv(yaml_path: str, exclude_tags: set[str]) -> str:
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    sections = [
        PREAMBLE,
        r"\begin{document}",
        "",
        render_header(data),
        "",
        render_education(data),
        "",
        render_employment(data),
        "",
        render_honors(data, exclude_tags),
        "",
        render_publications(data),
        "",
        render_talks(data, exclude_tags),
        "",
        render_teaching(data),
        "",
        render_service(data, exclude_tags),
        "",
        r"\end{document}",
        "",
    ]
    return "\n".join(sections)


def main():
    parser = argparse.ArgumentParser(description="Build LaTeX CV from YAML data")
    parser.add_argument(
        "--exclude-tags",
        nargs="*",
        default=["internal-informal", "archive"],
        help=(
            "Tags to exclude from output. "
            "Default: internal-informal. "
            "Use 'none' to include everything."
        ),
    )
    parser.add_argument(
        "--output",
        default="cv_generated.tex",
        help="Output .tex filename (default: cv_generated.tex)",
    )
    parser.add_argument(
        "--data",
        default="cv_data.yaml",
        help="Path to YAML data file (default: cv_data.yaml)",
    )
    args = parser.parse_args()

    if args.exclude_tags == ["none"]:
        exclude_tags = set()
    else:
        exclude_tags = set(args.exclude_tags)

    tex_content = build_cv(args.data, exclude_tags)

    output_path = Path(args.output)
    output_path.write_text(tex_content)
    print(f"Generated {output_path} (excluding tags: {exclude_tags or 'none'})")


if __name__ == "__main__":
    main()
