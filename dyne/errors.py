'''
Checking for errors in objects

Created by: Ankit Khambhati

Change Log
----------
2016/01/29 - Checking types and paths
'''

import os
import inspect


def check_type(obj, typ):
    '''
    Check if obj is of correct type

    Parameters
    ----------
        obj: any
            Input object for type checking

        typ: type
            Reference object type (e.g. str, int)
    '''

    if not isinstance(obj, typ):
        raise TypeError('%r is %r. Must be %r' % (obj, type(obj), typ))


def check_function(obj):
    '''
    Check if obj is a function

    Parameters
    ----------
        obj: any
            Input object for type checking
    '''

    if not inspect.isfunction(obj):
        raise TypeError('%r must be a function.' % (obj))


def check_path(path, exist):
    '''
    Check if path exists

    Parameters
    ----------
        path: str
            Check if valid path

        exist: bool
            If true, throw exception if path does not exist
            If false, throw exception if path does exist
    '''

    if exist:
        if not os.path.exists(path):
            raise IOError('%s does not exist' % path)
    else:
        if os.path.exists(path):
            raise IOError('%s already exists' % path)


def make_path(path):
    '''
    Make new path if path does not exist

    Parameters
    ----------
        path: str
            Make the specified path
    '''

    if not os.path.exists(path):
        os.makedirs(path)


def check_has_key(dictionary, key_ref):
    '''
    Check whether the dictionary has the specified key

    Parameters
    ----------
        dictionary: dict
            The dictionary to look through

        key_ref: str
            The key to look for
    '''

    if key_ref not in dictionary.keys():
        raise KeyError('%r should contain the %r key' % (dictionary, key_ref))
