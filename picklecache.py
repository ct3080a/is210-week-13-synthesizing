#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates custom classes."""

import os
import pickle


class PickleCache(object):
    """This class inherits from object."""
   
def __init__(self, file_path, autosync):
        """This constructor function has two arguments."""
        self.file_path = file_path
        self.autosync = autosync
        
if __name__ == '__main__':       
    PickleCache.__file_path =
    PickleCache.__data = {}
    if os.path.exists('datastore.pkl'):
        os.unlink('datastore.pkl')
 
