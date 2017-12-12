#!python3.6
import unittest
from MusicTheory.pitch.NoteNumber import NoteNumber
from MusicTheory.pitch.PitchClass import PitchClass
import Framework.ConstMeta
"""
NoteNumberのテスト。
"""
class TestNoteNumber(unittest.TestCase):
    def test_Min(self): self.assertEqual(0, NoteNumber.Min)
    def test_Min_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            NoteNumber.Min = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))    
    def test_Max(self): self.assertEqual(127, NoteNumber.Max)
    def test_Max_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            NoteNumber.Max = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    
    def test_Get(self):
        for halfToneNumber in range(NoteNumber.Min, NoteNumber.Max+1):
            with self.subTest(halfToneNumber=halfToneNumber):
                self.assertEqual(halfToneNumber, NoteNumber.Get(*PitchClass.Get(halfToneNumber)))
    
    """
    def test_Get(self):
        for halfToneNumber in range(NoteNumber.Min, NoteNumber.Max+1):
            NoteNumber.Get(halfToneNumber)
            with self.subTest(halfToneNumber=halfToneNumber):
                self.assertEqual(halfToneNumber, NoteNumber.Get(halfToneNumber))
    """
    
    def test_Get_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            NoteNumber.Get('pitch','octave')
        self.assertIn('引数pitchClass, relativeOctaveはint型にしてください。', str(e.exception))
    
    def test_Get_OutOfRange_Minus(self):
        with self.assertRaises(ValueError) as e:
            NoteNumber.Get(0, -1)
        self.assertIn(f'ノート番号が{NoteNumber.Min}〜{NoteNumber.Max}の範囲外になりました。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            NoteNumber.Get(-1, 0)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            NoteNumber.Get(-1, -1)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(e.exception))

    def test_Validate(self):
        for pitchClass in range(NoteNumber.Min, NoteNumber.Max+1):
            NoteNumber.Validate(pitchClass)
    def test_Validate_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            NoteNumber.Validate('無効な型')
        self.assertIn('引数noteNumberはint型にしてください。', str(e.exception))
    def test_Validate_OutOfRange_Minus(self):
        with self.assertRaises(ValueError) as e:
            NoteNumber.Validate(-1)
        self.assertIn(f'引数noteNumberは{NoteNumber.Min}〜{NoteNumber.Max}までの整数値にしてください。', str(e.exception))
    def test_Validate_OutOfRange_128(self):
        with self.assertRaises(ValueError) as e:
            NoteNumber.Validate(128)
        self.assertIn(f'引数noteNumberは{NoteNumber.Min}〜{NoteNumber.Max}までの整数値にしてください。', str(e.exception))


if __name__ == '__main__':
    unittest.main()
