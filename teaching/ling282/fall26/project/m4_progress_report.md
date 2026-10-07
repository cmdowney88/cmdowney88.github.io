---
layout: guide
title: Progress Report + Github Repo (M4)
subtitle: LING 282/482, Fall 2026
permalink: /teaching/ling282/fall26/project/m4/
---

**Due: Friday, November 6 (submit PDF on Blackboard)**

This milestone is a structured check-in: where is your project now, how does that compare to your
M3 plan, and what is the path from here to the finish line? It has two parts: a progress report and
a Github repository for your project.

By now you should have made meaningful progress — data in hand, at least some code running, and a
clearer sense of what your experiments will actually look like. The point of this milestone is to
surface that progress, surface any complications while there is still time to deal with them, and
make a concrete plan for the remaining weeks.

If you are working in a group, list all group members at the top, and all members should submit the
same document.

---

## Part 1: Progress Report

Address each of the following. There is no strict length requirement, but be specific — vague
answers ("we made good progress on the model") are not useful to you or to me.

### 1. What have you completed?

Describe concretely what you've done since M3. This might include obtaining and cleaning data,
writing a preprocessing pipeline, getting a baseline model training on BlueHive, reading related
work, or running initial experiments.

If you have preliminary results — even negative or inconclusive ones — report them here. A
baseline number, a training curve, or a sanity check showing that your pipeline behaves as
expected on a small sample are all worth including.

### 2. What has changed from your M3 plan?

Research rarely goes exactly as planned. If your research question, hypothesis, data, or methodology
has shifted since M3, explain what changed and why. A moderate course correction at this stage is
normal and expected: plans meet reality, and good researchers adapt.

What isn't expected at this point is a complete restart. If you're considering abandoning your M3
direction entirely, flag that clearly so we can talk it through before you invest more time.

If your hypothesis has changed, state the revised version explicitly. It should still make a
quantifiable prediction that your results can support or refute.

### 3. Revised completion plan

Update your week-by-week plan from M3 to reflect where you actually are. Your plan should account
for all the remaining deadlines:

| Date | Milestone |
|------|-----------|
| Week of Nov 16 | Code walkthrough (30-minute appointment) |
| Fri, Dec 4 | M5: Final progress report |
| Dec 7, 9, and 14 | Presentations |
| Dec 18 | Final writeup |

Be realistic. Your code should be complete or nearly complete by the code walkthrough, and the
weeks after that — which include Thanksgiving — should go mostly to running experiments and
analyzing results. A plan that depends on heroic effort in the final two weeks is not a good plan.
If you're behind where you hoped to be, your revised plan should say so and show a credible path to
having intermediate results to present by Dec 7.

### 4. What would you like guidance on?

Use this section to flag anything you'd like help with. I can respond in written feedback, or we
can discuss it at your code walkthrough. Things worth flagging:

- Experiments or training runs that aren't behaving as expected
- Uncertainty about how to set up comparisons, controls, or evaluation metrics
- Scope concerns — too much to finish in time, or results that feel thin
- Anything about the analysis that still feels unclear: what would actually count as support for
  your hypothesis?

---

## Part 2: Github Repository

By the M4 deadline, you must have a Github repository for your project containing at least starter
code or a skeleton outline. The repository can be private (add me as a collaborator:
`cmdowney88`) or public. Include a link to it at the top of your PDF.

Your `README.md` should include:

- A brief overview of your research question and methodology
- An explanation of the repository structure — where are the scripts for data processing? Model
  training? Analysis?
- Instructions for obtaining the data (see below)
- Even if the code isn't fleshed out yet, an explanation of how you plan to structure it

A well-organized skeleton with clear documentation is better than a pile of undocumented files.

### Guidelines

- **Any part of your process that involves code should go into a script in the repository.** This
  is vital for replication: someone else (or you, in December) should be able to rerun every step.
  This includes the job scripts you submit to BlueHive.
- **Don't commit the data itself**, especially if you don't own the copyright. Instead, include a
  script that downloads it, or step-by-step instructions for obtaining it.
- Don't commit model checkpoints or other large generated files either. Record how to regenerate
  them instead, and use a `.gitignore` to keep them out of the repository.
- If you're working in a group, everyone should be committing to the repository. At the code
  walkthrough, every group member is responsible for understanding all of the code, not only the
  parts they wrote.

---

## Formatting and logistics

- Submit the progress report as a single PDF on Blackboard
- Put the link to your Github repository at the top of the PDF
- If working in a group, all members submit the same document
