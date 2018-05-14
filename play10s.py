#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:10:21 2018

@author: li
"""

import sounddevice as sd
import numpy as np
myarray = np.load('./my_record_30s_1.npy')
fs = 44100 # Hz
sd.play(myarray,fs)