#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses I/O functions."""
import os
import pickle


class PickleCache(object):
    """A class with two args."""
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickleCache class
        Args:
             file_path (string, optional) Defaults to datastore.pkl
             autosync (bool, optional) Defaults to False
        Attributes:
             file_path (string, optional) Defaults to datastore.pkl
             autosync (bool, optional) Defaults to False
             data (dict)
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """Creates storage for key and value pairs in dictionary. 
        Args:
            key (required)
            value (required)
         """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Returns self._data length."""
        return len(self.__data)

    def __getitem__(self, key):
        """Retreives data from the class object.
        Args:
             key (required)
        """
        return self.__data[key]
    
    def __delitem__(self, key):
        """Deletes data from class object.
        Args:
            key (required)       """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Opens and reads files."""
        if os.path.exists(self.__file_path) is True and \
                          os.path.getsize (self.__file_path) > 0:
            filehandler = open(self.__file_path, 'r')
            self.__data = pickle.load(filehandler)
        filehandler.close()

    def flush(self):
        """Stores data."""
        filehandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, filehandler)
        filehandler.close()
