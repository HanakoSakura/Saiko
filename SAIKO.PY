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
    
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    else:
        file_name = input('>')
        
    # Read Score
    with open(file_name+'.json') as f:
        SCORE = json.load(f)
    
    TEMP_TRACK = []
    
    t1 = time.perf_counter_ns()
    
    TEMP_TRACK,size=SAIKO.synthesis(SCORE)
    
    GLOBAL_TRACK.append(
        TEMP_TRACK
    )
    
    t2 = time.perf_counter_ns()
    
    print()
    
    print('{:.3f}'.format((t2-t1)/1000000000),'s',end='  |  ')
    print('{:.3f}'.format((t2-t1)/size/1000000),'ms / item')
    
    print('Overwriting...')
    SAIKO.OUTPUT.OUTPUT(
        file_name=file_name+'.wav',w=GLOBAL_TRACK[0]
    )
    
    
    if not '--noplay' in sys.argv:
        import winsound
        print('Playing...')
        winsound.PlaySound(file_name+'.wav',winsound.SND_ALIAS)
    
except Exception:
    traceback.print_exc()

