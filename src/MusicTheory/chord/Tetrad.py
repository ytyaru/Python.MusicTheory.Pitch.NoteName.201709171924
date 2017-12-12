from Triad import Triad
#四和音 https://ja.wikipedia.org/wiki/%E5%9B%9B%E5%92%8C%E9%9F%B3
class Tetrad:
    _names = ('7', 'm7', 'M7', 'dim7', 'M7+5', 'm7-5', 'mM7', '6', 'm6')
    @classmethod
    def Get(cls, name=None):
        triad = Triad.Get(name)
        if None is triad: return triad
        seventh = cls.GetSeventh(name)
        if None is seventh: return Triad.Get(name)
        else: return Triad.Get(name) + [seventh]
    #http://ww2.wt.tiki.ne.jp/~nk_sounds/compose06.htm
    #通常"M"は省略して"m"は省略しない。しかし7thは逆。"M"を明記し"m"を省略する。なぜなら7thは短7だから。他は長(2,3,6)。
    @classmethod
    def GetSeventh(cls, name):
        i = name.find('6')
        #構成音と半音程の差しかないと響きが汚いためその音は使わない。m6はP5と半音程差なので使わない。ただしオクターブ上げてテンション・ノートとして使える
        #https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q10125386745
        if -1 < i: return 'M6'            
        i = name.find('7')
        if -1 < i:
            if 0 < i and 'M' == name[i-1]: return 'M7'
            else: return 'm7'
#        return 'm7' # 五和音の場合7thが省略されている。例えばC9はm7を返す。CM9はM7を返す。
        return None

"""
7	P1,M3,P5,m7	属七の和音	Seventh
m7	P1,m3,P5,m7	短七の和音	MinorSeventh
M7	P1,M3,P5,M7	長七の和音	MajorSeventh
dim7	P1,m3,d5,d7	減七の和音	DiminishedSeventh
M7+5	P1,M3,a5,M7	増七の和音	AugmentedSeventh                augM7
m7-5	P1,m3,d5,m7	減五短七の和音	HalfDiminishedSeventh       dimm7
mM7	P1,m3,P5,M7	短三長七の和音	MinorMajorSeventh
6	P1,M3,P5,M6	メジャーシックスス	MajorSixth
m6	P1,m3,P5,M6	マイナーシックスス	MinorSixth


C5: P1, P5
C-5: P1, M3, d5
C+5: P1, M3, a5
Cdim: P1, m3, d5, (d7を付与する場合もある。dim7と使い分けたいならdimでは7thを付与しない)
Caug: P1, M3, a5
C7: P1, M3, P5, m7
Cdim7: P1, m3, d5, d7（dimとdim7を使い分ける場合、dimにはd7を加えない）
Caug7: P1, M3, P5, m7
CaugM7: P1, M3, P5, M7

+5M7
-5m7
"""
