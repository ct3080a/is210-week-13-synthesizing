#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates custom classes."""

import os
import pickle

class PickleCache(object):
    """This class inherits from object."""
    def __init__(self, file_path, autosync):
        """This function has two aregumnets.
            Args:
            file_path: (string, optional) Defaults to datastore.pkl
            autosync (bool, optional) Defaults to False

            Returns:
            class attributes

            Examples
            >>> cacher = PickleCache()
            >>> kprint cacher._PickleCache__file_path
            'datastore.pkl'
            >>> print cacher._PickleCache__file_object
            None
            >>> print cacher._PickleCache__data
            {}
        """
        self.file_path = file_path
        self.autosync = autosync
        __data = {}
        Cache_file = PickleCache()
        
        
                         
