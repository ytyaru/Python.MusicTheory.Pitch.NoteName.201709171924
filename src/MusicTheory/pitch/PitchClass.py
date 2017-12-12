#!python3.6
import collections
from Framework.ConstMeta import ConstMeta
"""
半音数からピッチクラスと相対オクターブを取得する。
"""
class PitchClass(metaclass=ConstMeta):
    __PitchClass = collections.namedtuple('PitchClass', ['PitchClass', 'RelativeOctave'])
    Max = 11
    Min = 0

    @classmethod
    def Get(cls, halfToneNum:int):
        if not isinstance(halfToneNum, int): raise TypeError(f'引数halfToneNumはint型にしてください。: type(halfToneNum)={type(halfToneNum)}')
        pitchClass = halfToneNum % (cls.Max+1)
        relativeOctave = halfToneNum // (cls.Max+1)
        if pitchClass < cls.Min:
            pitchClass += (cls.Max+1)
        return cls.__PitchClass(pitchClass, relativeOctave)

    @classmethod
    def Validate(cls, pitchClass:int):
        if not isinstance(pitchClass, int): raise TypeError(f'引数pitchClassはint型にしてください。: type(pitchClass)={type(pitchClass)}')
        if pitchClass < cls.Min or cls.Max < pitchClass: raise ValueError(f'引数pitchClassは{cls.Min}〜{cls.Max}までの整数値にしてください。')
