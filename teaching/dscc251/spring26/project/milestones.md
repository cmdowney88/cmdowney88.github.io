# DSCC/LING 251/451: Term Project Milestones

This document describes the requirements for each project milestone throughout the semester.

---

## M1: Interest Survey (Due Jan 29)

Submit via the course form.

**Question 1: Project Ideas**

What ideas do you have for potential topics for your term project? It's early in the course, so you may not have an exact research question or methodology in mind. However, you can still identify topic areas or personal interests. For instance:

- Are there specific application domains you're interested in? (e.g., medical imaging, NLP, climate science, robotics)
- Any particular data constraints you'd like to explore? (e.g., rare events, expensive annotation, domain shift)
- Any data-efficient ML techniques you're already curious about?

Please answer in a paragraph or two, being as specific as possible. If you already have a research question in mind, feel free to share it.

**Question 2: Group Preferences**

Is there anyone in the class you'd prefer to work with? I'll use responses to suggest potential groupings based on shared interests, but group formation is ultimately up to you.

**Question 3: Background**

Rate your comfort level (1-5) with:
- Python programming
- Machine learning (theory and practice)
- Command-line interfaces / computing clusters

---

## M2: Two Proposals (Due Feb 24)

Submit a PDF with the following:

**Group Information**

If you plan to work with partners, list all group members. All members should submit the same document.

**Two Project Ideas** (1-2 paragraphs each)

For each proposal, address:

1. **Working title** for the project
2. **Research question**: What will you investigate? The question must be testable through controlled experiments. You may not have a formal hypothesis yet, but you need some idea of how experiments can answer the question.
3. **Data**: What data will you need? Can you identify an existing dataset? Provide URLs or references. If not, where might you find it?
4. **Methodology**: What experiments will you run? Your methodology should involve applying data-efficient ML techniques from this course (e.g., transfer learning, active learning, semi-supervised learning, etc.).
5. **Significance**: What bigger-picture questions might this contribute to? What practical impact could the answer have?

The specifics will evolve through later milestones. The next milestone will have you commit to one idea and write a formal abstract.

---

## M3: Abstract + Completion Plan (Due Mar 5)

### Abstract

Narrow down to one project idea and write a formal abstract. Your abstract should include:

- A working title
- What your project will investigate
- The dataset you will use (be specific—if you can't obtain the data, consider a different idea)
- What methods you will use
- **A testable scientific hypothesis**: At least one aspect of your study must pose a quantifiable prediction that can be supported or refuted by results
- What you expect to find
- The significance of your findings

### Completion Plan

Enumerate all broad tasks necessary for project completion. Organize these into a week-by-week plan through the end of the semester. If working in a group, specify how tasks will be distributed and briefly justify the distribution.

### Incorporate Feedback

20% of this milestone grade is based on adequately addressing feedback from M2. "Addressing" doesn't necessarily mean accepting my feedback—it could mean clarifying or providing a counterargument.

### Ask for Guidance

Use this milestone to request any specific guidance you think would help. I can incorporate this into written feedback, or we can meet to discuss.

---

## M4: Progress Report + GitHub Repo (Due Mar 24)

### Progress Report (PDF)

Report on:
1. What work you've completed so far
2. Any changes to your initial plan or research question
3. A revised plan for completion
4. Anything you'd like guidance on

### GitHub Repository

Create a GitHub repository for your project with at least starter code or a skeleton outline. The repository can be private (add me as collaborator: `cmdowney88`) or public.

Your `README.md` should contain:
- A brief overview of your research question and methodology
- An explanation of the repository structure (e.g., where are scripts for data processing? Model training? Analysis?)
- Even if code isn't fleshed out yet, explain how you plan to structure it

**Guidelines:**
- Any part of your process involving code should go into a script in the repository (vital for replication)
- Data itself should not be committed, especially if you don't own the copyright. Instead, include scripts or instructions for obtaining it.

---

## Code Walkthrough (Week of Apr 7)

Book a 30-minute appointment to review your software infrastructure (scripts for data gathering, cleaning, training, analysis).

At this stage, your code should be complete or nearly complete, and your attention should shift to running experiments. All group members are responsible for understanding all aspects of the code.

---

## M5: Final Progress Report (Due Apr 14)

Submit a PDF progress report including:
1. Work completed since M4
2. Any changes to your plan
3. How you plan to complete the project in time for presentations and writeup

**Important**: Your completion plan should be detailed, complete, and viable. You don't need every aspect finished for the presentation, but you must have intermediate results to present.

---

## Presentation (Apr 28-30)

You will give a 20-minute presentation plus 5 minutes for questions. Plan accordingly.

Your presentation should cover:
- Introduction, motivation, and background
- Data description (source, processing, role in project)
- Your hypothesis
- Methodology, including any models used and how
- Results, with visualizations where helpful
- Discussion/analysis of what results mean for the topic

Your project doesn't need to be fully finalized, but you should address all points above. Address feedback from your presentation in the final writeup.

---

## Final Writeup (Due Finals Week)

Submit a PDF, 6-8 pages in [ACL format](https://github.com/acl-org/acl-style-files). I recommend the [ACL Overleaf template](https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj).

### Required Sections

1. **Introduction/Background**: Motivate your project—the subject matter, the question, and why it matters.
2. **Related Work**: Overview closely related scholarly work. Cite sources with a bibliography.
3. **Data**: Describe the data used.
4. **Methodology**: Provide enough detail that another researcher could replicate your results. Describe data processing and modeling decisions. You may cite code where appropriate.
5. **Results**: Describe outcomes objectively, without editorializing about what they mean.
6. **Analysis/Discussion**: Interpret what the results mean and their significance for your research question.
7. **Conclusion/Future Work**: Briefly restate high-level takeaways and ideas for continuing this research.

### GitHub Repository (Final State)

Your repository should be finalized with:
- A `README.md` explaining how to run your code and replicate all experiments
- A guide to the repository structure
- Well-commented code
