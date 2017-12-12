#三和音 https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
#和音名(ChordName)から音程名(IntervalName)を返す
#三和音のうち、長、短の2種を実装する
#増減の2種は別に実装する
class Triad:
    @classmethod
    def Get(cls, name):
#        if None is name or 0 == len(name.strip()): return None
        if None is name: return None
        elif 0 == len(name.strip()): return ['P1','M3','P5']
        else: return ['P1', cls.GetThird(name), cls.GetFifth(name)]
    @classmethod
    def GetThird(cls, name): return 'm3' if 'm' == name[0] else 'M3'
    @classmethod
    def GetFifth(cls, name):
        if 0 < name.count('-5'): return 'd5'
        elif 0 < name.count('+5'): return 'a5'
        else: return 'P5'

