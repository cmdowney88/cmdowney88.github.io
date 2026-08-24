# Course Page Conventions

Shared structure across all course websites in `teaching/`.

## Directory Layout

```
teaching/<course>/<term>/
├── index.html      # the syllabus: Information, Policies, Schedule
├── slides/         # lecture PDFs, created when the first deck is published
├── hw/             # homework PDFs and .tex sources
├── docs/           # student-facing guides
└── project/        # term project milestone specs
```

Term directories are named `fall26`, `spring26` — lowercase season plus two-digit year.

## Page Title and Navbar Brand

Two different strings, two different formats:

```html
<title>LING 282/482 (Fall 2026)</title>
<a class="navbar-brand" href="#page-top">LING 282/482: Deep Learning in Computational Linguistics (Fall '26)</a>
```

- **`<title>`** — course number, then the term with a **full year** in parentheses. No
  institution prefix: **UR is the unmarked case** while the instructor is employed there.
  `teaching/uw_574` therefore keeps its `UW` prefix — it is the one non-UR course, and the prefix
  is what distinguishes its `LING 574` from the UR LING courses. If the instructor moves
  institutions, that convention would be revisited; until then, don't add `UR` anywhere.
- **`navbar-brand`** — course number, colon, full course name, then the term with an
  **abbreviated year** in parentheses: `(Fall '26)`, not `(Fall 2026)`.

Both were inconsistent across offerings and were normalised retroactively. `teaching/uw_574` is
the only page still using square brackets (`[Spr '23]`); it is archived and non-UR, so it is left
as-is.

## Schedule Table

The schedule is the **last** `<tbody>` in the file; earlier tables hold meeting times and
teaching staff. Four columns: Date, Topics, Readings, Events. The Topics header is worded
slightly differently per course ("Topics", "Topics + Slides") — match on position, not text.

Lecture with slides linked:
```html
<td>
	<a href="slides/7_self-supervised.pdf" target="_blank">Self-supervised Learning</a>
</td>
```

Lecture not yet released — plain text, which `publish-slides` later wraps in a link:
```html
<td>Transfer learning</td>
```

Holiday or no-class row:
```html
<td colspan="3" align="center">Fall Break: no class</td>
```

Student-led discussion or in-class activity — never link these:
```html
<td><em>Student-led discussion: Transfer learning</em></td>
```

Slide filenames follow `N_topic.pdf`. Numbers may skip; some decks have no number
(`pytorch.pdf`). Course pages are indented with **tabs**; `index.html` and
`teaching/index.html` use spaces.

## Term Projects

LING 250/450, DSCC 251/451, and LING 282/482 use a milestone-based term project. Students
investigate a research question rather than demonstrating a technique, and develop the project
incrementally with feedback at each checkpoint.

Standard sequence:

| Milestone | Content |
|---|---|
| M1 | Interest survey / initial brainstorming |
| M2 | Two informal proposals |
| M3 | Abstract + completion plan — commit to one idea |
| M4 | Progress checkpoint, with GitHub repo |
| *(appointments)* | 30-minute code walkthrough, between M4 and M5 |
| M5 | Final progress report |
| — | Presentations, final class sessions |
| — | Final writeup, finals week |

DSCC 251 and LING 282 both run the full sequence. Milestone deadlines fall on **Fridays** and are
placed in the Events column of the preceding class row, worded "due Friday M/D".

Some courses schedule an in-class workshop session where groups exchange feedback. Whether there
is one, and where it falls, is a per-course choice — DSCC 251 puts a peer-review workshop
immediately before M3; LING 282 has none. Do not assume a course has one, or where.

Final deliverables: presentation, GitHub repository, and a writeup in the style of a scientific
research paper. Students may pivot direction between milestones; the syllabi state this
explicitly.

Milestone specs live in `teaching/<course>/<term>/project/`, linked from the schedule's Events
column. **All milestone specs are Jekyll guide pages** (see `.claude/site/jekyll.md`): Markdown
with front matter, the title in front matter rather than an H1 in the body, and an explicit
`permalink`. Link to them by permalink (`project/m1/`), never by filename.

Permalinks are `/teaching/<course>/<term>/project/<slug>/`, with these slugs:

| File | Slug |
|---|---|
| `milestones.md` | `overview` |
| `m1_interest_survey.md` … `m5_final_progress_report.md` | `m1` … `m5` |
| `code_walkthrough.md` | `code-walkthrough` |
| `presentation.md` | `presentation` |
| `writeup.md` | `writeup` |

The filenames stay descriptive; only the URLs are short. Titles drop the course prefix, since the
`subtitle` carries it (`DSCC 251/451, Spring 2026`). The overview page gets a `{:toc}`; the
individual specs do not.

## GenAI Policy

Shared across courses: generative AI is not permitted for written assignments or project
writeups, and is permitted for programming work on the term project only.
