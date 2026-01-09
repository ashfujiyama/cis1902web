---
layout: page
title: WS0 "Getting Started"
description: >-
    Worksheet 0: "Getting Started"
active_tab: homework
parent: Assignments
nav_order: 1
nav_exclude: false
search_exclude: false
---

Worksheet 0: Getting Started
=============================================================

## Objectives

- Ensure you have Python 3 installed
- Familiarize yourself with the homework submission process

## Starter files

- [ws0.py](../ws0.py)

## Installing Python

Let's first make sure you have Python installed. We will be using Python 3 this semester. Please download and install the latest Python 3 version [here](https://www.python.org/downloads/), which is Python 3.11.1. 

<!--Alternatively, you can install Python 3 through a package manager like `brew` (for OSX),  `apt-get` (for Ubuntu), or some other package manager.
If you are using OSX or Linux, there's a decent chance you may already have Python 3 installed on your machine.
-->

{: .note }
If you have an M1 Mac, be sure to download the Universal2 installer of Python [here](https://www.python.org/downloads/macos/). This is to avoid hardware compatability issues with some of the packages we'll be using later in the semester.


 You can then verify your installation by running `python3` in your terminal. If you're greeted with the `>>>` prompt, along with an indicator of Python 3.x version, you're in good shape:

```bash
$python3
Python 3.11.1 (main, Jan  2 2023, 15:56:16) [GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


{: .note }
If you have issues getting Python installed, or have a different development environment (such as WSL on Windows), let us know on [Ed Discussion](https://edstem.org/us/courses/33747) and we can help out!

## Task 1: The Zen of Python [0.5 points]

Once inside the interpreter, we can run commands interactively just like what we saw in lecture. I encourage you to play around and familiarize yourself with the interpreter, as it is a nice way to debug and prototype snippets of code. There's a little easter egg if we run the code `import this`:

```bash
$ python3
Python 3.8.2 (default, Jul 16 2020, 14:00:26)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters
...
```

The so-called "Zen of Python" is printed to your terminal (are we sure Python programming isn't a cult?). In a later lecture, we will discuss what the keyword `import` means. But for now, after reading through the output, open up the starter file in your favorite text editor (I'm partial to [VS Code](https://code.visualstudio.com/), but use whatever you like!), and write one of the sayings that sticks out to you **as a single line comment**:


```python
# single line comments begin with a #
```

Once you're done with the interpreter, type `exit()` or hit `ctl-d` to exit.

## Task 2: Saying Wordle [1 point]
Now that you have `ws0.py` open in an editor, you'll see that we've provided a `wordle()` function definition in it, with a triple-quoted comment describing the function. You can see the docstring labelling it as the second task and providing a brief description of the function. There is more to be said about docstrings as well, but for now let's look at the end of the function:

```python
def wordle():
    """Task 2: a function that runs a wordle game"""
    secret = input("What is the secret word? ")

    # this print statement is only here to show you how input() works
    print(secret) # TODO delete this

    #TODO implement the rest
    raise NotImplementedError

if __name__ == '__main__':
    wordle()
```

Here is an example of raising an [Exception](https://docs.python.org/3/tutorial/errors.html), with the `raise` keyword operating much like the `throw` keyword in Java or C++. The `NotImplementedError` is a built-in Exception type, and indicates when...something is not implemented. All of the function stubs we will give in the homeworks will have this exception, which will be your cue to implement the function.

Another thing to note is the conditional statement `if __name__ == "__main__"` on line 5. The Python interpreter does a number of things under the hood, and one of the things it does is assign the variable `__name__`. If we run a `.py` from the command line using `python3`, it is as if the interpreter runs the following code before your code is executed:

```python
# the interpreter implicitly does this
__name__ = "__main__"
```

Thus, the `if __name__ == "__main__":` conditional is the Python paradigm for a "main" function. Let's see this and the exception in action by running `python3 ws1.py` in the terminal:

```bash
(.venv) afujiyama@Rikyuu-on-PC worksheets % python3 ws0.py
What is the secret word? hello
hello
Traceback (most recent call last):
  File "/Users/afujiyama/docs/cis1920/website/worksheets/ws0.py", line 17, in <module>
    wordle()
  File "/Users/afujiyama/docs/cis1920/website/worksheets/ws0.py", line 14, in wordle
    raise NotImplementedError
NotImplementedError
```

Python will usefully give the code traceback of where the error or exception occurred during runtime to help with debugging. Also note that there is no compilation process for Python programs because it’s being interpreted instead.

You can also see a new function: input().  Input will have your program for you to type something in the terminal and hit Enter.  When I ran the program, I typed “hello” and then enter.  When that happens, whatever was just typed is saved to the variable `secret`.  We provided an extra print statement to show that `secret` was assigned the value “hello”.

Your goal is remove that print statement and implement the rest of the Wordle game.  Here are the rules:
1. Your secret word has to be 5 characters long.  Your program does not need to check this, however.
2. The game will allow you 6 tries to guess the secret word.  Every time, it should prompt you to make a guess by asking, “What is the secret word?”
3. Once you guess, the program will give you clues about how close the guess was:
  - If your guess has no letters in common with the secret word, it will print 5 underscores: _ _ _ _ _ 
  - If your guess contains a correct character in the wrong spot, it will mark that with a “?” sign corresponding to the space in your guess that holds the correct letter.  If you guessed “abcde” and “d” is somewhere in the secret word but not the fourth letter, the program will print something like this: _ _ _ ? _.
  - If your guess contains a correct character in the correct spot, it will mark that space with a “!” sign.  If you figured out that “d” belongs to the second space, then the program will print something like this: _ ! _ _ _.
4. If you guess the entire word correctly, the program will print some congratulatory message (i.e. “you win!”).
5. If you run out of guesses, the program will print: “better luck next time! the word was [secret word]”, where [secret word] is replaced with the actual secret word.

Here are two examples of the game being played:
```bash
What is the secret word? hello
What is your guess? hoyos
!?_?_
What is your guess? hammo
!___!
What is your guess? hilts
!_!__
What is your guess? helio
!!!_!
What is your guess? hello
You win!
```

```bash
What is the secret word? bingo
What is your guess? frodo
__?_!
What is your guess? failu
__?__
What is your guess? throw
___?_
What is your guess? wrong
__???
What is your guess? ohnoo
?_!?!
What is your guess? noooo
????!
better luck next time! the word was bingo
```

Hint: to print the clues after a guess is made, you need 5 separate print statements to happen.  To get all the printed text on a single line, add `end = ""`as a second argument to the print function so it looks like this: print("_", end=””).  This indicates to the function to not add a newline character at the end of the printed statement (which is the default ending and causes the multiple print statements to be separated by line).


## Task 3: Tell us about yourself [0.5 points]

Finally, we'd like to get to know everyone in the course a little better. In the **multi-line** triple-quote comment provided, fill out your responses to the following questions:

- Where is your hometown?
- What do you want to get out of this course?
- Is there anything you'd like us to know about? This could pertain to your learning situation this semester, or something more general.

## Submitting to Gradescope

Now that we're done with everything, let's submit this worksheet to Gradescope to get a feel of the submission process. Navigate to the [Worksheet 0 Gradescope assignment](https://www.gradescope.com/courses/), and upload your `ws0.py` submission.

You will then see the autograder process your file, which should give you full credit for your implemented `hello()` function:

{:.centered.imgmax}
![](../ws0_screenshot.png)

Both homework and worksheets will be autograded whenever possible this semester, so be sure to reach out on Piazza if you have any issues with this submission. One common gotcha is that the file name must remain the same as we give it to you, so that the autograder knows which file to look for.

{: .note }
On assignmen ts going forward, sometimes functions will be dependent on other functions in their implementation. Since assignments are autograded, it is important that you do not change the names of functions in the starter files we provide you unless instructed to do so.

That's it, worksheet 0 complete!

