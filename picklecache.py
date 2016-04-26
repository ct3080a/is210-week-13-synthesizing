#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates custom classes."""

import os
import pickle


class PickleCache(object):
    """This class inherits from object."""
    
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """This constructor function has two arguments.

        Args:
        file_path (string, optional): Defaults to datastore.pkl
        autosync (bool, optional): Defaults to False

        Attributes:
        autosync(bool): defaults to False
        __file__path(string): creates a string object.
        __data(dictionary): a set of empty key value pairs.

        Returns:
            None

        Example:
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
           'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.__file_object = None
        self.load()
        self.autosync = self.autosync
