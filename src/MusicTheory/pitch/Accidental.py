#!python3.6
from Framework.ConstMeta import ConstMeta
"""
変化記号から相対半音数を取得する。
"""
class Accidental(metaclass=ConstMeta):
    Accidentals = {'♯': 1, '#': 1, '+': 1, '♭': -1, 'b': -1, '-': -1}

    @classmethod
    def Get(cls, accidental:str):
        if not cls.__CheckParameter(accidental): return 0
        return sum([cls.Accidentals[c] for c in accidental])

    @classmethod
    def __CheckParameter(cls, accidental):
        if None is accidental: return False
        if not isinstance(accidental, str): raise TypeError(f'引数accidentalは文字列型にしてください。: {cls.Accidentals.keys()}')
        if 0 == len(accidental): return False
        cls.__IsSameChars(accidental)
        if accidental[0] not in cls.Accidentals.keys(): raise ValueError(f'引数accidentalに使える文字は次のものだけです。: {cls.Accidentals.keys()}')
        return True

    @classmethod
    def __IsSameChars(cls, accidental):
        for c in accidental:
            if c != accidental[0]: raise ValueError(f'引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。: {accidental}')
        return True
