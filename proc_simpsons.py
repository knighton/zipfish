from collections import Counter, defaultdict
import csv


def extra_norm(s: str) -> str:
    s = s.lower()

    for c in ':().?!"\'':
        s = s.replace(c, '')

    if not c.isalnum():
        for c in s:
            assert c.isalnum() or c in '-_ ', s

    return s


f = 'data/simpsons_script_lines.csv'
s2n = Counter()
for x in csv.reader(open(f)):
    s = extra_norm(x[-2])
    for s in s.split():
        s2n[s] += 1

nn_ss = []
for s, n in s2n.items():
    nn_ss.append((n, s))
nn_ss.sort()

g = 'data/simpsons_token_freqs.txt'
with open(g, 'w') as g:
    for n, s in nn_ss:
        g.write(f'{n} {s}\n')

n2m = Counter()
for n in s2n.values():
    n2m[n] += 1

nn_mm = []
for n, m in n2m.items():
    nn_mm.append((n, m))
nn_mm.sort()

h = 'data/simpsons_token_freq_freqs.txt'
with open(h, 'w') as h:
    for n, m in nn_mm:
        h.write(f'{m} {n}\n')
