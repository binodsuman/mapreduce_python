#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:57:29 2020

@author: binod
"""

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
