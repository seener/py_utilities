# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:50:23 2018

@author: Sean Howard
"""

import numpy as np
import pandas as pd


def avg_standardize(vector_of_values):
    """
    Return the list values divided by the average value.

    Dependency
    ----------
    numPy
    pandas

    Parameters
    ----------
    values: list numeric values, tuple of numeric values, pandas series
        a list of numbers.

    Returns
    -------
    result: numpy array numeric, numeric
        A list of numbers divided by their mean.
        The average value for the original list of values.

    Example
    -------
    values = [5, 10]
    >>> avg_standardize(values)
        [0.66666, 1.33333], 7.5
    """
    if isinstance(vector_of_values, (list, tuple, pd.core.series.Series)):
        vector_of_values = np.array(vector_of_values)
        try:
            avg = np.average(vector_of_values)
            output = vector_of_values / avg
            return output, avg
        except TypeError:
            print("The data provided is not appropriate. Double check you input.")
            return None
    else:
        print("The type of object provided is not correct.")
        return None


def max_standardize(vector_of_values):
    """
    Return the list values divided by the maximum value.

    Dependency
    ----------
    pandas

    Parameters
    ----------
    values: list numeric values, tuple or pandas series of numeric values
        a list of numbers.

    Returns
    -------
    result: numpy array numeric, numeric
        A list of numbers divided by their maximum.
        The maximum value for the original list of values.

    Example
    -------
    values = [5, 10]
    >>> max_standardize(values)
        [0.5, 1.0], 10
    """
    if isinstance(vector_of_values, (list, tuple, pd.core.series.Series)):
        vector_of_values = np.array(vector_of_values)
        try:
            max_value = max(vector_of_values)
            output = vector_of_values / max_value
            return output, max_value
        except TypeError:
            print("The data provided is not appropriate. Double check you input.")
            return None
    else:
        print("The type of object provided is not correct.")
        return None


def sum_standardize(vector_of_values):
    """
    Return the list values divided by the sum of all value.

    Dependency
    ----------
    pandas

    Parameters
    ----------
    values: list numeric values, tuple or pandas series of numeric values
        a list of numbers.

    Returns
    -------
    result: numpy array numeric, numeric
        A list of numbers divided by their sum.
        The sum for the original list of values.

    Example
    -------
    values = [5, 10]
    >>> sum_standardize(values)
        [0.33333, 0.66666], 15
    """
    if isinstance(vector_of_values, (list, tuple, pd.core.series.Series)):
        vector_of_values = np.array(vector_of_values)
        try:
            sum_values = sum(vector_of_values)
            output = vector_of_values / sum_values
            return output, sum_values
        except TypeError:
            print("The data provided is not appropriate. Double check you input.")
            return None
    else:
        print("The type of object provided is not correct.")
        return None


def zsc_standardize(vector_of_values):
    """
    Return the list values z-scored (value - avg) / stdev.

    Dependency
    ----------
    numPy
    pandas

    Parameters
    ----------
    values: list numeric values, tuple or pandas series of numeric values
        a list of numbers.

    Returns
    -------
    result: numpy array numeric, numeric, numeric
        A list of numbers z-scored.
        The average value for the original list of values.
        The standard deviation for the original list of values.

    Example
    -------
    values = [5, 10]
    >>> zsc_standardize(values)
        [-1, 1], 7.5, 2.5
    """
    if isinstance(vector_of_values, (list, tuple, pd.core.series.Series)):
        vector_of_values = np.array(vector_of_values)
        try:
            avg = np.average(vector_of_values)
            stdev = np.std(vector_of_values)
            output = (vector_of_values - avg) / stdev
            return output, avg, stdev
        except TypeError:
            print("The data provided is not appropriate. Double check you input.")
            return None
    else:
        print("The type of object provided is not correct.")
        return None


def all_standardize(vector_of_values, standardization_type):
    """
    Return the list values standardized based on method chosen.

    Dependency
    ----------
    numPy
    pandas
    avg_standardize()
    max_standardize()
    sum_standardize()
    zsc_standardize()

    Parameters
    ----------
    values: list numeric values, tuple or pandas series of numeric values,
    type of standardization to use
        values - A list or tuple of numbers
        standardization_type - One of "a", "m", "s", "z"
            a = average standardization - avg_standardize()
            m = max standardization     - max_standardize()
            s = sum standardization     - sum_standardize()
            z = z-score standardization - zsc_standardize()

    Returns
    -------
    result: numpy array numeric, numeric, numeric
        A list of numbers standardized.
        The average, maximum or sum value for the original list of values.
        The standard deviation for the original list of values.
        Only z-score returns 3 results all others return 2.

    Example
    -------
    values = [5, 10]
    >>> all_standardize(vector_of_values, "a")
        [0.66666, 1.33333], 7.5
    >>> all_standardize(vector_of_values, "m")
        [0.5, 1.0], 10
    >>> all_standardize(vector_of_values, "s")
        [0.33333, 0.66666], 15
    >>> all_standardize(vector_of_values, "z")
        [-1, 1], 7.5, 2.5
    """
    if standardization_type not in ("a", "m", "s", "z"):
        print("The t parameter has to be one of 'a', 'm', 's', 'z'. See help for details")
        return None
    if standardization_type == "a":
        return avg_standardize(vector_of_values)
    if standardization_type == "m":
        return max_standardize(vector_of_values)
    if standardization_type == "s":
        return sum_standardize(vector_of_values)
    if standardization_type == "z":
        return zsc_standardize(vector_of_values)
    print("Something went wrong. Check your inputs. See help for details.")
    return None


"""
# test cases
v = [5, 10]
q = (5, 10)
i = range(1,1000001)
a,b,c = map(np.random.normal, (100, 50, 25), (20, 10, 5), ([1000000] * 3))
data = pd.DataFrame({"var1": a, "var2": b, "var3": c}, index = i)

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

# run pandas test
data_stand = pd.DataFrame()

print("---- average pandas ----")
z = list(map(all_standardize, (data.var1, data.var2, data.var3), (['a']*3)))
data_stand["var1"] = z[0][0]
data_stand["var2"] = z[1][0]
data_stand["var3"] = z[2][0]
data_stand.describe()

print("---- max pandas ----")
z = list(map(all_standardize, (data.var1, data.var2, data.var3), (['m']*3)))
data_stand["var1"] = z[0][0]
data_stand["var2"] = z[1][0]
data_stand["var3"] = z[2][0]
data_stand.describe()

print("---- sum pandas ----")
z = list(map(all_standardize, (data.var1, data.var2, data.var3), (['s']*3)))
data_stand["var1"] = z[0][0]
data_stand["var2"] = z[1][0]
data_stand["var3"] = z[2][0]
data_stand.describe()

print("---- z-score pandas ----")
z = list(map(all_standardize, (data.var1, data.var2, data.var3), (['z']*3)))
data_stand["var1"] = z[0][0]
data_stand["var2"] = z[1][0]
data_stand["var3"] = z[2][0]
data_stand.describe()
"""
