# -*- coding: utf-8 -*-
from math import gcd
import heapq

monograms = list('абвгдежзийклмнопрстуфхцчшщьыэюя')
most_used_ru_bigrams = ['ст', 'но', 'ен', 'то', 'на']
bigrams_text = [i + j for i in monograms for j in monograms]


def frequency_bigrams(message, bigrams):
    return {i: message.count(i) / len(message) for i in bigrams}


def get_five_bigrams(frequency):
    return heapq.nlargest(5, frequency, key=frequency.get)


def read_file(filename: str):
    text = open(filename, 'r', encoding='utf-8')
    texts = str(text.read())
    return texts


def extended_euclid(a, n):
    a = int(a)
    n = int(n)
    if (gcd(a, n)) != 1:
        return False
    u = [1, 0]
    v = [0, 1]
    r = [a, n]
    i = 2
    while u[-1] * a + v[-1] * n != 1:
        q = r[i - 2] // r[i - 1]
        r.append(r[i - 2] % r[i - 1])
        u.append(u[i - 2] - q * u[i - 1])
        v.append(v[i - 2] - q * v[i - 1])
        i += 1
    if u[-1] < 0:
        u[-1] += n
    return u[-1]


def calc_congruence(a, b, n):
    d = gcd(a, n)
    if d == 1:
        return [(extended_euclid(a, n) * b) % n]
    if b % d != 0:
        return False
    res = []
    a1 = a / d
    b1 = b / d
    n1 = n / d
    x0 = (b1 * extended_euclid(a1, n1)) % n1
    for i in range(d):
        res.append(int(x0 + i * n1))
    return res


def text_to_bigrams(text):
    res = []
    for i in range(1, len(text), 2):
        let1 = text[i-1]
        let2 = text[i]
        res.append(calc_bigram_num(let1, let2))
    return res


def calc_bigram_num(let1, let2, m=31):
    x1 = monograms.index(let1)
    x2 = monograms.index(let2)
    return m * x1 + x2


def get_letters(x, m=31):
    x1 = monograms[x // m]
    x2 = monograms[x % m]
    return x1, x2


def find_keys(bi_ru, bi_cy):
    res = []
    for i in range(5):
        bi_ru1 = bi_ru[i]
        bi_1 = bi_cy[i]
        for j in range(5):
            bi_ru2 = bi_ru[j]
            bi_2 = bi_cy[j]
            key = _find_key((bi_ru1, bi_ru2), (bi_1, bi_2))
            if key:
                res.append(key)
    return res


def _find_key(bigrams_ru, bigrams_cypher, m=31):
    X1 = calc_bigram_num(bigrams_ru[0][0], bigrams_ru[0][1])
    X2 = calc_bigram_num(bigrams_ru[1][0], bigrams_ru[1][1])
    Y1 = calc_bigram_num(bigrams_cypher[0][0], bigrams_cypher[0][1])
    Y2 = calc_bigram_num(bigrams_cypher[1][0], bigrams_cypher[1][1])
    Y = Y1 - Y2
    X = X1 - X2
    if Y < 0:
        Y += m*m
    if X < 0:
        X += m*m
    a = calc_congruence(X, Y, m ** 2)
    b = []
    if not a:
        return None
    for r in a:
        b.append((Y1 - r * X1) % m ** 2)
    return a, b


def get_x(y, a, b, m=31):
    a_1 = extended_euclid(a, m ** 2)  # right
    if not a_1:
        return False
    return (a_1 * (y - b)) % m ** 2


def decypher_text(text, key):
    a = key[0]
    b = key[1]
    res = ''
    for y in text:
        x = get_x(y, a, b)
        x_let = get_letters(x, 31)
        res += x_let[0] + x_let[1]
    return res


def check_if_russian(text):
    if text.count('о')/len(text) < 0.07:
        return False
    if text.count('е')/len(text) < 0.06:
        return False
    if text.count('а')/len(text) < 0.05:
        return False
    if text.count('и')/len(text) < 0.05:
        return False
    if text.count('ф')/len(text) > 0.01:
        return False
    if text.count('э')/len(text) > 0.01:
        return False
    if text.count('щ')/len(text) > 0.05:
        return False
    return True


def find_correct(keys, num_text, nmax=1):
    res = []
    count = 1
    for key in keys:
        a, b = key
        for i in range(len(a)):
            txt = decypher_text(num_text, (a[i], b[i]))
            if check_if_russian(txt):
                res.append((txt, (a[i], b[i])))
                if count == nmax:
                    return res
                count += 1
    return res


def main():
    text = read_file('11.txt').replace('\n', '')
    bigs = frequency_bigrams(text, bigrams_text)
    most_used = get_five_bigrams(bigs)
    print(most_used)
    keys = find_keys(most_used_ru_bigrams, most_used)
    print(keys)
    num_text = text_to_bigrams(text)
    # txt = decypher_text(num_text, (13, 151))
    res = find_correct(keys, num_text, 1)
    print(f'keys, a:{res[0][1][0]}, b:{res[0][1][1]}')
    print(f'text: {res[0][0]}')


if __name__ == '__main__':
    main()
