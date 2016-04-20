#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Task 01 - boroughs health violations module."""

import os
import pickle


class PickleCache(object):
    """ Implements a Pickle objec serializer """

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """ Constructor for PickleCache class

        Args:
            file_path (string, optional): path and file to receive serialized
                                            object.
            autosync (bool, optional): option for automatic sync.

        Attributes:
            autosync (bool): option for automatic sync.

            __file_path (string): path and file to receive serialized object.

            __data (dict): a dictionary of key-value pairs.
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """ Adds or replaces a dictionary key and value pair in __data.

        Args:
            key (immutable): key of dictionary entry.

            value (mixed): value to be assigned to the specified key.

        Returns:
            None.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
        """
        self.__data[key] = value

        if self.autosync:
            self.flush()

    def __len__(self):
        """ overrides builtin len function to return number of items in __data.

        Args:
            none.

        Returns:
            integer: number of elements in __data dictionary.

        Example:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """ Retrieves a dictionary item by its key and returns the value.

        Args:
            key (immutable): key of dictionary entry.

        Returns:
            mixed: value specified for the specified key.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            'hello'
        """
        return self.__data[key]

    def __delitem__(self, key):
        """ Removes a dictionary item by its key.

        Args:
            key (immutable): key of dictionary entry.

        Returns:
            None.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print len(pcache)
            1
            >>> del pcache['test']
            >>> print len(pcache)
            0
        """
        del self.__data[key]

        if self.autosync:
            self.flush()

    def load(self):
        """ load the pickled dictionary opbject from the file.

        Args:
            none.

        Returns:
            None.

        Examples:
            >>> import pickle
            >>> fh = open('datastore.pkl', 'w')
            >>> pickle.dump({'foo': 'bar'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'bar'
        """
        if os.path.exists(self.__file_path) and \
           os.path.getsize(self.__file_path) > 0:

            try:

                pfile = open(self.__file_path, 'r')
                self.__data = pickle.load(pfile)

            except IOError as ioe:
                raise ioe

            finally:
                pfile.close()

    def flush(self):
        """ dump the dictionary object to the file.

        Args:
            none.

        Returns:
            None.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
       """
        try:

            pfile = open(self.__file_path, 'w')
            pickle.dump(self.__data, pfile)

        except IOError as ioe:
            raise ioe

        finally:
            pfile.close()
