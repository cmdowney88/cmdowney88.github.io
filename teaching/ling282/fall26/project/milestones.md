---
layout: guide
title: Term Project Milestones
subtitle: LING 282/482, Fall 2026
permalink: /teaching/ling282/fall26/project/overview/
---

This document describes the requirements for each project milestone throughout the semester.

* placeholder
{:toc}

## What the project is

You will answer a **question about language or linguistic theory** using deep learning methods.
The project must minimally involve training or fine-tuning a neural model of language (though not
necessarily a Language Model in the technical sense).

The project is **scientifically oriented**. This is the single most important thing to understand
about it: the goal is not to engineer a model that solves an NLP task well, but to use neural
models as instruments for learning something about Language or about Language Models. A project
that gets state-of-the-art accuracy on a benchmark but tells us nothing new is not a successful
project for this course; a project whose model performs mediocrely but produces a clear,
well-supported finding about how language works — or about how models represent it — is.

Within these parameters, you are encouraged to creatively pursue a topic of interest to you.

## Groups

Working in a group is **highly encouraged, but not required**. After M1, I will announce suggested
groupings based on shared interests, but forming a group is ultimately up to you.

One thing to be clear about up front: **I expect the same level of quality from an individual
project as from a group project.** The scope of what a group can accomplish is simply larger, and
working alone does not lower the bar. Factor that into your decision.

Where a milestone asks for a PDF, list all group members at the top, and all members submit the
same document.

Your research direction may evolve as you work. Pivoting is allowed — and often necessary — when
original plans prove unfruitful. The milestone structure exists precisely to catch these moments
early.

All computational work for the project can be run on UR's BlueHive cluster.

---

## M1: Interest Survey (Due Friday, Sep 18)

Submit via the Google Form linked on Blackboard. See [full requirements](../m1/).

The survey collects your topic interests, your background in programming and in linguistics, and
your preferences about groupmates. Your responses are what I use to announce suggested groupings
after this milestone.

---

## M2: Two Proposals (Due Friday, Oct 2)

Submit a PDF on Blackboard. See [full requirements](../m2/).

Two proposals, 1-2 paragraphs each, covering:

1. **Working title**
2. **Research question**: what you will investigate, framed so that experiments could support or
   refute an answer
3. **Data**: what language data you need, and whether an existing corpus provides it
4. **Methodology**: what you would train or fine-tune, and what experiments you would run
5. **Significance**: what the answer would contribute to our understanding of language or of
   language models

You submit two so that you have options. I give feedback on both, and you commit to one (or a
hybrid) in M3.

---

## M3: Abstract + Completion Plan (Due Friday, Oct 9)

### Abstract

Narrow down to one project idea and write a formal abstract, including:

- A working title
- What your project will investigate
- The data you will use (be specific — if you can't obtain the data, consider a different idea)
- What model(s) you will train or fine-tune, and what methods you will use
- **A testable scientific hypothesis**: at least one aspect of your study must pose a quantifiable
  prediction about language or about model behavior that your results can support or refute
- What you expect to find
- The significance of your findings

### Completion Plan

Enumerate all broad tasks necessary for project completion. Organize these into a week-by-week
plan through the end of the semester. If you are working in a group, specify how tasks will be
distributed across group members and briefly justify the distribution.

### Incorporate Feedback

20% of this milestone grade is based on adequately addressing feedback from M2. "Addressing"
doesn't necessarily mean accepting my feedback — it could mean clarifying or providing a
counterargument.

### Ask for Guidance

Use this milestone to request any specific guidance you think would help. I can incorporate this
into written feedback, or we can meet to discuss.

---

## M4: Progress Report + Github Repo (Due Friday, Nov 6)

### Progress Report (PDF)

Report on:

1. What work you've completed so far
2. Any changes to your initial plan or research question
3. A revised plan for completion
4. Anything you'd like guidance on

### Github Repository

Create a Github repository for your project with at least starter code or a skeleton outline. The
repository can be private (add me as a collaborator: `cmdowney88`) or public.

Your `README.md` should contain:

- A brief overview of your research question and methodology
- An explanation of the repository structure (e.g. where are scripts for data processing? Model
  training? Analysis?)
- Even if code isn't fleshed out yet, an explanation of how you plan to structure it

**Guidelines:**

- Any part of your process involving code should go into a script in the repository (vital for
  replication). This includes BlueHive job scripts.
- Data itself should not be committed, especially if you don't own the copyright. Instead, include
  scripts or instructions for obtaining it.

---

## Code Walkthrough (Week of Nov 16)

Book a 30-minute appointment to review your software infrastructure (scripts for data gathering,
cleaning, training, and analysis).

At this stage, your code should be complete or nearly complete, and your attention should shift to
running experiments. If you are working in a group, all members are responsible for understanding
all aspects of the code.

---

## M5: Final Progress Report (Due Friday, Dec 4)

Submit a PDF progress report including:

1. Work completed since M4
2. Any changes to your plan
3. How you plan to complete the project in time for presentations and the writeup

**Important**: your completion plan should be detailed, complete, and viable. You don't need every
aspect finished for the presentation, but you must have intermediate results to present.

---

## Presentations (Dec 7, 9, and 14)

Each project is presented to the class, followed by questions. Presentation length depends on how
many projects there are and will be announced with the presentation specification.

Your presentation should cover:

- Introduction, motivation, and background
- Data description (source, processing, role in project)
- Your hypothesis
- Methodology, including which models you used and how
- Results, with visualizations where helpful
- Discussion/analysis of what the results mean for the question you asked

Your project doesn't need to be fully finalized, but you should address all points above. Address
feedback from your presentation in the final writeup.

---

## Final Writeup (Due Dec 18)

Submit a PDF in the style of a scientific research paper. Full requirements will be posted with the
writeup specification.

### Required Sections

1. **Introduction/Background**: motivate your project — the subject matter, the question, and why
   it matters.
2. **Related Work**: overview closely related scholarly work. Cite sources with a bibliography.
3. **Data**: describe the language data used.
4. **Methodology**: provide enough detail that another researcher could replicate your results.
   Describe data processing, model architecture and training decisions, and hyperparameters. You
   may cite code where appropriate.
5. **Results**: describe outcomes objectively, without editorializing about what they mean.
6. **Analysis/Discussion**: interpret what the results mean and their significance for your
   research question.
7. **Conclusion/Future Work**: briefly restate high-level takeaways and ideas for continuing this
   research.

### Github Repository (Final State)

Your repository should be finalized with:

- A `README.md` explaining how to run your code and replicate all experiments
- A guide to the repository structure
- Well-commented code
