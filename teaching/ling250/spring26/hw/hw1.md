# Ling250/450: Homework 1

**Due: Monday February 9, 11pm**

This homework is to give you some practice with shell commands, Python, and Regular Expressions. This document is written in Markdown format (.md), which is encoded as plain text, but can be displayed with nice formatting. To view the Markdown file side-by-side with the rendered version, open the Markdown file in VS Code and use the shortcut ⌘+K then V on Mac or ctrl+K then V on Windows.

You should submit your completed work **on Blackboard, as a PDF**. To convert your Markdown file to a PDF, you will need to install one extra Extension to VS Code. Go to Settings > Extensions, and search for "Markdown PDF", then install it. To convert to PDF, use the keyboard shortcut shift+⌘+P on Mac or shift+ctrl+P on Windows to open the "Command Palette". In the Palette, search for the command "Markdown PDF: Export (pdf)" and run it. An HTML file will be created for just a moment while the export is running, and then your PDF should appear in the same folder as the Markdown file.

Here is a guide for writing in Markdown: https://www.markdownguide.org/basic-syntax/

## Q1
Using only the shell commands `head`, `tail`, and `wc`, as well as the redirect operator `>`, how would you divide a text file into three different files containing the first 1/3, the second 1/3, and third 1/3 of lines respectively? Write the exact commands you would use to do this. To make this exercise concrete, you can figure this out using the accompanying file `thirds.txt` (download [here](https://cmdowney88.github.io/teaching/ling250/spring26/hw/thirds.txt)), which is divided into three even sections. Your solution can assume that the number of lines in the file is divisible by 3, and you can also use the "pipe" operator `|` if you wish.

## A1
Your answer to Q1 goes here! Your answer will often be best expressed in the format of a "code block", which is just a nicely-formatted area to write several lines of code or commands. In markdown, a code block can be formatted simply by indenting (with a tab or four spaces). Below is an example of a code block:

    print("This is an example codeblock")
    my_string = "It doesn't actually highlight Python in different colors"

## Q2
Assume you have read the contents of a text file into Python, and you now have it as a **list of strings**, where each string is a single line of text. We'll assume you have this in a variable called `lines`. Write a function that takes in a list of strings like this, and returns a list with **only** the lines that contain a certain word. So your function will take **two arguments**: the list of lines (as strings), and the word we want to search for. For this question, you **may not use Regular Expressions or NLTK**. Your function should be written in "pure" Python. A starter function is included in the answer area below. A helpful resource will be a guide on python string methods [like this](https://www.geeksforgeeks.org/python-string-methods/).

## A2
Your answer to Q2 goes here!

    def filter_sentences(sentences, word_to_keep):
        # Your function goes here

## Q3
Let's now use Regular Expressions in Python to identify linguistically relevant patterns. Using the `re` package in Python, you will come up with a (single) regular expression that can identify proper nouns and proper noun phrases. Proper nouns in English are expressions that refer to a specific (named) person, place, thing, or idea. In English, proper nouns are somewhat easy to identify because they almost always start with a capital letter. However, any word that comes at the beginning of a sentence is capitalized, so we can't completely rely on that heuristic.

Using the provided `Night_Vale.txt` as an example, come up with a regular expression that matches proper nouns and noun phrases. This should match single-word names such as "Cecil", as well as full names like "Hiram McDaniels", and more complex phrases like "Big Rico's Pizza" and "The Night Vale Department of Transportation". Here is some guidance for what your Regular Expression should capture:

- You can assume that all words in the phrases you match are capitalized by default, but in order to capture cases like "Department of Transportation", you should assume that a limited set of non-capitalized words may appear in between the capitalized ones.
- You should not match capitalized words at the beginning of sentences (this will give you some false negatives, but that's okay). **Hint**: it will be easiest for you to only consider words that come after other words (i.e. not considering words at the beginning of lines).
- For simplicity, you can assume that no words in matching results should end in a puntuation mark (except for the apostrophe).
- You should **not** assume a maximum number of words in phrases that you match.
- Note that the apostrophe that is used in `Night_Vale.txt` is **not** the same as the apostrophe that can be typed from your keyboard (your keyboard types a straight apostrophe `'` by default, whereas the text uses a styalized apostrophe `’`). The best way to make reference to this character in your Regular Expression is to copy and paste it from the text.
- It will help to enclose the results of the `re.findall` function in `set()` so that you only see one copy of each unique result. You can then change it back to a list with `list()` if you want to sort by length of the match, for example.

As you work on this problem, keep analyzing your results in terms of false positives (strings that do match but should not) and false negatives (strings that should match but do not). Your final RegEx will **not be perfect**, but it should at least match the examples given below. In the answer area, give your final RegEx, and also answer the following:

1. What were some REs you tried before arriving at your final solution, and what problems did they have in terms of false positives and false negatives?
2. What false positives and false negatives does your final RE have?
3. What was the trickiest type of proper noun phrase to match? How did you match it?

**List of examples your RE should match:**

- Cecil
- Hiram McDaniels
- Mayor Pamela Winchell
- Big Rico’s Pizza
- Sheriff’s Secret Police Coin Grading Service
- Teddy Williams’ Desert Flower Bowling Alley
- Moonlight All-Night Diner
- Parade of the Mysterious Hooded Figures
- Murakami’s The Wind-Up Bird Chronicle

## A3

    r"Your Regular Expression here"
