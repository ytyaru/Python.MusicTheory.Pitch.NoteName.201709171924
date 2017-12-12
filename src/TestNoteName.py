#!python3.6
import unittest
from MusicTheory.pitch.NoteName import NoteName
from MusicTheory.pitch.NoteNumber import NoteNumber
from MusicTheory.pitch.Key import Key
from MusicTheory.pitch.PitchClass import PitchClass
import Framework.ConstMeta
"""
NoteNameのテスト。
"""
class TestNoteName(unittest.TestCase):
    def test_Get_SPN(self):
        self.assertEqual(0, NoteName.Get('C-1'))
        self.assertEqual(69, NoteName.Get('A4'))
        self.assertEqual(127, NoteName.Get('G9'))
        lowerLimit = -1
        for k in Key.Keys.keys():
            for o in range(lowerLimit, lowerLimit+10, 1):
                with self.subTest(key=k, octave=o):
                    octave = o + abs(lowerLimit) if lowerLimit < 0 else o - abs(lowerLimit)
                    expected = PitchClass.Get(Key.Get(k))[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + str(o)))
                    expected = PitchClass.Get(Key.Get(k)+1)[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + '#' + str(o)))
                    expected = PitchClass.Get(Key.Get(k)-1)[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + 'b' + str(o)))
                
    def test_Get_YAMAHA(self):
        lowerLimit = -2
        self.assertEqual(0, NoteName.Get('C-2', lowerLimit))
        self.assertEqual(69, NoteName.Get('A3', lowerLimit))
        self.assertEqual(127, NoteName.Get('G8', lowerLimit))
        for k in Key.Keys.keys():
            for o in range(lowerLimit, lowerLimit+10, 1):
                with self.subTest(key=k, octave=o):
                    octave = o + abs(lowerLimit) if lowerLimit < 0 else o - abs(lowerLimit)
                    expected = PitchClass.Get(Key.Get(k))[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + str(o), lowerLimit))
                    expected = PitchClass.Get(Key.Get(k)+1)[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + '#' + str(o), lowerLimit))
                    expected = PitchClass.Get(Key.Get(k)-1)[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + 'b' + str(o), lowerLimit))
                
    def test_Get_ZERO(self):
        lowerLimit = 0
        self.assertEqual(0, NoteName.Get('C0', lowerLimit))
        self.assertEqual(69, NoteName.Get('A5', lowerLimit))
        self.assertEqual(127, NoteName.Get('G10', lowerLimit))
        for k in Key.Keys.keys():
            for o in range(lowerLimit, lowerLimit+10, 1):
                with self.subTest(key=k, octave=o):
                    octave = o + abs(lowerLimit) if lowerLimit < 0 else o - abs(lowerLimit)
                    expected = PitchClass.Get(Key.Get(k))[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + str(o), lowerLimit))
                    expected = PitchClass.Get(Key.Get(k)+1)[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + '#' + str(o), lowerLimit))
                    expected = PitchClass.Get(Key.Get(k)-1)[0] + (octave * (PitchClass.Max+1))
                    self.assertEqual(expected, NoteName.Get(k + 'b' + str(o), lowerLimit))
                
    def test_Get_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            NoteName.Get(100)
        self.assertIn('引数nameはstr型にしてください。', str(e.exception))
    
    def test_Get_Invalid_Format(self):
        with self.assertRaises(ValueError) as e:
            NoteName.Get('無効値')
        self.assertIn('引数nameが有効な書式ではありません。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C')
        self.assertIn('引数nameが有効な書式ではありません。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            NoteName.Get('c1')
        self.assertIn('引数nameが有効な書式ではありません。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C--1')
        self.assertIn('引数nameが有効な書式ではありません。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C+-1')
        self.assertIn('引数nameが有効な書式ではありません。', str(e.exception))
    
    def test_GetOctave_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            NoteName.Get('C0', '無効値')
        self.assertIn(f"引数lowerLimitはint型にしてください。", str(e.exception))
    
    def test_GetOctave_SPN_OutOfRange_LOW(self):
        lowerLimit = -1
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C-2', lowerLimit)
        typ = 'SPN'
        self.assertIn(f"lowerLimit={lowerLimit}のときoctaveは{lowerLimit}〜{lowerLimit+10}までです。", str(e.exception))
    
    def test_GetOctave_SPN_OutOfRange_UP(self):
        lowerLimit = -1
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C10', lowerLimit)
        self.assertIn(f"lowerLimit={lowerLimit}のときoctaveは{lowerLimit}〜{lowerLimit+10}までです。", str(e.exception))

    def test_GetOctave_YAMAHA_OutOfRange_LOW(self):
        lowerLimit = -2
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C-3', lowerLimit)
        typ = 'SPN'
        self.assertIn(f"lowerLimit={lowerLimit}のときoctaveは{lowerLimit}〜{lowerLimit+10}までです。", str(e.exception))
    
    def test_GetOctave_YAMAHA_OutOfRange_UP(self):
        lowerLimit = -2
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C9', lowerLimit)
        self.assertIn(f"lowerLimit={lowerLimit}のときoctaveは{lowerLimit}〜{lowerLimit+10}までです。", str(e.exception))

    def test_GetOctave_ZERO_OutOfRange_LOW(self):
        lowerLimit = 0
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C-1', lowerLimit)
        typ = 'SPN'
        self.assertIn(f"lowerLimit={lowerLimit}のときoctaveは{lowerLimit}〜{lowerLimit+10}までです。", str(e.exception))
    
    def test_GetOctave_ZERO_OutOfRange_UP(self):
        lowerLimit = 0
        with self.assertRaises(ValueError) as e:
            NoteName.Get('C11', lowerLimit)
        self.assertIn(f"lowerLimit={lowerLimit}のときoctaveは{lowerLimit}〜{lowerLimit+10}までです。", str(e.exception))


if __name__ == '__main__':
    unittest.main()
