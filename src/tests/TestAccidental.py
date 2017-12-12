#!python3.6
import unittest
from MusicTheory.pitch.Accidental import Accidental
import Framework.ConstMeta
"""
Degreeのテスト。
"""
class TestAccidental(unittest.TestCase):
    def test_Accidentals(self):
        self.assertEqual(Accidental.Accidentals, {'♯': 1, '#': 1, '+': 1, '♭': -1, 'b': -1, '-': -1})
    def test_Accidentals_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Accidental.Accidentals = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_Get(self):
        for count in range(1, 4):
            for name, interval in Accidental.Accidentals.items():
                if not name: continue
                with self.subTest(accidenta=name, count=count):
                    self.assertEqual(Accidental.Get(name * count), interval * count)
    def test_Get_None(self): self.assertEqual(Accidental.Get(None), 0)
    def test_Get_Blank(self): self.assertEqual(Accidental.Get(''), 0)
    def test_Get_int(self):
        with self.assertRaises(TypeError) as e:
            Accidental.Get(100)
        self.assertIn('引数accidentalは文字列型にしてください。', str(e.exception))
    def test_Get_NotSameChars(self):
        with self.assertRaises(ValueError) as e:
            Accidental.Get('無効な文字')
        self.assertIn('引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。', str(e.exception))
    def test_Get_Invalid(self):
        with self.assertRaises(ValueError) as e:
            Accidental.Get('無無無')
        self.assertIn('引数accidentalに使える文字は次のものだけです。', str(e.exception))
    def test_Get_Valid_NotSameChars(self):
        with self.assertRaises(ValueError) as e:
            Accidental.Get('+-')
        self.assertIn('引数accidentalは同じ文字のみ連続使用を許されます。異なる文字を混在させることはできません。', str(e.exception))


if __name__ == '__main__':
    unittest.main()
