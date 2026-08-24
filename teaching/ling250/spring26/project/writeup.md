---
layout: guide
title: Final Writeup
subtitle: LING 250/450, Spring 2026
permalink: /teaching/ling250/spring26/project/writeup/
---

**Due: May 11, 11:00pm (submit PDF on Blackboard)**

The writeup is the standalone record of your project. It should be readable as a self-contained document by someone who wasn't in the class and didn't see your presentation. Think of it as writing up your work as a short research paper — not a lab report, and not a reflection on the process, but a scientific account of what you did and what you found.

Use your presentation as a starting point, but don't just transcribe your slides. The writeup is more detailed, more precise, and more carefully organized. Address any gaps or questions that came up during your presentation.

---

## Format

Submit a PDF formatted using [ACL style files](https://github.com/acl-org/acl-style-files) (recommended: use the [ACL Overleaf template](https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj)). If you'd like to use a different format, get approval from me before the deadline.

- **Length**: 6–8 pages, not including bibliography or appendix
- **Bibliography**: cite all data sources, software packages, and prior work in a reference list at the end
- **Appendix**: optional; use it for supporting material (additional figures, tables, code snippets) that would interrupt the main narrative but that you want reviewers to be able to consult

If working with a partner, submit one document with both names on it. Both partners submit on Blackboard.

---

## Required Sections

### 1. Introduction and Background

Motivate your project: what linguistic phenomenon or question are you investigating, and why does it matter? Provide enough context that a reader unfamiliar with your specific domain can follow the rest of the paper.

This section should end with a clear statement of your research question. The reader should know exactly what you set out to find out before they reach the methods section.

### 2. Related Work

Briefly survey prior research that is directly relevant to your question. This doesn't need to be exhaustive, but it should situate your work — what has already been done in this area, and how does your project build on, replicate, or extend it? Cite sources with a bibliography.

If you are explicitly replicating or extending a prior study, this is the place to describe that study in detail.

### 3. Data

Describe the dataset(s) you used:

- Where the data comes from and who created it (with a citation or URL)
- What the data contains and how much there is (number of tokens, utterances, speakers, documents, etc.)
- Any preprocessing, filtering, or operationalization decisions you made
- Anything notable about the data's provenance, coverage, or limitations

Be specific. "A corpus of English text" is not a data description. "The Brown Corpus (Francis & Kučera, 1967), containing approximately one million words of written American English sampled from 500 texts across 15 genres" is.

### 4. Methods

Describe your analysis in enough detail that another researcher could replicate it. This should cover:

- How you processed or prepared the data for analysis (feature extraction, measurement, annotation, etc.)
- What statistical test(s) you used, and why they are appropriate for your data and research question
- What your dependent and independent variables are
- What conditions, groups, or comparisons your analysis is organized around

For any statistical test, explain the choice briefly — not just "I ran a t-test," but why a t-test is the right tool for these particular data and this particular hypothesis.

### 5. Results

Report your results objectively, without interpreting what they mean. That belongs in the next section. Describe what you observed; save evaluation for Discussion.

All quantitative claims must be supported by statistical evidence. See **Reporting Statistical Results** below for guidance on what to include.

Include figures or tables where they help. Visualizations are often more informative than prose descriptions of numbers. If you include a figure or table, it must be referenced in the text and contain a caption that makes it interpretable without reading the surrounding prose.

If any of your results were null, negative, or unexpected, report them fully. Null results are results.

### 6. Discussion

Interpret what your results mean. Connect your findings back to your hypothesis — does the evidence support it, refute it, or is the picture more complicated? If you found unexpected patterns, discuss why they might have occurred.

This section is also the place to address limitations: what couldn't you control for, what alternative explanations exist, and how would you address them in future work?

### 7. Conclusion and Future Work

Briefly restate your key findings and their significance for your research question. What is the one-sentence takeaway? Then identify the most promising directions for extending this work.

### 8. Process Reflection

In one paragraph, describe the real arc of your project: what didn't go as planned, what you had to change, and what you'd do differently. This isn't evaluated for how smoothly things went — it's evaluated for honest engagement with the research process. Every research project involves dead ends and course corrections; documenting them is part of doing science.

---

## Reporting Statistical Results

Any statistical claim — about a difference, a relationship, an effect — must be accompanied by the numbers that support it. The convention in linguistics and related fields is to report the test statistic, its degrees of freedom, and the p-value together, in line with the claim.

**The p-value is required for all tests.** Report the exact value when possible (e.g., *p* = .034), rather than only a threshold (e.g., "p < .05"). Use *p* < .001 when the value is very small. A p-value alone is not sufficient — always include the test statistic and degrees of freedom so the result can be evaluated and reproduced.

### By test type

**t-test** — report the t-statistic, degrees of freedom, and p-value. Include group means and standard deviations in the surrounding prose.

> "Mean vowel duration was significantly longer for stressed syllables (*M* = 145 ms, *SD* = 23 ms) than for unstressed syllables (*M* = 98 ms, *SD* = 18 ms), *t*(47) = 8.43, *p* < .001."

**ANOVA** — report the F-statistic with both the effect and error degrees of freedom, and the p-value. If you followed up with post-hoc comparisons, report those separately.

> "There was a significant main effect of dialect on F1, *F*(2, 117) = 12.4, *p* < .001."

**Correlation** — report the correlation coefficient and p-value.

> "Syllable duration was positively correlated with stress level, *r*(45) = .62, *p* < .001."

**Linear regression** — report the overall model fit (R² and its associated F-statistic and p-value), then the relevant predictors (coefficient estimate, standard error, t-statistic, and p-value for each).

> "The model explained 34% of variance in vowel duration (*R*² = .34, *F*(2, 97) = 25.1, *p* < .001). Vowel height was a significant negative predictor (β = −0.42, *SE* = 0.11, *t*(97) = −3.8, *p* < .001)."

**Logistic regression** — report the same elements as linear regression, but use the log-odds coefficient (β) and its associated Wald z-statistic (or χ²) and p-value. Report odds ratios if they aid interpretation.

> "Higher word frequency significantly reduced the probability of disfluency (β = −0.31, *SE* = 0.08, *z* = −3.9, *p* < .001; odds ratio = 0.73)."

### What the numbers mean (briefly)

- **Test statistic** (*t*, *F*, *r*, *z*, etc.): measures how large the observed effect is relative to sampling variability. Larger values indicate stronger evidence against the null hypothesis.
- **Degrees of freedom**: determines the reference distribution used to compute the p-value. Report them so readers can verify your results.
- **p-value**: the probability of observing a result at least this extreme if the null hypothesis were true. A small p-value does not mean the effect is large or practically important — only that it is unlikely under the null. A large p-value does not prove the null is true.
- **R² / R²\_adj**: in regression, the proportion of variance in the outcome explained by the model. A useful measure of practical significance, independent of sample size.
- **β (coefficient)**: in regression, the estimated change in the outcome per unit change in the predictor (holding other predictors constant). This is often more interpretable than the p-value for communicating the size and direction of an effect.

---

## GitHub Repository

Finalize your project repository alongside the writeup submission. The repository should be in a state where someone else could read it and reproduce your analysis.

**README.md** should include:

- A brief description of your research question and methodology (a few sentences)
- A guide to the repository structure: what's in each folder, what each script or notebook does
- Instructions for obtaining the data (do not commit data you don't own; link to the source and/or include a download script)
- Instructions for running your code from start to finish

**Other requirements:**

- Add a `LICENSE` file. For research code, [MIT](https://choosealicense.com/licenses/mit/) or [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) are standard open-source licenses; for data/content, [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) is a common choice.
- Scripts and notebooks should be clean: remove dead code, print statements left over from debugging, and cells that no longer run in order. If you're submitting a Jupyter notebook, it should run cleanly from top to bottom ("Restart & Run All").
- Add me as a collaborator if the repository is private (`cmdowney88`).

---

## Formatting and Logistics

- Submit as a PDF on Blackboard by the deadline
- If working with a partner, both members submit the same document and both names appear on it
- The bibliography and any appendix do not count toward the 6–8 page limit
- Figures and tables count toward the page limit
- GenAI may not be used to produce the writeup text or analysis — see the course academic honesty policy
