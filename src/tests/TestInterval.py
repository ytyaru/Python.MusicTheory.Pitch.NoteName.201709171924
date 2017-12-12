#!python3.6
import unittest
from MusicTheory.pitch.Interval import Interval
from MusicTheory.pitch.Degree import Degree
from MusicTheory.pitch.Accidental import Accidental
import Framework.ConstMeta
"""
Intervalのテスト。
"""
class TestInterval(unittest.TestCase):
    def test_Perfects(self):
        self.assertEqual(Interval.Perfects, (1,4,5,8,11,12))
    def test_Perfects_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Interval.Perfects = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_Majors(self):
        self.assertEqual(Interval.Majors, (2,3,6,7,9,10,13,14))
    def test_Majors_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Interval.Majors = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))
    def test_Prefixes(self):
        self.assertEqual(Interval.Prefixes, ('P','M','m','a','d'))
    def test_Prefixes_NotSet(self):
        with self.assertRaises(Framework.ConstMeta.ConstMeta.ConstError) as e:
            Interval.Prefixes = 'some value.'
        self.assertEqual('readonly。再代入禁止です。', str(e.exception))

    def test_Get_Perfects(self):
        for degree in Interval.Perfects:            
            with self.subTest(prefix='P', degree=degree):
                self.assertEqual(Degree.Get(degree), Interval.Get('P'+str(degree)))
    def test_Get_Majors(self):
        for degree in Interval.Majors:
            with self.subTest(prefix='M', degree=degree):
                self.assertEqual(Degree.Get(degree), Interval.Get('M'+str(degree)))
    def test_Get_Minors(self):
        for degree in Interval.Majors:
            with self.subTest(prefix='m', degree=degree):
                self.assertEqual(Degree.Get(str(degree))-1, Interval.Get('m'+str(degree)))
    def test_Get_Augumented(self):
        degrees = list(Interval.Perfects) + list(Interval.Majors); degrees.sort();
        for degree in degrees:
            with self.subTest(prefix='a', degree=degree):
                self.assertEqual(Degree.Get(str(degree))+1, Interval.Get('a'+str(degree)))
    def test_Get_Diminished(self):
        for degree in Interval.Perfects:
            with self.subTest(prefix='d', degree=degree):
                self.assertEqual(Degree.Get(str(degree))-1, Interval.Get('d'+str(degree)))
        for degree in Interval.Majors:
            with self.subTest(prefix='d', degree=degree):
                self.assertEqual(Degree.Get(str(degree))-2, Interval.Get('d'+str(degree)))

    def test_Get_int(self):
        with self.assertRaises(TypeError) as e:
            Interval.Get(100)
        self.assertIn('引数nameはstr型にしてください。', str(e.exception))
    def test_Get_OutOfRange_0(self):
        with self.assertRaises(ValueError) as e:
            Interval.Get('P0')
        self.assertIn('degreeは1〜14までの自然数にしてください。', str(e.exception))
    def test_Get_OutOfRange_15(self):
        with self.assertRaises(ValueError) as e:
            Interval.Get('P15')
        self.assertIn('degreeは1〜14までの自然数にしてください。', str(e.exception))

    def test_Get_Invalid(self):
        with self.assertRaises(ValueError) as e:
            Interval.Get('無効値')
        self.assertIn('引数nameが有効な書式ではありません。', str(e.exception))

    def test_Get_Bad_Combination(self):
        with self.assertRaises(ValueError) as e:
            Interval.Get('P2')
        self.assertIn('prefixとdegreeの組合せが不正です。P(1|4|5|8|11|12), M|m(2|3|6|7|9|10|13|14), a|d(1〜14) のいずれかにしてください。', str(e.exception))
        for degree in Interval.Perfects:
            for prefix in ['M','m']:
                with self.subTest(prefix=prefix, degree=degree):
                    with self.assertRaises(ValueError) as e:
                        Interval.Get(prefix + str(degree))
                    self.assertIn('prefixとdegreeの組合せが不正です。P(1|4|5|8|11|12), M|m(2|3|6|7|9|10|13|14), a|d(1〜14) のいずれかにしてください。', str(e.exception))
        for degree in Interval.Majors:
            with self.subTest(prefix=prefix, degree=degree):
                with self.assertRaises(ValueError) as e:
                    Interval.Get('P' + str(degree))
                self.assertIn('prefixとdegreeの組合せが不正です。P(1|4|5|8|11|12), M|m(2|3|6|7|9|10|13|14), a|d(1〜14) のいずれかにしてください。', str(e.exception))


if __name__ == '__main__':
    unittest.main()
