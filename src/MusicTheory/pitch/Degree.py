#!python3.6
import re
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from Framework.ConstMeta import ConstMeta
"""
音度から半音数を取得する。
"""
class Degree(metaclass=ConstMeta):
    __Pattern = re.compile(r'[0-9]{1,}')
    Degrees = ((1,0),(2,2),(3,4),(4,5),(5,7),(6,9),(7,11))
    
    @classmethod
    def Get(cls, name):
        if isinstance(name, int): return cls.__GetDegree(name)
        if not (isinstance(name, str)): raise TypeError('引数nameはstr型かint型にしてください。')
        d, a = cls.__Split(name)
        degree = cls.__GetDegree(int(d))
        accidental = Accidental.Get(a)
        return degree + accidental
        
    @classmethod
    def __Split(cls, name):
        match = cls.__Pattern.search(name)
        if not(match): raise ValueError('引数nameに有効な数字が含まれていません。1〜14までの自然数を含めてください。')
        return (name[match.start():match.end()+1], name[:match.start()])

    @classmethod
    def __GetDegree(cls, degree:int):
        if 0 < degree and degree < 8: return cls.__GetDefaultHalfToneNum(degree)
        elif 7 < degree and degree < 15: return cls.__GetDefaultHalfToneNum(degree - 7) + 12
        else: raise ValueError(f'degreeは1〜14までの自然数のみ有効です。degree={degree}')

    @classmethod
    def __GetDefaultHalfToneNum(cls, degree):
        for d in cls.Degrees:
            if d[0] == degree: return d[1]
        raise ValueError('引数degreeは1〜7までの自然数のみ有効です。')

