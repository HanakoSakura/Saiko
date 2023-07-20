# -*- coding: utf-8 -*-
'''
Useless SAIKO
'''

VOICE_LIBRARY = {
    'default' : {
        1.0:0.0+0.0j
    },
    'sin' : {
        1.0:0.0+1.0j
    },
    'cos' : {
        1.0:1.0+0.0j
    }
}

from . import VOICE,ENVELOP,OUTPUT,pitch

def synthesis(score:dict)->list[int]:
    '''SAIKO Synthesis Main Magic'''
    global VOICE_LIBRARY
    
    # Get Global Voice
    useVoice = score.get('use voice',None)
    if useVoice == None:
        print('Cannot find Use VOice')
        useVoice = VOICE_LIBRARY['sin']
    # Get Score (list)
    useScore = score.get('score')
    # Get Global Beat Unit
    useBeat = score.get('beat',640)
    
    track = []
    
    i = 0
    p = int(i/len(useScore)*100)
    print('\rSynthesis',end=' |')
    print('#'*p,end='')
    print(' '*(100-p)+'|',i,'/',len(useScore),end='   ')
    
    for note in useScore:
        # Get note parameters
        
        Voice = note.get('voice')
        if VOICE_LIBRARY.get(Voice)==None :
            Voice = VOICE_LIBRARY.get(useVoice)
        else :
            Voice = VOICE_LIBRARY.get(Voice)
        
        
        freq = note.get('pitch')
        if freq==None :
            freq = 1000.0
        if type(freq)==str :
            freq = 440*(2**(pitch.PITCH[freq]/12))
            
        if note.get('freq') != None:
            freq = note.get('freq')
        
        vol = note.get('vol')
        if vol==None:
            vol = 1.0
        
        delay = note.get('beat')
        if delay==None:
            delay = 1
        
        # Start Magic
        tmp = Voice
        track += VOICE.VOICE(
            Voice,freq,delay*useBeat,vol,ENVELOP.ENVELOP['test1']
        )
        
        i+=1
        p = int(i/len(useScore)*100)
        print('\rSynthesis',end=' |')
        print('#'*p,end='')
        print('_'*(100-p)+'|',i,'/',len(useScore),end='   ')
        
    return track,len(useScore)


        