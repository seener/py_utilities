# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:50:23 2018

@author: Sean Howard
"""

import numpy as np


def avg_standardize(v):
    """
    Return the list values divided by the average value.

    Dependency
    ----------
    numPy

    Parameters
    ----------
    values: list numeric values or tuple of numeric values
        a list of numbers.

    Returns
    -------
    result: list numeric, numeric
        A list of numbers divided by their mean.
        The average value for the original list of values.

    Example
    -------
    v = [5, 10]
    >>> avg_standardize(v)
        [0.66666, 1.33333], 7.5
    """
    if type(v) not in (list, tuple):
        print("The type of object provided is not correct.")
        return None
    try:
        avg = np.average(v)
        if type(v) is tuple:
            output = tuple(v / avg)
        else:
            output = list(v / avg)
        return output, avg
    except TypeError:
        print("The data provided is not appropriate. Double check you input.")
        return None


def max_standardize(v):
    """
    Return the list values divided by the maximum value.

    Dependency
    ----------

    Parameters
    ----------
    values: list numeric values or tuple of numeric values
        a list of numbers.

    Returns
    -------
    result: list numeric, numeric
        A list of numbers divided by their maximum.
        The maximum value for the original list of values.

    Example
    -------
    v = [5, 10]
    >>> max_standardize(v)
        [0.5, 1.0], 10
    """
    if type(v) not in (list, tuple):
        print("The type of object provided is not correct.")
        return None
    try:
        mx = max(v)
        if type(v) is tuple:
            output = tuple([i / mx for i in v])
        else:
            output = [i / mx for i in v]
        return output, mx
    except TypeError:
        print("The data provided is not appropriate. Double check you input.")
        return None


def sum_standardize(v):
    """
    Return the list values divided by the sum of all value.

    Dependency
    ----------

    Parameters
    ----------
    values: list numeric values or tuple of numeric values
        a list of numbers.

    Returns
    -------
    result: list numeric, numeric
        A list of numbers divided by their sum.
        The sum for the original list of values.

    Example
    -------
    v = [5, 10]
    >>> sum_standardize(v)
        [0.33333, 0.66666], 15
    """
    if type(v) not in (list, tuple):
        print("The type of object provided is not correct.")
        return None
    try:
        sm = np.float(sum(v))
        if type(v) is tuple:
            output = tuple([i / sm for i in v])
        else:
            output = [i / sm for i in v]
        return output, sm
    except TypeError:
        print("The data provided is not appropriate. Double check you input.")
        return None


def zsc_standardize(v):
    """
    Return the list values z-scored (value - avg) / stdev.

    Dependency
    ----------
    numPy

    Parameters
    ----------
    values: list numeric values or tuple of numeric values
        a list of numbers.

    Returns
    -------
    result: list numeric, numeric, numeric
        A list of numbers z-scored.
        The average value for the original list of values.
        The standard deviation for the original list of values.

    Example
    -------
    v = [5, 10]
    >>> zsc_standardize(v)
        [-1, 1], 7.5, 2.5
    """
    if type(v) not in (list, tuple):
        print("The type of object provided is not correct.")
        return None
    try:
        avg = np.average(v)
        std = np.std(v)
        if type(v) is tuple:
            output = tuple((v - avg) / std)
        else:
            output = list((v - avg) / std)
        return output, avg, std
    except TypeError:
        print("The data provided is not appropriate. Double check you input.")
        return None


def all_standardize(v, t):
    """
    Return the list values standardized based on method chosen.

    Dependency
    ----------
    numPy
    avg_standardize()
    max_standardize()
    sum_standardize()
    zsc_standardize()

    Parameters
    ----------
    values: list numeric values or tuple of numeric values, type of standardization to use
        v - A list or tuple of numbers
        t - One of "a", "m", "s", "z"
        a = average standardization - avg_standardize()
        m = max standardization     - max_standardize()
        s = sum standardization     - sum_standardize()
        z = z-score standardization - zsc_standardize()

    Returns
    -------
    result: list numeric, numeric, numeric
        A list of numbers standardized.
        The average, maximum or sum value for the original list of values.
        The standard deviation for the original list of values.
        Only z-score returns 3 results all others return 2.

    Example
    -------
    v = [5, 10]
    >>> all_standardize(v, "a")
        [0.66666, 1.33333], 7.5
    >>> all_standardize(v, "m")
        [0.5, 1.0], 10
    >>> all_standardize(v, "s")
        [0.33333, 0.66666], 15
    >>> all_standardize(v, "z")
        [-1, 1], 7.5, 2.5
    """
    if t not in ("a", "m", "s", "z"):
        print("The t parameter has to be one of 'a', 'm', 's', 'z'. See help for details")
        return None
    if t == "a":
        return avg_standardize(v)
    elif t == "m":
        return max_standardize(v)
    elif t == "s":
        return sum_standardize(v)
    elif t == "z":
        return zsc_standardize(v)
    else:
        print("Something went wrong. Check your inputs. See help for details.")
        return None


"""
# test cases
v = [5, 10]
q = (5, 10)

# run tests
print("Run avg_standardize(v) and avg_standardize(q)")
print(str(avg_standardize(v)))
print(str(avg_standardize(q)))
print("Run max_standardize(v) and max_standardize(q)")
print(str(max_standardize(v)))
print(str(max_standardize(q)))
print("Run sum_standardize(v) and sum_standardize(q)")
print(str(sum_standardize(v)))
print(str(sum_standardize(q)))
print("Run zsc_standardize(v) and zsc_standardize(q)")
print(str(zsc_standardize(v)))
print(str(zsc_standardize(q)))
print("Run all_standardize(v, ) and all_standardize(q, )")
print("---- average ----")
print(str(all_standardize(v, "a")))
print(str(all_standardize(q, "a")))
print("---- maximum ----")
print(str(all_standardize(v, "m")))
print(str(all_standardize(q, "m")))
print("---- sum ----")
print(str(all_standardize(v, "s")))
print(str(all_standardize(q, "s")))
print("---- z-score ----")
print(str(all_standardize(v, "z")))
print(str(all_standardize(q, "z")))
"""
