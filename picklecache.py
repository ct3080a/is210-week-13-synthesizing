#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""In a Pickle"""

import os
import pickle


class PickleCache(object):
    """A Class to Read Pickle File"""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """A constructor for PickleCache

        Arguments:
        file_path (string, optional): Path that defaults to datastore.pkl
        autosync (bool, optional): Defaults to False.

        Attributes:
         __file_path(string): Constructor Variable that has the file_path value.
         __data (dict): Empty Dictionary Object.
        autosync: A non-private Attribute.

        Returns:
            None

        Example:
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
        """A functions that makes the cache act like a dictionary. Also allows
            __data attribute accessible to outside objects.

        Arguments:
        key (strings): Keys to the dictionary _data.
        value (mix): Values that will be stored in the data dictionary.

        Return:
            None

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello world'
            >>> print pcache._PickleCache__data['test']
            'hello world'
        """

        try:
            self.__data[key] = values
            if self.autosync is True:

                self.flush()
        except (TypeError, KeyError) as error:
            raise error

    def __len__(self):
        """A function that Determines the length of the __data dictionary

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
        """A Function that retrieves items in the __data dictionary

        Arguments:
            key (mix): Key to gain access to items in the __data dictionary.

        Return:
            The requested value in self.__data dictionary.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'Hello World'
            >>> print pcache['test']
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
        """ A Funciton that determines and deletes entries from the __data dict.

        Arguments:
            key (mix):  Location of entries to be deleted from the __data dict.

        Return:
            none

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
        """ A function to open and read a file.

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
        """A function that saves the data found in the PickleCache __data dict.

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
