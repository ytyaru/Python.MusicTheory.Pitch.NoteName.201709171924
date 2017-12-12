from Triad import Triad
from Tetrad import Tetrad
import re
#五和音
class Tension:
    _names = ('9', '7-9')
    
    @classmethod
    def Get(cls, name=None):
        if None is name or 0 == len(name.strip()): return Triad.Get(name)
        # 四和音を取得する
        tetrad = Tetrad.Get(name)
        # テンション取得
        tension = cls.__GetTensions(name)
        tetrad += tension
        # C(9),C(11),C(13)などの場合7th付与（テンションがある＆6,7thが無い＆add系でない場合）
        if 0 < len(tension) and not cls.__IsExist7th(tetrad) and 'add' not in name:
            # 7th付与（ただし後でdim7の場合'd7'にすべき。M7の場合すでに'M7'音が存在するはず）
            tetrad.append('m7')
        return tetrad
        
    @classmethod
    def __IsExist7th(cls, intervals):
        for interval in intervals:
            if interval[-1] in ['6', '7']: return True
        return False
        
    #CM7(9, +11, -13): [長三和音,M7,M9,a11,d13]   複数テンションが付与される場合有り
    #C9: [長三和音,m7,M9]
    #CM9: [長三和音,M7,M9]
    #Cadd9: [長三和音,M9]
    #C13: [長三和音,m7,M9,M11,M13]
    @classmethod
    def __GetTensions(cls, name):
        tensions = []
        tension_pattern = re.compile(r'(\(.+\))')
        tension_value_pattern = re.compile(r'([+|-]*)(9|11|13)')
        match = tension_pattern.search(name)
        if not match: return tensions
#        print(match.groups()[0])
        for match in tension_value_pattern.finditer(match.groups()[0]):
            accidental, interval = match.groups()
            tensions.append(cls.__AccidentalToDegreeName(accidental) + interval)
        return tensions
        
    # 変化記号
    # なし: M
    # +   : a
    # -   : m
    # --  : d
    @classmethod
    def __AccidentalToDegreeName(cls, accidental):
        if None is accidental or 0 == len(accidental): return 'M'
        elif '+' == accidental: return 'a'
        elif '-' == accidental: return 'm'
        elif '--' == accidental: return 'd'
        else: raise Exception('変化記号のパターンは, +,-,--,(なし),のいずれかにしてください。')

"""
9	P1,M3,P5,m7,M9	長九の和音	Ninth
7-9	P1,M3,P5,m7,m9	短九の和音	MajorNinth
"""

