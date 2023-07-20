# -*- coding: utf-8 -*-

# SampleRate : 64000

from math import sin,cos,pi

def VOICE(
    VOICE_VOICE:dict[float:complex],
    VOICE_FREQ:float = 1.0,
    VOICE_SIZE:int = 64000,
    VOICE_VOL:float = 1.0,
    VOICE_ENVELOP:float = lambda x : 1.0 
)->(None|list[int]):
    if VOICE_FREQ <= 0.0:
        return None
    
    track = [] # SoundTrack
    
    for i in range(VOICE_SIZE):
        x = i/64000
        s = 0.0
        # ergodic
        for key in VOICE_VOICE:
            s += \
                VOICE_VOICE[key].real * cos(key*VOICE_FREQ*x * 2*pi) + \
                VOICE_VOICE[key].imag * sin(key*VOICE_FREQ*x * 2*pi)
            s *= VOICE_VOL
            s *= VOICE_ENVELOP(i/VOICE_SIZE)
        track.append(int(s*30000))
    return track

def VOICE_VOICE_CONVERT(j:list[list])->dict:
    ret = {}
    for n in j:
        ret[n[0]]=complex(n[1],n[2])
    return ret

def VOICE_JSON_CONVERT(j:dict[float:complex])->list:
    ret = []
    for key in j:
        tmp = [ key , j[key].real , j[key].imag ]
        ret.append(tmp)
    return ret


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    a = VOICE({1:1j})
    plt.plot(range(64000),a)
    plt.show()