---
layout: page
title: WS1 "FP and List Comprehension"
description: >-
    Worksheet 1: "FP and List Comprehension"
active_tab: homework
parent: Assignments
nav_order: 3
nav_exclude: false
search_exclude: false
---

Worksheet 1: FP and List Comprehension 📋
=============================================================
## Objectives

- Introduce functional programming methods `map()`, `zip()`, `filter()`
- Explore nested list comprehensions

## Starter files

- [ws1.py](ws1.py)


{: .note }
   As this worksheet introduces some concepts that we did not directly talk about in class,
   please do not spend too much time on it. If you get stuck and are unable to implement the functions
   within ~2 hours or so, you can submit what you have on Gradescope and it will be still given full credit.

## Map, filter, zip

Python, having functional programming components, has built-in functions `zip()`, `map()`, and `reduce()`. Let's take a look at the help messages for these functions:

```python
>>> help(zip)
class zip(object)
 |  zip(*iterables) --> zip object
 |
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.
 |  ...
```

`zip()` takes a tuple unpacked set of iterable argument(s), creating an iterable `zip` object that yields tuples of the i-th element from each of the provided iterables. Zip gives us arguably the most pythonic way of iterating over two lists:

```python
>>> ranks = ["J", "Q", "K", "A"]
>>> suits = ["hearts", "spades", "clubs", "diamonds"]
>>> for rank, suit in zip(ranks, suits):
...     print(rank, suit)
...
J hearts
Q spades
K clubs
A diamonds
```

Now let's look at map:

```python
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  ...
```

We see it takes as the first argument a function, and unpacked iterable argument(s). It then returns a map object that can be iterated over with the function being applied to each individual value. Note that we can provide *multiple* iterables to the map function, so that functions that take multiple arguments can be used:

```python
# take the pairwise minimum between two lists
>>> a = [2,4,6,8]
>>> b = [1,5,3,7]
>>> list(map(min, a, b))
[1, 4, 3, 7]
```

Similarly, for `filter()`:

```python
>>> help(filter)
Help on class filter in module builtins:

class filter(object)
 |  filter(function or None, iterable) --> filter object
 |
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |  ...
```

These functions can be used to reproduce the same behavior as list comprehensions. Say we're trying to compute the squares of only even numbers in a given list, similar to what we saw in class.

We can use a for loop:

``` python
# not concise, but is readable
>>> nums = [1,2,3,4,6,7,9,10]
>>> even_squares = []
>>> for i in nums:
...     if i % 2 == 0:
...         even_squares.append(i ** 2)
...
>>> print(even_squares)
[4, 16, 36, 100]
```

A combination of `map()` and `filter()`, where `lambda` indicates an *anonymous function*:

``` python
# a one-liner, but a bit of a mess
>>> even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
>>> print(even_squares)
[4, 16, 36, 100]
```

{: .note }
    Anonymous functions are simple functions restricted to a single expression and can be written in one line, or even within another statement. For example, the squaring anonymous function `lambda x: x ** 2` above is equivalent to:
    ``` python
    def square(x):
        return x ** 2
    ```
    We'll talk more about anonymous functions and their use cases next lecture.


Or a list comprehension:

```python
# better!
>>> even_squares = [x ** 2 for x in nums if x % 2 == 0]
>>> print(even_squares)
[4, 16, 36, 100]
```

Here we see that the `map()/filter()` implementation is a bit clunky. In fact, Guido van Rossum, the creator of Python, [is of the opinion](https://www.artima.com/weblogs/viewpost.jsp?thread=98196) that `map()` and `filter()` should be phased out in favor of comprehensions. However, there are still situations where these functions may be useful.

### Task 1: Matrix transpose [0.5 points]

Let's implement a matrix `transpose()` function, where we represent square 2D matrices with a list of lists:

```python
# a 3x3 matrix
>>> mat = [[1, 2, 3],
...        [4, 5, 6],
...        [7, 8, 9]]

# and its transpose
>>> mat_T = [[1, 4, 7],
...          [2, 5, 8],
...          [3, 6, 9]]
```

Formally, for a square matrix $A$, $A^T$ is defined such that for each element, $A^T_{ij} = A_{ji}$. This can easily be done with a nested for loop but we encourage you to think about how you can use `map` and `zip` for a more concise implementation.

{. :note }
In practice we'll never write any standard matrix operations ourselves, as [NumPy](https://numpy.org/) will likely have a much more performant implementation. We'll work with NumPy when we cover data science and machine learning.

## Nested list comprehensions

An additional wrinkle in list comprehensions is that they can be nested:

```python
# one-liner to flatten a list of lists (or a matrix)!
>>> [elem for row in mat for elem in row]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The syntax can be harder to read than a single level list comprehension, so think of each additional `for` statement as another level in a typical nested `for` loop:

```python
# the same as above
>>> for row in mat:
...     for elem in row:
...         l.append(elem)
...
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Conditionals can also be nested:

```python
>>> [elem for row in mat if sum(row) < 10 for elem in row if elem % 2 == 0]
[2]
```

The conditionals also are read as if they are applied to the subsequent level of the for loop:

```python
# same as above, getting a bit unwieldy...
>>> l = []
>>> for row in mat:
...     if sum(row) < 10:
...         for elem in row:
...             if elem % 2 == 0:
...                 l.append(elem)
...
>>> l
[2]
```

### Task 2: Evens and odds [0.5 points]

Let's implement a function called `evens_and_odds()`. It takes an integer $n$ as input, and returns a list of all pairs (represented as tuples) of numbers between $0$ and $n-1$ where the first number is even and the second number is odd:

``` python
>>> evens_and_odds(5)
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
```

Play with the implementation of this function using comprehensions or standard for loops. What approach do you prefer in terms of code readability?

## Task 3: Course feedback [1 point]

In a multi-line comment, please respond to the following questions:

1. On a scale of 0 to 10, how have the lectures been so far? (0 = not useful at all and 10 = extremely valuable)

2. What comments do you have for future lectures and assignments? What did you like? What suggestions do you have for change?

3. What remaining questions do you have about the topics we have covered in the course so far?

That's it, worksheet 1 complete!
