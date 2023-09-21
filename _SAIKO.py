# -*- coding: utf-8 -*-
import traceback

try:
    import sys
    import SAIKO
    import os
    import json
    import time

    # GetPath
    EXIST_PATH = os.path.split(os.path.realpath(__file__))[0]
    MAGIC_MATH = os.getcwd()
    
    GLOBAL_TRACK = []
    
    file_name = input('>')
        
    # Read Score
    with open(file_name+'.json') as f:
        SCORE = json.load(f)
    
    TEMP_TRACK = []
    SIZE = 0
    
    t1 = 1
    i = 1
    for score in SCORE:
        print(i,'/',len(SCORE))
        TEMP_TRACK,size=SAIKO.synthesis(score=score)
        GLOBAL_TRACK.append(TEMP_TRACK)
        SIZE += size
        i += 1
        
    
    tmp = []
    for t in GLOBAL_TRACK:
        tmp.append( len(t) )
    
    max_size = max(tmp)
    
    del tmp
    
    WRITE_TRACK = [0]*max_size
    
    t2 = 1
    
    print('Waiting to remix...')
    
    for t in GLOBAL_TRACK:
        for i in range(len(t)):
            WRITE_TRACK[i] += t[i]
    
    for i in range(len(WRITE_TRACK)):
        if WRITE_TRACK[i] > 32767:
            WRITE_TRACK[i] = 32767
        if WRITE_TRACK[i] < -32767:
            WRITE_TRACK[i] = -32767
        
    
    
    
    print()
    
    print('{:.3f}'.format((t2-t1)/1000000000),'s',end='  |  ')
    print('{:.3f}'.format((t2-t1)/size/1000000),'ms / item')
    
    print('Overwriting...')
    SAIKO.OUTPUT.OUTPUT(
        file_name=file_name+'.wav',w=WRITE_TRACK
    )
    
    
    
except Exception:
    traceback.print_exc()
    input()
