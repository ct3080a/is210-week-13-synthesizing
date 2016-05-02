#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The module for the Pickle Cache."""

import os
import pickle


class PickleCache(object):
    """Defines the PickleCache class"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Creates a constructor for the PickleCache class.

        Args:
            file_path (str): The filepath for the file, default of datastore.pk1
            autosync (bool): Whether autosync is enabled, default to False.

        Attributes:
            __file_path (str): a pseudo-private attribute
            __data (dict): an empty dictionary object
            autosync (bool): a non-private attribute
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Defines a function tp store key and value pairs.

        Args:
            key
            value
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Defines a function to return the length of the data."""
        return len(self.__data)

    def __getitem__(self, key):
        """Defines a function to retrieve data.

        Args:
            key
        """
        return self.__data[key]

    def __delitem__(self, key):
        """Defines a function to delete data.

        Args:
            key
        """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Defines a function to open the file to be read"""
        if os.path.exists(self.__file_path) is True and \
           os.path.getsize(self.__file_path) > 0:
            filedata = open(self.__file_path, 'r')
            self.__data = pickle.load(filedata)
            filedata.close()

    def flush(self):
        """Defines a function to save data to the file"""
        filedata = open(self.__file_path, 'w')
        pickle.dump(self.__data, filedata)
        filedata.close()
