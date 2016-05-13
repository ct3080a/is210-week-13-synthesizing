#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pickle Cache"""


import os
import pickle


class PickleCache(object):
    """Class for PickCache"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickCache
        file_path(str): Path of the file, def = datastore.pkl
        autosync(bool): optional def = false
        Atributes: Pseudo-private attribute*, assigned the constructor
        variable file_path value, Pseudo-private attribute,
        instantiated as an empty dictionary object
        A non-private attribute"""

        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Creates key and the value of key into a dict
            key(mix): key of dict
            value(mix): value of key"""
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Amount of data in a dict set"""
        len_data = len(self.__data)
        return len_data

    def __getitem__(self, key):
        """tests if key is in dict
            key(mixed): key which is checked with dict key
            returns the value of the key if it exists or raises an error"""
        try:
            if self.__data[key]:
                return self.__data[key]
        except (TypeError, KeyError) as error:
            raise error

    def __delitem__(self, key):
        """removes unwanted objects
            key(mixed): key which is checked with dict key"""
        if self.__data[key]:
            del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Pickles and saves it to a file. This way the data can be accessed
        the next time the program runs."""
        if os.path.exists(self.__file_path) and \
           os.path.getsize(self.__file_path) > 0:
            read_file = open(self.__file_path, 'r')
            self.__data = pickle.load(read_file)
            read_file.close()

    def flush(self):
        """Cache is saved and stored"""
        writefile = open(self.__file_path, 'w')
        pickle.dump(self.__data, writefile)
        writefile.close()
