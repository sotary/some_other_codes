#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:23:57 2018

@author: li
"""
import sounddevice as sd
import numpy as np
fs = 44100 # Hz
f = 440 # Hz
length = 10 #s
#myarray = np.arange(fs * length)
#myarray = np.sin(2 * np.pi * f / fs * myarray)
#sd.play(myarray,fs)
#sd.default.device[0]=3

print(sd.query_devices())

recording = sd.rec(frames=fs * length, samplerate=fs, blocking=True, channels=1)
