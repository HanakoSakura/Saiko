import ctypes
import wave

def OUTPUT(file_name:str,w:list[int]):
        f =wave.open(file_name,'wb')
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(64000)
        f.writeframes(\
            bytes((ctypes.c_int16 * len(w))(*w))\
        )
        f.close()