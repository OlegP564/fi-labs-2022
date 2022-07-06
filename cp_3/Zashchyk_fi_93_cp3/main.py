# -*- coding: utf-8 -*-
import pandas as pd
import codecs
import math
from collections import OrderedDict

# розширений алгоритм Евкліда
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, u, v = extended_gcd(b % a, a)
        return gcd, v - (b // a) * u, u

def inverse(a, n):
    gcd, u, v = extended_gcd(a, n)
    return u%n
def getGCD(a, n):
    gcd, u, v = extended_gcd(a, n)
    return abs(gcd)

# розв'язання системи з двох конгруенцій
def systemSolve(X1, Y1, X2, Y2, mod):
    listOfA = []
    listOfB = []

    oX1 = X1
    oY1 = Y1
    oMod = mod

    X = (X1 - X2)
    Y = (Y1 - Y2)
    mX = X%mod
    mY = Y%mod
    n = getGCD(mX, mY)
    
    if(mod%n == 0):
        mX = mX / n
        mY = mY / n
        mod = mod / n

    a = (inverse(mX, mod)*mY)%mod
    for i in range(n):
        temp = (a + mod*i)
        if(getGCD(temp, oMod) == 1):
            listOfA.append(temp)

    for i in range(len(listOfA)):
        listOfB.append((oY1 - listOfA[i]*oX1) % oMod)

    return listOfA, listOfB, len(listOfA)


# підрахунок частот біграм

f = codecs.open("TEXT.txt", "r", "utf-8")
fileString = f.read()
newString = fileString.replace(" ", "")
charList = list(newString)

dictStep = {
    "а": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "б": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "в": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "г": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "д": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "е": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ж": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "з": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "и": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "й": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "к": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "л": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "м": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "н": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "о": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "п": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "р": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "с": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "т": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "у": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ф": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "х": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ц": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ч": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ш": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "щ": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ы": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ь": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "э": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "ю": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "я": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
# для а
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'а' and charList[i + 1] == 'а'):
        dictStep["а"][0] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'б'):
        dictStep["а"][1] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'в'):
        dictStep["а"][2] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'г'):
        dictStep["а"][3] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'д'):
        dictStep["а"][4] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'е'):
        dictStep["а"][5] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ж'):
        dictStep["а"][6] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'з'):
        dictStep["а"][7] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'и'):
        dictStep["а"][8] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'й'):
        dictStep["а"][9] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'к'):
        dictStep["а"][10] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'л'):
        dictStep["а"][11] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'м'):
        dictStep["а"][12] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'н'):
        dictStep["а"][13] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'о'):
        dictStep["а"][14] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'п'):
        dictStep["а"][15] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'р'):
        dictStep["а"][16] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'с'):
        dictStep["а"][17] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'т'):
        dictStep["а"][18] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'у'):
        dictStep["а"][19] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ф'):
        dictStep["а"][20] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'х'):
        dictStep["а"][21] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ц'):
        dictStep["а"][22] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ч'):
        dictStep["а"][23] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ш'):
        dictStep["а"][24] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'щ'):
        dictStep["а"][25] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ы'):
        dictStep["а"][26] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ь'):
        dictStep["а"][27] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'э'):
        dictStep["а"][28] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ю'):
        dictStep["а"][29] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'я'):
        dictStep["а"][30] += 1
# для б
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'б' and charList[i + 1] == 'а'):
        dictStep["б"][0] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'б'):
        dictStep["б"][1] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'в'):
        dictStep["б"][2] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'г'):
        dictStep["б"][3] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'д'):
        dictStep["б"][4] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'е'):
        dictStep["б"][5] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ж'):
        dictStep["б"][6] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'з'):
        dictStep["б"][7] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'и'):
        dictStep["б"][8] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'й'):
        dictStep["б"][9] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'к'):
        dictStep["б"][10] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'л'):
        dictStep["б"][11] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'м'):
        dictStep["б"][12] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'н'):
        dictStep["б"][13] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'о'):
        dictStep["б"][14] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'п'):
        dictStep["б"][15] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'р'):
        dictStep["б"][16] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'с'):
        dictStep["б"][17] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'т'):
        dictStep["б"][18] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'у'):
        dictStep["б"][19] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ф'):
        dictStep["б"][20] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'х'):
        dictStep["б"][21] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ц'):
        dictStep["б"][22] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ч'):
        dictStep["б"][23] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ш'):
        dictStep["б"][24] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'щ'):
        dictStep["б"][25] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ы'):
        dictStep["б"][25] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ь'):
        dictStep["б"][26] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'э'):
        dictStep["б"][27] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ю'):
        dictStep["б"][28] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'я'):
        dictStep["б"][29] += 1
# для в
for i in range(0, len(newString) - 1, 2) :
    if (charList[i] == 'в' and charList[i + 1] == 'а'):
        dictStep["в"][0] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'б'):
        dictStep["в"][1] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'в'):
        dictStep["в"][2] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'г'):
        dictStep["в"][3] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'д'):
        dictStep["в"][4] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'е'):
        dictStep["в"][5] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ж'):
        dictStep["в"][6] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'з'):
        dictStep["в"][7] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'и'):
        dictStep["в"][8] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'й'):
        dictStep["в"][9] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'к'):
        dictStep["в"][10] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'л'):
        dictStep["в"][11] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'м'):
        dictStep["в"][12] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'н'):
        dictStep["в"][13] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'о'):
        dictStep["в"][14] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'п'):
        dictStep["в"][15] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'р'):
        dictStep["в"][16] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'с'):
        dictStep["в"][17] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'т'):
        dictStep["в"][18] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'у'):
        dictStep["в"][19] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ф'):
        dictStep["в"][20] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'х'):
        dictStep["в"][21] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ц'):
        dictStep["в"][22] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ч'):
        dictStep["в"][23] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ш'):
        dictStep["в"][24] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'щ'):
        dictStep["в"][25] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ы'):
        dictStep["в"][26] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ь'):
        dictStep["в"][27] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'э'):
        dictStep["в"][28] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ю'):
        dictStep["в"][29] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'я'):
        dictStep["в"][30] += 1
# для г
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'г' and charList[i + 1] == 'а'):
        dictStep["г"][0] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'б'):
        dictStep["г"][1] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'в'):
        dictStep["г"][2] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'г'):
        dictStep["г"][3] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'д'):
        dictStep["г"][4] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'е'):
        dictStep["г"][5] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ж'):
        dictStep["г"][6] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'з'):
        dictStep["г"][7] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'и'):
        dictStep["г"][8] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'й'):
        dictStep["г"][9] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'к'):
        dictStep["г"][10] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'л'):
        dictStep["г"][11] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'м'):
        dictStep["г"][12] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'н'):
        dictStep["г"][13] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'о'):
        dictStep["г"][14] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'п'):
        dictStep["г"][15] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'р'):
        dictStep["г"][16] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'с'):
        dictStep["г"][17] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'т'):
        dictStep["г"][18] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'у'):
        dictStep["г"][19] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ф'):
        dictStep["г"][20] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'х'):
        dictStep["г"][21] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ц'):
        dictStep["г"][22] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ч'):
        dictStep["г"][23] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ш'):
        dictStep["г"][24] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'щ'):
        dictStep["г"][25] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ы'):
        dictStep["г"][26] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ь'):
        dictStep["г"][27] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'э'):
        dictStep["г"][28] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ю'):
        dictStep["г"][29] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'я'):
        dictStep["г"][30] += 1
# для д
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'д' and charList[i + 1] == 'а'):
        dictStep["д"][0] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'б'):
        dictStep["д"][1] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'в'):
        dictStep["д"][2] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'г'):
        dictStep["д"][3] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'д'):
        dictStep["д"][4] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'е'):
        dictStep["д"][5] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ж'):
        dictStep["д"][6] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'з'):
        dictStep["д"][7] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'и'):
        dictStep["д"][8] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'й'):
        dictStep["д"][9] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'к'):
        dictStep["д"][10] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'л'):
        dictStep["д"][11] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'м'):
        dictStep["д"][12] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'н'):
        dictStep["д"][13] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'о'):
        dictStep["д"][14] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'п'):
        dictStep["д"][15] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'р'):
        dictStep["д"][16] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'с'):
        dictStep["д"][17] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'т'):
        dictStep["д"][18] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'у'):
        dictStep["д"][19] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ф'):
        dictStep["д"][20] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'х'):
        dictStep["д"][21] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ц'):
        dictStep["д"][22] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ч'):
        dictStep["д"][23] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ш'):
        dictStep["д"][24] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'щ'):
        dictStep["д"][25] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ы'):
        dictStep["д"][26] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ь'):
        dictStep["д"][27] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'э'):
        dictStep["д"][28] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ю'):
        dictStep["д"][29] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'я'):
        dictStep["д"][30] += 1
# для е
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'е' and charList[i + 1] == 'а'):
        dictStep["е"][0] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'б'):
        dictStep["е"][1] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'в'):
        dictStep["е"][2] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'г'):
        dictStep["е"][3] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'д'):
        dictStep["е"][4] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'е'):
        dictStep["е"][5] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ж'):
        dictStep["е"][6] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'з'):
        dictStep["е"][7] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'и'):
        dictStep["е"][8] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'й'):
        dictStep["е"][9] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'к'):
        dictStep["е"][10] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'л'):
        dictStep["е"][11] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'м'):
        dictStep["е"][12] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'н'):
        dictStep["е"][13] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'о'):
        dictStep["е"][14] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'п'):
        dictStep["е"][15] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'р'):
        dictStep["е"][16] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'с'):
        dictStep["е"][17] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'т'):
        dictStep["е"][18] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'у'):
        dictStep["е"][19] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ф'):
        dictStep["е"][20] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'х'):
        dictStep["е"][21] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ц'):
        dictStep["е"][22] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ч'):
        dictStep["е"][23] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ш'):
        dictStep["е"][24] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'щ'):
        dictStep["е"][25] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ы'):
        dictStep["е"][26] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ь'):
        dictStep["е"][27] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'э'):
        dictStep["е"][28] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ю'):
        dictStep["е"][29] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'я'):
        dictStep["е"][30] += 1
# для ж
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ж' and charList[i + 1] == 'а'):
        dictStep["ж"][0] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'б'):
        dictStep["ж"][1] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'в'):
        dictStep["ж"][2] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'г'):
        dictStep["ж"][3] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'д'):
        dictStep["ж"][4] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'е'):
        dictStep["ж"][5] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ж'):
        dictStep["ж"][6] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'з'):
        dictStep["ж"][7] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'и'):
        dictStep["ж"][8] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'й'):
        dictStep["ж"][9] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'к'):
        dictStep["ж"][10] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'л'):
        dictStep["ж"][11] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'м'):
        dictStep["ж"][12] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'н'):
        dictStep["ж"][13] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'о'):
        dictStep["ж"][14] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'п'):
        dictStep["ж"][15] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'р'):
        dictStep["ж"][16] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'с'):
        dictStep["ж"][17] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'т'):
        dictStep["ж"][18] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'у'):
        dictStep["ж"][19] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ф'):
        dictStep["ж"][20] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'х'):
        dictStep["ж"][21] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ц'):
        dictStep["ж"][22] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ч'):
        dictStep["ж"][23] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ш'):
        dictStep["ж"][24] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'щ'):
        dictStep["ж"][25] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ы'):
        dictStep["ж"][26] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ь'):
        dictStep["ж"][27] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'э'):
        dictStep["ж"][28] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ю'):
        dictStep["ж"][29] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'я'):
        dictStep["ж"][30] += 1
# для з
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'з' and charList[i + 1] == 'а'):
        dictStep["з"][0] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'б'):
        dictStep["з"][1] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'в'):
        dictStep["з"][2] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'г'):
        dictStep["з"][3] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'д'):
        dictStep["з"][4] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'е'):
        dictStep["з"][5] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ж'):
        dictStep["з"][6] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'з'):
        dictStep["з"][7] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'и'):
        dictStep["з"][8] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'й'):
        dictStep["з"][9] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'к'):
        dictStep["з"][10] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'л'):
        dictStep["з"][11] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'м'):
        dictStep["з"][12] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'н'):
        dictStep["з"][13] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'о'):
        dictStep["з"][14] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'п'):
        dictStep["з"][15] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'р'):
        dictStep["з"][16] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'с'):
        dictStep["з"][17] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'т'):
        dictStep["з"][18] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'у'):
        dictStep["з"][19] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ф'):
        dictStep["з"][20] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'х'):
        dictStep["з"][21] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ц'):
        dictStep["з"][22] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ч'):
        dictStep["з"][23] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ш'):
        dictStep["з"][24] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'щ'):
        dictStep["з"][25] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ы'):
        dictStep["з"][26] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ь'):
        dictStep["з"][27] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'э'):
        dictStep["з"][28] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ю'):
        dictStep["з"][29] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'я'):
        dictStep["з"][30] += 1
# для и
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'и' and charList[i + 1] == 'а'):
        dictStep["и"][0] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'б'):
        dictStep["и"][1] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'в'):
        dictStep["и"][2] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'г'):
        dictStep["и"][3] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'д'):
        dictStep["и"][4] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'е'):
        dictStep["и"][5] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ж'):
        dictStep["и"][6] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'з'):
        dictStep["и"][7] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'и'):
        dictStep["и"][8] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'й'):
        dictStep["и"][9] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'к'):
        dictStep["и"][10] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'л'):
        dictStep["и"][11] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'м'):
        dictStep["и"][12] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'н'):
        dictStep["и"][13] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'о'):
        dictStep["и"][14] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'п'):
        dictStep["и"][15] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'р'):
        dictStep["и"][16] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'с'):
        dictStep["и"][17] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'т'):
        dictStep["и"][18] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'у'):
        dictStep["и"][19] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ф'):
        dictStep["и"][20] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'х'):
        dictStep["и"][21] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ц'):
        dictStep["и"][22] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ч'):
        dictStep["и"][23] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ш'):
        dictStep["и"][24] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'щ'):
        dictStep["и"][25] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ы'):
        dictStep["и"][26] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ь'):
        dictStep["и"][27] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'э'):
        dictStep["и"][28] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ю'):
        dictStep["и"][29] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'я'):
        dictStep["и"][30] += 1
# для й
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'й' and charList[i + 1] == 'а'):
        dictStep["й"][0] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'б'):
        dictStep["й"][1] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'в'):
        dictStep["й"][2] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'г'):
        dictStep["й"][3] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'д'):
        dictStep["й"][4] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'е'):
        dictStep["й"][5] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ж'):
        dictStep["й"][6] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'з'):
        dictStep["й"][7] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'и'):
        dictStep["й"][8] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'й'):
        dictStep["й"][9] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'к'):
        dictStep["й"][10] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'л'):
        dictStep["й"][11] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'м'):
        dictStep["й"][12] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'н'):
        dictStep["й"][13] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'о'):
        dictStep["й"][14] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'п'):
        dictStep["й"][15] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'р'):
        dictStep["й"][16] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'с'):
        dictStep["й"][17] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'т'):
        dictStep["й"][18] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'у'):
        dictStep["й"][19] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ф'):
        dictStep["й"][20] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'х'):
        dictStep["й"][21] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ц'):
        dictStep["й"][22] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ч'):
        dictStep["й"][23] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ш'):
        dictStep["й"][24] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'щ'):
        dictStep["й"][25] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ы'):
        dictStep["й"][26] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ь'):
        dictStep["й"][27] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'э'):
        dictStep["й"][28] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ю'):
        dictStep["й"][29] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'я'):
        dictStep["й"][30] += 1
# для к
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'к' and charList[i + 1] == 'а'):
        dictStep["к"][0] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'б'):
        dictStep["к"][1] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'в'):
        dictStep["к"][2] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'г'):
        dictStep["к"][3] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'д'):
        dictStep["к"][4] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'е'):
        dictStep["к"][5] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ж'):
        dictStep["к"][6] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'з'):
        dictStep["к"][7] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'и'):
        dictStep["к"][8] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'й'):
        dictStep["к"][9] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'к'):
        dictStep["к"][10] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'л'):
        dictStep["к"][11] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'м'):
        dictStep["к"][12] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'н'):
        dictStep["к"][13] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'о'):
        dictStep["к"][14] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'п'):
        dictStep["к"][15] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'р'):
        dictStep["к"][16] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'с'):
        dictStep["к"][17] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'т'):
        dictStep["к"][18] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'у'):
        dictStep["к"][19] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ф'):
        dictStep["к"][20] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'х'):
        dictStep["к"][21] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ц'):
        dictStep["к"][22] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ч'):
        dictStep["к"][23] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ш'):
        dictStep["к"][24] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'щ'):
        dictStep["к"][25] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ы'):
        dictStep["к"][26] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ь'):
        dictStep["к"][27] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'э'):
        dictStep["к"][28] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ю'):
        dictStep["к"][29] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'я'):
        dictStep["к"][30] += 1
# для л
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'л' and charList[i + 1] == 'а'):
        dictStep["л"][0] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'б'):
        dictStep["л"][1] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'в'):
        dictStep["л"][2] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'г'):
        dictStep["л"][3] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'д'):
        dictStep["л"][4] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'е'):
        dictStep["л"][5] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ж'):
        dictStep["л"][6] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'з'):
        dictStep["л"][7] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'и'):
        dictStep["л"][8] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'й'):
        dictStep["л"][9] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'к'):
        dictStep["л"][10] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'л'):
        dictStep["л"][11] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'м'):
        dictStep["л"][12] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'н'):
        dictStep["л"][13] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'о'):
        dictStep["л"][14] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'п'):
        dictStep["л"][15] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'р'):
        dictStep["л"][16] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'с'):
        dictStep["л"][17] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'т'):
        dictStep["л"][18] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'у'):
        dictStep["л"][19] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ф'):
        dictStep["л"][20] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'х'):
        dictStep["л"][21] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ц'):
        dictStep["л"][22] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ч'):
        dictStep["л"][23] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ш'):
        dictStep["л"][24] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'щ'):
        dictStep["л"][25] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ы'):
        dictStep["л"][26] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ь'):
        dictStep["л"][27] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'э'):
        dictStep["л"][28] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ю'):
        dictStep["л"][29] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'я'):
        dictStep["л"][30] += 1
# для м
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'м' and charList[i + 1] == 'а'):
        dictStep["м"][0] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'б'):
        dictStep["м"][1] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'в'):
        dictStep["м"][2] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'г'):
        dictStep["м"][3] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'д'):
        dictStep["м"][4] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'е'):
        dictStep["м"][5] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ж'):
        dictStep["м"][6] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'з'):
        dictStep["м"][7] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'и'):
        dictStep["м"][8] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'й'):
        dictStep["м"][9] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'к'):
        dictStep["м"][10] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'л'):
        dictStep["м"][11] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'м'):
        dictStep["м"][12] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'н'):
        dictStep["м"][13] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'о'):
        dictStep["м"][14] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'п'):
        dictStep["м"][15] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'р'):
        dictStep["м"][16] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'с'):
        dictStep["м"][17] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'т'):
        dictStep["м"][18] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'у'):
        dictStep["м"][19] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ф'):
        dictStep["м"][20] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'х'):
        dictStep["м"][21] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ц'):
        dictStep["м"][22] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ч'):
        dictStep["м"][23] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ш'):
        dictStep["м"][24] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'щ'):
        dictStep["м"][25] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ы'):
        dictStep["м"][26] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ь'):
        dictStep["м"][27] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'э'):
        dictStep["м"][28] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ю'):
        dictStep["м"][29] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'я'):
        dictStep["м"][30] += 1
# для н
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'н' and charList[i + 1] == 'а'):
        dictStep["н"][0] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'б'):
        dictStep["н"][1] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'в'):
        dictStep["н"][2] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'г'):
        dictStep["н"][3] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'д'):
        dictStep["н"][4] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'е'):
        dictStep["н"][5] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ж'):
        dictStep["н"][6] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'з'):
        dictStep["н"][7] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'и'):
        dictStep["н"][8] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'й'):
        dictStep["н"][9] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'к'):
        dictStep["н"][10] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'л'):
        dictStep["н"][11] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'м'):
        dictStep["н"][12] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'н'):
        dictStep["н"][13] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'о'):
        dictStep["н"][14] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'п'):
        dictStep["н"][15] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'р'):
        dictStep["н"][16] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'с'):
        dictStep["н"][17] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'т'):
        dictStep["н"][18] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'у'):
        dictStep["н"][19] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ф'):
        dictStep["н"][20] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'х'):
        dictStep["н"][21] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ц'):
        dictStep["н"][22] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ч'):
        dictStep["н"][23] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ш'):
        dictStep["н"][24] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'щ'):
        dictStep["н"][25] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ы'):
        dictStep["н"][26] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ь'):
        dictStep["н"][27] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'э'):
        dictStep["н"][28] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ю'):
        dictStep["н"][29] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'я'):
        dictStep["н"][30] += 1
# для о
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'о' and charList[i + 1] == 'а'):
        dictStep["о"][0] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'б'):
        dictStep["о"][1] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'в'):
        dictStep["о"][2] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'г'):
        dictStep["о"][3] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'д'):
        dictStep["о"][4] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'е'):
        dictStep["о"][5] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ж'):
        dictStep["о"][6] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'з'):
        dictStep["о"][7] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'и'):
        dictStep["о"][8] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'й'):
        dictStep["о"][9] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'к'):
        dictStep["о"][10] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'л'):
        dictStep["о"][11] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'м'):
        dictStep["о"][12] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'н'):
        dictStep["о"][13] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'о'):
        dictStep["о"][14] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'п'):
        dictStep["о"][15] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'р'):
        dictStep["о"][16] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'с'):
        dictStep["о"][17] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'т'):
        dictStep["о"][18] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'у'):
        dictStep["о"][19] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ф'):
        dictStep["о"][20] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'х'):
        dictStep["о"][21] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ц'):
        dictStep["о"][22] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ч'):
        dictStep["о"][23] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ш'):
        dictStep["о"][24] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'щ'):
        dictStep["о"][25] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ы'):
        dictStep["о"][26] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ь'):
        dictStep["о"][27] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'э'):
        dictStep["о"][28] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ю'):
        dictStep["о"][29] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'я'):
        dictStep["о"][30] += 1
# для п
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'п' and charList[i + 1] == 'а'):
        dictStep["п"][0] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'б'):
        dictStep["п"][1] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'в'):
        dictStep["п"][2] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'г'):
        dictStep["п"][3] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'д'):
        dictStep["п"][4] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'е'):
        dictStep["п"][5] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ж'):
        dictStep["п"][6] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'з'):
        dictStep["п"][7] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'и'):
        dictStep["п"][8] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'й'):
        dictStep["п"][9] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'к'):
        dictStep["п"][10] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'л'):
        dictStep["п"][11] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'м'):
        dictStep["п"][12] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'н'):
        dictStep["п"][13] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'о'):
        dictStep["п"][14] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'п'):
        dictStep["п"][15] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'р'):
        dictStep["п"][16] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'с'):
        dictStep["п"][17] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'т'):
        dictStep["п"][18] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'у'):
        dictStep["п"][19] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ф'):
        dictStep["п"][20] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'х'):
        dictStep["п"][21] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ц'):
        dictStep["п"][22] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ч'):
        dictStep["п"][23] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ш'):
        dictStep["п"][24] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'щ'):
        dictStep["п"][25] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ы'):
        dictStep["п"][26] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ь'):
        dictStep["п"][27] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'э'):
        dictStep["п"][28] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ю'):
        dictStep["п"][29] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'я'):
        dictStep["п"][30] += 1
# для р
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'р' and charList[i + 1] == 'а'):
        dictStep["р"][0] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'б'):
        dictStep["р"][1] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'в'):
        dictStep["р"][2] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'г'):
        dictStep["р"][3] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'д'):
        dictStep["р"][4] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'е'):
        dictStep["р"][5] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ж'):
        dictStep["р"][6] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'з'):
        dictStep["р"][7] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'и'):
        dictStep["р"][8] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'й'):
        dictStep["р"][9] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'к'):
        dictStep["р"][10] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'л'):
        dictStep["р"][11] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'м'):
        dictStep["р"][12] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'н'):
        dictStep["р"][13] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'о'):
        dictStep["р"][14] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'п'):
        dictStep["р"][15] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'р'):
        dictStep["р"][16] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'с'):
        dictStep["р"][17] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'т'):
        dictStep["р"][18] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'у'):
        dictStep["р"][19] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ф'):
        dictStep["р"][20] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'х'):
        dictStep["р"][21] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ц'):
        dictStep["р"][22] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ч'):
        dictStep["р"][23] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ш'):
        dictStep["р"][24] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'щ'):
        dictStep["р"][25] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ы'):
        dictStep["р"][26] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ь'):
        dictStep["р"][27] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'э'):
        dictStep["р"][28] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ю'):
        dictStep["р"][29] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'я'):
        dictStep["р"][30] += 1
# для с
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'с' and charList[i + 1] == 'а'):
        dictStep["с"][0] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'б'):
        dictStep["с"][1] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'в'):
        dictStep["с"][2] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'г'):
        dictStep["с"][3] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'д'):
        dictStep["с"][4] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'е'):
        dictStep["с"][5] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ж'):
        dictStep["с"][6] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'з'):
        dictStep["с"][7] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'и'):
        dictStep["с"][8] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'й'):
        dictStep["с"][9] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'к'):
        dictStep["с"][10] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'л'):
        dictStep["с"][11] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'м'):
        dictStep["с"][12] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'н'):
        dictStep["с"][13] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'о'):
        dictStep["с"][14] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'п'):
        dictStep["с"][15] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'р'):
        dictStep["с"][16] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'с'):
        dictStep["с"][17] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'т'):
        dictStep["с"][18] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'у'):
        dictStep["с"][19] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ф'):
        dictStep["с"][20] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'х'):
        dictStep["с"][21] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ц'):
        dictStep["с"][22] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ч'):
        dictStep["с"][23] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ш'):
        dictStep["с"][24] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'щ'):
        dictStep["с"][25] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ы'):
        dictStep["с"][26] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ь'):
        dictStep["с"][27] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'э'):
        dictStep["с"][28] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ю'):
        dictStep["с"][29] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'я'):
        dictStep["с"][30] += 1
# для т
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'т' and charList[i + 1] == 'а'):
        dictStep["т"][0] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'б'):
        dictStep["т"][1] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'в'):
        dictStep["т"][2] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'г'):
        dictStep["т"][3] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'д'):
        dictStep["т"][4] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'е'):
        dictStep["т"][5] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ж'):
        dictStep["т"][6] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'з'):
        dictStep["т"][7] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'и'):
        dictStep["т"][8] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'й'):
        dictStep["т"][9] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'к'):
        dictStep["т"][10] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'л'):
        dictStep["т"][11] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'м'):
        dictStep["т"][12] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'н'):
        dictStep["т"][13] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'о'):
        dictStep["т"][14] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'п'):
        dictStep["т"][15] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'р'):
        dictStep["т"][16] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'с'):
        dictStep["т"][17] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'т'):
        dictStep["т"][18] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'у'):
        dictStep["т"][19] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ф'):
        dictStep["т"][20] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'х'):
        dictStep["т"][21] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ц'):
        dictStep["т"][22] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ч'):
        dictStep["т"][23] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ш'):
        dictStep["т"][24] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'щ'):
        dictStep["т"][25] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ы'):
        dictStep["т"][26] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ь'):
        dictStep["т"][27] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'э'):
        dictStep["т"][28] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ю'):
        dictStep["т"][29] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'я'):
        dictStep["т"][30] += 1
# для у
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'у' and charList[i + 1] == 'а'):
        dictStep["у"][0] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'б'):
        dictStep["у"][1] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'в'):
        dictStep["у"][2] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'г'):
        dictStep["у"][3] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'д'):
        dictStep["у"][4] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'е'):
        dictStep["у"][5] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ж'):
        dictStep["у"][6] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'з'):
        dictStep["у"][7] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'и'):
        dictStep["у"][8] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'й'):
        dictStep["у"][9] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'к'):
        dictStep["у"][10] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'л'):
        dictStep["у"][11] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'м'):
        dictStep["у"][12] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'н'):
        dictStep["у"][13] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'о'):
        dictStep["у"][14] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'п'):
        dictStep["у"][15] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'р'):
        dictStep["у"][16] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'с'):
        dictStep["у"][17] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'т'):
        dictStep["у"][18] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'у'):
        dictStep["у"][19] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ф'):
        dictStep["у"][20] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'х'):
        dictStep["у"][21] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ц'):
        dictStep["у"][22] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ч'):
        dictStep["у"][23] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ш'):
        dictStep["у"][24] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'щ'):
        dictStep["у"][25] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ы'):
        dictStep["у"][26] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ь'):
        dictStep["у"][27] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'э'):
        dictStep["у"][28] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ю'):
        dictStep["у"][29] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'я'):
        dictStep["у"][30] += 1
# для ф
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ф' and charList[i + 1] == 'а'):
        dictStep["ф"][0] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'б'):
        dictStep["ф"][1] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'в'):
        dictStep["ф"][2] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'г'):
        dictStep["ф"][3] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'д'):
        dictStep["ф"][4] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'е'):
        dictStep["ф"][5] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ж'):
        dictStep["ф"][6] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'з'):
        dictStep["ф"][7] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'и'):
        dictStep["ф"][8] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'й'):
        dictStep["ф"][9] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'к'):
        dictStep["ф"][10] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'л'):
        dictStep["ф"][11] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'м'):
        dictStep["ф"][12] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'н'):
        dictStep["ф"][13] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'о'):
        dictStep["ф"][14] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'п'):
        dictStep["ф"][15] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'р'):
        dictStep["ф"][16] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'с'):
        dictStep["ф"][17] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'т'):
        dictStep["ф"][18] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'у'):
        dictStep["ф"][19] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ф'):
        dictStep["ф"][20] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'х'):
        dictStep["ф"][21] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ц'):
        dictStep["ф"][22] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ч'):
        dictStep["ф"][23] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ш'):
        dictStep["ф"][24] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'щ'):
        dictStep["ф"][25] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ы'):
        dictStep["ф"][26] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ь'):
        dictStep["ф"][27] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'э'):
        dictStep["ф"][28] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ю'):
        dictStep["ф"][29] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'я'):
        dictStep["ф"][30] += 1
# для х
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'х' and charList[i + 1] == 'а'):
        dictStep["х"][0] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'б'):
        dictStep["х"][1] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'в'):
        dictStep["х"][2] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'г'):
        dictStep["х"][3] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'д'):
        dictStep["х"][4] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'е'):
        dictStep["х"][5] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ж'):
        dictStep["х"][6] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'з'):
        dictStep["х"][7] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'и'):
        dictStep["х"][8] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'й'):
        dictStep["х"][9] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'к'):
        dictStep["х"][10] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'л'):
        dictStep["х"][11] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'м'):
        dictStep["х"][12] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'н'):
        dictStep["х"][13] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'о'):
        dictStep["х"][14] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'п'):
        dictStep["х"][15] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'р'):
        dictStep["х"][16] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'с'):
        dictStep["х"][17] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'т'):
        dictStep["х"][18] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'у'):
        dictStep["х"][19] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ф'):
        dictStep["х"][20] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'х'):
        dictStep["х"][21] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ц'):
        dictStep["х"][22] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ч'):
        dictStep["х"][23] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ш'):
        dictStep["х"][24] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'щ'):
        dictStep["х"][25] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ы'):
        dictStep["х"][26] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ь'):
        dictStep["х"][27] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'э'):
        dictStep["х"][28] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ю'):
        dictStep["х"][29] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'я'):
        dictStep["х"][30] += 1
# для ц
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ц' and charList[i + 1] == 'а'):
        dictStep["ц"][0] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'б'):
        dictStep["ц"][1] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'в'):
        dictStep["ц"][2] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'г'):
        dictStep["ц"][3] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'д'):
        dictStep["ц"][4] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'е'):
        dictStep["ц"][5] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ж'):
        dictStep["ц"][6] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'з'):
        dictStep["ц"][7] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'и'):
        dictStep["ц"][8] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'й'):
        dictStep["ц"][9] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'к'):
        dictStep["ц"][10] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'л'):
        dictStep["ц"][11] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'м'):
        dictStep["ц"][12] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'н'):
        dictStep["ц"][13] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'о'):
        dictStep["ц"][14] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'п'):
        dictStep["ц"][15] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'р'):
        dictStep["ц"][16] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'с'):
        dictStep["ц"][17] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'т'):
        dictStep["ц"][18] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'у'):
        dictStep["ц"][19] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ф'):
        dictStep["ц"][20] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'х'):
        dictStep["ц"][21] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ц'):
        dictStep["ц"][22] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ч'):
        dictStep["ц"][23] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ш'):
        dictStep["ц"][24] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'щ'):
        dictStep["ц"][25] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ы'):
        dictStep["ц"][26] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ь'):
        dictStep["ц"][27] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'э'):
        dictStep["ц"][28] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ю'):
        dictStep["ц"][29] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'я'):
        dictStep["ц"][30] += 1
# для ч
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ч' and charList[i + 1] == 'а'):
        dictStep["ч"][0] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'б'):
        dictStep["ч"][1] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'в'):
        dictStep["ч"][2] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'г'):
        dictStep["ч"][3] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'д'):
        dictStep["ч"][4] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'е'):
        dictStep["ч"][5] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ж'):
        dictStep["ч"][6] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'з'):
        dictStep["ч"][7] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'и'):
        dictStep["ч"][8] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'й'):
        dictStep["ч"][9] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'к'):
        dictStep["ч"][10] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'л'):
        dictStep["ч"][11] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'м'):
        dictStep["ч"][12] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'н'):
        dictStep["ч"][13] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'о'):
        dictStep["ч"][14] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'п'):
        dictStep["ч"][15] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'р'):
        dictStep["ч"][16] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'с'):
        dictStep["ч"][17] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'т'):
        dictStep["ч"][18] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'у'):
        dictStep["ч"][19] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ф'):
        dictStep["ч"][20] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'х'):
        dictStep["ч"][21] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ц'):
        dictStep["ч"][22] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ч'):
        dictStep["ч"][23] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ш'):
        dictStep["ч"][24] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'щ'):
        dictStep["ч"][25] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ы'):
        dictStep["ч"][26] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ь'):
        dictStep["ч"][27] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'э'):
        dictStep["ч"][28] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ю'):
        dictStep["ч"][29] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'я'):
        dictStep["ч"][30] += 1
# для ш
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ш' and charList[i + 1] == 'а'):
        dictStep["ш"][0] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'б'):
        dictStep["ш"][1] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'в'):
        dictStep["ш"][2] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'г'):
        dictStep["ш"][3] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'д'):
        dictStep["ш"][4] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'е'):
        dictStep["ш"][5] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ж'):
        dictStep["ш"][6] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'з'):
        dictStep["ш"][7] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'и'):
        dictStep["ш"][8] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'й'):
        dictStep["ш"][9] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'к'):
        dictStep["ш"][10] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'л'):
        dictStep["ш"][11] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'м'):
        dictStep["ш"][12] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'н'):
        dictStep["ш"][13] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'о'):
        dictStep["ш"][14] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'п'):
        dictStep["ш"][15] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'р'):
        dictStep["ш"][16] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'с'):
        dictStep["ш"][17] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'т'):
        dictStep["ш"][18] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'у'):
        dictStep["ш"][19] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ф'):
        dictStep["ш"][20] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'х'):
        dictStep["ш"][21] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ц'):
        dictStep["ш"][22] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ч'):
        dictStep["ш"][23] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ш'):
        dictStep["ш"][24] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'щ'):
        dictStep["ш"][25] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ы'):
        dictStep["ш"][26] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ь'):
        dictStep["ш"][27] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'э'):
        dictStep["ш"][28] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ю'):
        dictStep["ш"][29] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'я'):
        dictStep["ш"][30] += 1
# для щ
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'щ' and charList[i + 1] == 'а'):
        dictStep["щ"][0] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'б'):
        dictStep["щ"][1] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'в'):
        dictStep["щ"][2] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'г'):
        dictStep["щ"][3] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'д'):
        dictStep["щ"][4] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'е'):
        dictStep["щ"][5] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ж'):
        dictStep["щ"][6] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'з'):
        dictStep["щ"][7] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'и'):
        dictStep["щ"][8] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'й'):
        dictStep["щ"][9] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'к'):
        dictStep["щ"][10] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'л'):
        dictStep["щ"][11] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'м'):
        dictStep["щ"][12] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'н'):
        dictStep["щ"][13] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'о'):
        dictStep["щ"][14] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'п'):
        dictStep["щ"][15] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'р'):
        dictStep["щ"][16] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'с'):
        dictStep["щ"][17] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'т'):
        dictStep["щ"][18] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'у'):
        dictStep["щ"][19] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ф'):
        dictStep["щ"][20] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'х'):
        dictStep["щ"][21] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ц'):
        dictStep["щ"][22] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ч'):
        dictStep["щ"][23] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ш'):
        dictStep["щ"][24] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'щ'):
        dictStep["щ"][25] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ы'):
        dictStep["щ"][26] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ь'):
        dictStep["щ"][27] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'э'):
        dictStep["щ"][28] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ю'):
        dictStep["щ"][29] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'я'):
        dictStep["щ"][30] += 1
# для ы
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ы' and charList[i + 1] == 'а'):
        dictStep["ы"][0] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'б'):
        dictStep["ы"][1] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'в'):
        dictStep["ы"][2] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'г'):
        dictStep["ы"][3] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'д'):
        dictStep["ы"][4] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'е'):
        dictStep["ы"][5] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ж'):
        dictStep["ы"][6] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'з'):
        dictStep["ы"][7] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'и'):
        dictStep["ы"][8] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'й'):
        dictStep["ы"][9] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'к'):
        dictStep["ы"][10] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'л'):
        dictStep["ы"][11] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'м'):
        dictStep["ы"][12] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'н'):
        dictStep["ы"][13] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'о'):
        dictStep["ы"][14] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'п'):
        dictStep["ы"][15] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'р'):
        dictStep["ы"][16] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'с'):
        dictStep["ы"][17] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'т'):
        dictStep["ы"][18] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'у'):
        dictStep["ы"][19] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ф'):
        dictStep["ы"][20] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'х'):
        dictStep["ы"][21] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ц'):
        dictStep["ы"][22] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ч'):
        dictStep["ы"][23] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ш'):
        dictStep["ы"][24] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'щ'):
        dictStep["ы"][25] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ы'):
        dictStep["ы"][26] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ь'):
        dictStep["ы"][27] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'э'):
        dictStep["ы"][28] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ю'):
        dictStep["ы"][29] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'я'):
        dictStep["ы"][30] += 1
# для ь
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ь' and charList[i + 1] == 'а'):
        dictStep["ь"][0] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'б'):
        dictStep["ь"][1] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'в'):
        dictStep["ь"][2] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'г'):
        dictStep["ь"][3] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'д'):
        dictStep["ь"][4] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'е'):
        dictStep["ь"][5] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ж'):
        dictStep["ь"][6] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'з'):
        dictStep["ь"][7] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'и'):
        dictStep["ь"][8] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'й'):
        dictStep["ь"][9] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'к'):
        dictStep["ь"][10] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'л'):
        dictStep["ь"][11] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'м'):
        dictStep["ь"][12] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'н'):
        dictStep["ь"][13] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'о'):
        dictStep["ь"][14] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'п'):
        dictStep["ь"][15] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'р'):
        dictStep["ь"][16] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'с'):
        dictStep["ь"][17] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'т'):
        dictStep["ь"][18] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'у'):
        dictStep["ь"][19] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ф'):
        dictStep["ь"][20] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'х'):
        dictStep["ь"][21] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ц'):
        dictStep["ь"][22] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ч'):
        dictStep["ь"][23] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ш'):
        dictStep["ь"][24] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'щ'):
        dictStep["ь"][25] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ы'):
        dictStep["ь"][26] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ь'):
        dictStep["ь"][27] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'э'):
        dictStep["ь"][28] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ю'):
        dictStep["ь"][29] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'я'):
        dictStep["ь"][30] += 1
# для э
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'э' and charList[i + 1] == 'а'):
        dictStep["э"][0] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'б'):
        dictStep["э"][1] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'в'):
        dictStep["э"][2] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'г'):
        dictStep["э"][3] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'д'):
        dictStep["э"][4] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'е'):
        dictStep["э"][5] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ж'):
        dictStep["э"][6] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'з'):
        dictStep["э"][7] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'и'):
        dictStep["э"][8] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'й'):
        dictStep["э"][9] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'к'):
        dictStep["э"][10] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'л'):
        dictStep["э"][11] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'м'):
        dictStep["э"][12] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'н'):
        dictStep["э"][13] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'о'):
        dictStep["э"][14] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'п'):
        dictStep["э"][15] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'р'):
        dictStep["э"][16] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'с'):
        dictStep["э"][17] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'т'):
        dictStep["э"][18] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'у'):
        dictStep["э"][19] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ф'):
        dictStep["э"][20] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'х'):
        dictStep["э"][21] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ц'):
        dictStep["э"][22] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ч'):
        dictStep["э"][23] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ш'):
        dictStep["э"][24] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'щ'):
        dictStep["э"][25] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ы'):
        dictStep["э"][26] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ь'):
        dictStep["э"][27] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'э'):
        dictStep["э"][28] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ю'):
        dictStep["э"][29] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'я'):
        dictStep["э"][30] += 1
# для ю
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'ю' and charList[i + 1] == 'а'):
        dictStep["ю"][0] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'б'):
        dictStep["ю"][1] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'в'):
        dictStep["ю"][2] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'г'):
        dictStep["ю"][3] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'д'):
        dictStep["ю"][4] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'е'):
        dictStep["ю"][5] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ж'):
        dictStep["ю"][6] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'з'):
        dictStep["ю"][7] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'и'):
        dictStep["ю"][8] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'й'):
        dictStep["ю"][9] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'к'):
        dictStep["ю"][10] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'л'):
        dictStep["ю"][11] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'м'):
        dictStep["ю"][12] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'н'):
        dictStep["ю"][13] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'о'):
        dictStep["ю"][14] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'п'):
        dictStep["ю"][15] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'р'):
        dictStep["ю"][16] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'с'):
        dictStep["ю"][17] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'т'):
        dictStep["ю"][18] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'у'):
        dictStep["ю"][19] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ф'):
        dictStep["ю"][20] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'х'):
        dictStep["ю"][21] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ц'):
        dictStep["ю"][22] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ч'):
        dictStep["ю"][23] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ш'):
        dictStep["ю"][24] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'щ'):
        dictStep["ю"][25] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ы'):
        dictStep["ю"][26] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ь'):
        dictStep["ю"][27] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'э'):
        dictStep["ю"][28] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ю'):
        dictStep["ю"][29] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'я'):
        dictStep["ю"][30] += 1
# для я
for i in range(0, len(newString) - 1, 2):
    if (charList[i] == 'я' and charList[i + 1] == 'а'):
        dictStep["я"][0] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'б'):
        dictStep["я"][1] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'в'):
        dictStep["я"][2] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'г'):
        dictStep["я"][3] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'д'):
        dictStep["я"][4] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'е'):
        dictStep["я"][5] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ж'):
        dictStep["я"][6] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'з'):
        dictStep["я"][7] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'и'):
        dictStep["я"][8] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'й'):
        dictStep["я"][9] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'к'):
        dictStep["я"][10] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'л'):
        dictStep["я"][11] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'м'):
        dictStep["я"][12] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'н'):
        dictStep["я"][13] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'о'):
        dictStep["я"][14] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'п'):
        dictStep["я"][15] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'р'):
        dictStep["я"][16] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'с'):
        dictStep["я"][17] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'т'):
        dictStep["я"][18] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'у'):
        dictStep["я"][19] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ф'):
        dictStep["я"][20] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'х'):
        dictStep["я"][21] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ц'):
        dictStep["я"][22] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ч'):
        dictStep["я"][23] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ш'):
        dictStep["я"][24] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'щ'):
        dictStep["я"][25] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ы'):
        dictStep["я"][26] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ь'):
        dictStep["я"][27] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'э'):
        dictStep["я"][28] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ю'):
        dictStep["я"][29] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'я'):
        dictStep["я"][30] += 1

pd.set_option("display.max_rows", None, "display.max_columns", None)
dfS = pd.DataFrame(dictStep, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
#print()
#print("Кількість біграм без перетину (без пробілів):")
#print(dfS)

alphabet = {
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
    26: "ы",
    27: "ь",
    28: "э",
    29: "ю",
    30: "я",
}
alphabetInverted = {
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
    "ы": 26,
    "ь": 27,
    "э": 28,
    "ю": 29,
    "я": 30

}

def convertTupleToDict(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di

def popularBigrams(dict):
    newDict = {}
    topBigramsStr = ""

    for key in dict:

        newDict[key+alphabet[dictStep[key].index(max(dictStep[key]))]] = max(dictStep[key])
    newDict = (sorted(newDict.items(), key=lambda item: item[1]))
    newDict2 = {}
    convertTupleToDict(newDict, newDict2)
    for key in newDict2:
        topBigramsStr = topBigramsStr + key
    topBigrams = list(topBigramsStr)
    #print(topBigrams)

    #print(newDict2)
    res = OrderedDict(reversed(list(newDict2.items())))
    newDict3 = {}
    convertTupleToDict(res, newDict3)
    #print(newDict3)
    topBigramsrReverse = []
    for key in newDict3:
        topBigramsrReverse.append(key)
        topBigramsrReverse.append(newDict3[key][0])
    #print(topBigramsrReverse)
    return topBigramsrReverse


# підбирання ключа

m = 31

listOfTopBigrams= popularBigrams(dictStep)

def recognizer(word):
    no = newString.count('о')
    no = (no*100)/len(word)

    na = newString.count('а')
    na = (na * 100) / len(word)

    ne = newString.count('е')
    ne = (ne * 100) / len(word)
    if (no < 9.3 and na < 8.7 and ne < 8.1):
        return 0
    else:
        return 1

def bigramToNumber(letter1, letter2):
    l1 = alphabetInverted[letter1]
    l2 = alphabetInverted[letter2]
    number = l1*31 + l2
    return number

def numberToBigram(number):
    bigram = ""
    l1 = number//31
    l2 = number%31
    letter1 = alphabet[l1]
    letter2 = alphabet[l2]
    bigram = letter1 + letter2
    return bigram

def wordToNumbers(word):
    res = []
    for i in range(0, len(word) - 1, 2):
        res.append(bigramToNumber(word[i], word[i + 1]))
    return res

def numbersToWord(list):
    res = ""
    for i in range(len(list)):
        res += numberToBigram(list[i])
    return res

def decypherPart1(a, b, sqrtMod, word):
    decryptedWord = ""
    for i in range(0, len(word)):
        X = inverse(a, sqrtMod * sqrtMod) * (word[i] - b) % (sqrtMod * sqrtMod)
        decryptedWord += numberToBigram(X)
    return decryptedWord

def wordToNumbers(word):
    result = []
    for i in range(0, len(word), 2):
        result.append(bigramToNumber(word[i], word[i + 1]))
    return result

numberWord = wordToNumbers(newString)

dataForY = [545, 417, 572, 403, 168]

topBigrams = ""
for i in range(0, len(listOfTopBigrams)):
    topBigrams += listOfTopBigrams[i]

dataForX = wordToNumbers(topBigrams)


def decypherPart2(X1, Y1, X2, Y2):
    listOfA, listOfB, n = systemSolve(X1, Y1, X2, Y2, m*m)
    for i in range(n):
        #print(X1, Y1, X2, Y2)
        #print(listOfA, listOfB)
        print("Recognition status:", recognizer(decypherPart1(listOfA[i], listOfB[i], m, numberWord)))
        print("a =", listOfA[i], "b =", listOfB[i], ":", decypherPart1(listOfA[i], listOfB[i], m, numberWord))
        if(recognizer(decypherPart1(listOfA[i], listOfB[i], m, numberWord)) == 1):
            break

for i in range(29):
    for t in range(i, 30):
        for j in range(0, 3):
            for k in range(j, 4):
                #print(dataForX[i], dataForY[j], dataForX[t + 1], dataForY[k + 1])
                decypherPart2(dataForX[i], dataForY[j], dataForX[t + 1], dataForY[k + 1])

