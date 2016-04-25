#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Picklecache instances."""


import os
import pickle

class PickleCache(object):
    """Construction function for picklecache."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Picklecache constructor.        

        Attributes:
            file_path (str): Path to file. Default = datastore.pkl.
            autosync (bool): Define if autosync enabled. Default = False.

        Returns:
            Dict: Empty dictionary as __data.
        Example:
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()


    def __setitem__(self, key, value):
        """Key/values passed into dictionary.

        Args:
            key (str): Dictionary key; required.
            value (str): Dictionary valtue; required.

        Returns:
            dict: Key/values saved into dictionary.

        Examples:
            >>>
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()


    def __len__(self):
        """Return length of self.__data.

        Args:
            self

        Returns:
            len: Lenght of self.__data.

        Examples:
            >>>
        """
        return len(self.__data)


    def __getitem__(self, key):
        """Retrieve PickleCache object.

        Args:
            key (mixed): Key of the dictionary.

        Returns:
            mixed: Value of associated key in dictionary.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        value = self.__data[key]
        if value is None:
            raise TypeError
        return value


    def __delitem__(self, key):
        """Delete PickleCache object.

        Args:
            key (mixed): Key of the dictionary.

        Returns:
            mixed: Value of associated key in the dictionary.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
        """
        if key in self.__data:
            del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Open file in read only."""
        if os.path.exists(self.__file_path) \
           and os.path.getsize(self.__file_path) > 0:
            pfile = open(self.__file_path, 'r')
            self.__data = pickle.load(pfile)
            pfile.close()

    def flush(self):
        """Save stored data to file."""
        pfile = open(self.__file_path, 'w')
        pickle.dump(self.__data, pfile)
        pfile.close()
            
        
