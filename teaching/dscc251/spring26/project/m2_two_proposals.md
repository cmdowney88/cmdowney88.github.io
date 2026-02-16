# Project Milestone 2: Two Proposals

**Due: February 24 (submit PDF on Blackboard)**

For this milestone, submit two project proposals. The purpose of submitting two is to give you options — I'll give feedback on both, and you'll commit to one (or a hybrid) in M3. Your direction may evolve, and that's expected. The milestone structure exists to catch these pivots early.

If you plan to work with partners, list all group members at the top. All members should submit the same document.

## For each proposal, address the following (1–2 paragraphs each is fine):

### 1. Working title

### 2. Research question

This is the most important part. A good research question is *testable* — your experiments should be able to support or refute an answer. You don't need a formal hypothesis yet, but you need to be heading toward one.

Some guidance on framing:
- A research question is **not** the same as a project description. "I want to apply transfer learning to medical images" describes a project, but it doesn't ask a question. What *about* transfer learning on medical images? Does fine-tuning on a small specialized dataset outperform training from scratch? Does the source domain matter?
- Try phrasing it as: *"Does [method/approach] improve [metric] for [task] compared to [baseline], given [data constraint]?"* You don't have to use that exact template, but it can help.
- It's okay if your question is broad at this stage. M3 is where you'll sharpen it into a specific hypothesis.

Examples of good research questions for this course:
- *Does active learning reduce the amount of labeled data needed for [task] compared to random sampling, and by how much?*
- *Can self-supervised pretraining on unlabeled domain-specific text improve classification accuracy when labeled training data is limited to N examples?*
- *How does the effectiveness of data augmentation strategies vary across different levels of training data scarcity for [task]?*

### 3. Data

Be as specific as you can. Ideally, name an existing dataset and provide a URL or citation. If you're planning to collect or compile data, describe where it would come from and roughly how much you'd need.

If you're not sure where to find data, here are some starting points:
- [Hugging Face Datasets](https://huggingface.co/datasets) — large catalog, searchable by task and domain
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Papers With Code](https://paperswithcode.com/datasets) — find datasets by task, see what benchmarks exist
- Domain-specific repositories (e.g., PhysioNet for medical data, UCI ML Repository)
- The papers you're reading for discussions — check what datasets they use

A concrete data plan is important. Projects that stall often do so because the data turned out to be harder to obtain or messier than expected. If you're uncertain about data access, say so — I can help you evaluate feasibility.

### 4. Methodology

What experiments would you run? Your methodology should involve at least one data-efficient ML technique from this course (past or upcoming topics: unsupervised/self-supervised learning, semi-supervised learning, active learning, weak supervision, transfer learning, few-shot learning, data augmentation, etc.).

Think about:
- What is your baseline? (What would a naive approach look like?)
- What technique(s) would you apply, and what do you expect them to improve?
- How would you measure success? (What metric, on what evaluation set?)

You don't need a fully fleshed-out experimental design — that comes in M3. But I should be able to see the shape of what you'd actually *do*.

### 5. Significance

Briefly: why does this matter beyond the scope of a class project? What bigger question does it connect to? What practical impact could the answer have?

## Formatting and logistics

- Submit as a single PDF on Blackboard
- No strict length requirement, but 1-2 pages total is typical
- Both proposals in the same document
- If working in a group, all members submit the same document

I'll give written feedback on both proposals. Use that feedback when narrowing to one idea for M3 (Abstract + Completion Plan, due March 5).
