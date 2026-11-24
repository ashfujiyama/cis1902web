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

## Requirements

### Command Line Args

Your `hw6.py` script should take in one argument: a path to a single student's submission directory.  Your code needs to check if a path was provided, and it also needs to check if the path is valid.  If either of those conditions is not met, print an error message that starts with "Error:" and exit with exit status = 1.

### Java Compilation

### Autograder Test Cases

### Extraneous Output

### Output Format

### Tips

