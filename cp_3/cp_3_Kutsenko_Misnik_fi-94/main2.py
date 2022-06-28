import codecs
import random


def parseFile(name):
    parsed = ""
    file = codecs.open(name, "r", "utf-8")
    for line in file:
        for ch in line.lower():
            # print(ord(ch),end=" ")
            temp = ord(ch)
            if temp == 1098:
                ch = 'ь'
            if 1072 <= temp < 1104:
                parsed += ch
            if temp == 1105:
                parsed += 'е'
    return parsed


def bigrams(text, etalon):
    bigrams = []
    for i in range(0, 31):
        bigrams.append([])
        for j in range(0, 31):
            bigrams[i].append(0)
    for i in range(0, int(len(text) / 2)):
        ch1 = ord(text[i * 2])
        ch2 = ord(text[i * 2 + 1])
        bigrams[etalon.index(ch1)][etalon.index(ch2)] += 1
    maxIJ = []
    maxVal = []

    for i in range(0, 31):
        for j in range(0, 31):
            bigrams[i][j] /= int(len(text) / 2)

    for i in range(0, 10):
        maxS = 0
        tempIJ = [0, 0]
        for i in range(0, 31):
            for j in range(0, 31):
                if maxS < bigrams[i][j] and bigrams[i][j] not in maxVal and [i, j] not in maxIJ:
                    maxS = bigrams[i][j]
                    tempIJ = [i, j]
        # print(bigrams[tempIJ[0]][tempIJ[1]])
        maxVal.append(maxS)
        maxIJ.append(tempIJ)
    return bigrams, maxIJ


def euclid_ext(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = euclid_ext(b, a % b)
        return d, y, x - y * (a // b)


def solveSystem(m, x1, y1, x2, y2):
    a = (euclid_ext(x1 - x2, m)[1] * (y1 - y2)) % m
    if a < 0:
        a += m
    b = (y1 - a * x1) % m
    return a, b


def restore(text, a, b, etalon):
    result = ""
    for i in range(0, int(len(text) / 2)):
        ch1 = ord(text[i * 2])
        ch2 = ord(text[i * 2 + 1])

        x = etalon.index(ch1) * 31 + etalon.index(ch2)
        y = (euclid_ext(a, 31 * 31)[1]) * (x - b) % (31 * 31)  # (a * x + b) % (31 * 31)
        if y < 0:
            y += 31 * 31

        ych1 = int(y / 31)
        ych2 = int(y % 31)

        result += chr(etalon[ych1]) + chr(etalon[ych2])
    return result


def affin(text, a, b, etalon):
    result = ""
    for i in range(0, int(len(text) / 2)):
        ch1 = ord(text[i * 2])
        ch2 = ord(text[i * 2 + 1])

        x = etalon.index(ch1) * 31 + etalon.index(ch2)
        y = (a * x + b) % (31 * 31)
        if y < 0:
            y += 31 * 31

        ych1 = int(y / 31)
        ych2 = int(y % 31)

        result += chr(etalon[ych1]) + chr(etalon[ych2])
    return result


if __name__ == '__main__':
    for i in range(0, 32):
        print(chr(1072 + i) + " " + str(i + 1072) + " " + str(i))
    etalon = [1072
        , 1073
        , 1074
        , 1075
        , 1076
        , 1077
        , 1078
        , 1079
        , 1080
        , 1081
        , 1082
        , 1083
        , 1084
        , 1085
        , 1086
        , 1087
        , 1088
        , 1089
        , 1090
        , 1091
        , 1092
        , 1093
        , 1094
        , 1095
        , 1096
        , 1097
        , 1100  #
        , 1099  #
        , 1101
        , 1102
        , 1103]
    etalon2 = [1072
        , 1073
        , 1074
        , 1075
        , 1076
        , 1077
        , 1078
        , 1079
        , 1080
        , 1081
        , 1082
        , 1083
        , 1084
        , 1085
        , 1086
        , 1087
        , 1088
        , 1089
        , 1090
        , 1091
        , 1092
        , 1093
        , 1094
        , 1095
        , 1096
        , 1097
        , 1100  #
        , 1099  #
        , 1101
        , 1102
        , 1103]
    text = parseFile("text2.txt")
    textBigrams, maxTextBigrams = bigrams(text, etalon2)
    baseBigrams = [[17, 18], [13, 14], [18, 14], [13, 0], [5, 13], [0, 13], [16, 0], [14, 2], [10, 14], [13, 8]]
    print(maxTextBigrams)
    for h in range(0, 10):
        for i in range(0, 10):
            for j in range(0, 10):
                if i != j and h != j:
                    x1 = baseBigrams[i][0] * 31 + baseBigrams[i][1]
                    y1 = maxTextBigrams[h][0] * 31 + maxTextBigrams[h][1]
                    x2 = baseBigrams[j][0] * 31 + baseBigrams[j][1]
                    y2 = maxTextBigrams[j][0] * 31 + maxTextBigrams[j][1]
                    a, b = solveSystem(31 * 31, x1, y1, x2, y2)
                    restored = restore(text, a, b, etalon2)
                    if (a != 0 and "аь" not in restored and "оь" not in restored
                            and "уь" not in restored and "уь" not in restored and "ыь" not in restored
                            and "юь" not in restored and "яь" not in restored and "йь" not in restored
                            and "бй" not in restored and "вй" not in restored and "гй" not in restored
                            and "кй" not in restored and "зй" not in restored and "жй" not in restored
                            and "сй" not in restored and "тй" not in restored and "рй" not in restored
                            and "пй" not in restored and "хй" not in restored and "шй" not in restored
                            and "нй" not in restored and "мй" not in restored and "лй" not in restored
                            and "чй" not in restored and "цй" not in restored and "щй" not in restored
                            and "еъ" not in restored and "аъ" not in restored and "оъ" not in restored
                            and "иъ" not in restored and "юъ" not in restored and "яъ" not in restored
                            and "ыъ" not in restored and "уъ" not in restored and "ьъ" not in restored
                    ):
                        print(str(a) + " " + str(b))
                        print(restored)

    print(" ")

    # test = parseFile("testF.txt")
    # print(test)
    # t2 = affin("ыпсь",10,10,etalon)
    # print(t2)
    # t3 = restore("ыечц",10,10,etalon)
    # print(t3)
    """
    
    for i in range(0,31*31):
        print(i)
        for j in range(0,int(31*31/10)):
            a = i
            b = j
            restored = restore(text, a, b)
            if (a != 0 and "аь" not in restored and "оь" not in restored
                    and "уь" not in restored and "уь" not in restored and "ыь" not in restored
                    and "юь" not in restored and "яь" not in restored and "йь" not in restored
                    and "бй" not in restored and "вй" not in restored and "гй" not in restored
                    and "кй" not in restored and "зй" not in restored and "жй" not in restored
                    and "сй" not in restored and "тй" not in restored and "рй" not in restored
                    and "пй" not in restored and "хй" not in restored and "шй" not in restored
                    and "нй" not in restored and "мй" not in restored and "лй" not in restored
                    and "чй" not in restored and "цй" not in restored and "щй" not in restored
                    and "еъ" not in restored and "аъ" not in restored and "оъ" not in restored
                    and "иъ" not in restored and "юъ" not in restored and "яъ" not in restored
                    and "ыъ" not in restored and "уъ" not in restored and "ьъ" not in restored
            ):
                print(str(a) + " " + str(b))
                print(restored)
    """
