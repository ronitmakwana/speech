#!/usr/bin/env python3

import argparse
from hashlib import blake2b
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import pyaudio

# def show():
#     q = queue.Queue()

#     def int_or_str(text):
#         """Helper function for argument parsing."""
#         try:
#             return int(text,',----')
#         except ValueError:
#             return text

#     def callback(indata, frames, time, status):
#         """This is called (from a separate thread) for each audio block."""
#         if status:
#             print(status, file=sys.stderr)
#         q.put(bytes(indata))

#     parser = argparse.ArgumentParser(add_help=False)
#     parser.add_argument(
#         '-l', '--list-devices', action='store_true',
#         help='show list of audio devices and exit')
#     args, remaining = parser.parse_known_args()
#     if args.list_devices:
#         print(sd.query_devices())
#         parser.exit(0)
#     parser = argparse.ArgumentParser(
#         description=__doc__,
#         formatter_class=argparse.RawDescriptionHelpFormatter,
#         parents=[parser])
#     parser.add_argument(
#         '-f', '--filename', type=str, metavar='FILENAME',
#         help='audio file to store recording to')
#     parser.add_argument(
#         '-d', '--device', type=int_or_str,
#         help='input device (numeric ID or substring)')
#     parser.add_argument(
#         '-r', '--samplerate', type=int, help='sampling rate')
#     args = parser.parse_args(remaining)

#     try:
#         if args.samplerate is None:
#             device_info = sd.query_devices(args.device, 'input')
#             # soundfile expects an int, sounddevice provides a float:
#             args.samplerate = int(device_info['default_samplerate'])

#         model = vosk.Model(lang="en-us")

#         if args.filename:
#             dump_fn = open(args.filename, "wb")
#         else:
#             dump_fn = None

#         with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
#                                 channels=1, callback=callback):
#                 print('#' * 80)
#                 print('Press Ctrl+C to stop the recording')
#                 print('#' * 80)
                
#                 rec = vosk.KaldiRecognizer(model, args.samplerate)
#                 while True:
                    
#                     data = q.get()
#                     if rec.AcceptWaveform(data):
#                         a = rec.Result()
#                         print(a)
#                         txt = json.loads(a)
#                         b = list(txt.values())
#                         print(b)
#                         lat=[]
#                         long=[]
                        
#                         for i in b:
#                             print(i)
#                             c = i
#                             if i == 'latitude':
#                                 print('speck latitude')
#                                 if i =="one" or "four":
#                                     lat.append(c)
#                             elif i=="long":
#                                 print('speack longitute')
#                                 if i == "three":
#                                     long.append(c)
#                             elif i == 'stop':
#                                 exit()
#                             elif i == 'stat':
#                                 def run(runfile):
#                                     with open(runfile,"r") as rnf:
#                                         exec(rnf.read())
#                                 run('/home/ronit/vosk-api/python/example/try.py')
                         
                               
#                             elif i == 'so':
#                                 print(long,'-------------',lat)


                    
#                         print(type(a))
                    


                    
                        
#                     # else:
        
#                     #     print(rec.PartialResult())
#                     #     print('mid')
#                     # if dump_fn is not None:
#                     #     dump_fn.write(data)
#                     #     print('lst')

                   
                

#     except KeyboardInterrupt:
#         print('\nDone')
#     # return i
#     #     parser.exit(0)
#     # except Exception as e:
#     #     parser.exit(type(e).__name__ + ': ' + str(e))

                    


# show()


# model1 = vosk.Model(lang="en-us")
# reco = vosk.KaldiRecognizer(model1,16000)

# cap = pyaudio.PyAudio()
# stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True,frames_per_buffer=8192)
# stream.start_stream()
# while True:
#     data=stream.read(4096)
#     if len(data) == 0:
#         break
#     if reco.AcceptWaveform(data):
#         print(reco.Result())



#!/usr/bin/env python3

import argparse
from hashlib import blake2b
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import pyaudio
# from speak import listen
from vosk import SetLogLevel

SetLogLevel(-1) # Hide Vosk logs


def show():
    q = queue.Queue()

    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text,',----')
        except ValueError:
            return text

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        '-f', '--filename', type=str, metavar='FILENAME',
        help='audio file to store recording to')
    parser.add_argument(
        '-d', '--device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-r', '--samplerate', type=int, help='sampling rate')
    args = parser.parse_args(remaining)

    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])

        model = vosk.Model(lang="en-us")

        if args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
                                channels=1, callback=callback):
                print('#' * 80)
                print('Press Ctrl+C to stop the recording')
                print('#' * 80)
                
                rec = vosk.KaldiRecognizer(model, args.samplerate)
                while True:
                    
                    data = q.get()
                    if rec.AcceptWaveform(data):
                        a = rec.Result()
                        print(a)
                        txt = json.loads(a)
                        b = list(txt.values())
                        print(b)
                        lat=[]
                        long=[]
                        # x = listen()
                        # print('--000',x)
                        
                        for i in b:
                            print(i)
                            c = i
                            if i == 'latitude':
                                print('speck latitude')
                                if i =="one" or "four":
                                    lat.append(c)
                          
                            elif i=="he":
                                print('speack longitute')
                                
                                model1 = vosk.Model(lang="en-us")
                                reco = vosk.KaldiRecognizer(model1,16000)

                                cap = pyaudio.PyAudio()
                                stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True,frames_per_buffer=8192)
                                stream.start_stream()
                                while True:
                                    data=stream.read(4096)
                                    if len(data) == 0:
                                        break
                                    if reco.AcceptWaveform(data):
                                        s = reco.Result()

                                        dic = json.loads(s)
                                        x = dic.values()
                                        lt = list(x)
                                        for j in lt:
                                            print(j)
                                            long.append(j)
                                            if j == "go":
                                                print('----------',long)
                                    
                                           
                                        if j == "out":
                                            
                                           break


                                
                                # if i == "three":
                                #     long.append(c)
                            elif i == 'stop':
                                 parser.exit(0)
                            elif i == 'stat':
                                def run(runfile):
                                    with open(runfile,"r") as rnf:
                                        exec(rnf.read())
                                run('/home/ronit/vosk-api/python/example/try.py')
                         
                               
                            elif i == 'so':
                                print(long,'-------------',lat)


                    
                        print(type(a))
                    


                    
                        
                    # else:
        
                    #     print(rec.PartialResult())
                    #     print('mid')
                    # if dump_fn is not None:
                    #     dump_fn.write(data)
                    #     print('lst')

                   
                

    except KeyboardInterrupt:
        print('\nDone')
    # return i
    #     parser.exit(0)
    # except Exception as e:
    #     parser.exit(type(e).__name__ + ': ' + str(e))

                    


show()


