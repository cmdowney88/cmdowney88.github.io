---
layout: guide
title: Two Proposals (M2)
subtitle: LING 282/482, Fall 2026
permalink: /teaching/ling282/fall26/project/m2/
---

**Due: Friday, October 2 (submit PDF on Blackboard)**

For this milestone, submit two project proposals. The purpose of submitting two is to give you
options — I'll give feedback on both, and you'll commit to one (or a hybrid) in M3. Your direction
may evolve, and that's expected. The milestone structure exists to catch these pivots early.

If you are working in a group, list all group members at the top, and all members should submit the
same document. Working in a group is highly encouraged but not required — bear in mind that I expect
the same quality of work either way, since the scope a group can take on is simply larger.

## Before you start: what kind of project this is

Both proposals should aim at answering a **question about language or about language models**, and
both should minimally involve training or fine-tuning a neural model of language.

The distinction that matters most here is between engineering and science. "I will fine-tune a
Transformer to classify X as accurately as possible" is an engineering goal — the model is the
product. In this course the model is the *instrument*: you train or fine-tune it in order to
measure something, and the finding is the product. A proposal that describes a system you'd build,
without saying what you'd learn from it, will get feedback asking you to reframe.

Two broad families of question work well:

- **Questions about language**, where the model is a tool for studying linguistic structure,
  variation, acquisition, or change.
- **Questions about models**, where the object of study is what neural models learn, represent, or
  fail to represent about language.

## For each proposal, address the following (1-2 paragraphs each is fine):

### 1. Working title

### 2. Research question

This is the most important part. A good research question is *testable* — your experiments should
be able to support or refute an answer. You don't need a formal hypothesis yet, but you need to be
heading toward one.

Some guidance on framing:

- A research question is **not** the same as a project description. "I want to fine-tune BERT on
  historical English" describes a project, but it doesn't ask a question. What *about* historical
  English? Does the model's representation of a construction shift across periods in a way that
  tracks the documented change?
- Try phrasing it as: *"Does [linguistic property / model property] hold for [language, construction,
  or model], as measured by [experiment]?"* You don't have to use that exact template, but it can
  help.
- It's okay if your question is broad at this stage. M3 is where you'll sharpen it into a specific
  hypothesis.

Examples of the kind of question that works well for this course:

- *Do multilingual language models represent the same syntactic relation similarly across languages
  that mark it differently — and does typological distance predict how similar?*
- *Does a language model's difficulty on a construction correlate with the difficulty children show
  when acquiring it?*
- *Does subword tokenization disadvantage morphologically rich languages, and can that disadvantage
  be measured directly in language modeling performance?*
- *What does a speech model's representation encode about speaker identity versus phonetic content,
  and at which layers?*
- *Does a model trained only on text show evidence of representing a distinction that is only
  reliably marked prosodically?*

### 3. Data

Be as specific as you can. Ideally, name an existing corpus or dataset and provide a URL or
citation. If you're planning to collect or compile data, describe where it would come from and
roughly how much you'd need.

If you're not sure where to find data, here are some starting points:

- [Hugging Face Datasets](https://huggingface.co/datasets) — large catalog, searchable by task and
  language
- [Universal Dependencies](https://universaldependencies.org/) — syntactically annotated treebanks
  for 100+ languages
- [CHILDES](https://childes.talkbank.org/) — child language acquisition data
- [Papers With Code](https://paperswithcode.com/datasets) — find datasets by task, see what
  benchmarks exist
- [OPUS](https://opus.nlpl.eu/) — parallel corpora
- [Common Voice](https://commonvoice.mozilla.org/) and [LibriSpeech](https://www.openslr.org/12) —
  open speech data
- The Linguistic Data Consortium (LDC) — note that many LDC corpora are licensed; check access
  before building a plan around one
- The papers you're reading — check what datasets they use

A concrete data plan is important. Projects that stall often do so because the data turned out to
be harder to obtain or messier than expected. This is especially true for less-resourced languages,
where a corpus may exist on paper but be tiny, inconsistently annotated, or unavailable in
practice. If you're uncertain about data access, say so — I can help you evaluate feasibility.

### 4. Methodology

What experiments would you run? Your methodology must minimally involve training or fine-tuning a
neural model of language, drawing on techniques from this course (past or upcoming topics: word
vectors, feed-forward and recurrent language models, Transformers, pre-training and fine-tuning,
tokenization, multilingual models, speech models).

Think about:

- What is your baseline? (What would a naive approach, or a null result, look like?)
- What would you train or fine-tune, on what data, and what would you measure?
- How would you tell whether your hypothesis was supported? (What number, on what evaluation set,
  moving in what direction?)
- Is this feasible on BlueHive in the time available? Fine-tuning a moderately sized pre-trained
  model is realistic; pre-training a large model from scratch generally is not.

You don't need a fully fleshed-out experimental design — that comes in M3. But I should be able to
see the shape of what you'd actually *do*.

### 5. Significance

Briefly: why does this matter beyond the scope of a class project? What does the answer tell us
about language, or about how models represent it? What bigger question does it connect to?

## Formatting and logistics

- Submit as a single PDF on Blackboard
- No strict length requirement, but 1-2 pages total is typical
- Both proposals in the same document
- If working in a group, all members submit the same document

I'll give written feedback on both proposals. Use that feedback when narrowing to one idea for M3
(Abstract + Completion Plan, due Friday, Oct 9). The turnaround is short, so if you'd like to talk
through the choice rather than wait on written comments, come to office hours.
