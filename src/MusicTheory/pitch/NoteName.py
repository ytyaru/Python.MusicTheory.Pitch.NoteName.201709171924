#!python3.6
import re
import collections
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Accidental import Accidental
from MusicTheory.pitch.Key import Key
from MusicTheory.pitch.NoteNumber import NoteNumber
from Framework.ConstMeta import ConstMeta
"""
MIDIノート名からMIDIノート番号を取得する。(0〜127。C0〜G9)
octaveは国際式とYAMAHA式の2種類ある。(-1〜9。-2〜8)
https://www.g200kg.com/archives/2013/01/440hza4a3.html
"""
class NoteName(metaclass=ConstMeta):
    __PatternFormat = r'(?P<key>[A-G][b|♭|#|♯]?)(?P<octave>[\-]?[0-9]{1,})'#変化記号+,-は使えない。octaveの負数と被る。音名にbは使えない。変化記号のbと被る。
    __Pattern = re.compile(__PatternFormat)
    __OctaveTypeDescriptions = {
        'SPN': {'min':-1, 'ja':'国際式', 'Description': 'MIDI鍵盤の最低音はA0である。'}, 
        'YAMAHA': {'min':-2, 'ja':'ヤマハ式', 'Description': '根拠不明。'}, 
        'Zero': {'min':0, 'ja':'最低値0式', 'Description': '負数を無くすため最低値を0にする。'}}
    """
    def __new__(cls):
        OctaveType = collections.namedtuple('OctaveType', ['name', 'min', 'name_ja', 'description_ja'])
        cls.OctaveTypes = (
            OctaveType('SPN', -1, '国際式', 'MIDI鍵盤の最低音はA0である。'),
            OctaveType('YAMAHA', -2, 'ヤマハ式', '根拠不明。'),
            OctaveType('Zero', 0, '最低値0式', '負数を無くすため最低値を0にする。'),
        )
    """
    
    @classmethod
    def Get(cls, name:str, lowerLimit=-1):
        if not(name and isinstance(name, str)): raise TypeError(f'引数nameはstr型にしてください。: type(name)={type(name)}')
        k, o = cls.__Split(name)
        pitch_class = PitchClass.Get(Key.Get(k))[0]# B#の場合、Cになる。相対オクターブは無視される
        octave_class = cls.__GetOctave(o, lowerLimit)
        return NoteNumber.Get(pitch_class, octave_class)
    
    @classmethod
    def __Split(cls, name):
        match = cls.__Pattern.fullmatch(name)
        if not(match): raise ValueError(f'引数nameが有効な書式ではありません。{cls.__PatternFormat}の書式にしてください。: name={name}')
        return match.group('key'), int(match.group('octave'))
    
    #最低値を0とするOctaveClassに変換する
    # 国際式     :-1〜9
    # YAMAHA式   :-2〜8
    # OctaveClass:0〜10 (16進数表記は使えない。key(A〜G)と被るから)
    @classmethod
    def __GetOctave(cls, octave, lowerLimit=-1):
        if not(isinstance(lowerLimit, int)): raise TypeError(f'引数lowerLimitはint型にしてください。: type(lowerLimit)={type(lowerLimit)}')
        if lowerLimit not in [0, -1, -2]: raise ValueError(f'引数lowerLimitは次の値のいずれかにしてください。0, -1, -2。YAMAHA式は-2, 国際式は-1, 負数を無くすには0。: lowerLimit={lowerLimit}')
        if octave < lowerLimit or lowerLimit+10 < octave: raise ValueError(f"lowerLimit={lowerLimit}のときoctaveは{lowerLimit}〜{lowerLimit+10}までです。: lowerLimit={lowerLimit}, octave={octave}")
        if lowerLimit < 0: return octave + abs(lowerLimit)
        elif 0 < lowerLimit: return octave - abs(lowerLimit) # 最低値が0より大きい方式は現在存在しない
        else: return octave
    
