# test code

## 1.Class vs. Instance

Please not at XXX we comply with pep8 coding standards and
Google Style Python Docstrings,
please implement those techniques into your python script.

Class vs. Instance

Write a Person class with an instance variable `age`
and a constructor that takes an integer `initial_age` as a parameter.
The constructor must assign `initial_age` to `age` after validating the
value in`initial_age`. In addition,
you must write the following
instance methods:

1.`year_passes()` should increase the `age` instance variable by 1.

2.`what_am_i()` should perform the following conditional actions:
1.if age < 13 print `You are young...`
2.if `age >= 13` and `age < 18`, print `You are a teenager...`

    3.Otherwise, print `You are an adult...`

## 2.Nuke Dependencies graph

In this task, I would like you to construct a script that reads the upstream dependencies of a specific node.

As a submission, please provide a python script that

Take input - Node (Any)
Prints a list of dependencies
E.g. When I submit a script to render, I want the nodes piped into the selected Write node - one thing to remember.

    *cloned nodes
    *expression nodes
