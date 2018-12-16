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
    values: list numeric values, tuple of numeric values, pandas series,
    numpy array
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


def un_all_standardize(vector_of_values, standardization_type, standardization_dic):
    """
    Return the list values de-standardized based on method chosen.

    Dependency
    ----------
    numPy
    pandas
    un_standardize()
    un_zsc_standardize()

    Parameters
    ----------
    values: list numeric values, tuple,  pandas series of numeric values,
    numpy array; type of standardization to use; standardization parameters
        values - A list or tuple of numbers
        standardization_type - One of "a", "m", "s", "z"
            a = average standardization - un_standardize()
            m = max standardization     - un_standardize()
            s = sum standardization     - un_standardize()
            z = z-score standardization - un_zsc_standardize()
        standardization_dic - {"avg": #, "max": #, "sum": #, "std": #}

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
        try:
            avg = standardization_dic['avg']
        except KeyError:
            print("The standardization_dic expects a {'avg': #} check you parameters")
            return None
        return un_standardize(vector_of_values, avg)
    if standardization_type == "m":
        try:
            mxm = standardization_dic['max']
        except KeyError:
            print("The standardization_dic expects a {'max': #} check you parameters")
            return None
        return un_standardize(vector_of_values, mxm)
    if standardization_type == "s":
        try:
            smv = standardization_dic['sum']
        except KeyError:
            print("The standardization_dic expects a {'sum': #} check you parameters")
            return None
        return un_standardize(vector_of_values, smv)
    if standardization_type == "z":
        try:
            avg = standardization_dic['avg']
            std = standardization_dic['std']
        except KeyError:
            print("The standardization_dic expects a {'avg': #, 'std': #} check you parameters")
            return None
        return un_zsc_standardize(vector_of_values, avg, std)
    print("Something went wrong. Check your inputs. See help for details.")
    return None


"""
# test cases
runfile('./data_standardization_methods.py')

i = range(0,100)

a,b,c,d = map(
np.random.normal,
(100, 50, 25, 5),
(20, 10, 5, 1),
(100,100,100,100))

data = pd.DataFrame({"var1": a, "var2": b, "var3": c, "var4": d}, index = i)

# standardize values
stand_out = list(map(
    all_standardize,
    (data.var1, data.var2, data.var3, data.var4),
    ('a', 'm', 's', 'z')))

# put standardize values into a data frame
data_stand = pd.DataFrame()
data_stand["var1"] = stand_out[0][0]
data_stand["var2"] = stand_out[1][0]
data_stand["var3"] = stand_out[2][0]
data_stand["var4"] = stand_out[3][0]

var1_stnd = {'avg': stand_out[0][1]}
var2_stnd = {'max': stand_out[1][1]}
var3_stnd = {'sum': stand_out[2][1]}
var4_stnd = {'avg': stand_out[3][1], 'std': stand_out[3][2]}

# unstandardize the data
data_unstand = pd.DataFrame()

unstand_out = list(map(
    un_all_standardize,
    (data_stand.var1, data_stand.var2, data_stand.var3, data_stand.var4),
    ('a', 'm', 's', 'z'),
    (var1_stnd, var2_stnd, var3_stnd, var4_stnd)))

data_unstand["var1"] = unstand_out[0]
data_unstand["var2"] = unstand_out[1]
data_unstand["var3"] = unstand_out[2]
data_unstand["var4"] = unstand_out[3]

#compare unstandardized results to original values - should return 0
round(sum(abs(data_unstand.var1 - data.var1)), 6)
round(sum(abs(data_unstand.var2 - data.var2)), 6)
round(sum(abs(data_unstand.var3 - data.var3)), 6)
"""
