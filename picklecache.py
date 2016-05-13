#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for PickleCache."""


import os
import pickle


class PickleCache(object):
    """A small docstring for PickleCache constructor."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Docstring for PickleCache constructor.
        Attributes:
            file_path (str): Path of a file string. Default = datastore.pkl.
            autosync (bool): Truthy or falsey value. Default = False.
        Returns:
            dict: Empty dictionary as __data.
        Examples:
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
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Key/values passed into dictionary.
        Args:
            key (str): A key string in dictionary; required.
            value (str): A value string found in dictionary; required.
        Returns:
            dict: Key or values saved into the dictionary.
        Examples:
            >>>
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """A docstring for length of __data.
        Args:
            self
        Returns:
            len : Length of self.__data.
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """A docstring for retrieving PickleCache object.
        Args:
            key (mixed): Key in the dictionary.
        Returns:
            mixed: Value of key in the dictionary.
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
        """A docstring to delete PickleCache object.
        Args:
            key (mixed): Key in the dictionary.
        Returns:
            mixed: Value of key in the dictionary.
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """
        if key in self.__data:
            del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """A docstring for opening file in read-only."""
        if os.path.exists(self.__file_path) \
           and os.path.getsize(self.__file_path) > 0:
            pfile = open(self.__file_path, 'r')
            self.__data = pickle.load(pfile)
            pfile.close()

    def flush(self):
        """A docstring to save stored data to a file."""
        pfile = open(self.__file_path, 'w')
        pickle.dump(self.__data, pfile)
        pfile.close()
