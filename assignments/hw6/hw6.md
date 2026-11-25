---
layout: page
title: HW 6 "Autograder"
description: >-
    Homework 6: "Autograder"
active_tab: homework
parent: Assignments
nav_order: 4
nav_exclude: false
search_exclude: false
---

Homework 6: Autograder
=============================================================

## Learning Objectives
- Familiarization with the subprocess module
- Experience writing an open-ended program

## Starter Files
- [hw6.zip](./hw6.zip)

## Setup

You can download the starter files in the link above.  When you uncompress the zip file, add a new file called `hw6.py` inside the directory `hw6`.  Your file tree should look something like this:
```
hw6/
├─ solution/
│  ├─ Calculator.java
├─ submissions/
│  ├─ Hau/
│  │  ├─ Calculator.java
│  ├─ Kiawe/
│  │  ├─ Calculator.java
│  ├─ Lana/
│  │  ├─ Calculator.java
│  ├─ Lily/
│  │  ├─ Calculator.java
│  ├─ Mallow/
│  │  ├─ Calculator.java
│  ├─ Sophocles/
│  │  ├─ Calculator.java
├─ hw6.py
```

You will also need to have a Java installed.  Go to your terminal and type
```
javac -version
java -version
```

If you do not have a Java compiler installed on your computer, go to the [official website](https://www.oracle.com/java/technologies/downloads/) and download a recent version (I recommend JDK 25).

## Autograder

Autograders are an essential part of any programming class.  A high level description of what an autograder does is that it runs your code on some input and compares the output your code produces with the expected output.  If the outputs match up, yay!  The student gets full points.  Otherwise, the student will receive a zero for that particular test (at least in our implementation).

In this assignment, you will be autograding a homework assignment that was written in Java.  Using the power of the subprocess module, we can run Java code in a Python program!  You will be doing this assignment from scratch, but I've given a few files that will assist your development.

- `solution` is a directory that contains a single file, `Calculator.java` - you will use the behavior of this file as the ground truth for your autograder implementation.  That is, you will run the student submission and the solution on the same input and compare both outputs against each other to determine if the student submission passes the test.
- `submissions` is the other directory, and it contains the homework submissions of 6 students.  Each file is also called `Calculator.py` and they're all separated into their own directories featuring each student's name.  For example, `submissions/Lana` is one submission, and `submissions/Mallow` is another.
- `calculator_cases.py` is a file that contains a single dictionary that holds all the test cases for the homework assignment.  You are expected to use these cases in your autograder (don't change or make your own!), but you're not expected to have your autograder read from this file.  Instead, you may copy the data and paste it in whatever format you would like into your source code.

{: .warning }
You will need to ensure your file tree is exactly as shown in [Setup](#setup), otherwise it will not pass the autograder on Gradescope!

### The Homework Assignment

The homework assignment you will be autograding is a simple addition calculator.  The program takes in a mathematical expression, evaluates it, and then prints the results.  The program should be able to handle positive and negative integer operands, and catch any syntax errors such as:
- invalid operands used (e.g. subtraction, multiplication, parentheses)
- 2 plus signs happening in a row (e.g. `3 + 3 + + 6`)
- 2 operands in a row (e.g. `3 9 + 42`)

Anytime an error is caught, the program prints an error message starting with "Error:" (case insensitive) and exits with status = 1.

An example commmand used to run the solution would be `java solution/Calculator 3 + 4 + 7`.  Note that operators and operands are separated by a single space.

## Requirements

### Command Line Args

Your `hw6.py` script should take in one argument: a path to a single student's submission directory.  Your code needs to check if a path was provided, and it also needs to check if the path is valid.  If either of those conditions is not met, print an error message that starts with "Error:" and exit with exit status = 1.

### Java Compilation

Before we can run the Java files, you must first run the command to compile the code first.  To give an example, the command to compile the solution file is `javac solution/Calculator.java`.

### Autograder Test Cases

As stated above, the test cases that your autograder should run have been provided for you in a file called `calculator_cases.py`.  Your autograder implementation is not required to read or parse this file, instead you may copy and paste the test cases into your source code and format it in a way that best suits your implementation.  Do **not** add any other test cases.

### Output Format

After completing the requisite setup, your autograder should run all of the tests.  After running each test, the autograder should compare the solution output (and exit status) against that of the student's submission.  Note that the students are allowed to have slightly different error messages, and your autograder should account for this.  The results should be stored in a .json file called `results.json`.  Below, we have included an example of this file when we run it on a buggy student submission found in `submissions/Acerola/`.

```
{
    "tests": [
        {
            "case name": "Simple 1",
            "input": "0",
            "score": 0,
            "max_score": 5,
            "output": "A single digit...\nERROR: expected 0, got 1\n"
        },
        {
            "case name": "Simple 2",
            "input": "39",
            "score": 5,
            "max_score": 5,
            "output": "A single integer...\n"
        },
        {
            "case name": "Simple 3",
            "input": "-42",
            "score": 0,
            "max_score": 5,
            "output": "A negative integer...\nERROR: expected -42, got -41\n"
        },
        {
            "case name": "Simple 4",
            "input": "-42 + 43",
            "score": 5,
            "max_score": 5,
            "output": "Simple addition...\n"
        },
        {
            "case name": "Invalid Simple 1",
            "input": "-14 +",
            "score": 5,
            "max_score": 5,
            "output": "Missing a second operand...\n"
        },
        {
            "case name": "Invalid Simple 2",
            "input": "+ 36",
            "score": 5,
            "max_score": 5,
            "output": "Missing initial operand...\n"
        },
        {
            "case name": "Invalid Simple 3",
            "input": "3990 - 360",
            "score": 0,
            "max_score": 5,
            "output": "Incorrect operator...\nERROR: student code returned with zero exit status\n"
        },
        {
            "case name": "Invalid Simple 4",
            "input": " ",
            "score": 0,
            "max_score": 5,
            "output": "No expression provided...\nERROR: student code did not handle error appropriately\n"
        },
        {
            "case name": "Invalid Long 1",
            "input": "10 + 20 + 30 + 40 + + 50 + 60",
            "score": 5,
            "max_score": 5,
            "output": "Putting 2 plus signs in a row...\n"
        },
        {
            "case name": "Invalid Long 2",
            "input": "10 + 20 + 30 + 40 + 50 + 60 70 + 80 + 90",
            "score": 5,
            "max_score": 5,
            "output": "Putting two integers in a row...\n"
        },
        {
            "case name": "Invalid Long 3",
            "input": "10 + 20 + 30 + 40 + 5 + 50 + 60 + 70 + +",
            "score": 5,
            "max_score": 5,
            "output": "Ending with double plus signs...\n"
        },
        {
            "case name": "Invalid Long 4",
            "input": "10 + 20 + 30 + 40 + 50 + 60 + 70 + 50+ 80 + 90",
            "score": 5,
            "max_score": 5,
            "output": "Forgetting a space between operator and operand...\n"
        },
        {
            "case name": "Pi",
            "input": "3 + 14 + -159 + 265 + 35 + 8979 + -32384 + -6 + 2 + 64 + 338 + -3 + 279 + 50 + 28 + -84 + 179 + 196",
            "score": 0,
            "max_score": 5,
            "output": "many integers, should result in negative sum...\nERROR: expected -22204, got -22203\n"
        },
        {
            "case name": "Zeros",
            "input": "0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0",
            "score": 0,
            "max_score": 5,
            "output": "many zeros added still results in zero...\nERROR: expected 0, got 1\n"
        },
        {
            "case name": "Consecutive Sum",
            "input": "0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20",
            "score": 0,
            "max_score": 5,
            "output": "Sum of all integers from 0 to 20, inclusive...\nERROR: expected 210, got 211\n"
        },
        {
            "case name": "Complex Invalid: Jabberwock",
            "input": "\\'Twas brillig, and the slithy toves    Did gyre and gimble in the wabe\\; All mimsy were the borogoves,    And the mome raths outgrabe.  \\<Beware the Jabberwock, my son    The jaws that bite, the claws that catch\\! Beware the Jubjub bird, and shun    The frumious Bandersnatch\\!\\>  He took his vorpal sword in hand\\;    Long time the manxome foe he sought- So rested he by the Tumtum tree,    And stood awhile in thought.  And, as in uffish thought he stood,    The Jabberwock, with eyes of flame, Came whiffling through the tulgey wood,    And burbled as it came\\!  One, two\\! One, two\\! And through and through    The vorpal blade went snicker-snack\\! He left it dead, and with its head    He went galumphing back.  \\<And hast thou slain the Jabberwock?    Come to my arms, my beamish boy\\! O frabjous day\\! Callooh\\! Callay\\!\\>    He chortled in his joy.  \\'Twas brillig, and the slithy toves    Did gyre and gimble in the wabe\\; All mimsy were the borogoves,    And the mome raths outgrabe.",
            "score": 5,
            "max_score": 5,
            "output": "Very long poem...\n"
        }
    ],
    "output": ""
}
```

Note that you should match this pretty close. The only fields that can have some difference is how you format the value of output for each test. The test output should always start with the test description with a **...\n** following that, but what is stored after that can vary. If a test does fail for a submission, you should put a descriptive error message there and include the word “error” somewhere. (We will be checking this, but have some leniency here. Don’t just put “ERROR: test case failed”.)

### Extraneous Output

Your autograder should not print anything unecessary or create any output files other than `results.json`. By output files, we mean things that are generated when you run the tests. This is not the same as files that are used to build your autograder or files created during the compilation process.  You should also not hold any data in subprocess.PIPE that you do not plan to use (e.g. stderr content).

### Style

Because this is an open-ended assignment, we will be taking a close look at your style choices.  Be sure to break your code into helper functions (you should have at least 2 useful helper functions, minimum).  You are also required to write docstrings for each helper and useful comments that will help us understand your implementation.

### Import Requirements

You are only allowed to use the following imports:
- sys
- argparse
- os
- subprocess
- json

Be sure to only import libraries you end up using!

### Submission

Please submit your `hw6.py` to Gradescope.  We will be performing manual examination of the code to check for style errors and ensure that none of the rules that were outlined in this specification were violated.
