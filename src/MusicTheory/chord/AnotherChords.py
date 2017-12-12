import re
#変化系: 構成音の音高を変化する
#追加系: 構成音に音を追加する
class AnotherChords:
    #add,sus,dim,add系の変化をセットする。
    @classmethod
    def Set(cls, name, intervals):
        cls.Add(name, intervals)
        cls.Sus(name, intervals)
        cls.Dim(name, intervals)
        cls.Aug(name, intervals)
        
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

    #add系: 2, 4, 9, 11, 13 を追加する（6,7はC6,C7で済む。1,3,5は三和音内に存在する。C9,C11,C13だと7th以上9,11,13以下の音も含まれる）
    @classmethod
    def Add(cls, name, intervals):
        tensions = []
#        tension_pattern = re.compile(r'(\(.+\))')
        pattern = re.compile(r'add([+|-]*)(2|4|9|11|13)')
        match = pattern.search(name)
        if match:
            accidental, interval = match.groups()
            intervals.append(cls.__AccidentalToDegreeName(accidental) + interval)

    @classmethod
    def __Set(cls, intervals, target, value):
        for i in range(len(intervals)):
            if str(target) == intervals[i][1:]: intervals[i] = value
    
    #sus系: 3rdを2nd,4thに変える
    @classmethod
    def Sus(cls, name, intervals):
        if 0 < name.count('sus2'): cls.__Set(intervals, 3, 'M2')
        elif 0 < name.count('sus4'): cls.__Set(intervals, 3, 'P4')
        else: pass
        return intervals

    #dim系: 根音から半音3つ分ずつ音を重ねていく
    @classmethod
    def Dim(cls, name, intervals):
        if 0 < name.count('dim'):
            cls.__Set(intervals, 3, 'm3')
            cls.__Set(intervals, 5, 'd5')
            if 0 < name.count('M7'): cls.__Set(intervals, 7, 'M7')
            else:                    cls.__Set(intervals, 7, 'd7')

    #aug系: 根音から半音4つ分ずつ音を重ねていく
    @classmethod
    def Aug(cls, name, intervals):
        if 0 < name.count('aug'):
            cls.__Set(intervals, 3, 'M3')
            cls.__Set(intervals, 5, 'a5')

