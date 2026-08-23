# cmdowney88.github.io

Personal academic website: hand-coded HTML + Bootstrap on GitHub Pages, plus the course
websites under `teaching/` and the CV build system under `cv/`.

## Where Things Are

| Need | Read |
|---|---|
| HTML/CSS conventions, colors, paths, what not to change | `.claude/site/architecture.md` |
| Markdown guides, Jekyll layouts, local preview | `.claude/site/jekyll.md` |
| Course page structure, schedule tables, term projects | `.claude/courses/conventions.md` |
| A specific course's facts | `.claude/courses/<course>.md` |
| Committing, splitting changes, line endings | `.claude/git-workflow.md` |
| CV build, tags, website-vs-PDF differences | the `update-cv` skill |

Read the relevant file when a task touches it — not preemptively. When the user names a course
(`ling282`, `ling250`, `dscc251`), read `.claude/courses/<course>.md`, then ask what they'd like
to work on.

## Skills

- `new-course-page` — port a course site to a new semester
- `edit-schedule` — restructure an existing schedule: cancel a session, add or drop an activity,
  shift content, move a deadline
- `publish-slides` — link newly exported slide PDFs in a course schedule
- `update-cv` — rebuild the CV and sync outward after editing `cv/cv_data.yaml`

## Outside This Repo

- `~/CourseMaterials/<course>/` — git-tracked source files for course materials (slide sources,
  figures, handouts, R notebooks, LaTeX homework). Some are public student-facing repos, some are
  instructor-private. This is the one to work in.
- `~/Documents/Teaching/` — Keynote decks and similar binary artifacts. Not git-tracked, not
  something Claude needs to touch, and not readable anyway (macOS privacy restriction). Slide
  PDFs reach the website by being exported here and placed in the course's `slides/` directory.
- `~/Obsidian/Teaching/<course>/` — lesson plans, per-lecture teaching notes, and course design
  notes including pedagogical rationale. Private, synced via Obsidian, **not** git-tracked.
  Course design notes live at `~/Obsidian/Teaching/<course>/design-notes.md`.

Note that `.claude/` is committed to a public repository. Keep pedagogy, student information,
enrollment figures, teaching self-assessments, and unapproved departmental business in the
Obsidian vault instead.
