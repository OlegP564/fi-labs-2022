# -*- coding: utf-8 -*-
import codecs
import pandas as pd

f = codecs.open("TEXT.txt", "r", "utf-8")
fileString = f.read()

alphabetInverted = {
    0: "а",
    1: "б",
    2: "в",
    3: "г",
    4: "д",
    5: "е",
    6: "ж",
    7: "з",
    8: "и",
    9: "й",
    10: "к",
    11: "л",
    12: "м",
    13: "н",
    14: "о",
    15: "п",
    16: "р",
    17: "с",
    18: "т",
    19: "у",
    20: "ф",
    21: "х",
    22: "ц",
    23: "ч",
    24: "ш",
    25: "щ",
    26: "ъ",
    27: "ы",
    28: "ь",
    29: "э",
    30: "ю",
    31: "я",
}

alphabet = {
    "а": 0,
    "б": 1,
    "в": 2,
    "г": 3,
    "д": 4,
    "е": 5,
    "ж": 6,
    "з": 7,
    "и": 8,
    "й": 9,
    "к": 10,
    "л": 11,
    "м": 12,
    "н": 13,
    "о": 14,
    "п": 15,
    "р": 16,
    "с": 17,
    "т": 18,
    "у": 19,
    "ф": 20,
    "х": 21,
    "ц": 22,
    "ч": 23,
    "ш": 24,
    "щ": 25,
    "ъ": 26,
    "ы": 27,
    "ь": 28,
    "э": 29,
    "ю": 30,
    "я": 31,

}

def LTN(word):
    for i in range(0, len(word)):
        word[i] = int(alphabet[word[i]])

def NTL(word):
    for i in range(0, len(word)):
        word[i] = alphabetInverted[word[i]]

def ListToString(list):
    string = ""
    for i in range(0, len(list)):
        string += list[i]

def countLetter(letter, list):
    counter = 0
    for i in range(0, len(list)):
        if(list[i] == letter):
            counter += 1
    return counter

def index(word):
    index = 0
    for i in range(0, 31):
        index += countLetter(i, word)*(countLetter(i, word) - 1)
    index = index/(839*838)
    return index

word = list(fileString)
s = ""
x = s.join(word)
print("Початкове слово:", x)

LTN(word)

encryptedWord = word

# ключ довжини 2
key1 = ["т", "о"]
LTN(key1)

for i in range(0, len(word)):
    encryptedWord[i] = (word[i] + key1[i % 2]) % 32

print()
print("Index:", index(encryptedWord))
NTL(encryptedWord)
s = ""
x = s.join(encryptedWord)
print("Зашифрований текст (ключ довжини 2)", x)

# ключ довжини 3
key2 = ["т", "о", "м"]
LTN(key2)

word = list(fileString)

LTN(word)

for i in range(0, len(word)):
    encryptedWord[i] = (word[i] + key2[i % 3]) % 32

print()
print("Index:", index(encryptedWord))
NTL(encryptedWord)
s = ""
x = s.join(encryptedWord)
print("Зашифрований текст (ключ довжини 3)", x)

# ключ довжини 4
key3 = ["т", "о", "м", "и"]
LTN(key3)

word = list(fileString)

LTN(word)

for i in range(0, len(word)):
    encryptedWord[i] = (word[i] + key3[i % 4]) % 32

print()
print("Index:", index(encryptedWord))
NTL(encryptedWord)
s = ""
x = s.join(encryptedWord)
print("Зашифрований текст (ключ довжини 4)", x)

# ключ довжини 5
key4 = ["т", "о", "м", "и", "д"]
LTN(key4)

word = list(fileString)

LTN(word)

for i in range(0, len(word)):
    encryptedWord[i] = (word[i] + key4[i % 5]) % 32

print()
print("Index:", index(encryptedWord))
NTL(encryptedWord)
s = ""
x = s.join(encryptedWord)
print("Зашифрований текст (ключ довжини 5)", x)

# ключ довжини 11
key4 = ["д", "ж", "о", "м", "о", "л", "у", "н", "г", "м", "а"]
LTN(key4)

word = list(fileString)

LTN(word)

for i in range(0, len(word)):
    encryptedWord[i] = (word[i] + key4[i % 11]) % 32

print()
print("Index:", index(encryptedWord))
NTL(encryptedWord)
s = ""
x = s.join(encryptedWord)
print("Зашифрований текст (ключ довжини 11)", x)
print()

def Dr(word, r):
    Dr = 0
    for i in range(0, len(word) - r):
        if(word[i] == word[i+r]):
            Dr += 1
    return Dr

f2 = codecs.open("TEXT2.txt", "r", "utf-8")
fileString2 = f2.read()
encryptedWord2 = list(fileString2)

LTN(encryptedWord2)

word2 = encryptedWord2

for r in range(6, 21):
    print("Dr =", Dr(encryptedWord2, r), "for R =", r)
print()

tempList = []

tempDict = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}

for r in range(13):
    for key in alphabetInverted:
        counter = 0
        for i in range(r, len(encryptedWord2), 13):
            if(key == encryptedWord2[i]):
                counter += 1
        tempDict[r].append(counter)
    tempList.append(max(tempDict[r]))


longKey = []

for key in tempDict:
    max_value = max(tempDict[key])
    max_index = tempDict[key].index(max_value)
    longKey.append(max_index)

for i in range(len(longKey)):
  longKey[i] = (longKey[i] - 14)%32


NTL(longKey)
print("Ключ, отриманий першим способом:", longKey)

frequencyS = [0.062, 0.014, 0.038, 0.013, 0.025, 0.072, 0.007, 0.016, 0.062, 0.010, 0.028, 0.035, 0.026, 0.053, 0.090, 0.023, 0.040, 0.045, 0.053, 0.021, 0.002, 0.009, 0.004, 0.012, 0.006, 0.003, 0.014, 0.016, 0.014, 0.003, 0.006, 0.018]


tempDict2 = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: [],
    21: [],
    22: [],
    23: [],
    24: [],
    25: [],
    26: [],
    27: [],
    28: [],
    29: [],
    30: [],
    31: []
}

for i in range(32):
    for key in tempDict:
        tempDict2[i].append(tempDict[key][i])

#for key in tempDict2:
#   print(tempDict2[key])

frequency = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: [],
    21: [],
    22: [],
    23: [],
    24: [],
    25: [],
    26: [],
    27: [],
    28: [],
    29: [],
    30: [],
    31: []
}

for key in tempDict2:
    for i in range(13):
        frequency[key].append(tempDict2[key][i]/len(fileString2))


tempDict3 = {
    0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    3: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    4: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    5: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    6: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    7: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    8: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    9: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    10: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    11: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    12: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    13: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    14: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    15: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    16: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    17: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    18: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    19: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    20: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    21: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    22: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    23: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    24: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    25: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    26: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    27: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    28: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    29: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    30: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    31: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

###
for i in range(13):
    for g in range(32):
        for t in tempDict2:
            tempDict3[g][i] += frequencyS[t] * tempDict2[(t + g) % 32][i]
###

f5 = open('output.txt', 'w')


for key in tempDict3:
    f5.write('%.2f' % tempDict3[key][12]+'\n')

finalKey = []
finalDict = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}
for i in range(13):
    for key in tempDict3:
        finalDict[i].append(tempDict3[key][i])

for key in finalDict:
    max_value = max(finalDict[key])
    max_index = finalDict[key].index(max_value)
    finalKey.append(max_index)

NTL(finalKey)
print("Ключ, одержаний другим способом:",finalKey)

# розшифровка

f3 = codecs.open("TEXT3.txt", "r", "utf-8")
fileStringTest = f3.read()

trueKey = ['г', 'р', 'о', 'м', 'ы', 'к', 'о', 'в', 'ь', 'д', 'у', 'м', 'а']
LTN(trueKey)
text = list(fileStringTest)
LTN(text)
DecryptedWord = list(fileStringTest)
LTN(DecryptedWord)

for i in range(0, len(fileStringTest)):
    DecryptedWord[i] = (text[i] - trueKey[i % 13]) % 32

print()
NTL(DecryptedWord)
s = ""
x = s.join(DecryptedWord)
print("Розшифрований текст:", x)