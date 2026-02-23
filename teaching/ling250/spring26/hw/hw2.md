# Ling250/450: Homework 2

**Due: Monday March 2, 11pm**

This homework is to give you some practice with the NLTK library. This document is written in Markdown format (.md), which is encoded as plain text, but can be displayed with nice formatting. To view the Markdown file side-by-side with the rendered version, open the Markdown file in VS Code and use the shortcut ⌘+K then V on Mac or ctrl+K then V on Windows.

You should submit your completed work **on Blackboard, as a PDF**. To convert your Markdown file to a PDF, you will need to install one extra Extension to VS Code. Go to Settings > Extensions, and search for "Markdown PDF", then install it. To convert to PDF, use the keyboard shortcut shift+⌘+P on Mac or shift+ctrl+P on Windows to open the "Command Palette". In the Palette, search for the command "Markdown PDF: Export (pdf)" and run it. An HTML file will be created for just a moment while the export is running, and then your PDF should appear in the same folder as the Markdown file.

Here is a guide for writing in Markdown: https://www.markdownguide.org/basic-syntax/

## Q1
"Entropy" is a measure of uncertainty in probability distributions. For example, a fair coin with a 50/50 chance of landing heads or tails is a maximally *uncertain* coin (has the highest entropy), whereas a trick coin that is rigged to land on heads 100% of the time is maximally *certain* (lowest entropy). Let's use entropy to quantify the differences between different genres of text.

Here is a Python function to compute entropy from a list of probabilities. Don't worry about how the calculation works. Just know that higher entropy means more uncertainty. **NOTE**: this function requires you to import the `math` library with `import math` before you use it.

    def entropy(distribution_list):
        total = 0
        for probability in distribution_list:
            if not 0 < probability <= 1:
                raise ValueError(f"{probability} is not a valid probability!")
            total += -probability * math.log2(probability)
        return total

    # Example usage:
    # dist = [0.2, 0.1, 0.1, 0.6]
    # entropy(dist)

Using this function and NLTK, write a script to find the entropy for the probability distribution over all words for at least three genres of the Brown corpus (`nltk.corpus.brown`), separately (i.e. you should get a different entropy for each genre). You can get this probability distribution by using the `nltk.FreqDist` class. For your answer, **include the Python commands you used** to arrive at the answer. **Hints**:

- In addition to the `FreqDist` methods we used in class (like `.most_common()`, `[word]` for counts, etc.), there is a `.freq()` method that returns a word's **probability** (i.e. its count divided by the total number of tokens). For example, given a `FreqDist` saved in the variable `fd`, `fd.freq('cat')` returns the proportion of all tokens that are "cat". This is different from `fd['cat']`, which gives the raw **count**.
- You can loop over all words/items in a `FreqDist` as if it were a list, e.g. `[word for word in fd]`

## A1

## Q2
In the same three or more Brown genres you chose, find the word with the **highest entropy in tags**, considering only words that appear at least 10 times in that genre. For example, maybe the word "dress" receives the tag "VERB" 80% of the time and the tag "NOUN" 20% of the time. This constitutes a probability distribution over possible tags for that word, and we can calculate the entropy of that distribution. The frequency threshold ensures you find genuinely ambiguous words rather than rare words whose tags are unreliable. For each of the genres, you can get the tag distribution using `nltk.ConditionalFreqDist`. In your answer, specify what the highest-entropy word was for each genre, and what its possible tags were. Explain the different meaning of the word that corresponds to each different tag. As before **include the Python commands you used** to arrive at this solution. **Hints**:

- In NLTK's terminology, the word/token should be the **condition** and the tag should be the **sample**. So if we have a `ConditionalFreqDist` saved as `cfd`, `cfd['dress']` will give the Frequency Distribution over Part-of-Speech tags that "dress" can appear with.
- Note that while `cfd` is a `ConditionalFreqDist` object, `cfd['dress']` is a `FreqDist` object.
- Since `cfd['dress']` is a `FreqDist`, you can use the `.freq()` method described in Q1. For example, `cfd['dress'].freq('NOUN')` returns the probability of "dress" being tagged as a noun. In contrast, `cfd['dress']['NOUN']` would give the raw **count** of times that "dress" occurred as a noun.
- You can get the total number of times a word appears across all tags with `cfd[word].N()`. Use this to enforce the frequency threshold.
- Please use the **universal tagset** when getting the tagged version of the Brown corpus. For example, to get the tagged words in the Romance genre, the command is `nltk.corpus.brown.tagged_words(categories=['romance'], tagset='universal')`

## A2

## Q3
To finish off, let's try to discover distinctive linguistic features of a certain genre. Start by selecting three genres from the Brown corpus to investigate, then pick one in particular to look at. For example, if you pick Romance, Government, and Hobbies, and you select Romance to investigate further, you should try to find quantifiable linguistic patterns that differentiate Romance from the other two. This problem is **exploratory**. We will talk a little about "statistically significant" differences later in the course. For now just try to find patterns that convincingly differentiate the genres in a quantifiable way. Here are some ideas for what you can quantify:

- Frequency of individual words
- Frequency of Part of Speech tags
- Frequency of bigrams
- Frequency of POS tag bigrams
- Distribution of POS tags for certain words

You must **select two** different quantifiable patterns that make your chosen genre distinctive from the other two, given the following requirements:

- The two patterns you choose must be different types. For example, if you look at the frequency of individual words, you must look at bigrams, tags, etc. for the second pattern.
- If you choose to compare frequencies of individual words, you must find at least ten words that distinguish your chosen genre from the other. (i.e. it is not enough to observe that "laser" occurs more in Sci-Fi than it does in Romance)
- **At least one** of the two patterns you investigate must involve Part of Speech tags.
- **At least one** of the two patterns you investigate must involve a `ConditionalFreqDist` (rather than a `FreqDist`), and the condition should **not** be the genre itself. I.e. you need to investigate something like bigrams, word-tag pairs, or tag bigrams.

Finally, use NLTK's tools to find specific examples of the distinctive linguistic patterns you find within the corpus. For example, if you find a certain bigram is distinctive of a genre, you should find some example sentences where it is used. Give a hypothesis or description of why you think the pattern is distinctive of the genre.

Your final answer should include:

- All Python code you used to arrive at your answer (or at least what you used to get your final answer, not necessarily exploration that leads to dead ends).
- Measurements (such as probability, entropy, or differences in probability) that back up your conclusions.
- The examples of your linguistic patterns you find in the corpus.

## A3
