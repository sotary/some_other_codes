#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:46:01 2018

@author: li
"""

import soundfile as sf
import sounddevice as sd
#default.device[0] is input device
print(sd.query_devices(None,'input')) 
#default.device[0] is  out device number