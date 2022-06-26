ALPHABET = tuple(['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
                  'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                  'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])

ALPHABET_DICT = {0: 'а', 1: 'б', 2: 'в', 3: 'г', 4: 'д', 5: 'е', 6: 'ж', 7: 'з', 8: 'и', 9: 'й', 10: 'к',
                 11: 'л', 12: 'м', 13: 'н', 14: 'о', 15: 'п', 16: 'р', 17: 'с', 18: 'т', 19: 'у', 20: 'ф', 21: 'х',
                 22: 'ц',
                 23: 'ч', 24: 'ш', 25: 'щ', 26: 'ь', 27: 'ы', 28: 'э', 29: 'ю', 30: 'я'}

rashist_5_bi = ['ст', 'но', 'то', 'на', 'ен']


def Euclid_alg(a, b, advanced_flag):
    r = [a, b]
    q = [0]
    i = 2
    while r[-1] != 0:
        q.append(r[i - 2] // r[i - 1])
        r.append(r[i - 2] % r[i - 1])
        i += 1
    d = r[-2]
    if advanced_flag == False:
        return d
    else:
        u = [1, 0]
        v = [0, 1]
        k = 2
        while len(u) != len(r) - 1:
            u.append(u[k - 2] - q[k - 1] * u[k - 1])
            v.append(v[k - 2] - q[k - 1] * v[k - 1])
            k += 1
        if u[-1] * a + v[-1] * b == 1:
            # print(f'The reversed for {a} exist')
            return u[-1], v[-1]
        elif v[-1] * a + u[-1] * b == 1:
            # print(f'The reversed for {a} exist')
            return v[-1], u[-1]
        else:
            # print(f'The reversed for {a} doesn\'t exist')
            return None, None


def linear_comparison(a, b, n):
    x = []
    d = Euclid_alg(a, n, False)
    if d == 1:
        a_reversed, n_reversed = Euclid_alg(a, n, True)
        x.append((a_reversed * b) % n)
    elif b % d != 0:
        return f'There is no solution'
    else:
        n1 = n // d
        a1 = a // d
        b1 = b // d
        temp = linear_comparison(a1, b1, n1)
        x0 = temp[0]
        for i in range(d):
            x.append(x0 + i * n1)
    return x


def print_chart(list):
    for i in list:
        print(i[0], ':', i[1])


def gram_freq(dict, num):
    for key in dict:
        dict[key] /= num
    mono_list = list(dict.items())
    mono_list.sort(key=lambda i: i[1], reverse=True)
    return mono_list


def one_chr_to_num(smb):
    for j in range(32):
        if smb == ALPHABET_DICT[j]:
            smb = j
            break
    return smb


def one_num_to_chr(smb):
    smb = ALPHABET_DICT[smb]
    return smb


def transform_bi_to_num(bi, n):
    two_letters = list(bi)
    Xi = one_chr_to_num(two_letters[0]) * n + one_chr_to_num(two_letters[1])
    return Xi


def list_bi_to_num(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(transform_bi_to_num(lst[i], 31))
    return new_list


def transform_num_to_bi(num, n):
    lt1 = one_num_to_chr(num // n)
    lt2 = one_num_to_chr(num % n)
    return lt1 + lt2


def list_num_to_bi(list):
    list = [transform_num_to_bi(list[i], 31) for i in range(len(list))]
    return list


def rashism_recognizer(dict):
    banned_bigrams = ['аь', 'оь', 'уь', 'ыь', 'йь', 'еь', 'ць', 'юь', 'ьь', 'аы', 'оы', 'уы', 'ьы',
                      'йы', 'еы', 'жы', 'щы', 'юы', 'ыы', 'шы', 'хь', 'эы', 'эи', 'эю', 'эа', 'эе',
                      'эь', 'эя', 'эж', 'эч', 'эц', 'эщ', 'гь']
    for key in dict.keys():
        for bi in banned_bigrams:
            if key == bi:
                return False
    return True


def system_equat(X1, Y1, X2, Y2, m):
    a = (X1 - X2) % (m ** 2)
    b = (Y1 - Y2) % (m ** 2)
    A = linear_comparison(a, b, m ** 2)
    B = []
    if isinstance(A, str) == False:
        for ai in A:
            B.append((Y1 - ai * X1) % (m ** 2))
        return A, B
    else:
        return False

def make_dict(our_list):
    divide_list = [list(our_list[i]) for i in range(len(our_list))]
    new_list = []
    for i in range(len(divide_list)):
        for j in range(2):
            new_list.append(divide_list[i][j])
    i = 1
    dict = {}
    while i < len(new_list):
        prev = new_list[i - 1]
        char = new_list[i]
        word = prev + char
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
        i += 1
    return dict


def enciphering(a, b, m, cipher_list):
    num_list = list_bi_to_num(cipher_list)
    for i in range(len(a)):
        new_list = []
        a_rev, m_rev = Euclid_alg(a[i], m**2, True)
        if a_rev != None:
            for j in range(len(num_list)):
                temp = transform_num_to_bi((a_rev * (num_list[j] - b[i])) % (m ** 2), 31)
                new_list.append(temp)
            new_list_dict = make_dict(new_list)
            if rashism_recognizer(new_list_dict) == True:
                print('You\'ve found your plaintext:\n')
                print_text(new_list)
                print (f'\nYour key is: ({a[i]}, {b[i]})')
                return True
    return False


def print_text(list):
    for i in range(len(list)):
        print(list[i], end='')

def brute_force(cipher_bi, plain_bi, cipher_list):
    num_cipher_bi = list_bi_to_num(cipher_bi)
    num_plain_bi = list_bi_to_num(plain_bi)
    break_flag = False
    for y1 in num_cipher_bi:
        for x1 in num_plain_bi:
            for y2 in num_cipher_bi:
                for x2 in num_plain_bi:
                    if (y2 != y1 and x2 != x1):
                        if system_equat(x1, y1, x2, y2, 31) != False:
                            a, b = system_equat(x1, y1, x2, y2, 31)
                            if enciphering(a, b, 31, cipher_list) != False:
                                break_flag = True
                                break
                if break_flag:
                    break
            if break_flag:
                break
        if break_flag:
            break



data_list = []
bigram_data = []
bigram_dict = {}
bigram_amount = 0

with open('var.txt', 'r') as text:
    for char in text.read():
        if char in ALPHABET:
            data_list.append(char)

i = 1
while i < len(data_list):
    prev = data_list[i - 1]
    char = data_list[i]
    bigram = prev + char
    bigram_data.append(bigram)
    if bigram in bigram_dict:
        bigram_dict[bigram] += 1
    else:
        bigram_dict[bigram] = 1
    bigram_amount += 1
    i += 2

bigram_list = gram_freq(bigram_dict, bigram_amount)

cipher_5_bi = ['сг', 'жэ', 'ям', 'нг', 'тм']
print('\nFive the most frequent bigrams in the ciphertext:')
print(cipher_5_bi)
print('\nYour ciphertext:\n')
print_text(bigram_data)
print('\n')
brute_force(cipher_5_bi, rashist_5_bi, bigram_data)

