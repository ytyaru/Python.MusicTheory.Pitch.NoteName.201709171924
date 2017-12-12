#!python3.6
import re
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from Framework.ConstMeta import ConstMeta
"""
ピッチクラスとオクターブからMIDIノート番号を取得する。(0〜127。C0〜G9)
MIDIノート番号は最低音高=0としたときの半音数と同値である。
"""
class NoteNumber(metaclass=ConstMeta):
    Min = 0
    Max = 127

    @classmethod
    def Get(cls, pitchClass:int, relativeOctave:int):
        if not(isinstance(pitchClass, int) and isinstance(relativeOctave, int)): raise TypeError(f'引数pitchClass, relativeOctaveはint型にしてください。: type(pitchClass)={type(pitchClass)}, type(relativeOctave)={type(relativeOctave)}')
        PitchClass.Validate(pitchClass)
        noteNumber = pitchClass + (relativeOctave * (PitchClass.Max+1))
#        print('noteNumber:', noteNumber, 'pitchClass:', pitchClass, 'relativeOctave:', relativeOctave)
        if noteNumber < cls.Min or cls.Max < noteNumber: raise ValueError(f'ノート番号が{cls.Min}〜{cls.Max}の範囲外になりました。pitchClass, relativeOctave, 共に0以上の整数値にして範囲内になるようにしてください。: noteNumber={noteNumber}, pitchClass={pitchClass}, relativeOctave={relativeOctave}')
        return noteNumber
    
    @classmethod
    def Validate(cls, noteNumber:int):
        if not isinstance(noteNumber, int): raise TypeError(f'引数noteNumberはint型にしてください。: type(noteNumber)={type(noteNumber)}')
        if noteNumber < cls.Min or cls.Max < noteNumber: raise ValueError(f'引数noteNumberは{cls.Min}〜{cls.Max}までの整数値にしてください。')
    
    """    
    @classmethod
    def Get(cls, halfToneNum:int):
        if cls.Min < halfToneNum or halfToneNum < cls.Max: raise ValueError('halfToneNumは{cls.Min}〜{cls.Max}の整数値にしてください。')
        pitchClass, relativeOctave = PitchClass.Get(halfToneNum)
        return pitchClass + (relativeOctave * PitchClass.Max)
    """

