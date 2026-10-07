# Testing

Testing is really important! It helps make sure things are happening as you would expect them to. The python package [`pytest`](https://docs.pytest.org/en/stable/) is really useful for setting up tests for your project.

## Good Tests

A good test should test one thing, and test it well. Tests are things that can run quickly (generally) as a check to make sure your code works the way you expect it to.

They're really important, because if you start writing complicated stuff, you want to make sure that your figures, tables and statistical tests are actually showing what you expect them to show.

For example, if you are loading data from a CSV file and turning it into a `dict` in Python, turn it into a function, and write a test for it:

```python
def load_data(filename:str) -> dict:
    ...
    # Assume we expect the column names to be 'id', 'size' and 'width'.
    return whatever
```

Then your test can look like this (using `pytest`):

```python
import best_practices

FILENAME = 'myfilename.csv'

def test_load():
    aa = load_data(FILENAME)
    assert isinstance(aa, dict), "The load_file function does not return a dict."

```

If this fails, then that tells us that any of our figures, or tests that depend on this table are likely not showing us what we expected.

## Using `pytest`

There is very good documentation online for the [`pytest`](https://docs.pytest.org/en/stable/) that explains how to use it, how to set up tests and how to manage and report testing. This template creates a simple `pytest` file out of the box for you.
