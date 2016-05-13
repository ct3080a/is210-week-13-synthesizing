#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Synthesizing Tasks"""

import os
import pickle


class PickleCache(object):
    """PickleCache Class"""
    def __init__(self, file_path="datastore.pkl", autosync=False):
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        self.__data[key] = value
        if self.autosync:
            self.flush()

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, key):
        return self.__data[key]

    def __delitem__(self, key):
        del self.__data[key]
        if self.autosync:
            self.flush()

    def load(self):
        """load class method"""
        if os.path.exists(self.__file_path)\
                and os.path.getsize(self.__file_path) > 0:
            file_object = open(self.__file_path, 'r')
            self.__data = pickle.load(file_object)
            file_object.close()

    def flush(self):
        """flush class method"""
        file_object = open(self.__file_path, 'w')
        pickle.dump(self.__data, file_object)
        file_object.close()
