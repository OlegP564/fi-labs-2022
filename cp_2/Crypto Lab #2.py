from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
all_r = ['да', 'нет', 'мама', 'хорол', 'мамапапа', 'какутебядела']

m = 32

probability = [0.07657778115128833, 0.016759600394700733, 0.043686831825958, 0.0162574663249041,
              0.029881648167502585, 0.08499728497276214, 0.011135698812978415, 0.014484816283156905,
              0.06228797972779662, 0.009776433563575429, 0.03135418552102248, 0.044598847427146766,
              0.030166580058270907, 0.061594334059286854, 0.11077194355078852, 0.024570704564165144,
              0.03885233171210201, 0.05001839211999837, 0.06267800944712704, 0.028835340896484478,
              0.001070830097682593, 0.008219817947205858, 0.002677659121031827, 0.017307276856874273,
              0.008027138594842033, 0.002931061663231525, 0.0002382217447407295, 0.01616988480110236,
              0.022518961399903076, 0.0029404036924370433, 0.005505958463002645, 0.020197467142331654]

def Read_File(filename: str):
    text = open(filename, 'r', encoding='utf-8')
    texts = str(text.read())
    return texts


def Encode(text, key):
    real_key, lenght, text = [], len(text), list(text)
    for i in range (lenght):
        real_key.append(key[i % len(key)])
   
    encrypt = [0]*lenght
    for j in range (lenght):
        encrypt[j] = (ord(text[j]) + ord(real_key[j]) - 2*1072) % m
    
    for k in range (lenght):
        encrypt[k] = chr(encrypt[k] + 1072)
    
    return "".join(encrypt)


def Decode(cryptotext, key):
    n, k = len(cryptotext), len(key)
    decrypt = [(ord(cryptotext[i]) - ord(key[i % k]) -2*1072) % m for i in range(n)]
    real_message = [chr(decrypt[i] + 1072) for i in range(n)]
    return "".join(real_message)
 
 
def Match_Index(text):
    n, s, counter = len(text), 0, Counter(text)
    for letter in alphabet:
        s+= counter[letter]*(counter[letter] - 1)
    return s/(n*(n - 1))


def Blocking(text, r):
    return [text[i::r] for i in range(r)]


def Get_Key_Lenght(cryptotext):
    max_len, k = 30, 1
    mean_values =[]
    while k < max_len:
        blocks = Blocking(cryptotext, k)
        indexes = [Match_Index(block) for block in blocks]
        mean_values.append(sum(indexes)/len(indexes))
        k = k + 1
    return mean_values


def M(block, letter):
    summ, counter  = 0, Counter(block)
    for i, ltr in enumerate(alphabet) :
        summ += probability[i]*counter[chr(((ord(ltr) + ord(letter) - 2*1072) % m) + 1072)] 
    return summ


def Key_Letter_1(block):
    results = [M(block, letter) for letter in alphabet]
    return chr(results.index(max(results)) + 1072)


def Key_Letter_2(block):
    max_letter = Counter(block).most_common(1)[0][0]
    return chr(((ord(max_letter) - ord('о') - 2*1072) % m + 1072))


def Key_1(crypto_text,key_lenght):
    blocks = Blocking(crypto_text, key_lenght)
    return ''.join([Key_Letter_1(block) for block in blocks])


def Key_2(crypto_text,key_lenght):
    blocks = Blocking(crypto_text, key_lenght)
    return ''.join([Key_Letter_2(block) for block in blocks])


def main():
    text = Read_File('text_for_encoding.txt').replace('\n', '')
    crypto_text = Read_File('variant.txt').replace('\n', '')
    text_for_encoding = (''.join(filter(str.isalpha, text))).lower()
    encoded_texts = [(r,Encode(text_for_encoding, r)) for r in all_r]
    indexes_r = [Match_Index(cypher[1]) for cypher in encoded_texts]
    key_lenght = Get_Key_Lenght(crypto_text).index(max(Get_Key_Lenght(crypto_text))) + 1
    for j in range(len(Get_Key_Lenght(crypto_text))):
        print(f'Match index for blocks with period {j+1}:{Get_Key_Lenght(crypto_text)[j]}')
    key_1, key_2  = str(Key_1(crypto_text,key_lenght )), str(Key_2(crypto_text,key_lenght))
    real_message_1, real_message_2  = Decode(crypto_text, key_1), Decode(crypto_text, key_2)
    print(f'Match index for start text:{Match_Index(text_for_encoding)}\n')
    for i in range(len(all_r)):
        print(f'Match index for encoded text with key "{all_r[i]}":, {indexes_r[i]}')
    print(f'This is the key lenght: {key_lenght}\nThis is the key from comparison method:{key_2}')
    print(f'This is the key from M_i(g) method :{key_1}\n This is the text:{real_message_1}')

if __name__ == '__main__':
    main()
    