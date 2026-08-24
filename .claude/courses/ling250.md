# LING 250/450: Data Science for Linguistics

Cross-listed undergrad/grad, Linguistics. Taught in spring semesters.

**Most recent offering**: Spring 2026 — `teaching/ling250/spring26/index.html`
**Prior offerings**: `spring25/`

## Meeting

Monday and Wednesday, 9:00–10:15 AM.

## Grading

- 40% Term project
- 20% Midterm project
- 20% Homework
- 10% Attendance (2 absences without penalty)
- 10% Participation

## Topic Sequence

28 sessions. Pre-spring-break:

- Foundations: introduction and setup, shell commands, Python review, regular expressions
- Text processing: NLTK and corpus methods, git & GitHub
- Linguistic data types: common data formats (JSON, CSV, XML); annotated text I (treebanks,
  tagged corpora — PTB, Brown); annotated text II (Universal Dependencies, annotation schemes);
  speech data I (waveform, sampling, digitization); speech data II (spectrograms, formants,
  Praat/ELAN, time-aligned tiers, forced alignment)
- Term project round-robin; midterm project due

Post-break:

- Computational corpus analysis: topic modeling and word vectors
- Statistics in R: R basics and descriptive statistics; correlation and probability
  distributions; hypothesis testing and t-tests; ANOVA and linear regression
- Data visualization & the Grammar of Graphics; interactions, polynomial regression,
  mixed-effects models
- Peer-review workshop; data publishing and open access
- Term project presentations; writeup due finals week

## Projects

**Midterm project** — structured data processing task with precise specifications, exercising
the linguistic data formats from the first half.

**Term project** — open-ended research project investigating a linguistic question with data;
individual or pairs. Milestones follow the standard sequence in `conventions.md`.

## Homework Format

Homework lives in `teaching/ling250/<term>/hw/` as **raw Markdown** (`hw1.md`, …), linked
directly from the schedule and served as plain text.

**Do not convert these to Jekyll guide pages.** Unlike the milestone specs, these are templates
students download and type their answers into — the Markdown file *is* the artifact they submit.
Rendering them to HTML would defeat that. This is a deliberate exception to the "Markdown with
front matter becomes a page" pattern in `.claude/site/jekyll.md`.

## Materials

- Public student repo: `~/CourseMaterials/ling250-materials/` →
  github.com/cmdowney88/ling250-materials. Contains `lectures/` (follow-along tutorials in
  markdown and Jupyter), `demos/`, `audio/`, `data/`. Students clone once and `git pull` for
  updates. Some data files are gitignored for copyright and distributed via Blackboard instead.
- Instructor-only materials: `~/CourseMaterials/ling250-private/` — never publish or link.
- Lesson plans: `~/Obsidian/Teaching/ling250/`

Note: this course's Topics cells link out to notebooks in the `ling250-materials` GitHub repo
rather than to local slide PDFs. Do not apply the local-PDF pattern here without asking.
