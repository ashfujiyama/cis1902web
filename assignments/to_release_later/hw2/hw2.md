---
layout: page
title: HW 2 "Scripting and Testing"
description: >-
    Homework 2: "Scripting and Testing"
active_tab: homework
parent: Assignments
nav_order: 5
nav_exclude: false
search_exclude: false
---

Homework 2: Scripting and Testing
=============================================================
## Learning objectives

- Familiarization with first party modules
    - `argparse`
    - `json`
    - `unittest`

- Familiarization with third party modules
    - `requests`

- Practice writing unit tests

## Starter files

- [nytimes.py](./nytimes.py)
- [test_nytimes.py](./test_nytimes.py)

## Python as a scripting language

As we have seen so far, Python is a high-level and interpreted language with clear and concise syntax. These attributes make it a good choice for a number of tasks, such as [scripting](https://en.wikipedia.org/wiki/Scripting_language).

A script is a short, relatively simple program which is executed from the command line with the goal of consolidating multiple complex Terminal commands into a single simpler command. A few examples of scripting languages include Python, Bash, and PowerShell.

In this homework, you will build a command line utility that manipulates JSON data and presents that data in the Terminal. For those of you who have never used JSON, it uses the JavaScript Object Notation to encode data as a series of keys and values. If you are unfamiliar with JSON, [click here](https://www.w3schools.com/js/js_json_intro.asp) to learn more.

In addition to manipulating JSON data, you will also practice writing unit tests for your script to ensure correct behavior.

### Setup

This is our first homework assignment that uses modules, including a 3rd party module that does not come installed by default. You can install `requests` like we did in lecture by executing `python3 -m pip install requests`:

``` bash
# the output of your terminal may look something like this
$ python3 -m pip install requests

Collecting requests
  Using cached requests-2.24.0-py2.py3-none-any.whl (61 kB)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Using cached urllib3-1.25.10-py2.py3-none-any.whl (127 kB)
Requirement already satisfied: certifi>=2017.4.17 in ...
Collecting chardet<4,>=3.0.2
  Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna<3,>=2.5
  Using cached idna-2.10-py2.py3-none-any.whl (58 kB)
Installing collected packages: urllib3, chardet, idna, requests
Successfully installed chardet-3.0.4 idna-2.10 requests-2.24.0 urllib3-1.25.10
```

Further documentation for using the `requests` module can be found [here](https://requests.readthedocs.io/en/master/).


## The Times from the terminal

With web browsers these days tracking your every move, and with pesky advisers or managers peeking over your shoulder to see what's on your computer screen, sometimes you just want to do some browsing from the safety of your inconspicuous terminal. This script `nytimes.py` will do exactly that, allowing you to pull top article headlines from the New York Times and display them in your terminal window.

Running any script or command with the `-h` (meaning "help") flag provides the user with a small help page for running that script/command, including possible options and arguments to change the execution. See a sample `python3 nytimes.py -h` output below:

```bash
$ python3 nytimes.py -h
usage: nytimes.py [-h] [-n N] [-o {title,time}] [-t T] url

Pulls top articles from New York Times and displays them in terminal

positional arguments:
  section           the section of articles to display

optional arguments:
  -h, --help        show this help message and exit
  -n N              number of articles to display (default: 10)
  -o {title,time}   field to sort articles by (default: title)
  -t T              truncate title to specified length (default: 60)
```

{: .note }
When you run `python3 nytimes.py -h` you may have a slightly different output depending on what help text you write.

- The `-n` flag specifies the number of articles to display. By default, this is 10.

- The `-o` flag specifies the article attribute to use for sorting. By default, this should be title. Note, if the parameter is time, then the articles should be ordered in descending order. Otherwise, the articles should be ranked in ascending order.

- The `-t` flag specifies the maximum length for the articles' titles. Titles longer than this value should be truncated. The default value is 60.

### Example Usage
``` bash
# view the top articles in the "science" section with default parameters
$ python3 nytimes.py science
0.      A.I. Is Finding Sperm Where Doctors Couldn’t (Date: 2026-08-11T05:02:13-04:00)
        https://www.nytimes.com/2026/08/11/science/ai-infertile-men-sperm.html
1.      An Electric Motorcycle Revolution (Date: 2026-08-11T13:47:26-04:00)
        https://www.nytimes.com/2026/08/11/climate/electric-motorcycle-boom-developing-countries.html
2.      As Europe Faces Another Heat Wave, Travelers Are Forced to A (Date: 2026-08-12T14:46:04-04:00)
        https://www.nytimes.com/2026/08/12/travel/europe-travel-tourism-wildfires-heat-waves.html
3.      Early-Onset El Niño (Date: 2026-08-13T15:28:25-04:00)
        https://www.nytimes.com/2026/08/13/climate/el-nino-effects.html
4.      Federal Job Cuts Are Making Wildfires Harder to Fight (Date: 2026-08-14T05:02:10-04:00)
        https://www.nytimes.com/2026/08/14/climate/wildfires-forest-service-trump-cuts.html
5.      Federal Judge Orders Pentagon to Lift Freeze on Wind Power (Date: 2026-08-06T14:24:31-04:00)
        https://www.nytimes.com/2026/08/06/climate/pentagon-reviews-wind-farms-court-order.html
6.      Frenzy for Solar Eclipse Glasses Takes Over London (Date: 2026-08-11T11:17:06-04:00)
        https://www.nytimes.com/2026/08/11/world/europe/solar-eclipse-glasses-uk.html
7.      From Nest to Deathbed, Jackie the Eagle Entranced California (Date: 2026-08-10T15:58:19-04:00)
        https://www.nytimes.com/2026/08/10/us/jackie-bald-eagle-california-dead.html
8.      Get Ready for Europe’s First Total Solar Eclipse in Decades (Date: 2026-08-10T00:01:06-04:00)
        https://www.nytimes.com/2026/08/10/science/europe-total-solar-eclipse-how-to-watch.html
9.     How Cyclospora Evaded the U.S. Food Safety System to Sicken  (Date: 2026-08-15T05:01:56-04:00)
        https://www.nytimes.com/2026/08/15/health/cyclospora-invesigation-fda.html

# view the 5 most recent articles from the home page
$ python3 nytimes.py home -n 5
0.      An Island Used to Storms Readies for One of the Strongest in (Date: 2026-08-15T14:26:29-04:00)
        https://www.nytimes.com/2026/08/15/weather/hurricane-lala-hawaii-emergency-prep.html
1.      As China Pushes to Expand in Asia, Trump Focuses on Iran (Date: 2026-08-15T05:01:01-04:00)
        https://www.nytimes.com/2026/08/15/us/politics/china-expansion-asia-trump-iran.html
2.      Canadian Petition to Expel U.S. Ambassador Pete Hoekstra Tak (Date: 2026-08-15T05:02:15-04:00)
        https://www.nytimes.com/2026/08/15/world/canada/hoekstra-ambassador-petition-canada-trump.html
3.      Central Synagogue Attack Rattles Jewish New Yorkers (Date: 2026-08-15T15:04:11-04:00)
        https://www.nytimes.com/2026/08/15/nyregion/central-synagogue-shabbat-assault.html
4.      Democrats Reshape 2028 Presidential Primary Calendar, and Pu (Date: 2026-08-15T14:27:45-04:00)
        https://www.nytimes.com/2026/08/15/us/politics/democrats-new-presidential-primary-calendar.html

# view 2 food articles sorted by time (most recently published articles first) with shortened titles
$ python3 nytimes.py business -n 2 -o time -t 30
0.      ‘I Will be Making This on Repe (Date: 2026-08-15T11:00:07-04:00)
        https://www.nytimes.com/2026/08/15/dining/i-will-be-making-this-on-repeat-until-i-cant-look-at-eggs-or-tomatoes-anymore.html
1.      The Original Viral Recipe (Date: 2026-08-15T10:00:05-04:00)
        https://www.nytimes.com/2026/08/15/dining/the-original-viral-recipe.html

# view 2 articles from the world section sorted by title
$ python3 nytimes.py world -n 2 -o title
0.      $10 Million in Gold Found Buried Under Former Brewery in Bel (Date: 2026-08-15T15:36:29-04:00)
        https://www.nytimes.com/2026/08/15/world/europe/gold-bars-coins-belgium.html
1.      8 Matisse Works, Looted from Library in Brazil, Are Recovere (Date: 2026-08-14T06:56:23-04:00)
        https://www.nytimes.com/2026/08/14/world/americas/matisse-stolen-art-found-sao-paulo-brazil-heist.html
```

{: .note }
Since we're pulling data from an active website, the articles will likely have changed when you run these commands.

### The New York Times API

When you read the news online on [https://www.nytimes.com/](https://www.nytimes.com/), you're using the New York Time's *user interface (UI)* to access their news data.  Buttons, clickable links, and navigation menus are a few examples of ways that you (the user) can interact with the service.

On the other hand, your script will be utilizing NY Times' *application programming interface (API)* to access any NYT article information.  An API is specifically designed for other software (such as your terminal script) to access the services offered, and is not designed for direct human use (with the exception of programmers).  Instead of clicking buttons or navigating visual menus, our script will be making "API calls" to browse the NYT news.

It is lucky that the New York Times not only has their own API, but it is also free to use!  Some apps don't release their own APIs (meaning you would need to find a 3rd party API) or charge money for access.  Some apps may offer a free tier, but would impose limits that may incentivize the user to pay for upgraded access.  Common limits include:
1. Rate-limit establishment: Users can only make a certain number of API calls per hour (or day).  For example, NYT has a limit of 5 API calls per minute, and they recommend having your script sleep for 12 seconds in between calls.
2. Delayed Return Values: While the NYT returns real-time data (returned articles match what the NYT is currently displaying on their webpage), other services may return data that is 12 or 24 hours out-of-date.

### Creating a NYT Developer Account

In exchange for using their free service, New York Times requires users to adhere to their [Terms of Use](https://developer.nytimes.com/terms).  One such term is (b.) the creation and use of a singular API key as a means for the New York Times to identify and track your usage.

{: .note }
These steps can also be found at [https://developer.nytimes.com/get-started](https://developer.nytimes.com/get-started), but they are also enumerated here for your convenience.

1. Register for a new account by going to [https://developer.nytimes.com/accounts/create](https://developer.nytimes.com/accounts/create).  Fill in your first name, last name, *Penn email*, and password.  Agree to the terms, then click "Create New Account."
2. Go to your Penn email inbox and locate the email sent by `code@nytimes.com`.  Click on the link in the email to verify your account.
3. Log into your newly verified account, then go to [https://developer.nytimes.com/my-apps](https://developer.nytimes.com/my-apps).  Click on the button that says `+New App`.
4. Enter in the information to register a new app that is now attached to your NYT Dev account.  In the Overview section, our app name will be `HW2 Script`, and we will leave the description field blank.  In the APIs section, we want to enable the very last API: "**Top Stories API**".  Once you click `Enable` for that API, click the `Save` button on the bottom right corner.  You should now see that your app, "HW2 Script", should be assigned an App ID, and it also now has an API Key and Secret.  You will need the API Key later.


## Implementation details

### nytimes.py

You will implement the following functions:

- `build_parser()`: returns an [ArgumentParser](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) instance with the defined parameters above.
- `load_data()`: Loads New York Times data from a given news section into a list of dicts.
- `format_data()`: Sorts and formats the list of dicts from `load_data()`
- `print_data()`: Prints the given list of New York Times data in the specified string format

Further details on the function behvaior can be found in the docstrings provided in the starter file.

<!-- {: .note }
For code style this assignment, we will be performing a close read of `format_data()` **and** the unit test associated with it, `test_format_data()`. -->

Now that we have our NYT Developer account and the script's stub file, how do we make API calls?  With HTTP!

### HTTP - Some Background

[Hypertext Transfer Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP) is the protocol through which clients and servers communicate. Traditionally, a client (e.g. your computer) will send an HTTP request to some server (e.g. The New York Times) by clicking on a link. The server (which is just another computer that holds the data you're requesting) will give an HTTP response back to the client, which will either contain the content that the client requested (e.g. the NYT homepage) or an error explaining that something went wrong. There are a few different kinds of HTTP requests, but you only need to worry about [GET requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET).

However, a user surfing the web isn't the only way that HTTP requests can be sent. Programs can also send HTTP requests to retrieve information from a server to use as a part of its execution.  Your script will be making an API call using an HTTP GET request, using the [`requests.get()`](https://requests.readthedocs.io/en/master/api/#requests.get) method, which requires a URL argument.

For the sake of simplicity, you do not need to handle HTTP errors, and you only need to worry about sending HTTP [GET requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET).

You can see an example of how to make a GET request below:

``` python
url = "https://api.nytimes.com/svc/topstories/v2/arts.json?api-key=abc123abc123"
response = requests.get(url)
```

{: .warning }
You are required to use the following line in your code: `response = requests.get(url)`.  The autograder will not work if you don't use this exact line in your `load_data()` function!

Notice how the URL contains all of the necessary context for the NYT to return the information we need.  You can see "topstories" which indicates the API we're using, and "arts" is the news section we want to get articles from.  We also included our API key in the URL (though you will need to replace `abc123abc123` with your actual API key associated with your NYT Developer account).

The New York Times' API will send the data through an HTTP response, formatted in JSON.  This is what `requests.get(url)` returns.  JSON is a way for servers to encode information that a program might request.  The simple key-value representation makes it easy for programmers to dissect and use the information coming from the request.

### JSON

We can then access the JSON data from the response in the form of a Python dict by calling the `response.json()` method:

``` python
print(response.json())
{'status': 'OK', 'copyright': 'Copyright (c) 2026 The New York Times Company. All Rights Reserved.', 'section': 'Arts', 'last_updated': '2026-08-04T05:42:33-04:00', 'num_results': 37, 'results': ...
```

The output from `response.json()` can be treated like a normal Python dict. You should use this dict to retrieve the New York Times data to display as output.

The resulting dict may be a bit overwhelming to look at, so to make viewing easier you can pretty print it using:

``` python
print(json.dumps(response.json(), indent=4))
{
    "status": "OK",
    "copyright": "Copyright (c) 2026 The New York Times Company. All Rights Reserved.",
    "section": "home",
    "last_updated": "2026-08-03T17:10:39-04:00",
    "num_results": 24,
    "results": [
        {
            "section": "us",
            "subsection": "",
            "title": "Trump\u2019s Meddling in Justice Dept. Causes Problems of His Own Making",
            "abstract": "In the past week alone, President Trump\u2019s interference has imperiled one criminal case, set the stage for sanctions in a second and hindered the confirmation chances of his pick for attorney general.",
            "url": "https://www.nytimes.com/2026/08/03/us/trump-doj-comey-reflecting-pool-blanche.html",
...
```

### test_nyt.py

For this homework assignment, you will write your own unit tests to check the correctness of your function implementation. We've provided function stubs in `test_nytimes.py` for you to do so, with the exception of `print_data()`, which you do not have to test. You can run your unit tests like we did in lecture by executing `python3 test_nytimes.py`:

```bash
$ python3 test_nytimes.py
usage: test_nytimes.py [-h] [-n N] [-o {title,time}] [-t T] section

Pulls top articles from New York Times and displays them in terminal

positional arguments:
  section           the section of New York Times to display

optional arguments:
  -h, --help        show this help message and exit
  -n N              number of articles to display (default: 10)
  -o {title,time}   field to sort articles by (default: title)
  -t T              truncate title to specified length (default: 60)
...
----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK
```

You are free to write whatever test cases you'd like in order to ensure proper functionality of your implementation.  Most importantly, we will be checking whether your unit tests have adequate **code coverage,** which is the percentage of the lines of code your test cases cover out of all the lines of code. You will receive full credit if your unit tests cover **at least 80% of your code**.

{: .note }
Note that code coverage considers which lines of code are run during a test, not whether each individual line of code has a test case associated with it.

For example, this simple unit test we wrote during lecture for `fib_generator()` has 100% code coverage:
``` python
# this example function is a generator which creates an iterable Fibonacci sequence
def fib_generator(max_iter=5):
    """Generate the fibonacci sequence for the specified iterations."""
    prev, curr = 0, 1

    for _ in range(max_iter):
        yield curr

        prev, curr = curr, prev + curr

# this is an example test of the above Fibonacci generator function
def test_fib_generator(self):
    """Tests fib_generator()"""                     # triple quotes is a description of the test
    expected_five = [1,1,2,3,5]

    # tests default max_iter
    actual_five = list(fib_generator())

    self.assertEqual(actual_five, expected_five)    # assertEqual compares 2 values, just like JUnit

```

We have already provided a test case for `build_parser()` in the starter file as an additional example.

To check your unit test coverage, simply submit `test_nytimes.py` and `nytimes.py` to Gradescope and you will see an output like the following.

{:.centered.imgmax}
![](../hw2_coverage.png)

Don't worry too much about the code coverage threshold -- if you implement all of the test stubs with one test per function, your code coverage should be more than enough. The autograder in Gradescope will also tell you which lines of code are not covered if you do not meet the threshold, which will help you adjust your test cases.

Outside of the unit test coverage, we will check the functionality of your implementation by running the four commands shown above in the "Example Usage" section.

<!-- **Since the subreddits are live and post scores can change in real time, we do not expect the outputs to match exactly.** -->

{: .note }
When you submit to Gradescope, the four commands will be autograded, and you will see the output we will use to manually check the functionality of your script, so you can verify the output is similar:

{:.centered.imgmax}
![](../hw2_functionality.png)

### Other Requirements

{: .warning }
No libraries outside of `argparse`, `json`, `requests`, and `unittest` may be imported for this homework.

## Rubric

| Section | Points |
|---------|--------|
Name, PennKey, and hours filled in | 0.5
All functions in `nytimes.py` are implemented | 0.5
All test cases in `test_nytimes.py` are implemented | 0.5
Test cases achieve at least 80% code coverage | 3
`python3 nytimes.py home` correctness | 1
`python3 nytimes.py science -n 5` correctness| 1
`python3 nytimes.py world -n 2 -o time -t 30` correctness | 1
`python3 nytimes.py us -n 2 -o title` correctness | 1
code style | 3
**Total** | 11.5

## Submission

You will upload both your `nytimes.py` and `nytimes.py` code to [**Gradescope**](https://www.gradescope.com/courses) for submission -- **be sure to upload both files at the same time!** We encourage you to work iteratively, implementing functions one at a time to verify their correctness before moving on to the next function. To facilitate this, you are welcome
to submit to Gradescope to verify your code against the autograder as many times as you would like before the submission due date without penalty.

Please keep in mind that the Gradescope automatically locks your homework submissions after the due date, and you will need to request a homework re-opening using the weekly Google Form.

## Attribution

This homework assignment was adapted from [Peter Bui's](https://engineering.nd.edu/faculty/peter-bui/) Python scripting assignment, which is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

<!-- This homework assignment was adapted from [Peter Bui's](https://engineering.nd.edu/faculty/peter-bui/) [Python scripting assignment](https://www3.nd.edu/~pbui/teaching/cse.20289.sp20/homework05.html), which is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). -->
