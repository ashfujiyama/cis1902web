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

After completing the requisite setup, your autograder should run all of the tests.  After running each test, the autograder should compare the solution output (and exit status) against that of the student's submission.  Note that the students are allowed to have slightly different error messages, and your autograder should account for this.  The results should be stored in a .json file called `results.json`.  Below, we have included an example of this file when we run it on a buggy student submission.

[TODO: insert results.json output here]

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

### Submission

Please submit your `hw6.py` to Gradescope.  We will be performing manual examination of the code to check for style errors and ensure that none of the rules that were outlined in this specification were violated.
