from Chords import Chords

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

def add_patterns():
    for add in [None, 2, 4, 9, 11, 13]: yield 'add' + str(add) if add else ''
def sus_patterns():
    for sus in [None, 2, 4]: yield 'sus' + str(sus) if sus else ''

with open('../../res/chords_3.tsv', mode='w', encoding='utf-8') as f:
    print('-----','三和音','-----')
    for chord in ['','m','dim','aug','sus2','sus4','-5','+5']:
        f.write(chord + '\t' + ','.join(','.join(Chords.Get(chord))) + '\n')

with open('../../res/chords_4.tsv', mode='w', encoding='utf-8') as f:
    print('-----','四和音','-----')
    for chord in ['6','m6','7','m7','M7','dim7','m7-5','M7+5','mM7']:
        f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_5.tsv', mode='w', encoding='utf-8') as f:
    print('-----','五和音','-----')
    #全テンションパターン網羅
    for t in tension_list_patterns():
        tension_str = ','.join(t)
        tension_str = '(' + tension_str + ')'
        f.write(tension_str + '\t' + ','.join(Chords.Get(tension_str)) + '\n')
        
with open('../../res/chords_another.tsv', mode='w', encoding='utf-8') as f:
    print('-----','他 add系','-----')
    for tone in [2, 4, 9, 11, 13]:
        chord = 'add' + str(tone)
        f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')
    print('-----','他 sus系','-----')
    for tone in [2, 4]:
        chord = 'sus' + str(tone)
        f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')
    print('-----','他 dim系','-----')#dim7のときは7thも半音下がる(根音から半音3つずつ足した音の1つ)。dim6は単に6th付与
    for tone in ['','6','7','M7']:
        chord = 'dim' + tone
        f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')
    print('-----','他 aug系','-----')
    for tone in ['', '6', '7','M7']:
        chord = 'aug' + tone
        f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_3mM_7_5da.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(3rd(m/M) + 7th + 5th(d/a))','-----')
    for third in ['','m']:
        for seventh in ['6','7','M7']:
            for fifth in ['-5','+5']:
                chord = third + seventh + fifth
                f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_3mM_7_5da.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(7th + 5th(d/a) + 3rd(sus))','-----')
    #msus4などは存在しない。3rdはmならm3,sus4ならP4になる。どちらを優先すべきか判断できない。
    for seventh in ['6','7','M7']:
        for sus in sus_patterns():
            for fifth in ['','-5','+5']:
                chord = seventh + fifth + sus
                f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_3mM_add.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(3rd(m/M) + add)','-----')
    for third in ['m']:
        for add in add_patterns():
            chord = third + add
            f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_3sus_add.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(3rd(sus) + add)','-----')
    for sus in sus_patterns():
        for add in add_patterns():
            if sus != add:
                chord = sus + add
                f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_3dimaug_7_add.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(3rd(dim/aug) + 7th + add)','-----')
    for third in ['dim','aug']:
        for seventh in ['','6','7','M7']:
            for add in add_patterns():
                chord = third + seventh + add
                f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_7_sus_add.tsv', mode='w', encoding='utf-8') as f:
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
                    f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')
                    
with open('../../res/chords_3dimaug_7_tension.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(3rd(dim/aug) + 7th + tension)','-----')
    for third in ['dim','aug']:
        for seventh in ['6','7','M7']:
            for t in tension_list_patterns():
                tension_str = ','.join(t)
                tension_str = '(' + tension_str + ')'
                chord = third + seventh + tension_str
                f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

with open('../../res/chords_3mM_7_5Pad_tension.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(3rd(m/M) + 7th + 5th(P/a/d) + tension)','-----')#susとmは一方のみ
    for third in ['','m']:
        for seventh in ['6','7','M7']:
            for fifth in ['','-5','+5']:
                for t in tension_list_patterns():
                    tension_str = ','.join(t)
                    tension_str = '(' + tension_str + ')'
                    chord = third + seventh + fifth + tension_str
                    f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

# addとtensionsの音程差が1しかないか否か
# (和音の構成音同士の音程差が半音1つ分しか無いなら響きが濁るため構成音にすべきでない)
def IsDiffOneInterval(add, tensions):
    for t in tensions:
        if 0 < t.count(str(add)) and 0 == t.count('--'): return True
    return False

with open('../../res/chords_3mM_7_5Pad_sus_add_tension.tsv', mode='w', encoding='utf-8') as f:
    print('-----','複合(7th + 5th(P/a/d) + sus + add + tension)','-----')#susとmは一方のみ
    for seventh in ['6','7','M7']:
        for fifth in ['','-5','+5']:
            for s in [None, 2, 4]:
                for a in [None, 2, 4, 9, 11, 13]:
                    for t in tension_list_patterns():
                        if s != a and not IsDiffOneInterval(a, t):
                            add = ''
                            if None is not a: add = 'add' + str(a)
                            sus = ''
                            if None is not s: sus = 'sus' + str(s)
                            tension_str = ','.join(t)
                            tension_str = '(' + tension_str + ')'
                            chord = seventh + fifth + sus + add + tension_str
                            f.write(chord + '\t' + ','.join(Chords.Get(chord)) + '\n')

print('***** 完了 *****')
