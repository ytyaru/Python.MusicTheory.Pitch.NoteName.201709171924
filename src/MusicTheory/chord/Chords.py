from Tension import Tension
from AnotherChords import AnotherChords
#コードネームから構成音の音度名を取得する(IN:"Cm", OUT:[P1,m3,P5])
class Chords:
    @classmethod
    def Get(cls, name=None):
        chords = Tension.Get(name)#三和音、四和音に加えてテンション付与
        if None is chords: return Triad.Get('')
        AnotherChords.Set(name, chords)#dim,aug,sus,add系
        #重複削除＆並び替え
        return sorted(set(chords), key=lambda x: int(x[1:]))


if __name__ == '__main__':
    print('-----','三和音','-----')
    for chord in ['','m','dim','aug','sus2','sus4','-5','+5']:
        print(chord, Chords.Get(chord))
    print('-----','四和音','-----')
    for chord in ['6','m6','7','m7','M7','dim7','m7-5','M7+5','mM7']:
        print(chord, Chords.Get(chord))
    print('-----','五和音','-----')
    # '++13'から数値13だけを抜き取る
    def get_degree_value(degree_name):
        v = degree_name
        v = v.replace('+','')
        v = v.replace('-','')
        return int(v)
    
    #9,11,13と変化記号の組合せ '9','+11','--13'等
    def tension_note_patterns():
        for t in ('9', '11', '13'):
            for accidental in ('','+','-','--'):
                yield accidental + t
    
    #テンション1,2,3個の全パターン ('9'),('+9','-11'),('9','+11','--13')等
    def tension_list_patterns():
        for t in tension_note_patterns(): yield (t,)
        for t in tension_note_patterns():
            for s in tension_note_patterns():
                if get_degree_value(t) < get_degree_value(s): yield (t,s)
        for t in tension_note_patterns():
            for s in tension_note_patterns():
                for v in tension_note_patterns():
                    if get_degree_value(t) < get_degree_value(s) and get_degree_value(s) < get_degree_value(v): yield (t,s,v)

    #全テンションパターン網羅
    for t in tension_list_patterns():
        tension_str = ','.join(t)
        tension_str = '(' + tension_str + ')'
        print(tension_str, Chords.Get(tension_str))
        
    print('-----','他 add系','-----')
    for tone in [2, 4, 9, 11, 13]:
        chord = 'add' + str(tone)
        print(chord, Chords.Get(chord))
    print('-----','他 sus系','-----')
    for tone in [2, 4]:
        chord = 'sus' + str(tone)
        print(chord, Chords.Get(chord))
    print('-----','他 dim系','-----')#dim7のときは7thも半音下がる(根音から半音3つずつ足した音の1つ)。dim6は単に6th付与
    for tone in ['','6','7','M7']:
        chord = 'dim' + tone
        print(chord, Chords.Get(chord))
    print('-----','他 aug系','-----')
    for tone in ['', '6', '7','M7']:
        chord = 'aug' + tone
        print(chord, Chords.Get(chord))
    
    print('-----','複合(3rd(m/M) + 7th + 5th(d/a))','-----')
    for third in ['','m']:
        for seventh in ['6','7','M7']:
            for fifth in ['-5','+5']:
                chord = third + seventh + fifth
                print(chord, Chords.Get(chord))
    
    def add_patterns():
        for add in [None, 2, 4, 9, 11, 13]: yield 'add' + str(add) if add else ''
    def sus_patterns():
        for add in [None, 2, 4]: yield 'add' + str(add) if add else ''

    print('-----','複合(7th + 5th(d/a) + 3rd(sus))','-----')
    #msus4などは存在しない。3rdはmならm3,sus4ならP4になる。どちらを優先すべきか判断できない。
    for seventh in ['6','7','M7']:
        for sus in sus_patterns():
            for fifth in ['','-5','+5']:
                chord = seventh + fifth + sus
                print(chord, Chords.Get(chord))

    print('-----','複合(3rd(m/M) + add)','-----')
    for third in ['m']:
        for add in add_patterns():
            chord = third + add
            print(chord, Chords.Get(chord))

    print('-----','複合(3rd(sus) + add)','-----')
    for sus in sus_patterns():
        for add in add_patterns():
            if sus != add:
                chord = sus + add
                print(chord, Chords.Get(chord))

    print('-----','複合(3rd(dim/aug) + 7th + add)','-----')
    for third in ['dim','aug']:
        for seventh in ['','6','7','M7']:
            for add in add_patterns():
                chord = third + seventh + add
                print(chord, Chords.Get(chord))

    print('-----','複合(7th + sus + add)','-----')#susとmは一方のみ
    for seventh in ['6','7','M7']:
        for s in [None, 2, 4]:
            for a in [None, 2, 4, 9, 11, 13]:
                if s != a:
                    add = ''
                    if None is not a: add = 'add' + str(a)
                    sus = ''
                    if None is not s: sus = 'sus' + str(s)                    
                    chord = seventh + sus + add
                    print(chord, Chords.Get(chord))

    print('-----','複合(3rd(dim/aug) + 7th + tension)','-----')
    for third in ['dim','aug']:
        for seventh in ['6','7','M7']:
            for t in tension_list_patterns():
                tension_str = ','.join(t)
                tension_str = '(' + tension_str + ')'
                chord = third + seventh + tension_str
                print(chord, Chords.Get(chord))

    print('-----','複合(3rd(m/M) + 7th + 5th(P/a/d) + tension)','-----')#susとmは一方のみ
    for third in ['','m']:
        for seventh in ['6','7','M7']:
            for fifth in ['','-5','+5']:
                for t in tension_list_patterns():
                    tension_str = ','.join(t)
                    tension_str = '(' + tension_str + ')'
                    chord = third + seventh + fifth + tension_str
                    print(chord, Chords.Get(chord))

    print('-----','複合(7th + 5th(P/a/d) + sus + add + tension)','-----')#susとmは一方のみ
    for seventh in ['6','7','M7']:
        for fifth in ['','-5','+5']:
            for sus in [None, 2, 4]:
                for add in [None, 2, 4, 9, 11, 13]:
                    for t in tension_list_patterns():
                        if sus != add and str(sus) not in t and str(add) not in t:
#                        if sus != add and sus not in t and add not in t:
                            add = ''
                            if None is not a: add = 'add' + str(a)
                            sus = ''
                            if None is not s: sus = 'sus' + str(s)
                            tension_str = ','.join(t)
                            tension_str = '(' + tension_str + ')'
                            chord = seventh + fifth + sus + add + tension_str
                            print(chord, Chords.Get(chord))

