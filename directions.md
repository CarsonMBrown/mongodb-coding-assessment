# Coding Challenge

Welcome to your coding challenge!

Implement your solution in the language of your choosing.

**Create a github repo or gist for your solution** with a README that describes how to run it via the command line and accept input via stdin.

Please email us now to let us know you've started, and email us again once you're done. There's no time limit, but we'd like to know how much time you spend on this.

Thanks!

---


## Problem Description

Write a program that takes a JSON object as input and outputs a flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure.  Output should be valid JSON.

For example, consider the following JSON object:

```json
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    }
}
```

In this example the path to the terminal value `1` is `"a"` and the path to the terminal value `3` is `"c.d"`.

The output for the above object would be:

```json
{
    "a": 1,
    "b": true,
    "c.d": 3,
    "c.e": "test"
}
```

## Assumptions

* The input you receive will be a JSON object
* All keys named in the original object will be simple strings without ‘.’ characters
* The input JSON will not contain arrays
* You may use a library to parse JSON from a string to an object
* Command line should correspond to linux conventions, eg using pipes `cat test.json | mycode`
* Your code will be judged on correctness and code quality, but you do not need to focus on performance optimizations
* Please add tests to validate that your code works correctly.

## Working Times:
    29/3/21 11:40-12:58
