#!python3.6
import unittest
from MusicTheory.pitch.PitchClass import PitchClass
import Framework.ConstMeta
"""
PitchClassのテスト。
"""
class TestPitchClass(unittest.TestCase):
    def test_Max(self):
        self.assertEqual(11, PitchClass.Max)
    def test_Min(self):
        self.assertEqual(0, PitchClass.Min)
    def test_Max_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            PitchClass.Max = 'some value.'
        self.assertEqual(str(e.exception), 'readonly。再代入禁止です。')
    def test_Min_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            PitchClass.Min = 'some value.'
        self.assertEqual(str(e.exception), 'readonly。再代入禁止です。')
    def test_PitchClass(self):
        pitch_class = PitchClass.Get(0)
        self.assertTrue(hasattr(pitch_class, 'PitchClass'))
        self.assertTrue(hasattr(pitch_class, 'RelativeOctave'))
        #名前は変更されるかもしれない。この名前が最適か判断つかない。仮名である。（テストになっていない）
    def test_Get(self):
        for halfToneNum in range(12):
            self.assertEqual((halfToneNum, 0), PitchClass.Get(halfToneNum))
    def test_Get_Plus(self):
        self.assertEqual((11, 0), PitchClass.Get(11))
        self.assertEqual((0, 1), PitchClass.Get(12))
        self.assertEqual((1, 1), PitchClass.Get(13))
        self.assertEqual((11, 1), PitchClass.Get(23))
        self.assertEqual((0, 2), PitchClass.Get(24))
        for halfToneNum in range(12, 12*3):
            with self.subTest(halfToneNum=halfToneNum):
                self.assertEqual((halfToneNum % 12, halfToneNum // 12), PitchClass.Get(halfToneNum))
    def test_Get_Minus(self):
        self.assertEqual((11, -1), PitchClass.Get(-1))
        self.assertEqual((10, -1), PitchClass.Get(-2))
        self.assertEqual((0, -1), PitchClass.Get(-12))
        self.assertEqual((11, -2), PitchClass.Get(-13))
        self.assertEqual((0, -3), PitchClass.Get(-12*3))
        for halfToneNum in range(-12*3, 0):
            with self.subTest(halfToneNum=halfToneNum):
                expect = halfToneNum % 12
                if expect < 0: expect += 12
                self.assertEqual((expect, halfToneNum // 12), PitchClass.Get(halfToneNum))
    def test_Get_Invalid_Type(self):
        with self.assertRaises(TypeError) as e: #TypeError: not all arguments converted during string formatting
            PitchClass.Get('無効な型')
        self.assertIn('引数halfToneNumはint型にしてください。', str(e.exception))        

    def test_Validate(self):
        for pitchClass in range(PitchClass.Min, PitchClass.Max+1):
            PitchClass.Validate(pitchClass)
    def test_Validate_Invalid_Type(self):
        with self.assertRaises(TypeError) as e:
            PitchClass.Validate('無効な型')
        self.assertIn('引数pitchClassはint型にしてください。', str(e.exception))
    def test_Validate_OutOfRange_Minus(self):
        with self.assertRaises(ValueError) as e:
            PitchClass.Validate(-1)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(e.exception))
    def test_Validate_OutOfRange_128(self):
        with self.assertRaises(ValueError) as e:
            PitchClass.Validate(12)
        self.assertIn(f'引数pitchClassは{PitchClass.Min}〜{PitchClass.Max}までの整数値にしてください。', str(e.exception))
            

if __name__ == '__main__':
    unittest.main()
