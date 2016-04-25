#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Synthesizing tasks for the 13th week"""

import os
import pickle


class PickleCache(object):
    """thing goes here"""
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """constructor for PickleCache
        Args:
            file_path (string, optional): Defaults to datastore.pkl
            autosync (bool, optional): Defaults to False

        Attributes:
            __file_path(string): pseudo-private attr w/ file_path values
            __data (dict): pseudo-private attr instantiated as empty dict obj
            autosync: non-private attr

        Reutnrs:
            None

        Examples:
             >>> cacher = PickleCache()
            >>> print cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.__file_path = file_path
        self.__data = {}
        self.__file_object = None
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, values):
        """Makes cache work like a dict; allows __data attr accessible
        outside of objects

        Args:
            key (string): keys to dictionary _data
            value (mixed): what is stored in the dictionary

        Returns:
            None

        Examples:
        >>> pcache = PickleCache()
        >>> pcache['test'] = 'hello'
        >>> print pcache._PickleCache__data['test']
                'hello'
        """
        try:
            self.__data[key] = values
            if self.autosync is True:
                self.flush()
        except (TypeError, KeyError) as error:
            raise error

    def __len__(self):
        """Determines the length of __data dictionary
        Returns:
            Length of self.__data
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'Hello'
            >>> len(pcache)
            1
        """

        return len(self.__data)

    def __getitem__(self, key):
        """Gets items in the __data dictionary
        Arguments:
            key (mixed): Key to get hold of items in the __data dictionary.
        Returns:
            Requested value in self.__data dictionary.
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'Hello'
            >>> print pcache['test']
            'Hello'
        """

        try:
            if self.__data[key]:
                mykey = self.__data[key]
                if self.autosync is True:
                    self.flush()
            return mykey

        except (TypeError, KeyError) as error:
            raise error

    def __delitem__(self, key):
        """ Determines and deletes entries from the __data dict.
        Arguments:
            key (mixed): Location of entries to be deleted from the __data dict.
        Return:
            None
        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """

        if self.__data[key]:
            del self.__data[key]
            if self.autosync is True:
                self.flush()

    def load(self):
        """ Opens and reads a file.
        Returns:
            None
        Examples:
            >>> import pickle
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
        """

        loadfile = self.__file_path
        if os.path.exists(loadfile) and os.path.getsize(loadfile) > 0:
            filedata = open(self.__file_path, 'r')
            self.__data = pickle.load(filedata)
            filedata.close()

    def flush(self):
        """Saves all data found in PickleCache __data dict.
        Arguments:
            filedata (file): File that data will be writen to.
        Returns:
            None
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """

        filedata = open(self.__file_path, 'w')
        self.__file_object = filedata
        pickle.dump(self.__data, self.__file_object)
        filedata.close()
