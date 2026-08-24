---
layout: guide
title: Final Writeup
subtitle: DSCC 251/451, Spring 2026
permalink: /teaching/dscc251/spring26/project/writeup/
---

**Due: May 11, 11:00pm (submit PDF on Blackboard)**

The writeup is the standalone record of your project. It should be readable as a self-contained document by someone who wasn't in the class and didn't see your presentation — a reader with ML background, but not necessarily familiarity with your specific application domain or dataset. Think of it as writing up your work as a short research paper.

Use your presentation as a starting point, but don't just transcribe your slides. The writeup is more detailed, more precise, and more carefully argued. Address any gaps or questions that came up during your presentation.

---

## Format

Submit a PDF formatted using [ACL style files](https://github.com/acl-org/acl-style-files) (recommended: use the [ACL Overleaf template](https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj)). If you'd like to use a different format, get approval from me before the deadline.

- **Length**: 6–8 pages, not including bibliography or appendix
- **Bibliography**: cite all datasets, software, and prior work in a reference list at the end
- **Appendix**: optional; use it for supporting material (additional results tables, implementation details, ablations) that would interrupt the main narrative but that you want available for review

If working in a group, submit one document with all group members' names. All members submit on Blackboard.

---

## Required Sections

### 1. Introduction and Background

Motivate your project: what problem are you investigating, and why does it matter? Provide enough domain context that a reader unfamiliar with your specific application area can follow the rest of the paper.

End this section with a clear statement of your research question. The reader should know exactly what you set out to find out before they reach the methods section.

### 2. Related Work

Survey prior work that is directly relevant to your project. This should cover:

- Prior work on the problem or application domain you're studying
- Prior work on the data-efficient ML technique(s) you applied

You don't need to be exhaustive, but you should situate your project — what has already been done, and how does your work build on, replicate, or extend it? Cite sources with a bibliography.

### 3. Data

Describe the dataset(s) you used:

- Where the data comes from and who created it (with a citation or URL)
- What the data contains and how much there is (number of examples, classes, splits, etc.)
- Any preprocessing, filtering, or formatting decisions you made
- Anything notable about the data's provenance, coverage, or limitations that is relevant to interpreting your results

Be specific. "A dataset of medical records" is not a data description. "The MIMIC-III dataset (Johnson et al., 2016), containing 53,000 ICU patient records with associated diagnostic codes" is.

### 4. Methods

Describe your experimental setup in enough detail that another researcher could replicate your results. This should cover:

- The models or algorithms you used, with enough detail to understand what they are
- How you applied data-efficient ML techniques from this course — **make this connection explicit**. Which techniques did you use? What was the low-data constraint or challenge that motivated the choice? How did you implement or apply them?
- Your experimental conditions and comparisons (baselines, ablations, variants)
- Your evaluation metric(s) and why they are appropriate for the task

For any significant design decision — choice of model, hyperparameter tuning strategy, how you handled the data split — give a brief rationale.

### 5. Results

Report your results objectively, without interpreting what they mean. That belongs in the next section.

Present results in tables or figures where possible — a clearly organized results table is easier to read than prose descriptions of numbers. If you include a table or figure, it must be referenced in the text and contain a caption that makes it interpretable on its own.

Where results vary across runs or folds, report aggregate statistics (e.g., mean and standard deviation) rather than a single number. Differences in performance that fall within noise should be acknowledged as such.

If any of your results were negative, null, or unexpected, report them fully. Negative results are results.

### 6. Discussion

Interpret what your results mean. Connect your findings back to your hypothesis — does the evidence support it, refute it, or is the picture more complicated? If your data-efficient approach helped, by how much and under what conditions? If it didn't help as expected, why might that be?

Address limitations: what couldn't you control for, what confounds exist, and how would you address them in future work? What would you do differently?

### 7. Conclusion and Future Work

Briefly restate your key findings and their significance. What is the one- or two-sentence takeaway? Then identify the most promising directions for extending this work.

### 8. Process Reflection

In one paragraph, describe the real arc of your project: what didn't go as planned, what you had to change, and what you'd do differently. This is evaluated for honest engagement with the process, not for how smoothly things went. Every research project involves dead ends and course corrections; documenting them is part of doing science.

---

## GitHub Repository

By the writeup deadline, your repository should be in a state where someone else could read it and fully reproduce your analysis and experiments. The code walkthrough earlier in the semester was about correctness; this is about cleanliness and completeness.

**README.md** should include:

- A brief description of your research question and methodology (a few sentences)
- A guide to the repository structure: what's in each folder, what each script or notebook does
- Instructions for obtaining data (do not commit data files, especially if you don't own the copyright — link to the source and/or include a download script)
- Step-by-step instructions for running your code: how to set up the environment, reproduce preprocessing, run experiments, and regenerate reported results

**Other requirements:**

- Add a `LICENSE` file. [MIT](https://choosealicense.com/licenses/mit/) or [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) are standard choices for research code.
- Scripts and notebooks should be clean: remove dead code, debugging print statements, and commented-out experiments that didn't make it into the paper. If you're submitting Jupyter notebooks, they should run cleanly from top to bottom ("Restart & Run All").
- Configuration or hyperparameters used to produce reported results should be recorded — either as config files, argument defaults, or a clearly documented table.
- Add me as a collaborator if the repository is private (`cmdowney88`).

---

## Formatting and Logistics

- Submit as a PDF on Blackboard by the deadline
- If working in a group, all members submit the same document with all names on it
- The bibliography and any appendix do not count toward the 6–8 page limit
- Figures and tables count toward the page limit
- GenAI may not be used to produce the writeup text or analysis — see the course academic honesty policy
