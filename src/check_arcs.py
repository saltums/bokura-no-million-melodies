# -*- coding: utf-8 -*-
"""使い方: python3 check_arcs.py arcs_new/arcs_XX.py  → 問題を表示。0件ならOK。"""
import sys, importlib.util, random
import ongaku_storyline_gen as g
import arcs2_gen as A
THEMES = [t['n'] for t in g.THEMES]
def leaves(n): return 1 if 'e' in n else sum(leaves(k) for k in n['n'])
def main(f):
    spec = importlib.util.spec_from_file_location('x', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    arcs, pt = m.ARCS, getattr(m, 'PT', {}); bad = 0
    keys = set()
    for a in arcs:
        k = a.get('k', '?'); P = []
        for fld in 'k nm st y0 ge vg th sa tx roles tr par yr cv lb ev d eh ea'.split():
            if fld not in a: P.append('欠落:' + fld)
        if P: print(k, P); bad += 1; continue
        if k in keys: P.append('keが重複')
        keys.add(k)
        if a['st'] not in ('band', 'duo', 'solo', 'rap', 'beat', 'inst'): P.append('stが不正:' + a['st'])
        if a['vg'] not in ('m', 'f', 'x'): P.append("vgは 'm','f','x'")
        for t in a['th']:
            if t not in THEMES: P.append('テーマが不正:' + t)
        if len(a['th']) < 2: P.append('thは2つ以上')
        N = len(a['d'])
        if not 3 <= N <= 5: P.append('dは3〜5個')
        if len(a['ev']) < N + 1: P.append('evはN+1個以上')
        if len(a['cv']) < N + 1: P.append('cvはN+1段階')
        if len(a['lb']) < 1: P.append('lbが空')
        if len(a['ea']) < 2: P.append('eaは2つ以上')
        for d in a['d']:
            if len(d) != 7: P.append('dの要素は7個(問い,筋の選択,別の選択,筋の結果,別の結果,筋の影響,別の影響)'); break
        tot = sum(len(c) for c in a['cv'][:N + 1])
        if len(a['yr']) < tot: P.append('yrは%d個以上(作品の総数)' % tot)
        if a['par'] not in pt: P.append('PTにparのキーがない:' + a['par'])
        else:
            if len(pt[a['par']]) < 16: P.append('PTは16曲以上(いま%d)' % len(pt[a['par']]))
            if len(set(pt[a['par']])) != len(pt[a['par']]): P.append('PTに重複')
        for fld, v in (('nm', a['nm']),):
            if not v or len(v) > 40: P.append('nmが空か長すぎ')
        try:
            pool = pt.get(a['par']) or ['t%d' % i for i in range(30)]
            t = A.build(a, 0, pool)
            L = leaves(t['t']); 
            if L != 2 ** N: P.append('葉の数が%d(期待%d)' % (L, 2 ** N))
            for e in a.get('eras', []):
                if e != A.era_of(a['y0']): A.build(a, 0, pool, era=e, nm='x')
        except Exception as ex:
            P.append('buildで例外: ' + repr(ex))
        if P: print(k, P); bad += 1
    print('arcs', len(arcs), 'NG', bad); return bad
if __name__ == '__main__': sys.exit(1 if main(sys.argv[1]) else 0)
