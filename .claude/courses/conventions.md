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
| *(in class)* | Round-robin activity |
| M3 | Abstract + completion plan — commit to one idea |
| M4 | Progress checkpoint, with GitHub repo |
| M5 | Final progress report *(DSCC 251 only)* |
| *(in class)* | Peer-review workshop |
| — | Presentations, final class sessions |
| — | Final writeup, finals week |

DSCC 251 additionally schedules 30-minute code walkthrough appointments between M4 and M5.

Final deliverables: presentation, GitHub repository, and a writeup in the style of a scientific
research paper. Students may pivot direction between milestones; the syllabi state this
explicitly.

Milestone specs live in `teaching/<course>/<term>/project/`, linked from the schedule's Events
column.

## GenAI Policy

Shared across courses: generative AI is not permitted for written assignments or project
writeups, and is permitted for programming work on the term project only.
