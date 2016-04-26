#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates custom classes."""

import os
import pickle


class PickleCache(object):
    """This class inherits from object."""
    if __name__ == "__main__":
            '_PickleCache__file_path' == "file_path"
            '_PickleCache__data' == {}
           

def __init__(self, file_path='datastore.pkl', autosync=False):
        """This constructor function has two arguments.
        Args:
            file_path (string, optional): Defaults to datastore.pkl
            autosync (bool, optional): Defaults to False

        Attributes:
            autosync(bool): creates an auto sync

           __file__path(string): creates a string object

           __data(dictionary): a set of key value pairs
        """
        self.__file_path = file_path
        self.__data = {}
        self.load()
        autosync = self.autosync

        
