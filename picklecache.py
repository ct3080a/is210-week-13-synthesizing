#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Synth Week 13."""

import os
import pickle


class PickleCache(object):
    """A picklecache class. """

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
        """Creates storage for key, value pairs, #2

        Args:
            key (required)
            value (required)
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Returns self data length, #2"""
        return len(self.__data)

    def __getitem__(self, key):
        """Retreives data from class object, #3

        Args:
            key (required)
        """
        return self.__data[key]

    def __delitem__(self, key):
        """Deletes data from class object, #4

        Args:
            key (required)
        """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Opens and reads pickle files, #5"""
        if os.path.exists(self.__file_path)is True and \
           os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, 'r') as fhd:
                self.__data = pickle.load(fhd)
            fhd.close()

    def flush(self):
        """Saves and stores data, #6"""
        with open(self.__file_path, 'w') as fhd:
            pickle.dump(self.__data, fhd)
        fhd.close()
