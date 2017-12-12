#!python3.6
import re
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from MusicTheory.pitch.Degree import Degree
from Framework.ConstMeta import ConstMeta
"""
音程から半音数を取得する。
"""
class Interval(metaclass=ConstMeta):
    __PatternFormat = r'(?P<prefix>[P|M|m|a|d])(?P<degree>[0-9]{1,})'
    __Pattern = re.compile(__PatternFormat)
    
    def __new__(cls):
        p = [1,4,5]
        p += [i+7 for i in p]
        cls.Perfects = tuple(p)
        m = [2,3,6,7]
        m += [i+7 for i in m]
        cls.Majors = tuple(m)
        cls.Prefixes = ('P','M','m','a','d')
    
    @classmethod
    def Get(cls, name:str):
        if not (isinstance(name, str)): raise TypeError(f'引数nameはstr型にしてください。: type(name)={type(name)}')
        prefix, degree = cls.__Split(name)
        if degree < 1 or 14 < degree: raise ValueError(f'degreeは1〜14までの自然数にしてください。: degree={degree}')
        cls.__ValidPrefixDegree(prefix, degree)
        return Degree.Get(degree) + cls.__GetRelativeHalfToneNum(prefix, degree)
        
    @classmethod
    def __Split(cls, name):
        match = cls.__Pattern.search(name)
        if not(match): raise ValueError(f'引数nameが有効な書式ではありません。{cls.__PatternFormat}の書式にしてください。: name={name}')
        return match.group('prefix'), int(match.group('degree'))

    @classmethod
    def __ValidPrefixDegree(cls, prefix, degree):
        if 'P' == prefix and degree in cls.Perfects: return True
        elif prefix in ('M','m') and degree in cls.Majors: return True
        elif prefix in ('a','d') and (degree in cls.Perfects or degree in cls.Majors): return True
        else: raise ValueError(f'prefixとdegreeの組合せが不正です。P(1|4|5|8|11|12), M|m(2|3|6|7|9|10|13|14), a|d(1〜14) のいずれかにしてください。: prefix={prefix}, degree={degree}')

    @classmethod
    def __GetRelativeHalfToneNum(cls, prefix, degree):
        if 'P' == prefix or 'M' == prefix: return 0
        elif 'm' == prefix: return -1
        elif 'a' == prefix: return +1
        elif 'd' == prefix and degree in cls.Perfects: return -1
        elif 'd' == prefix and degree in cls.Majors: return -2
        else: raise ValueError(f'prefixやdegreeの値が不正か、組合せが不正です。P(1|4|5|8|11|12), M|m(2|3|6|7|9|10|13|14), a|d(1〜14) のいずれかにしてください。: prefix={prefix}, degree={degree}')

