#!python3.6
import re
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from Framework.ConstMeta import ConstMeta
"""
音名から半音数を取得する。
"""
class Key(metaclass=ConstMeta):
    Keys = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
    
    @classmethod
    def Get(cls, name:str):
        if not (isinstance(name, str)): raise TypeError('引数nameはstr型にしてください。')
        if isinstance(name, int): return cls.__GetDegree(name)
        k, a = cls.__Split(name)
        key = cls.__GetKeyHalfToneNum(k)
        accidental = Accidental.Get(a)
        return key + accidental
        
    @classmethod
    def __Split(cls, name): return (name[0], name[1:])
    
    @classmethod
    def __GetKeyHalfToneNum(cls, key:str):
        if key not in cls.Keys: raise ValueError(f'keyは次のうちのいずれかにしてください。{cls.Keys.keys()}。: key={key}')
        return cls.Keys[key]

