#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:35:38 2018

@author: li
"""
import time
words = input('you want say:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y)%len(item)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30,30)]) for y in range(12,-12,-1)]))
    time.sleep(1.5)
