---
layout: guide
title: Abstract + Completion Plan (M3)
subtitle: LING 282/482, Fall 2026
permalink: /teaching/ling282/fall26/project/m3/
---

**Due: Friday, October 16 (submit PDF on Blackboard)**

This milestone has two parts: a formal abstract for your project and a week-by-week plan for
completing it.

In M2 you explored two directions. Now it's time to commit to one — or a hybrid of the two — and
sharpen it into a concrete research plan. The goal isn't to have every detail figured out, but to
have a direction clear enough that you can make steady progress through the rest of the semester.

If you are working in a group, list all group members at the top, and all members should submit the
same document.

---

## Part 1: Abstract

Write a formal abstract for your project (roughly 200-300 words). This is the kind of abstract you
would submit to a conference: concise, specific, and self-contained. A reader who knows nothing
about your project should come away knowing what you are asking, how you will answer it, and why
it matters.

Your abstract should address all of the following.

### Working title

It doesn't have to be final, but it should reflect what your project is actually about.

### Research question and hypothesis

This is the most important part. In M2 you needed a question that was heading toward testability;
by M3 it should be specific enough to generate a **testable scientific hypothesis**. At least one
aspect of your study must make a quantifiable prediction about language or about model behavior —
one that your results can support or refute.

A hypothesis is stronger than a question: it commits to an expected direction, and ideally a rough
magnitude. For example:

- *Question: Does subword tokenization disadvantage morphologically rich languages?*
- *Hypothesis: Across the languages in our sample, a language model's per-character loss will
  correlate positively with a measure of morphological complexity (e.g. average morphemes per
  word), even when the amount of training data per language is held constant.*

Notice what the hypothesis adds: a measurement (per-character loss), a predictor (morphological
complexity), a direction (positive correlation), and a control (equal training data). Each of those
is a decision you will have to make anyway in order to run the experiment.

You don't need to be right — finding out is the point of the experiment. But you do need to make a
prediction, not just plan to observe what happens. A useful check: **what result would count
against your hypothesis?** If you can't say, the hypothesis isn't testable yet.

### Data

Name the specific corpus or dataset you will use, with a citation or URL. If you plan to collect or
compile data yourself, describe the source and the scope concretely: how much, in what format, with
what annotation.

By now you should have actually looked at the data, not just found its description. **If you can't
obtain the data, consider a different idea** — it is far cheaper to change direction now than in
November. If any uncertainty about access remains (licensing, size, annotation quality), say so
here and raise it under "Ask for Guidance" below.

### Methods

What model(s) will you train or fine-tune, on what data, and what will you measure? Be concrete:
"fine-tune a pre-trained multilingual Transformer on each treebank and compare probing accuracy by
layer" says what you will do; "use deep learning to study syntax" does not.

Make sure to name your **baseline or control** — the comparison that tells you whether a result
means anything. Depending on the project, that might be a simpler model, a model trained on
shuffled or ablated data, a randomly initialized model, or a chance-level classifier. Projects that
study what a model represents need this especially: a probe that succeeds can be telling you about
the probe rather than the model. Hewitt and Liang's
[Designing and Interpreting Probes with Control Tasks](https://aclanthology.org/D19-1275/) (2019)
is a good introduction to the problem.

Some of the methods you may want to use — Transformers, pre-training and fine-tuning, tokenization,
multilingual models — are covered later in the course. That's fine; plan around them, and note
where your plan depends on material we haven't reached yet.

### Expected findings

What do you expect to find, and why? A sentence or two connecting your hypothesis to your methods
is enough.

### Significance

Briefly: why does this matter beyond the scope of a class project? What does the answer tell us
about language, or about how models represent it?

---

## Part 2: Completion Plan

List all the broad tasks needed to complete the project, and organize them into a week-by-week plan
from now through the end of the semester. Your plan should account for all the remaining
deadlines:

| Date | Milestone |
|------|-----------|
| Fri, Nov 6 | M4: Progress report + Github repository |
| Week of Nov 16 | Code walkthrough (30-minute appointment) |
| Fri, Dec 4 | M5: Final progress report |
| Dec 7, 9, and 14 | Presentations |
| Dec 18 | Final writeup |

A good completion plan:

- Breaks the project into concrete tasks ("write a script to extract verb tokens from the
  treebank", not "work on the data")
- Shows a coherent arc from data → code → experiments → analysis → writing
- Is realistic about each window — Thanksgiving falls in the remaining weeks, and BlueHive jobs
  can sit in the queue or need to be rerun
- Reflects the fact that by the code walkthrough, your code should be **complete or nearly
  complete**, with the remaining time going to running experiments and analysis

If you're working in a group, specify how tasks will be distributed across group members and briefly
justify the distribution — for example, in terms of each person's background in programming or in
linguistics, or familiarity with the language being studied.

---

## Incorporate Feedback

**20% of this milestone's grade** is based on adequately addressing my feedback on M2. Addressing
feedback doesn't necessarily mean accepting it — it can also mean clarifying what you meant, or
making a reasoned argument for why you're keeping your original approach. What it can't mean is
ignoring it.

Include a short section (a paragraph or a bulleted list is fine) that summarizes the main points of
feedback you received on M2 and how you responded to each. If you combined your two proposals into
a hybrid, explain which parts came from where.

---

## Ask for Guidance

Use this milestone to request any specific guidance that would help you. I can respond in written
feedback, or we can meet to talk it through.

Some things worth flagging if they apply to you:

- Uncertainty about data access, quality, or size
- Modeling decisions you're not sure how to make
- Whether your project is feasible on BlueHive in the time available
- Questions about scope — too ambitious, or not ambitious enough
- Anything about the experimental design or the hypothesis that still feels underspecified

---

## Formatting and logistics

- Submit as a single PDF on Blackboard
- No strict length requirement, but 2-3 pages total is typical
- Include the abstract, completion plan, feedback response, and any requests for guidance in the
  same document
- If working in a group, all members submit the same document
