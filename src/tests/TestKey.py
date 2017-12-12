#!python3.6
import unittest
from MusicTheory.pitch.Key import Key
from MusicTheory.pitch.Accidental import Accidental
import Framework.ConstMeta
"""
Intervalのテスト。
"""
class TestKey(unittest.TestCase):
    def test_Keys(self): self.assertEqual(Key.Keys, {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11})
    def test_Perfects_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Key.Keys = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    
    def test_Get(self):
        for key, pitch_class in Key.Keys.items():
            with self.subTest(key=key):
                self.assertEqual(pitch_class, Key.Get(key))
    
    def test_Get_Accidental(self):
        for k, kp in Key.Keys.items():
            for acc_count in range(1, 4):
                for a, ap in Accidental.Accidentals.items():
                    key = k + a*acc_count
                    pitch = kp + (ap*acc_count)
                    with self.subTest(key=key):
                        self.assertEqual(pitch, Key.Get(key))
    
    def test_Get_int(self):
        with self.assertRaises(TypeError) as e:
            Key.Get(100)
        self.assertIn('引数nameはstr型にしてください。', str(e.exception))

    def test_Get_Invalid(self):
        with self.assertRaises(ValueError) as e:
            Key.Get('無効値')
        self.assertIn('keyは次のうちのいずれかにしてください。', str(e.exception))

    def test_Get_Bad_Combination(self):
        with self.assertRaises(ValueError) as e:
            Key.Get('c#')
        self.assertIn('keyは次のうちのいずれかにしてください。', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Key.Get('CC')
        self.assertIn('引数accidentalに使える文字は次のものだけです。', str(e.exception))


if __name__ == '__main__':
    unittest.main()
