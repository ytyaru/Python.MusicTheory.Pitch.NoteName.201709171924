#!python3.6
import unittest
from MusicTheory.pitch.Degree import Degree
from MusicTheory.pitch.Accidental import Accidental
import Framework.ConstMeta
"""
Degreeのテスト。
"""
class TestDegree(unittest.TestCase):
    def test_Degrees(self):
        self.assertEqual(Degree.Degrees, ((1,0),(2,2),(3,4),(4,5),(5,7),(6,9),(7,11)))
    def test_Degrees_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Degree.Degrees = 'some value.'
        self.assertEqual(str(e.exception), 'readonly。再代入禁止です。')
    def test_Get_1_7(self):
        for d in Degree.Degrees: self.assertEqual(d[1], Degree.Get(str(d[0])))
    def test_Get_8_14(self):
        for d in [(dd[0]+7,dd[1]+12) for dd in Degree.Degrees]: self.assertEqual(d[1], Degree.Get(str(d[0])))
    def test_Get(self):
        for degree in list(Degree.Degrees) + [(dd[0]+7,dd[1]+12) for dd in Degree.Degrees]:
            for acc_count in range(1, 4):
                for accidental in Accidental.Accidentals.keys():
                    if None is accidental: continue
                    with self.subTest(degree=degree, accidental=accidental*acc_count):
                        degreeName = (accidental * acc_count) + str(degree[0])
                        expected = degree[1] + (Accidental.Accidentals[accidental] * acc_count)
                        self.assertEqual(expected, Degree.Get(degreeName))
    def test_Get_None(self):
        with self.assertRaises(TypeError) as e:
            Degree.Get(None)
        self.assertIn('引数nameはstr型かint型にしてください。', str(e.exception))
    def test_Get_Blank(self):
        with self.assertRaises(ValueError) as e:
            Degree.Get('')
        self.assertIn('引数nameに有効な数字が含まれていません。1〜14までの自然数を含めてください。', str(e.exception))
    def test_Get_int(self):
        for degree in range(1, 15):
            i, o = (degree - 1, 0) if degree < 8 else ((degree - 1) - 7, 1)
            expected = Degree.Degrees[i][1] + o*12
            self.assertEqual(expected, Degree.Get(degree))
    def test_Get_int_0(self):
        with self.assertRaises(ValueError) as e:
            Degree.Get(0)
        self.assertIn('degreeは1〜14までの自然数のみ有効です。', str(e.exception))
    def test_Get_int_15(self):
        with self.assertRaises(ValueError) as e:
            Degree.Get(15)
        self.assertIn('degreeは1〜14までの自然数のみ有効です。', str(e.exception))
    def test_Get_NotInNumber(self):
        with self.assertRaises(ValueError) as e:
            Degree.Get('無効値')
        self.assertIn('引数nameに有効な数字が含まれていません。1〜14までの自然数を含めてください。', str(e.exception))
    def test_Get_OutOfRangeNumber_0(self):
        with self.assertRaises(ValueError) as e:
            Degree.Get('0')
        self.assertIn('degreeは1〜14までの自然数のみ有効です。', str(e.exception))
    def test_Get_OutOfRangeNumber_15(self):
        with self.assertRaises(ValueError) as e:
            Degree.Get('15')
        self.assertIn('degreeは1〜14までの自然数のみ有効です。', str(e.exception))


if __name__ == '__main__':
    unittest.main()
