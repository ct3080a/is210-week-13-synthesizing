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

    def __setitem__(self, key, values):
        """A functions that converts the cache to a dictionary.

        Arguments:
        Key (strings): Keys to the ditionary _data.
        value (mix): Values for the data dictionary.

        Return:
            None

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """

        try:
            self.__data[key] = values
            if self.autosync is True:

                self.flush()
        except (KeyError, TypeError) as error:
            raise error

        def __len__(self):
            """A function that controls the length of a dictionary

            Returns:
                The length of self.__data

            Example:
                >>> pcache = PickleCache()
                >>> pcache['test'] = 'Hello World'
                >>> len(pcache)
                2
            """

            return len(self.__data)

    def __getitem__(self, key):
        """A Function that gets items in the __data dictionary.

        Return:
            The value in self.__data dictionary.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'Hello World'
            >>> print pcachel['test']
            'Hello World'
        """

        try:
            if self.__data[key]:
                datakey = self.__data[key]
                if self.autosync is True:
                    self.flush()
            return datakey

        except (TypeError, KeyError) as error:
            raise error

    def __delitem__(self, key):
        """A function that edits the entries from the __data dict.

        Arguments:
            key (mix): Position of entries to be deleted from __data dict.

        Return:
            none

        Examples:
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
        """ A function that opens and reads a file.

        Returns:
            None

        Examples:
            >>> import pickle
            >>> filehandler = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, filehandler)
            >>> filehandler.close()
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
        """A function that stores data in PickleCache__data dict>.

        Arguments:
            filefdata (file): File to be written to.

        Returns:
            None

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhanfler = open(pcache.PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """

        filedata = open(self.__file_path, 'w')
        self.__file_object = filedata
        pickle.dump(self.__data, self.__file_object)
        filedata.close()           

            
            
