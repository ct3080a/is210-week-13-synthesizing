#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Docstring"""


import os
import pickle


class PickleCache(object):
    """PickleCache class"""

    def __init__(self, file_path="datastore.pkl", autosync=False):
        """Constructor for class."""
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Makes cache behave like a dictionary."""
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Returns the len"""
        return len(self.__data)

    def __getitem__(self, key):
        """Retrieves data from PickleCache object and handlers"""
        return self.__data[key]

    def __delitem__(self, key):
        """Deletes a value"""
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Pickles and saves data to a file"""
        if os.path.exists(self.__file_path) and\
           os.path.getsize(self.__file_path) > 0:
            file_object = open(self.__file_path, 'r')
            self.__data = pickle.load(file_object)
            file_object.close()

    def flush(self):
        """Saves stored data to file when commanded to do so."""
        file_name = open(self.__file_path, 'w')
        pickle.dump(self.__data, file_name)
        file_name.close()
