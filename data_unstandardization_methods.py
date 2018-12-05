# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:38:35 2018

@author: Sean Howard
"""

import numpy as np
import pandas as pd


def un_standardize(vector_of_values, standard_value):
    """
    Return the list values rollout against value used to standardize.
    This will work for avg, max and sum standardization.

    Dependency
    ----------
    numPy
    pandas

    Parameters
    ----------
    values: list numeric values, tuple of numeric values, pandas series, numpy array
        a list of numbers.

    Returns
    -------
    result: numpy array numeric, numeric
        A list of numbers multiplied by their standardization value.

    Example
    -------
    avg = 7.5
    max_value = 10
    sum_value = 15
    >>> unstandardize([0.66666, 1.33333], avg)
        [5.0, 10.0]
    >>> unstandardize([0.5, 1.0], max_value)
        [5.0, 10.0]
    >>> unstandardize([0.33333, 0.66666], sum_value)
        [5.0, 10.0]
    """
    if isinstance(vector_of_values, (list, tuple, pd.core.series.Series, np.array)):
        vector_of_values = np.array(vector_of_values)
        try:
            output = vector_of_values * standard_value
            return output
        except TypeError:
            print("The data provided is not appropriate. Double check you input.")
            return None
    else:
        print("The type of object provided is not correct.")
        return None


def un_zsc_standardize(vector_of_values, avg, stdev):
    """
    Return the list values converted from z-scored [(value - avg) / stdev] back
    to raw values.

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
    values = [-1, 1]
    average = 7.5
    standard_dev = 2.5
    >>> un_zsc_standardize(values, average, standard_dev)
        [5.0, 10.0]
    """

    if isinstance(vector_of_values, (list, tuple, pd.core.series.Series, np.array)):
        vector_of_values = np.array(vector_of_values)
        try:
            output = vector_of_values * stdev + avg
            return output
        except TypeError:
            print("The data provided is not appropriate. Double check you input.")
            return None
    else:
        print("The type of object provided is not correct.")
        return None


def all_un_standardize(vector_of_values, standardization_type, **kwargs):
    """
    Return the list values de-standardized based on method chosen.

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
    values: list numeric values, tuple,  pandas series of numeric values,
    numpy array; type of standardization to use; standardization parameters
        values - A list or tuple of numbers
        standardization_type - One of "a", "m", "s", "z"
            a = average standardization - avg_standardize()
            m = max standardization     - max_standardize()
            s = sum standardization     - sum_standardize()
            z = z-score standardization - zsc_standardize()
        kwargs - {"avg": #, "max": #, "sum": #, "std": #}

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
        avg = kwargs['avg']
        return un_standardize(vector_of_values, avg)
    if standardization_type == "m":
        mxm = kwargs['max']
        return un_standardize(vector_of_values, mxm)
    if standardization_type == "s":
        smv = kwargs['sum']
        return un_standardize(vector_of_values, smv)
    if standardization_type == "z":
        avg = kwargs['avg']
        std = kwargs['std']
        return un_zsc_standardize(vector_of_values, avg, std)
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
