#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Docstring"""

import os
import pickle

class PickleCache(object):
    """A picklecache class."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """A constructor for the file.

        Args:
            file_path(string, optional) Defaults to datastore.pkl
            autosync (bool, optional) Defaults to False

        Attributes:
            file_path (string, optional) Defaults to datastore.pkl
            autosync (bool, optional) Defaults to datastore.pkl
            data (dict)
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """Creates storage for key, value pairs

        Args:
            key (mixed)
            Value (mixed)
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Returns length."""
        return len(self.__data)

    def __getitem__(self, key):
        """Retrieves data.

        Args:
            key
        """
        return self.__data[key]

    def __delitem__(self, key):
        """Deletes items

        Args:
            key
        """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Iterates through pickle files."""
        if os.path.exists(self.__file_path) is True and \
           os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as fhd:
                self.__data = pickle.load(fhd)
            fhd.close()

    def flush(self):
        """Saves and manages files."""
        with open(self.__file_path, 'w') as fhd:
            pickle.dump(self.__data, fhd)
        fhd.close()
             
