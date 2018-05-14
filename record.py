#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:32:39 2018

@author: li
"""
import argparse
import tempfile
import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

class record(object):
    filename = tempfile.mktemp(prefix='delme_rec_unlimited_',
                                        suffix='.wav', dir='')
    device_info=sd.query_devices(None,'input')
    samplerate=int(device_info['default_samplerate'])
    channels=1
    subtype=None
    q = queue.Queue()
    device=3
    def callback(self,indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.q.put(indata.copy())
    
    def __init__(self):
        pass
    def record_run(self):
        try:
            with sf.SoundFile(self.filename, mode='x', samplerate=self.samplerate,
                      channels=self.channels, subtype=self.subtype) as file:
                with sd.InputStream(samplerate=self.samplerate, device=self.device,
                            channels=self.channels, callback=self.callback):
                    print('#' * 80)
                    print('press Ctrl+C to stop the recording')
                    print('#' * 80)
                    while True:
                        file.write(self.q.get())
        except KeyboardInterrupt:
            print('\nRecording finished: ' + repr(self.filename))
if __name__=='__main__':
    recordnow=record()
    recordnow.record_run()
        