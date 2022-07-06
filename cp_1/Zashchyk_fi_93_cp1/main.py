# -*- coding: utf-8 -*-
import pandas as pd
import codecs
import math

f = codecs.open("file1.txt", "r", "utf-8")
fileString = f.read()

newString = fileString.replace(" ", "")

charList = list(newString)
charListSpace = list(fileString)

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

#print("У таблиці літери по горизонталі йдуть пршими в парах.")
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfS = pd.DataFrame(dictStep, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Кількість біграм без перетину (без пробілів):")
print(dfS)

for key in dictStep:
    for i in range(0, 31):
        dictStep[key][i] = dictStep[key][i] / len(charList)

#Крок 1, без пробілів
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfSF = pd.DataFrame(dictStep, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Частота біграм без перетину (без пробілів):")
print(dfSF)


dictCross = {
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
for i in range(0, len(newString) - 1):
    if (charList[i] == 'а' and charList[i + 1] == 'а'):
        dictCross["а"][0] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'б'):
        dictCross["а"][1] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'в'):
        dictCross["а"][2] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'г'):
        dictCross["а"][3] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'д'):
        dictCross["а"][4] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'е'):
        dictCross["а"][5] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ж'):
        dictCross["а"][6] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'з'):
        dictCross["а"][7] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'и'):
        dictCross["а"][8] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'й'):
        dictCross["а"][9] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'к'):
        dictCross["а"][10] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'л'):
        dictCross["а"][11] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'м'):
        dictCross["а"][12] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'н'):
        dictCross["а"][13] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'о'):
        dictCross["а"][14] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'п'):
        dictCross["а"][15] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'р'):
        dictCross["а"][16] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'с'):
        dictCross["а"][17] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'т'):
        dictCross["а"][18] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'у'):
        dictCross["а"][19] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ф'):
        dictCross["а"][20] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'х'):
        dictCross["а"][21] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ц'):
        dictCross["а"][22] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ч'):
        dictCross["а"][23] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ш'):
        dictCross["а"][24] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'щ'):
        dictCross["а"][25] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ы'):
        dictCross["а"][26] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ь'):
        dictCross["а"][27] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'э'):
        dictCross["а"][28] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'ю'):
        dictCross["а"][29] += 1
    if (charList[i] == 'а' and charList[i + 1] == 'я'):
        dictCross["а"][30] += 1
# для б
for i in range(0, len(newString) - 1):
    if (charList[i] == 'б' and charList[i + 1] == 'а'):
        dictCross["б"][0] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'б'):
        dictCross["б"][1] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'в'):
        dictCross["б"][2] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'г'):
        dictCross["б"][3] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'д'):
        dictCross["б"][4] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'е'):
        dictCross["б"][5] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ж'):
        dictCross["б"][6] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'з'):
        dictCross["б"][7] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'и'):
        dictCross["б"][8] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'й'):
        dictCross["б"][9] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'к'):
        dictCross["б"][10] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'л'):
        dictCross["б"][11] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'м'):
        dictCross["б"][12] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'н'):
        dictCross["б"][13] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'о'):
        dictCross["б"][14] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'п'):
        dictCross["б"][15] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'р'):
        dictCross["б"][16] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'с'):
        dictCross["б"][17] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'т'):
        dictCross["б"][18] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'у'):
        dictCross["б"][19] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ф'):
        dictCross["б"][20] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'х'):
        dictCross["б"][21] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ц'):
        dictCross["б"][22] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ч'):
        dictCross["б"][23] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ш'):
        dictCross["б"][24] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'щ'):
        dictCross["б"][25] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ы'):
        dictCross["б"][25] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ь'):
        dictCross["б"][26] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'э'):
        dictCross["б"][27] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'ю'):
        dictCross["б"][28] += 1
    if (charList[i] == 'б' and charList[i + 1] == 'я'):
        dictCross["б"][29] += 1
# для в
for i in range(0, len(newString) - 1) :
    if (charList[i] == 'в' and charList[i + 1] == 'а'):
        dictCross["в"][0] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'б'):
        dictCross["в"][1] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'в'):
        dictCross["в"][2] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'г'):
        dictCross["в"][3] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'д'):
        dictCross["в"][4] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'е'):
        dictCross["в"][5] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ж'):
        dictCross["в"][6] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'з'):
        dictCross["в"][7] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'и'):
        dictCross["в"][8] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'й'):
        dictCross["в"][9] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'к'):
        dictCross["в"][10] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'л'):
        dictCross["в"][11] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'м'):
        dictCross["в"][12] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'н'):
        dictCross["в"][13] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'о'):
        dictCross["в"][14] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'п'):
        dictCross["в"][15] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'р'):
        dictCross["в"][16] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'с'):
        dictCross["в"][17] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'т'):
        dictCross["в"][18] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'у'):
        dictCross["в"][19] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ф'):
        dictCross["в"][20] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'х'):
        dictCross["в"][21] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ц'):
        dictCross["в"][22] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ч'):
        dictCross["в"][23] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ш'):
        dictCross["в"][24] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'щ'):
        dictCross["в"][25] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ы'):
        dictCross["в"][26] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ь'):
        dictCross["в"][27] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'э'):
        dictCross["в"][28] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'ю'):
        dictCross["в"][29] += 1
    if (charList[i] == 'в' and charList[i + 1] == 'я'):
        dictCross["в"][30] += 1
# для г
for i in range(0, len(newString) - 1):
    if (charList[i] == 'г' and charList[i + 1] == 'а'):
        dictCross["г"][0] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'б'):
        dictCross["г"][1] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'в'):
        dictCross["г"][2] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'г'):
        dictCross["г"][3] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'д'):
        dictCross["г"][4] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'е'):
        dictCross["г"][5] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ж'):
        dictCross["г"][6] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'з'):
        dictCross["г"][7] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'и'):
        dictCross["г"][8] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'й'):
        dictCross["г"][9] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'к'):
        dictCross["г"][10] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'л'):
        dictCross["г"][11] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'м'):
        dictCross["г"][12] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'н'):
        dictCross["г"][13] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'о'):
        dictCross["г"][14] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'п'):
        dictCross["г"][15] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'р'):
        dictCross["г"][16] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'с'):
        dictCross["г"][17] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'т'):
        dictCross["г"][18] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'у'):
        dictCross["г"][19] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ф'):
        dictCross["г"][20] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'х'):
        dictCross["г"][21] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ц'):
        dictCross["г"][22] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ч'):
        dictCross["г"][23] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ш'):
        dictCross["г"][24] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'щ'):
        dictCross["г"][25] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ы'):
        dictCross["г"][26] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ь'):
        dictCross["г"][27] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'э'):
        dictCross["г"][28] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'ю'):
        dictCross["г"][29] += 1
    if (charList[i] == 'г' and charList[i + 1] == 'я'):
        dictCross["г"][30] += 1
# для д
for i in range(0, len(newString) - 1):
    if (charList[i] == 'д' and charList[i + 1] == 'а'):
        dictCross["д"][0] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'б'):
        dictCross["д"][1] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'в'):
        dictCross["д"][2] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'г'):
        dictCross["д"][3] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'д'):
        dictCross["д"][4] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'е'):
        dictCross["д"][5] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ж'):
        dictCross["д"][6] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'з'):
        dictCross["д"][7] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'и'):
        dictCross["д"][8] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'й'):
        dictCross["д"][9] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'к'):
        dictCross["д"][10] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'л'):
        dictCross["д"][11] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'м'):
        dictCross["д"][12] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'н'):
        dictCross["д"][13] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'о'):
        dictCross["д"][14] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'п'):
        dictCross["д"][15] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'р'):
        dictCross["д"][16] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'с'):
        dictCross["д"][17] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'т'):
        dictCross["д"][18] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'у'):
        dictCross["д"][19] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ф'):
        dictCross["д"][20] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'х'):
        dictCross["д"][21] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ц'):
        dictCross["д"][22] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ч'):
        dictCross["д"][23] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ш'):
        dictCross["д"][24] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'щ'):
        dictCross["д"][25] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ы'):
        dictCross["д"][26] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ь'):
        dictCross["д"][27] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'э'):
        dictCross["д"][28] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'ю'):
        dictCross["д"][29] += 1
    if (charList[i] == 'д' and charList[i + 1] == 'я'):
        dictCross["д"][30] += 1
# для е
for i in range(0, len(newString) - 1):
    if (charList[i] == 'е' and charList[i + 1] == 'а'):
        dictCross["е"][0] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'б'):
        dictCross["е"][1] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'в'):
        dictCross["е"][2] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'г'):
        dictCross["е"][3] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'д'):
        dictCross["е"][4] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'е'):
        dictCross["е"][5] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ж'):
        dictCross["е"][6] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'з'):
        dictCross["е"][7] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'и'):
        dictCross["е"][8] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'й'):
        dictCross["е"][9] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'к'):
        dictCross["е"][10] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'л'):
        dictCross["е"][11] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'м'):
        dictCross["е"][12] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'н'):
        dictCross["е"][13] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'о'):
        dictCross["е"][14] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'п'):
        dictCross["е"][15] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'р'):
        dictCross["е"][16] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'с'):
        dictCross["е"][17] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'т'):
        dictCross["е"][18] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'у'):
        dictCross["е"][19] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ф'):
        dictCross["е"][20] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'х'):
        dictCross["е"][21] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ц'):
        dictCross["е"][22] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ч'):
        dictCross["е"][23] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ш'):
        dictCross["е"][24] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'щ'):
        dictCross["е"][25] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ы'):
        dictCross["е"][26] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ь'):
        dictCross["е"][27] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'э'):
        dictCross["е"][28] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'ю'):
        dictCross["е"][29] += 1
    if (charList[i] == 'е' and charList[i + 1] == 'я'):
        dictCross["е"][30] += 1
# для ж
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ж' and charList[i + 1] == 'а'):
        dictCross["ж"][0] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'б'):
        dictCross["ж"][1] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'в'):
        dictCross["ж"][2] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'г'):
        dictCross["ж"][3] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'д'):
        dictCross["ж"][4] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'е'):
        dictCross["ж"][5] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ж'):
        dictCross["ж"][6] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'з'):
        dictCross["ж"][7] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'и'):
        dictCross["ж"][8] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'й'):
        dictCross["ж"][9] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'к'):
        dictCross["ж"][10] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'л'):
        dictCross["ж"][11] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'м'):
        dictCross["ж"][12] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'н'):
        dictCross["ж"][13] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'о'):
        dictCross["ж"][14] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'п'):
        dictCross["ж"][15] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'р'):
        dictCross["ж"][16] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'с'):
        dictCross["ж"][17] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'т'):
        dictCross["ж"][18] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'у'):
        dictCross["ж"][19] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ф'):
        dictCross["ж"][20] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'х'):
        dictCross["ж"][21] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ц'):
        dictCross["ж"][22] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ч'):
        dictCross["ж"][23] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ш'):
        dictCross["ж"][24] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'щ'):
        dictCross["ж"][25] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ы'):
        dictCross["ж"][26] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ь'):
        dictCross["ж"][27] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'э'):
        dictCross["ж"][28] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'ю'):
        dictCross["ж"][29] += 1
    if (charList[i] == 'ж' and charList[i + 1] == 'я'):
        dictCross["ж"][30] += 1
# для з
for i in range(0, len(newString) - 1):
    if (charList[i] == 'з' and charList[i + 1] == 'а'):
        dictCross["з"][0] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'б'):
        dictCross["з"][1] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'в'):
        dictCross["з"][2] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'г'):
        dictCross["з"][3] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'д'):
        dictCross["з"][4] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'е'):
        dictCross["з"][5] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ж'):
        dictCross["з"][6] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'з'):
        dictCross["з"][7] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'и'):
        dictCross["з"][8] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'й'):
        dictCross["з"][9] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'к'):
        dictCross["з"][10] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'л'):
        dictCross["з"][11] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'м'):
        dictCross["з"][12] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'н'):
        dictCross["з"][13] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'о'):
        dictCross["з"][14] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'п'):
        dictCross["з"][15] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'р'):
        dictCross["з"][16] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'с'):
        dictCross["з"][17] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'т'):
        dictCross["з"][18] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'у'):
        dictCross["з"][19] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ф'):
        dictCross["з"][20] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'х'):
        dictCross["з"][21] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ц'):
        dictCross["з"][22] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ч'):
        dictCross["з"][23] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ш'):
        dictCross["з"][24] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'щ'):
        dictCross["з"][25] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ы'):
        dictCross["з"][26] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ь'):
        dictCross["з"][27] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'э'):
        dictCross["з"][28] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'ю'):
        dictCross["з"][29] += 1
    if (charList[i] == 'з' and charList[i + 1] == 'я'):
        dictCross["з"][30] += 1
# для и
for i in range(0, len(newString) - 1):
    if (charList[i] == 'и' and charList[i + 1] == 'а'):
        dictCross["и"][0] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'б'):
        dictCross["и"][1] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'в'):
        dictCross["и"][2] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'г'):
        dictCross["и"][3] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'д'):
        dictCross["и"][4] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'е'):
        dictCross["и"][5] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ж'):
        dictCross["и"][6] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'з'):
        dictCross["и"][7] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'и'):
        dictCross["и"][8] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'й'):
        dictCross["и"][9] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'к'):
        dictCross["и"][10] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'л'):
        dictCross["и"][11] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'м'):
        dictCross["и"][12] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'н'):
        dictCross["и"][13] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'о'):
        dictCross["и"][14] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'п'):
        dictCross["и"][15] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'р'):
        dictCross["и"][16] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'с'):
        dictCross["и"][17] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'т'):
        dictCross["и"][18] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'у'):
        dictCross["и"][19] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ф'):
        dictCross["и"][20] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'х'):
        dictCross["и"][21] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ц'):
        dictCross["и"][22] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ч'):
        dictCross["и"][23] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ш'):
        dictCross["и"][24] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'щ'):
        dictCross["и"][25] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ы'):
        dictCross["и"][26] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ь'):
        dictCross["и"][27] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'э'):
        dictCross["и"][28] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'ю'):
        dictCross["и"][29] += 1
    if (charList[i] == 'и' and charList[i + 1] == 'я'):
        dictCross["и"][30] += 1
# для й
for i in range(0, len(newString) - 1):
    if (charList[i] == 'й' and charList[i + 1] == 'а'):
        dictCross["й"][0] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'б'):
        dictCross["й"][1] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'в'):
        dictCross["й"][2] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'г'):
        dictCross["й"][3] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'д'):
        dictCross["й"][4] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'е'):
        dictCross["й"][5] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ж'):
        dictCross["й"][6] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'з'):
        dictCross["й"][7] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'и'):
        dictCross["й"][8] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'й'):
        dictCross["й"][9] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'к'):
        dictCross["й"][10] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'л'):
        dictCross["й"][11] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'м'):
        dictCross["й"][12] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'н'):
        dictCross["й"][13] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'о'):
        dictCross["й"][14] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'п'):
        dictCross["й"][15] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'р'):
        dictCross["й"][16] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'с'):
        dictCross["й"][17] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'т'):
        dictCross["й"][18] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'у'):
        dictCross["й"][19] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ф'):
        dictCross["й"][20] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'х'):
        dictCross["й"][21] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ц'):
        dictCross["й"][22] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ч'):
        dictCross["й"][23] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ш'):
        dictCross["й"][24] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'щ'):
        dictCross["й"][25] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ы'):
        dictCross["й"][26] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ь'):
        dictCross["й"][27] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'э'):
        dictCross["й"][28] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'ю'):
        dictCross["й"][29] += 1
    if (charList[i] == 'й' and charList[i + 1] == 'я'):
        dictCross["й"][30] += 1
# для к
for i in range(0, len(newString) - 1):
    if (charList[i] == 'к' and charList[i + 1] == 'а'):
        dictCross["к"][0] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'б'):
        dictCross["к"][1] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'в'):
        dictCross["к"][2] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'г'):
        dictCross["к"][3] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'д'):
        dictCross["к"][4] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'е'):
        dictCross["к"][5] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ж'):
        dictCross["к"][6] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'з'):
        dictCross["к"][7] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'и'):
        dictCross["к"][8] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'й'):
        dictCross["к"][9] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'к'):
        dictCross["к"][10] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'л'):
        dictCross["к"][11] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'м'):
        dictCross["к"][12] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'н'):
        dictCross["к"][13] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'о'):
        dictCross["к"][14] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'п'):
        dictCross["к"][15] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'р'):
        dictCross["к"][16] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'с'):
        dictCross["к"][17] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'т'):
        dictCross["к"][18] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'у'):
        dictCross["к"][19] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ф'):
        dictCross["к"][20] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'х'):
        dictCross["к"][21] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ц'):
        dictCross["к"][22] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ч'):
        dictCross["к"][23] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ш'):
        dictCross["к"][24] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'щ'):
        dictCross["к"][25] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ы'):
        dictCross["к"][26] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ь'):
        dictCross["к"][27] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'э'):
        dictCross["к"][28] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'ю'):
        dictCross["к"][29] += 1
    if (charList[i] == 'к' and charList[i + 1] == 'я'):
        dictCross["к"][30] += 1
# для л
for i in range(0, len(newString) - 1):
    if (charList[i] == 'л' and charList[i + 1] == 'а'):
        dictCross["л"][0] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'б'):
        dictCross["л"][1] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'в'):
        dictCross["л"][2] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'г'):
        dictCross["л"][3] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'д'):
        dictCross["л"][4] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'е'):
        dictCross["л"][5] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ж'):
        dictCross["л"][6] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'з'):
        dictCross["л"][7] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'и'):
        dictCross["л"][8] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'й'):
        dictCross["л"][9] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'к'):
        dictCross["л"][10] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'л'):
        dictCross["л"][11] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'м'):
        dictCross["л"][12] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'н'):
        dictCross["л"][13] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'о'):
        dictCross["л"][14] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'п'):
        dictCross["л"][15] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'р'):
        dictCross["л"][16] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'с'):
        dictCross["л"][17] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'т'):
        dictCross["л"][18] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'у'):
        dictCross["л"][19] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ф'):
        dictCross["л"][20] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'х'):
        dictCross["л"][21] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ц'):
        dictCross["л"][22] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ч'):
        dictCross["л"][23] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ш'):
        dictCross["л"][24] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'щ'):
        dictCross["л"][25] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ы'):
        dictCross["л"][26] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ь'):
        dictCross["л"][27] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'э'):
        dictCross["л"][28] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'ю'):
        dictCross["л"][29] += 1
    if (charList[i] == 'л' and charList[i + 1] == 'я'):
        dictCross["л"][30] += 1
# для м
for i in range(0, len(newString) - 1):
    if (charList[i] == 'м' and charList[i + 1] == 'а'):
        dictCross["м"][0] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'б'):
        dictCross["м"][1] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'в'):
        dictCross["м"][2] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'г'):
        dictCross["м"][3] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'д'):
        dictCross["м"][4] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'е'):
        dictCross["м"][5] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ж'):
        dictCross["м"][6] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'з'):
        dictCross["м"][7] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'и'):
        dictCross["м"][8] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'й'):
        dictCross["м"][9] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'к'):
        dictCross["м"][10] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'л'):
        dictCross["м"][11] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'м'):
        dictCross["м"][12] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'н'):
        dictCross["м"][13] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'о'):
        dictCross["м"][14] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'п'):
        dictCross["м"][15] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'р'):
        dictCross["м"][16] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'с'):
        dictCross["м"][17] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'т'):
        dictCross["м"][18] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'у'):
        dictCross["м"][19] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ф'):
        dictCross["м"][20] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'х'):
        dictCross["м"][21] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ц'):
        dictCross["м"][22] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ч'):
        dictCross["м"][23] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ш'):
        dictCross["м"][24] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'щ'):
        dictCross["м"][25] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ы'):
        dictCross["м"][26] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ь'):
        dictCross["м"][27] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'э'):
        dictCross["м"][28] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'ю'):
        dictCross["м"][29] += 1
    if (charList[i] == 'м' and charList[i + 1] == 'я'):
        dictCross["м"][30] += 1
# для н
for i in range(0, len(newString) - 1):
    if (charList[i] == 'н' and charList[i + 1] == 'а'):
        dictCross["н"][0] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'б'):
        dictCross["н"][1] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'в'):
        dictCross["н"][2] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'г'):
        dictCross["н"][3] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'д'):
        dictCross["н"][4] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'е'):
        dictCross["н"][5] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ж'):
        dictCross["н"][6] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'з'):
        dictCross["н"][7] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'и'):
        dictCross["н"][8] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'й'):
        dictCross["н"][9] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'к'):
        dictCross["н"][10] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'л'):
        dictCross["н"][11] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'м'):
        dictCross["н"][12] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'н'):
        dictCross["н"][13] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'о'):
        dictCross["н"][14] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'п'):
        dictCross["н"][15] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'р'):
        dictCross["н"][16] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'с'):
        dictCross["н"][17] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'т'):
        dictCross["н"][18] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'у'):
        dictCross["н"][19] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ф'):
        dictCross["н"][20] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'х'):
        dictCross["н"][21] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ц'):
        dictCross["н"][22] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ч'):
        dictCross["н"][23] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ш'):
        dictCross["н"][24] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'щ'):
        dictCross["н"][25] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ы'):
        dictCross["н"][26] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ь'):
        dictCross["н"][27] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'э'):
        dictCross["н"][28] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'ю'):
        dictCross["н"][29] += 1
    if (charList[i] == 'н' and charList[i + 1] == 'я'):
        dictCross["н"][30] += 1
# для о
for i in range(0, len(newString) - 1):
    if (charList[i] == 'о' and charList[i + 1] == 'а'):
        dictCross["о"][0] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'б'):
        dictCross["о"][1] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'в'):
        dictCross["о"][2] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'г'):
        dictCross["о"][3] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'д'):
        dictCross["о"][4] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'е'):
        dictCross["о"][5] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ж'):
        dictCross["о"][6] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'з'):
        dictCross["о"][7] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'и'):
        dictCross["о"][8] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'й'):
        dictCross["о"][9] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'к'):
        dictCross["о"][10] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'л'):
        dictCross["о"][11] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'м'):
        dictCross["о"][12] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'н'):
        dictCross["о"][13] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'о'):
        dictCross["о"][14] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'п'):
        dictCross["о"][15] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'р'):
        dictCross["о"][16] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'с'):
        dictCross["о"][17] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'т'):
        dictCross["о"][18] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'у'):
        dictCross["о"][19] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ф'):
        dictCross["о"][20] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'х'):
        dictCross["о"][21] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ц'):
        dictCross["о"][22] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ч'):
        dictCross["о"][23] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ш'):
        dictCross["о"][24] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'щ'):
        dictCross["о"][25] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ы'):
        dictCross["о"][26] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ь'):
        dictCross["о"][27] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'э'):
        dictCross["о"][28] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'ю'):
        dictCross["о"][29] += 1
    if (charList[i] == 'о' and charList[i + 1] == 'я'):
        dictCross["о"][30] += 1
# для п
for i in range(0, len(newString) - 1):
    if (charList[i] == 'п' and charList[i + 1] == 'а'):
        dictCross["п"][0] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'б'):
        dictCross["п"][1] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'в'):
        dictCross["п"][2] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'г'):
        dictCross["п"][3] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'д'):
        dictCross["п"][4] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'е'):
        dictCross["п"][5] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ж'):
        dictCross["п"][6] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'з'):
        dictCross["п"][7] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'и'):
        dictCross["п"][8] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'й'):
        dictCross["п"][9] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'к'):
        dictCross["п"][10] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'л'):
        dictCross["п"][11] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'м'):
        dictCross["п"][12] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'н'):
        dictCross["п"][13] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'о'):
        dictCross["п"][14] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'п'):
        dictCross["п"][15] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'р'):
        dictCross["п"][16] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'с'):
        dictCross["п"][17] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'т'):
        dictCross["п"][18] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'у'):
        dictCross["п"][19] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ф'):
        dictCross["п"][20] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'х'):
        dictCross["п"][21] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ц'):
        dictCross["п"][22] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ч'):
        dictCross["п"][23] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ш'):
        dictCross["п"][24] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'щ'):
        dictCross["п"][25] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ы'):
        dictCross["п"][26] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ь'):
        dictCross["п"][27] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'э'):
        dictCross["п"][28] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'ю'):
        dictCross["п"][29] += 1
    if (charList[i] == 'п' and charList[i + 1] == 'я'):
        dictCross["п"][30] += 1
# для р
for i in range(0, len(newString) - 1):
    if (charList[i] == 'р' and charList[i + 1] == 'а'):
        dictCross["р"][0] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'б'):
        dictCross["р"][1] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'в'):
        dictCross["р"][2] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'г'):
        dictCross["р"][3] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'д'):
        dictCross["р"][4] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'е'):
        dictCross["р"][5] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ж'):
        dictCross["р"][6] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'з'):
        dictCross["р"][7] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'и'):
        dictCross["р"][8] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'й'):
        dictCross["р"][9] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'к'):
        dictCross["р"][10] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'л'):
        dictCross["р"][11] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'м'):
        dictCross["р"][12] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'н'):
        dictCross["р"][13] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'о'):
        dictCross["р"][14] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'п'):
        dictCross["р"][15] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'р'):
        dictCross["р"][16] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'с'):
        dictCross["р"][17] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'т'):
        dictCross["р"][18] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'у'):
        dictCross["р"][19] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ф'):
        dictCross["р"][20] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'х'):
        dictCross["р"][21] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ц'):
        dictCross["р"][22] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ч'):
        dictCross["р"][23] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ш'):
        dictCross["р"][24] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'щ'):
        dictCross["р"][25] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ы'):
        dictCross["р"][26] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ь'):
        dictCross["р"][27] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'э'):
        dictCross["р"][28] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'ю'):
        dictCross["р"][29] += 1
    if (charList[i] == 'р' and charList[i + 1] == 'я'):
        dictCross["р"][30] += 1
# для с
for i in range(0, len(newString) - 1):
    if (charList[i] == 'с' and charList[i + 1] == 'а'):
        dictCross["с"][0] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'б'):
        dictCross["с"][1] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'в'):
        dictCross["с"][2] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'г'):
        dictCross["с"][3] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'д'):
        dictCross["с"][4] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'е'):
        dictCross["с"][5] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ж'):
        dictCross["с"][6] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'з'):
        dictCross["с"][7] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'и'):
        dictCross["с"][8] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'й'):
        dictCross["с"][9] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'к'):
        dictCross["с"][10] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'л'):
        dictCross["с"][11] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'м'):
        dictCross["с"][12] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'н'):
        dictCross["с"][13] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'о'):
        dictCross["с"][14] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'п'):
        dictCross["с"][15] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'р'):
        dictCross["с"][16] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'с'):
        dictCross["с"][17] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'т'):
        dictCross["с"][18] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'у'):
        dictCross["с"][19] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ф'):
        dictCross["с"][20] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'х'):
        dictCross["с"][21] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ц'):
        dictCross["с"][22] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ч'):
        dictCross["с"][23] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ш'):
        dictCross["с"][24] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'щ'):
        dictCross["с"][25] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ы'):
        dictCross["с"][26] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ь'):
        dictCross["с"][27] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'э'):
        dictCross["с"][28] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'ю'):
        dictCross["с"][29] += 1
    if (charList[i] == 'с' and charList[i + 1] == 'я'):
        dictCross["с"][30] += 1
# для т
for i in range(0, len(newString) - 1):
    if (charList[i] == 'т' and charList[i + 1] == 'а'):
        dictCross["т"][0] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'б'):
        dictCross["т"][1] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'в'):
        dictCross["т"][2] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'г'):
        dictCross["т"][3] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'д'):
        dictCross["т"][4] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'е'):
        dictCross["т"][5] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ж'):
        dictCross["т"][6] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'з'):
        dictCross["т"][7] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'и'):
        dictCross["т"][8] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'й'):
        dictCross["т"][9] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'к'):
        dictCross["т"][10] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'л'):
        dictCross["т"][11] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'м'):
        dictCross["т"][12] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'н'):
        dictCross["т"][13] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'о'):
        dictCross["т"][14] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'п'):
        dictCross["т"][15] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'р'):
        dictCross["т"][16] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'с'):
        dictCross["т"][17] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'т'):
        dictCross["т"][18] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'у'):
        dictCross["т"][19] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ф'):
        dictCross["т"][20] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'х'):
        dictCross["т"][21] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ц'):
        dictCross["т"][22] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ч'):
        dictCross["т"][23] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ш'):
        dictCross["т"][24] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'щ'):
        dictCross["т"][25] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ы'):
        dictCross["т"][26] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ь'):
        dictCross["т"][27] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'э'):
        dictCross["т"][28] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'ю'):
        dictCross["т"][29] += 1
    if (charList[i] == 'т' and charList[i + 1] == 'я'):
        dictCross["т"][30] += 1
# для у
for i in range(0, len(newString) - 1):
    if (charList[i] == 'у' and charList[i + 1] == 'а'):
        dictCross["у"][0] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'б'):
        dictCross["у"][1] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'в'):
        dictCross["у"][2] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'г'):
        dictCross["у"][3] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'д'):
        dictCross["у"][4] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'е'):
        dictCross["у"][5] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ж'):
        dictCross["у"][6] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'з'):
        dictCross["у"][7] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'и'):
        dictCross["у"][8] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'й'):
        dictCross["у"][9] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'к'):
        dictCross["у"][10] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'л'):
        dictCross["у"][11] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'м'):
        dictCross["у"][12] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'н'):
        dictCross["у"][13] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'о'):
        dictCross["у"][14] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'п'):
        dictCross["у"][15] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'р'):
        dictCross["у"][16] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'с'):
        dictCross["у"][17] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'т'):
        dictCross["у"][18] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'у'):
        dictCross["у"][19] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ф'):
        dictCross["у"][20] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'х'):
        dictCross["у"][21] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ц'):
        dictCross["у"][22] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ч'):
        dictCross["у"][23] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ш'):
        dictCross["у"][24] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'щ'):
        dictCross["у"][25] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ы'):
        dictCross["у"][26] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ь'):
        dictCross["у"][27] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'э'):
        dictCross["у"][28] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'ю'):
        dictCross["у"][29] += 1
    if (charList[i] == 'у' and charList[i + 1] == 'я'):
        dictCross["у"][30] += 1
# для ф
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ф' and charList[i + 1] == 'а'):
        dictCross["ф"][0] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'б'):
        dictCross["ф"][1] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'в'):
        dictCross["ф"][2] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'г'):
        dictCross["ф"][3] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'д'):
        dictCross["ф"][4] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'е'):
        dictCross["ф"][5] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ж'):
        dictCross["ф"][6] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'з'):
        dictCross["ф"][7] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'и'):
        dictCross["ф"][8] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'й'):
        dictCross["ф"][9] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'к'):
        dictCross["ф"][10] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'л'):
        dictCross["ф"][11] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'м'):
        dictCross["ф"][12] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'н'):
        dictCross["ф"][13] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'о'):
        dictCross["ф"][14] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'п'):
        dictCross["ф"][15] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'р'):
        dictCross["ф"][16] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'с'):
        dictCross["ф"][17] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'т'):
        dictCross["ф"][18] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'у'):
        dictCross["ф"][19] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ф'):
        dictCross["ф"][20] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'х'):
        dictCross["ф"][21] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ц'):
        dictCross["ф"][22] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ч'):
        dictCross["ф"][23] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ш'):
        dictCross["ф"][24] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'щ'):
        dictCross["ф"][25] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ы'):
        dictCross["ф"][26] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ь'):
        dictCross["ф"][27] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'э'):
        dictCross["ф"][28] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'ю'):
        dictCross["ф"][29] += 1
    if (charList[i] == 'ф' and charList[i + 1] == 'я'):
        dictCross["ф"][30] += 1
# для х
for i in range(0, len(newString) - 1):
    if (charList[i] == 'х' and charList[i + 1] == 'а'):
        dictCross["х"][0] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'б'):
        dictCross["х"][1] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'в'):
        dictCross["х"][2] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'г'):
        dictCross["х"][3] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'д'):
        dictCross["х"][4] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'е'):
        dictCross["х"][5] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ж'):
        dictCross["х"][6] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'з'):
        dictCross["х"][7] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'и'):
        dictCross["х"][8] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'й'):
        dictCross["х"][9] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'к'):
        dictCross["х"][10] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'л'):
        dictCross["х"][11] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'м'):
        dictCross["х"][12] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'н'):
        dictCross["х"][13] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'о'):
        dictCross["х"][14] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'п'):
        dictCross["х"][15] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'р'):
        dictCross["х"][16] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'с'):
        dictCross["х"][17] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'т'):
        dictCross["х"][18] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'у'):
        dictCross["х"][19] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ф'):
        dictCross["х"][20] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'х'):
        dictCross["х"][21] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ц'):
        dictCross["х"][22] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ч'):
        dictCross["х"][23] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ш'):
        dictCross["х"][24] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'щ'):
        dictCross["х"][25] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ы'):
        dictCross["х"][26] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ь'):
        dictCross["х"][27] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'э'):
        dictCross["х"][28] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'ю'):
        dictCross["х"][29] += 1
    if (charList[i] == 'х' and charList[i + 1] == 'я'):
        dictCross["х"][30] += 1
# для ц
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ц' and charList[i + 1] == 'а'):
        dictCross["ц"][0] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'б'):
        dictCross["ц"][1] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'в'):
        dictCross["ц"][2] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'г'):
        dictCross["ц"][3] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'д'):
        dictCross["ц"][4] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'е'):
        dictCross["ц"][5] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ж'):
        dictCross["ц"][6] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'з'):
        dictCross["ц"][7] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'и'):
        dictCross["ц"][8] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'й'):
        dictCross["ц"][9] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'к'):
        dictCross["ц"][10] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'л'):
        dictCross["ц"][11] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'м'):
        dictCross["ц"][12] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'н'):
        dictCross["ц"][13] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'о'):
        dictCross["ц"][14] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'п'):
        dictCross["ц"][15] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'р'):
        dictCross["ц"][16] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'с'):
        dictCross["ц"][17] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'т'):
        dictCross["ц"][18] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'у'):
        dictCross["ц"][19] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ф'):
        dictCross["ц"][20] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'х'):
        dictCross["ц"][21] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ц'):
        dictCross["ц"][22] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ч'):
        dictCross["ц"][23] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ш'):
        dictCross["ц"][24] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'щ'):
        dictCross["ц"][25] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ы'):
        dictCross["ц"][26] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ь'):
        dictCross["ц"][27] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'э'):
        dictCross["ц"][28] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'ю'):
        dictCross["ц"][29] += 1
    if (charList[i] == 'ц' and charList[i + 1] == 'я'):
        dictCross["ц"][30] += 1
# для ч
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ч' and charList[i + 1] == 'а'):
        dictCross["ч"][0] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'б'):
        dictCross["ч"][1] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'в'):
        dictCross["ч"][2] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'г'):
        dictCross["ч"][3] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'д'):
        dictCross["ч"][4] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'е'):
        dictCross["ч"][5] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ж'):
        dictCross["ч"][6] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'з'):
        dictCross["ч"][7] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'и'):
        dictCross["ч"][8] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'й'):
        dictCross["ч"][9] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'к'):
        dictCross["ч"][10] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'л'):
        dictCross["ч"][11] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'м'):
        dictCross["ч"][12] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'н'):
        dictCross["ч"][13] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'о'):
        dictCross["ч"][14] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'п'):
        dictCross["ч"][15] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'р'):
        dictCross["ч"][16] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'с'):
        dictCross["ч"][17] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'т'):
        dictCross["ч"][18] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'у'):
        dictCross["ч"][19] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ф'):
        dictCross["ч"][20] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'х'):
        dictCross["ч"][21] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ц'):
        dictCross["ч"][22] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ч'):
        dictCross["ч"][23] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ш'):
        dictCross["ч"][24] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'щ'):
        dictCross["ч"][25] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ы'):
        dictCross["ч"][26] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ь'):
        dictCross["ч"][27] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'э'):
        dictCross["ч"][28] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'ю'):
        dictCross["ч"][29] += 1
    if (charList[i] == 'ч' and charList[i + 1] == 'я'):
        dictCross["ч"][30] += 1
# для ш
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ш' and charList[i + 1] == 'а'):
        dictCross["ш"][0] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'б'):
        dictCross["ш"][1] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'в'):
        dictCross["ш"][2] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'г'):
        dictCross["ш"][3] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'д'):
        dictCross["ш"][4] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'е'):
        dictCross["ш"][5] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ж'):
        dictCross["ш"][6] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'з'):
        dictCross["ш"][7] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'и'):
        dictCross["ш"][8] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'й'):
        dictCross["ш"][9] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'к'):
        dictCross["ш"][10] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'л'):
        dictCross["ш"][11] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'м'):
        dictCross["ш"][12] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'н'):
        dictCross["ш"][13] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'о'):
        dictCross["ш"][14] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'п'):
        dictCross["ш"][15] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'р'):
        dictCross["ш"][16] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'с'):
        dictCross["ш"][17] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'т'):
        dictCross["ш"][18] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'у'):
        dictCross["ш"][19] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ф'):
        dictCross["ш"][20] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'х'):
        dictCross["ш"][21] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ц'):
        dictCross["ш"][22] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ч'):
        dictCross["ш"][23] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ш'):
        dictCross["ш"][24] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'щ'):
        dictCross["ш"][25] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ы'):
        dictCross["ш"][26] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ь'):
        dictCross["ш"][27] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'э'):
        dictCross["ш"][28] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'ю'):
        dictCross["ш"][29] += 1
    if (charList[i] == 'ш' and charList[i + 1] == 'я'):
        dictCross["ш"][30] += 1
# для щ
for i in range(0, len(newString) - 1):
    if (charList[i] == 'щ' and charList[i + 1] == 'а'):
        dictCross["щ"][0] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'б'):
        dictCross["щ"][1] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'в'):
        dictCross["щ"][2] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'г'):
        dictCross["щ"][3] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'д'):
        dictCross["щ"][4] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'е'):
        dictCross["щ"][5] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ж'):
        dictCross["щ"][6] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'з'):
        dictCross["щ"][7] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'и'):
        dictCross["щ"][8] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'й'):
        dictCross["щ"][9] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'к'):
        dictCross["щ"][10] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'л'):
        dictCross["щ"][11] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'м'):
        dictCross["щ"][12] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'н'):
        dictCross["щ"][13] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'о'):
        dictCross["щ"][14] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'п'):
        dictCross["щ"][15] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'р'):
        dictCross["щ"][16] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'с'):
        dictCross["щ"][17] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'т'):
        dictCross["щ"][18] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'у'):
        dictCross["щ"][19] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ф'):
        dictCross["щ"][20] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'х'):
        dictCross["щ"][21] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ц'):
        dictCross["щ"][22] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ч'):
        dictCross["щ"][23] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ш'):
        dictCross["щ"][24] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'щ'):
        dictCross["щ"][25] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ы'):
        dictCross["щ"][26] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ь'):
        dictCross["щ"][27] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'э'):
        dictCross["щ"][28] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'ю'):
        dictCross["щ"][29] += 1
    if (charList[i] == 'щ' and charList[i + 1] == 'я'):
        dictCross["щ"][30] += 1
# для ы
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ы' and charList[i + 1] == 'а'):
        dictCross["ы"][0] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'б'):
        dictCross["ы"][1] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'в'):
        dictCross["ы"][2] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'г'):
        dictCross["ы"][3] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'д'):
        dictCross["ы"][4] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'е'):
        dictCross["ы"][5] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ж'):
        dictCross["ы"][6] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'з'):
        dictCross["ы"][7] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'и'):
        dictCross["ы"][8] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'й'):
        dictCross["ы"][9] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'к'):
        dictCross["ы"][10] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'л'):
        dictCross["ы"][11] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'м'):
        dictCross["ы"][12] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'н'):
        dictCross["ы"][13] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'о'):
        dictCross["ы"][14] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'п'):
        dictCross["ы"][15] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'р'):
        dictCross["ы"][16] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'с'):
        dictCross["ы"][17] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'т'):
        dictCross["ы"][18] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'у'):
        dictCross["ы"][19] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ф'):
        dictCross["ы"][20] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'х'):
        dictCross["ы"][21] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ц'):
        dictCross["ы"][22] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ч'):
        dictCross["ы"][23] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ш'):
        dictCross["ы"][24] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'щ'):
        dictCross["ы"][25] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ы'):
        dictCross["ы"][26] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ь'):
        dictCross["ы"][27] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'э'):
        dictCross["ы"][28] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'ю'):
        dictCross["ы"][29] += 1
    if (charList[i] == 'ы' and charList[i + 1] == 'я'):
        dictCross["ы"][30] += 1
# для ь
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ь' and charList[i + 1] == 'а'):
        dictCross["ь"][0] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'б'):
        dictCross["ь"][1] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'в'):
        dictCross["ь"][2] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'г'):
        dictCross["ь"][3] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'д'):
        dictCross["ь"][4] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'е'):
        dictCross["ь"][5] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ж'):
        dictCross["ь"][6] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'з'):
        dictCross["ь"][7] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'и'):
        dictCross["ь"][8] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'й'):
        dictCross["ь"][9] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'к'):
        dictCross["ь"][10] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'л'):
        dictCross["ь"][11] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'м'):
        dictCross["ь"][12] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'н'):
        dictCross["ь"][13] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'о'):
        dictCross["ь"][14] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'п'):
        dictCross["ь"][15] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'р'):
        dictCross["ь"][16] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'с'):
        dictCross["ь"][17] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'т'):
        dictCross["ь"][18] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'у'):
        dictCross["ь"][19] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ф'):
        dictCross["ь"][20] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'х'):
        dictCross["ь"][21] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ц'):
        dictCross["ь"][22] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ч'):
        dictCross["ь"][23] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ш'):
        dictCross["ь"][24] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'щ'):
        dictCross["ь"][25] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ы'):
        dictCross["ь"][26] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ь'):
        dictCross["ь"][27] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'э'):
        dictCross["ь"][28] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'ю'):
        dictCross["ь"][29] += 1
    if (charList[i] == 'ь' and charList[i + 1] == 'я'):
        dictCross["ь"][30] += 1
# для э
for i in range(0, len(newString) - 1):
    if (charList[i] == 'э' and charList[i + 1] == 'а'):
        dictCross["э"][0] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'б'):
        dictCross["э"][1] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'в'):
        dictCross["э"][2] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'г'):
        dictCross["э"][3] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'д'):
        dictCross["э"][4] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'е'):
        dictCross["э"][5] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ж'):
        dictCross["э"][6] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'з'):
        dictCross["э"][7] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'и'):
        dictCross["э"][8] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'й'):
        dictCross["э"][9] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'к'):
        dictCross["э"][10] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'л'):
        dictCross["э"][11] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'м'):
        dictCross["э"][12] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'н'):
        dictCross["э"][13] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'о'):
        dictCross["э"][14] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'п'):
        dictCross["э"][15] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'р'):
        dictCross["э"][16] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'с'):
        dictCross["э"][17] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'т'):
        dictCross["э"][18] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'у'):
        dictCross["э"][19] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ф'):
        dictCross["э"][20] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'х'):
        dictCross["э"][21] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ц'):
        dictCross["э"][22] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ч'):
        dictCross["э"][23] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ш'):
        dictCross["э"][24] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'щ'):
        dictCross["э"][25] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ы'):
        dictCross["э"][26] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ь'):
        dictCross["э"][27] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'э'):
        dictCross["э"][28] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'ю'):
        dictCross["э"][29] += 1
    if (charList[i] == 'э' and charList[i + 1] == 'я'):
        dictCross["э"][30] += 1
# для ю
for i in range(0, len(newString) - 1):
    if (charList[i] == 'ю' and charList[i + 1] == 'а'):
        dictCross["ю"][0] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'б'):
        dictCross["ю"][1] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'в'):
        dictCross["ю"][2] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'г'):
        dictCross["ю"][3] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'д'):
        dictCross["ю"][4] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'е'):
        dictCross["ю"][5] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ж'):
        dictCross["ю"][6] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'з'):
        dictCross["ю"][7] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'и'):
        dictCross["ю"][8] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'й'):
        dictCross["ю"][9] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'к'):
        dictCross["ю"][10] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'л'):
        dictCross["ю"][11] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'м'):
        dictCross["ю"][12] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'н'):
        dictCross["ю"][13] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'о'):
        dictCross["ю"][14] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'п'):
        dictCross["ю"][15] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'р'):
        dictCross["ю"][16] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'с'):
        dictCross["ю"][17] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'т'):
        dictCross["ю"][18] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'у'):
        dictCross["ю"][19] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ф'):
        dictCross["ю"][20] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'х'):
        dictCross["ю"][21] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ц'):
        dictCross["ю"][22] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ч'):
        dictCross["ю"][23] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ш'):
        dictCross["ю"][24] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'щ'):
        dictCross["ю"][25] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ы'):
        dictCross["ю"][26] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ь'):
        dictCross["ю"][27] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'э'):
        dictCross["ю"][28] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'ю'):
        dictCross["ю"][29] += 1
    if (charList[i] == 'ю' and charList[i + 1] == 'я'):
        dictCross["ю"][30] += 1
# для я
for i in range(0, len(newString) - 1):
    if (charList[i] == 'я' and charList[i + 1] == 'а'):
        dictCross["я"][0] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'б'):
        dictCross["я"][1] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'в'):
        dictCross["я"][2] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'г'):
        dictCross["я"][3] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'д'):
        dictCross["я"][4] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'е'):
        dictCross["я"][5] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ж'):
        dictCross["я"][6] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'з'):
        dictCross["я"][7] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'и'):
        dictCross["я"][8] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'й'):
        dictCross["я"][9] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'к'):
        dictCross["я"][10] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'л'):
        dictCross["я"][11] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'м'):
        dictCross["я"][12] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'н'):
        dictCross["я"][13] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'о'):
        dictCross["я"][14] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'п'):
        dictCross["я"][15] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'р'):
        dictCross["я"][16] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'с'):
        dictCross["я"][17] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'т'):
        dictCross["я"][18] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'у'):
        dictCross["я"][19] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ф'):
        dictCross["я"][20] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'х'):
        dictCross["я"][21] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ц'):
        dictCross["я"][22] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ч'):
        dictCross["я"][23] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ш'):
        dictCross["я"][24] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'щ'):
        dictCross["я"][25] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ы'):
        dictCross["я"][26] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ь'):
        dictCross["я"][27] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'э'):
        dictCross["я"][28] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'ю'):
        dictCross["я"][29] += 1
    if (charList[i] == 'я' and charList[i + 1] == 'я'):
        dictCross["я"][30] += 1

print()
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfC = pd.DataFrame(dictCross, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Кількість біграм з перетином (без пробілів):")
print(dfC)

for key in dictCross:
    for i in range(0, 31):
        dictCross[key][i] = dictCross[key][i] / len(charList)

#Крок 2, без пробілів
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfCF = pd.DataFrame(dictCross, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Частота біграм з перетином (без пробілів):")
print(dfCF)


dictStepSpace = {
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
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'а'):
        dictStepSpace["а"][0] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'б'):
        dictStepSpace["а"][1] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'в'):
        dictStepSpace["а"][2] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'г'):
        dictStepSpace["а"][3] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'д'):
        dictStepSpace["а"][4] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'е'):
        dictStepSpace["а"][5] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["а"][6] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'з'):
        dictStepSpace["а"][7] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'и'):
        dictStepSpace["а"][8] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'й'):
        dictStepSpace["а"][9] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'к'):
        dictStepSpace["а"][10] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'л'):
        dictStepSpace["а"][11] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'м'):
        dictStepSpace["а"][12] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'н'):
        dictStepSpace["а"][13] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'о'):
        dictStepSpace["а"][14] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'п'):
        dictStepSpace["а"][15] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'р'):
        dictStepSpace["а"][16] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'с'):
        dictStepSpace["а"][17] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'т'):
        dictStepSpace["а"][18] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'у'):
        dictStepSpace["а"][19] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["а"][20] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'х'):
        dictStepSpace["а"][21] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["а"][22] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["а"][23] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["а"][24] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["а"][25] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["а"][26] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["а"][27] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'э'):
        dictStepSpace["а"][28] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["а"][29] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'я'):
        dictStepSpace["а"][30] += 1
# для б
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'а'):
        dictStepSpace["б"][0] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'б'):
        dictStepSpace["б"][1] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'в'):
        dictStepSpace["б"][2] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'г'):
        dictStepSpace["б"][3] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'д'):
        dictStepSpace["б"][4] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'е'):
        dictStepSpace["б"][5] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["б"][6] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'з'):
        dictStepSpace["б"][7] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'и'):
        dictStepSpace["б"][8] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'й'):
        dictStepSpace["б"][9] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'к'):
        dictStepSpace["б"][10] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'л'):
        dictStepSpace["б"][11] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'м'):
        dictStepSpace["б"][12] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'н'):
        dictStepSpace["б"][13] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'о'):
        dictStepSpace["б"][14] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'п'):
        dictStepSpace["б"][15] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'р'):
        dictStepSpace["б"][16] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'с'):
        dictStepSpace["б"][17] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'т'):
        dictStepSpace["б"][18] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'у'):
        dictStepSpace["б"][19] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["б"][20] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'х'):
        dictStepSpace["б"][21] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["б"][22] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["б"][23] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["б"][24] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["б"][25] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["б"][25] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["б"][26] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'э'):
        dictStepSpace["б"][27] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["б"][28] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'я'):
        dictStepSpace["б"][29] += 1
# для в
for i in range(0, len(fileString) - 1, 2) :
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'а'):
        dictStepSpace["в"][0] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'б'):
        dictStepSpace["в"][1] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'в'):
        dictStepSpace["в"][2] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'г'):
        dictStepSpace["в"][3] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'д'):
        dictStepSpace["в"][4] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'е'):
        dictStepSpace["в"][5] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["в"][6] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'з'):
        dictStepSpace["в"][7] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'и'):
        dictStepSpace["в"][8] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'й'):
        dictStepSpace["в"][9] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'к'):
        dictStepSpace["в"][10] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'л'):
        dictStepSpace["в"][11] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'м'):
        dictStepSpace["в"][12] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'н'):
        dictStepSpace["в"][13] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'о'):
        dictStepSpace["в"][14] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'п'):
        dictStepSpace["в"][15] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'р'):
        dictStepSpace["в"][16] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'с'):
        dictStepSpace["в"][17] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'т'):
        dictStepSpace["в"][18] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'у'):
        dictStepSpace["в"][19] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["в"][20] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'х'):
        dictStepSpace["в"][21] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["в"][22] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["в"][23] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["в"][24] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["в"][25] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["в"][26] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["в"][27] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'э'):
        dictStepSpace["в"][28] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["в"][29] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'я'):
        dictStepSpace["в"][30] += 1
# для г
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'а'):
        dictStepSpace["г"][0] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'б'):
        dictStepSpace["г"][1] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'в'):
        dictStepSpace["г"][2] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'г'):
        dictStepSpace["г"][3] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'д'):
        dictStepSpace["г"][4] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'е'):
        dictStepSpace["г"][5] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["г"][6] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'з'):
        dictStepSpace["г"][7] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'и'):
        dictStepSpace["г"][8] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'й'):
        dictStepSpace["г"][9] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'к'):
        dictStepSpace["г"][10] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'л'):
        dictStepSpace["г"][11] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'м'):
        dictStepSpace["г"][12] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'н'):
        dictStepSpace["г"][13] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'о'):
        dictStepSpace["г"][14] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'п'):
        dictStepSpace["г"][15] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'р'):
        dictStepSpace["г"][16] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'с'):
        dictStepSpace["г"][17] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'т'):
        dictStepSpace["г"][18] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'у'):
        dictStepSpace["г"][19] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["г"][20] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'х'):
        dictStepSpace["г"][21] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["г"][22] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["г"][23] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["г"][24] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["г"][25] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["г"][26] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["г"][27] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'э'):
        dictStepSpace["г"][28] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["г"][29] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'я'):
        dictStepSpace["г"][30] += 1
# для д
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'а'):
        dictStepSpace["д"][0] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'б'):
        dictStepSpace["д"][1] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'в'):
        dictStepSpace["д"][2] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'г'):
        dictStepSpace["д"][3] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'д'):
        dictStepSpace["д"][4] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'е'):
        dictStepSpace["д"][5] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["д"][6] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'з'):
        dictStepSpace["д"][7] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'и'):
        dictStepSpace["д"][8] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'й'):
        dictStepSpace["д"][9] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'к'):
        dictStepSpace["д"][10] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'л'):
        dictStepSpace["д"][11] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'м'):
        dictStepSpace["д"][12] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'н'):
        dictStepSpace["д"][13] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'о'):
        dictStepSpace["д"][14] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'п'):
        dictStepSpace["д"][15] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'р'):
        dictStepSpace["д"][16] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'с'):
        dictStepSpace["д"][17] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'т'):
        dictStepSpace["д"][18] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'у'):
        dictStepSpace["д"][19] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["д"][20] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'х'):
        dictStepSpace["д"][21] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["д"][22] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["д"][23] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["д"][24] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["д"][25] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["д"][26] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["д"][27] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'э'):
        dictStepSpace["д"][28] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["д"][29] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'я'):
        dictStepSpace["д"][30] += 1
# для е
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'а'):
        dictStepSpace["е"][0] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'б'):
        dictStepSpace["е"][1] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'в'):
        dictStepSpace["е"][2] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'г'):
        dictStepSpace["е"][3] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'д'):
        dictStepSpace["е"][4] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'е'):
        dictStepSpace["е"][5] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["е"][6] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'з'):
        dictStepSpace["е"][7] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'и'):
        dictStepSpace["е"][8] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'й'):
        dictStepSpace["е"][9] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'к'):
        dictStepSpace["е"][10] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'л'):
        dictStepSpace["е"][11] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'м'):
        dictStepSpace["е"][12] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'н'):
        dictStepSpace["е"][13] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'о'):
        dictStepSpace["е"][14] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'п'):
        dictStepSpace["е"][15] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'р'):
        dictStepSpace["е"][16] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'с'):
        dictStepSpace["е"][17] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'т'):
        dictStepSpace["е"][18] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'у'):
        dictStepSpace["е"][19] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["е"][20] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'х'):
        dictStepSpace["е"][21] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["е"][22] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["е"][23] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["е"][24] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["е"][25] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["е"][26] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["е"][27] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'э'):
        dictStepSpace["е"][28] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["е"][29] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'я'):
        dictStepSpace["е"][30] += 1
# для ж
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ж"][0] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ж"][1] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ж"][2] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ж"][3] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ж"][4] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ж"][5] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ж"][6] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ж"][7] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ж"][8] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ж"][9] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ж"][10] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ж"][11] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ж"][12] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ж"][13] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ж"][14] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ж"][15] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ж"][16] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ж"][17] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ж"][18] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ж"][19] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ж"][20] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ж"][21] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ж"][22] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ж"][23] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ж"][24] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ж"][25] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ж"][26] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ж"][27] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ж"][28] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ж"][29] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ж"][30] += 1
# для з
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'а'):
        dictStepSpace["з"][0] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'б'):
        dictStepSpace["з"][1] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'в'):
        dictStepSpace["з"][2] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'г'):
        dictStepSpace["з"][3] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'д'):
        dictStepSpace["з"][4] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'е'):
        dictStepSpace["з"][5] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["з"][6] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'з'):
        dictStepSpace["з"][7] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'и'):
        dictStepSpace["з"][8] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'й'):
        dictStepSpace["з"][9] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'к'):
        dictStepSpace["з"][10] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'л'):
        dictStepSpace["з"][11] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'м'):
        dictStepSpace["з"][12] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'н'):
        dictStepSpace["з"][13] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'о'):
        dictStepSpace["з"][14] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'п'):
        dictStepSpace["з"][15] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'р'):
        dictStepSpace["з"][16] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'с'):
        dictStepSpace["з"][17] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'т'):
        dictStepSpace["з"][18] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'у'):
        dictStepSpace["з"][19] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["з"][20] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'х'):
        dictStepSpace["з"][21] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["з"][22] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["з"][23] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["з"][24] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["з"][25] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["з"][26] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["з"][27] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'э'):
        dictStepSpace["з"][28] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["з"][29] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'я'):
        dictStepSpace["з"][30] += 1
# для и
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'а'):
        dictStepSpace["и"][0] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'б'):
        dictStepSpace["и"][1] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'в'):
        dictStepSpace["и"][2] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'г'):
        dictStepSpace["и"][3] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'д'):
        dictStepSpace["и"][4] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'е'):
        dictStepSpace["и"][5] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["и"][6] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'з'):
        dictStepSpace["и"][7] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'и'):
        dictStepSpace["и"][8] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'й'):
        dictStepSpace["и"][9] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'к'):
        dictStepSpace["и"][10] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'л'):
        dictStepSpace["и"][11] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'м'):
        dictStepSpace["и"][12] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'н'):
        dictStepSpace["и"][13] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'о'):
        dictStepSpace["и"][14] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'п'):
        dictStepSpace["и"][15] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'р'):
        dictStepSpace["и"][16] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'с'):
        dictStepSpace["и"][17] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'т'):
        dictStepSpace["и"][18] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'у'):
        dictStepSpace["и"][19] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["и"][20] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'х'):
        dictStepSpace["и"][21] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["и"][22] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["и"][23] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["и"][24] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["и"][25] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["и"][26] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["и"][27] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'э'):
        dictStepSpace["и"][28] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["и"][29] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'я'):
        dictStepSpace["и"][30] += 1
# для й
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'а'):
        dictStepSpace["й"][0] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'б'):
        dictStepSpace["й"][1] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'в'):
        dictStepSpace["й"][2] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'г'):
        dictStepSpace["й"][3] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'д'):
        dictStepSpace["й"][4] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'е'):
        dictStepSpace["й"][5] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["й"][6] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'з'):
        dictStepSpace["й"][7] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'и'):
        dictStepSpace["й"][8] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'й'):
        dictStepSpace["й"][9] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'к'):
        dictStepSpace["й"][10] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'л'):
        dictStepSpace["й"][11] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'м'):
        dictStepSpace["й"][12] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'н'):
        dictStepSpace["й"][13] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'о'):
        dictStepSpace["й"][14] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'п'):
        dictStepSpace["й"][15] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'р'):
        dictStepSpace["й"][16] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'с'):
        dictStepSpace["й"][17] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'т'):
        dictStepSpace["й"][18] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'у'):
        dictStepSpace["й"][19] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["й"][20] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'х'):
        dictStepSpace["й"][21] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["й"][22] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["й"][23] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["й"][24] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["й"][25] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["й"][26] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["й"][27] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'э'):
        dictStepSpace["й"][28] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["й"][29] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'я'):
        dictStepSpace["й"][30] += 1
# для к
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'а'):
        dictStepSpace["к"][0] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'б'):
        dictStepSpace["к"][1] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'в'):
        dictStepSpace["к"][2] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'г'):
        dictStepSpace["к"][3] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'д'):
        dictStepSpace["к"][4] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'е'):
        dictStepSpace["к"][5] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["к"][6] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'з'):
        dictStepSpace["к"][7] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'и'):
        dictStepSpace["к"][8] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'й'):
        dictStepSpace["к"][9] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'к'):
        dictStepSpace["к"][10] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'л'):
        dictStepSpace["к"][11] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'м'):
        dictStepSpace["к"][12] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'н'):
        dictStepSpace["к"][13] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'о'):
        dictStepSpace["к"][14] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'п'):
        dictStepSpace["к"][15] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'р'):
        dictStepSpace["к"][16] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'с'):
        dictStepSpace["к"][17] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'т'):
        dictStepSpace["к"][18] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'у'):
        dictStepSpace["к"][19] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["к"][20] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'х'):
        dictStepSpace["к"][21] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["к"][22] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["к"][23] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["к"][24] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["к"][25] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["к"][26] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["к"][27] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'э'):
        dictStepSpace["к"][28] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["к"][29] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'я'):
        dictStepSpace["к"][30] += 1
# для л
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'а'):
        dictStepSpace["л"][0] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'б'):
        dictStepSpace["л"][1] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'в'):
        dictStepSpace["л"][2] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'г'):
        dictStepSpace["л"][3] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'д'):
        dictStepSpace["л"][4] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'е'):
        dictStepSpace["л"][5] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["л"][6] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'з'):
        dictStepSpace["л"][7] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'и'):
        dictStepSpace["л"][8] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'й'):
        dictStepSpace["л"][9] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'к'):
        dictStepSpace["л"][10] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'л'):
        dictStepSpace["л"][11] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'м'):
        dictStepSpace["л"][12] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'н'):
        dictStepSpace["л"][13] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'о'):
        dictStepSpace["л"][14] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'п'):
        dictStepSpace["л"][15] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'р'):
        dictStepSpace["л"][16] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'с'):
        dictStepSpace["л"][17] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'т'):
        dictStepSpace["л"][18] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'у'):
        dictStepSpace["л"][19] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["л"][20] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'х'):
        dictStepSpace["л"][21] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["л"][22] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["л"][23] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["л"][24] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["л"][25] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["л"][26] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["л"][27] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'э'):
        dictStepSpace["л"][28] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["л"][29] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'я'):
        dictStepSpace["л"][30] += 1
# для м
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'а'):
        dictStepSpace["м"][0] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'б'):
        dictStepSpace["м"][1] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'в'):
        dictStepSpace["м"][2] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'г'):
        dictStepSpace["м"][3] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'д'):
        dictStepSpace["м"][4] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'е'):
        dictStepSpace["м"][5] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["м"][6] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'з'):
        dictStepSpace["м"][7] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'и'):
        dictStepSpace["м"][8] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'й'):
        dictStepSpace["м"][9] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'к'):
        dictStepSpace["м"][10] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'л'):
        dictStepSpace["м"][11] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'м'):
        dictStepSpace["м"][12] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'н'):
        dictStepSpace["м"][13] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'о'):
        dictStepSpace["м"][14] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'п'):
        dictStepSpace["м"][15] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'р'):
        dictStepSpace["м"][16] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'с'):
        dictStepSpace["м"][17] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'т'):
        dictStepSpace["м"][18] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'у'):
        dictStepSpace["м"][19] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["м"][20] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'х'):
        dictStepSpace["м"][21] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["м"][22] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["м"][23] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["м"][24] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["м"][25] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["м"][26] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["м"][27] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'э'):
        dictStepSpace["м"][28] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["м"][29] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'я'):
        dictStepSpace["м"][30] += 1
# для н
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'а'):
        dictStepSpace["н"][0] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'б'):
        dictStepSpace["н"][1] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'в'):
        dictStepSpace["н"][2] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'г'):
        dictStepSpace["н"][3] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'д'):
        dictStepSpace["н"][4] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'е'):
        dictStepSpace["н"][5] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["н"][6] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'з'):
        dictStepSpace["н"][7] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'и'):
        dictStepSpace["н"][8] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'й'):
        dictStepSpace["н"][9] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'к'):
        dictStepSpace["н"][10] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'л'):
        dictStepSpace["н"][11] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'м'):
        dictStepSpace["н"][12] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'н'):
        dictStepSpace["н"][13] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'о'):
        dictStepSpace["н"][14] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'п'):
        dictStepSpace["н"][15] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'р'):
        dictStepSpace["н"][16] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'с'):
        dictStepSpace["н"][17] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'т'):
        dictStepSpace["н"][18] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'у'):
        dictStepSpace["н"][19] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["н"][20] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'х'):
        dictStepSpace["н"][21] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["н"][22] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["н"][23] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["н"][24] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["н"][25] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["н"][26] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["н"][27] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'э'):
        dictStepSpace["н"][28] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["н"][29] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'я'):
        dictStepSpace["н"][30] += 1
# для о
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'а'):
        dictStepSpace["о"][0] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'б'):
        dictStepSpace["о"][1] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'в'):
        dictStepSpace["о"][2] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'г'):
        dictStepSpace["о"][3] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'д'):
        dictStepSpace["о"][4] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'е'):
        dictStepSpace["о"][5] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["о"][6] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'з'):
        dictStepSpace["о"][7] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'и'):
        dictStepSpace["о"][8] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'й'):
        dictStepSpace["о"][9] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'к'):
        dictStepSpace["о"][10] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'л'):
        dictStepSpace["о"][11] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'м'):
        dictStepSpace["о"][12] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'н'):
        dictStepSpace["о"][13] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'о'):
        dictStepSpace["о"][14] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'п'):
        dictStepSpace["о"][15] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'р'):
        dictStepSpace["о"][16] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'с'):
        dictStepSpace["о"][17] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'т'):
        dictStepSpace["о"][18] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'у'):
        dictStepSpace["о"][19] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["о"][20] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'х'):
        dictStepSpace["о"][21] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["о"][22] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["о"][23] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["о"][24] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["о"][25] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["о"][26] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["о"][27] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'э'):
        dictStepSpace["о"][28] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["о"][29] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'я'):
        dictStepSpace["о"][30] += 1
# для п
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'а'):
        dictStepSpace["п"][0] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'б'):
        dictStepSpace["п"][1] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'в'):
        dictStepSpace["п"][2] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'г'):
        dictStepSpace["п"][3] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'д'):
        dictStepSpace["п"][4] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'е'):
        dictStepSpace["п"][5] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["п"][6] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'з'):
        dictStepSpace["п"][7] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'и'):
        dictStepSpace["п"][8] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'й'):
        dictStepSpace["п"][9] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'к'):
        dictStepSpace["п"][10] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'л'):
        dictStepSpace["п"][11] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'м'):
        dictStepSpace["п"][12] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'н'):
        dictStepSpace["п"][13] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'о'):
        dictStepSpace["п"][14] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'п'):
        dictStepSpace["п"][15] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'р'):
        dictStepSpace["п"][16] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'с'):
        dictStepSpace["п"][17] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'т'):
        dictStepSpace["п"][18] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'у'):
        dictStepSpace["п"][19] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["п"][20] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'х'):
        dictStepSpace["п"][21] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["п"][22] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["п"][23] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["п"][24] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["п"][25] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["п"][26] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["п"][27] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'э'):
        dictStepSpace["п"][28] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["п"][29] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'я'):
        dictStepSpace["п"][30] += 1
# для р
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'а'):
        dictStepSpace["р"][0] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'б'):
        dictStepSpace["р"][1] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'в'):
        dictStepSpace["р"][2] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'г'):
        dictStepSpace["р"][3] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'д'):
        dictStepSpace["р"][4] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'е'):
        dictStepSpace["р"][5] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["р"][6] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'з'):
        dictStepSpace["р"][7] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'и'):
        dictStepSpace["р"][8] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'й'):
        dictStepSpace["р"][9] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'к'):
        dictStepSpace["р"][10] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'л'):
        dictStepSpace["р"][11] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'м'):
        dictStepSpace["р"][12] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'н'):
        dictStepSpace["р"][13] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'о'):
        dictStepSpace["р"][14] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'п'):
        dictStepSpace["р"][15] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'р'):
        dictStepSpace["р"][16] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'с'):
        dictStepSpace["р"][17] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'т'):
        dictStepSpace["р"][18] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'у'):
        dictStepSpace["р"][19] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["р"][20] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'х'):
        dictStepSpace["р"][21] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["р"][22] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["р"][23] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["р"][24] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["р"][25] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["р"][26] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["р"][27] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'э'):
        dictStepSpace["р"][28] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["р"][29] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'я'):
        dictStepSpace["р"][30] += 1
# для с
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'а'):
        dictStepSpace["с"][0] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'б'):
        dictStepSpace["с"][1] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'в'):
        dictStepSpace["с"][2] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'г'):
        dictStepSpace["с"][3] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'д'):
        dictStepSpace["с"][4] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'е'):
        dictStepSpace["с"][5] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["с"][6] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'з'):
        dictStepSpace["с"][7] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'и'):
        dictStepSpace["с"][8] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'й'):
        dictStepSpace["с"][9] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'к'):
        dictStepSpace["с"][10] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'л'):
        dictStepSpace["с"][11] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'м'):
        dictStepSpace["с"][12] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'н'):
        dictStepSpace["с"][13] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'о'):
        dictStepSpace["с"][14] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'п'):
        dictStepSpace["с"][15] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'р'):
        dictStepSpace["с"][16] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'с'):
        dictStepSpace["с"][17] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'т'):
        dictStepSpace["с"][18] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'у'):
        dictStepSpace["с"][19] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["с"][20] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'х'):
        dictStepSpace["с"][21] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["с"][22] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["с"][23] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["с"][24] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["с"][25] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["с"][26] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["с"][27] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'э'):
        dictStepSpace["с"][28] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["с"][29] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'я'):
        dictStepSpace["с"][30] += 1
# для т
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'а'):
        dictStepSpace["т"][0] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'б'):
        dictStepSpace["т"][1] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'в'):
        dictStepSpace["т"][2] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'г'):
        dictStepSpace["т"][3] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'д'):
        dictStepSpace["т"][4] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'е'):
        dictStepSpace["т"][5] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["т"][6] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'з'):
        dictStepSpace["т"][7] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'и'):
        dictStepSpace["т"][8] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'й'):
        dictStepSpace["т"][9] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'к'):
        dictStepSpace["т"][10] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'л'):
        dictStepSpace["т"][11] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'м'):
        dictStepSpace["т"][12] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'н'):
        dictStepSpace["т"][13] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'о'):
        dictStepSpace["т"][14] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'п'):
        dictStepSpace["т"][15] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'р'):
        dictStepSpace["т"][16] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'с'):
        dictStepSpace["т"][17] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'т'):
        dictStepSpace["т"][18] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'у'):
        dictStepSpace["т"][19] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["т"][20] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'х'):
        dictStepSpace["т"][21] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["т"][22] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["т"][23] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["т"][24] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["т"][25] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["т"][26] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["т"][27] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'э'):
        dictStepSpace["т"][28] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["т"][29] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'я'):
        dictStepSpace["т"][30] += 1
# для у
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'а'):
        dictStepSpace["у"][0] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'б'):
        dictStepSpace["у"][1] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'в'):
        dictStepSpace["у"][2] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'г'):
        dictStepSpace["у"][3] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'д'):
        dictStepSpace["у"][4] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'е'):
        dictStepSpace["у"][5] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["у"][6] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'з'):
        dictStepSpace["у"][7] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'и'):
        dictStepSpace["у"][8] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'й'):
        dictStepSpace["у"][9] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'к'):
        dictStepSpace["у"][10] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'л'):
        dictStepSpace["у"][11] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'м'):
        dictStepSpace["у"][12] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'н'):
        dictStepSpace["у"][13] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'о'):
        dictStepSpace["у"][14] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'п'):
        dictStepSpace["у"][15] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'р'):
        dictStepSpace["у"][16] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'с'):
        dictStepSpace["у"][17] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'т'):
        dictStepSpace["у"][18] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'у'):
        dictStepSpace["у"][19] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["у"][20] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'х'):
        dictStepSpace["у"][21] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["у"][22] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["у"][23] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["у"][24] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["у"][25] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["у"][26] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["у"][27] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'э'):
        dictStepSpace["у"][28] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["у"][29] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'я'):
        dictStepSpace["у"][30] += 1
# для ф
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ф"][0] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ф"][1] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ф"][2] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ф"][3] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ф"][4] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ф"][5] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ф"][6] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ф"][7] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ф"][8] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ф"][9] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ф"][10] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ф"][11] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ф"][12] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ф"][13] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ф"][14] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ф"][15] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ф"][16] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ф"][17] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ф"][18] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ф"][19] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ф"][20] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ф"][21] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ф"][22] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ф"][23] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ф"][24] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ф"][25] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ф"][26] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ф"][27] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ф"][28] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ф"][29] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ф"][30] += 1
# для х
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'а'):
        dictStepSpace["х"][0] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'б'):
        dictStepSpace["х"][1] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'в'):
        dictStepSpace["х"][2] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'г'):
        dictStepSpace["х"][3] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'д'):
        dictStepSpace["х"][4] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'е'):
        dictStepSpace["х"][5] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["х"][6] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'з'):
        dictStepSpace["х"][7] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'и'):
        dictStepSpace["х"][8] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'й'):
        dictStepSpace["х"][9] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'к'):
        dictStepSpace["х"][10] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'л'):
        dictStepSpace["х"][11] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'м'):
        dictStepSpace["х"][12] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'н'):
        dictStepSpace["х"][13] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'о'):
        dictStepSpace["х"][14] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'п'):
        dictStepSpace["х"][15] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'р'):
        dictStepSpace["х"][16] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'с'):
        dictStepSpace["х"][17] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'т'):
        dictStepSpace["х"][18] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'у'):
        dictStepSpace["х"][19] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["х"][20] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'х'):
        dictStepSpace["х"][21] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["х"][22] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["х"][23] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["х"][24] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["х"][25] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["х"][26] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["х"][27] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'э'):
        dictStepSpace["х"][28] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["х"][29] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'я'):
        dictStepSpace["х"][30] += 1
# для ц
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ц"][0] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ц"][1] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ц"][2] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ц"][3] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ц"][4] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ц"][5] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ц"][6] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ц"][7] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ц"][8] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ц"][9] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ц"][10] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ц"][11] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ц"][12] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ц"][13] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ц"][14] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ц"][15] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ц"][16] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ц"][17] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ц"][18] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ц"][19] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ц"][20] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ц"][21] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ц"][22] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ц"][23] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ц"][24] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ц"][25] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ц"][26] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ц"][27] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ц"][28] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ц"][29] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ц"][30] += 1
# для ч
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ч"][0] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ч"][1] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ч"][2] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ч"][3] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ч"][4] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ч"][5] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ч"][6] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ч"][7] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ч"][8] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ч"][9] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ч"][10] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ч"][11] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ч"][12] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ч"][13] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ч"][14] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ч"][15] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ч"][16] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ч"][17] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ч"][18] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ч"][19] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ч"][20] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ч"][21] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ч"][22] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ч"][23] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ч"][24] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ч"][25] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ч"][26] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ч"][27] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ч"][28] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ч"][29] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ч"][30] += 1
# для ш
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ш"][0] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ш"][1] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ш"][2] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ш"][3] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ш"][4] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ш"][5] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ш"][6] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ш"][7] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ш"][8] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ш"][9] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ш"][10] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ш"][11] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ш"][12] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ш"][13] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ш"][14] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ш"][15] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ш"][16] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ш"][17] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ш"][18] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ш"][19] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ш"][20] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ш"][21] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ш"][22] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ш"][23] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ш"][24] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ш"][25] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ш"][26] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ш"][27] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ш"][28] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ш"][29] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ш"][30] += 1
# для щ
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'а'):
        dictStepSpace["щ"][0] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'б'):
        dictStepSpace["щ"][1] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'в'):
        dictStepSpace["щ"][2] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'г'):
        dictStepSpace["щ"][3] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'д'):
        dictStepSpace["щ"][4] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'е'):
        dictStepSpace["щ"][5] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["щ"][6] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'з'):
        dictStepSpace["щ"][7] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'и'):
        dictStepSpace["щ"][8] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'й'):
        dictStepSpace["щ"][9] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'к'):
        dictStepSpace["щ"][10] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'л'):
        dictStepSpace["щ"][11] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'м'):
        dictStepSpace["щ"][12] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'н'):
        dictStepSpace["щ"][13] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'о'):
        dictStepSpace["щ"][14] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'п'):
        dictStepSpace["щ"][15] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'р'):
        dictStepSpace["щ"][16] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'с'):
        dictStepSpace["щ"][17] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'т'):
        dictStepSpace["щ"][18] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'у'):
        dictStepSpace["щ"][19] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["щ"][20] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'х'):
        dictStepSpace["щ"][21] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["щ"][22] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["щ"][23] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["щ"][24] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["щ"][25] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["щ"][26] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["щ"][27] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'э'):
        dictStepSpace["щ"][28] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["щ"][29] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'я'):
        dictStepSpace["щ"][30] += 1
# для ы
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ы"][0] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ы"][1] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ы"][2] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ы"][3] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ы"][4] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ы"][5] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ы"][6] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ы"][7] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ы"][8] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ы"][9] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ы"][10] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ы"][11] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ы"][12] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ы"][13] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ы"][14] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ы"][15] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ы"][16] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ы"][17] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ы"][18] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ы"][19] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ы"][20] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ы"][21] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ы"][22] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ы"][23] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ы"][24] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ы"][25] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ы"][26] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ы"][27] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ы"][28] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ы"][29] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ы"][30] += 1
# для ь
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ь"][0] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ь"][1] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ь"][2] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ь"][3] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ь"][4] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ь"][5] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ь"][6] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ь"][7] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ь"][8] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ь"][9] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ь"][10] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ь"][11] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ь"][12] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ь"][13] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ь"][14] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ь"][15] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ь"][16] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ь"][17] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ь"][18] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ь"][19] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ь"][20] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ь"][21] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ь"][22] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ь"][23] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ь"][24] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ь"][25] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ь"][26] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ь"][27] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ь"][28] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ь"][29] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ь"][30] += 1
# для э
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'а'):
        dictStepSpace["э"][0] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'б'):
        dictStepSpace["э"][1] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'в'):
        dictStepSpace["э"][2] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'г'):
        dictStepSpace["э"][3] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'д'):
        dictStepSpace["э"][4] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'е'):
        dictStepSpace["э"][5] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["э"][6] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'з'):
        dictStepSpace["э"][7] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'и'):
        dictStepSpace["э"][8] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'й'):
        dictStepSpace["э"][9] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'к'):
        dictStepSpace["э"][10] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'л'):
        dictStepSpace["э"][11] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'м'):
        dictStepSpace["э"][12] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'н'):
        dictStepSpace["э"][13] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'о'):
        dictStepSpace["э"][14] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'п'):
        dictStepSpace["э"][15] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'р'):
        dictStepSpace["э"][16] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'с'):
        dictStepSpace["э"][17] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'т'):
        dictStepSpace["э"][18] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'у'):
        dictStepSpace["э"][19] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["э"][20] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'х'):
        dictStepSpace["э"][21] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["э"][22] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["э"][23] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["э"][24] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["э"][25] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["э"][26] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["э"][27] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'э'):
        dictStepSpace["э"][28] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["э"][29] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'я'):
        dictStepSpace["э"][30] += 1
# для ю
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'а'):
        dictStepSpace["ю"][0] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'б'):
        dictStepSpace["ю"][1] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'в'):
        dictStepSpace["ю"][2] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'г'):
        dictStepSpace["ю"][3] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'д'):
        dictStepSpace["ю"][4] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'е'):
        dictStepSpace["ю"][5] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["ю"][6] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'з'):
        dictStepSpace["ю"][7] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'и'):
        dictStepSpace["ю"][8] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'й'):
        dictStepSpace["ю"][9] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'к'):
        dictStepSpace["ю"][10] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'л'):
        dictStepSpace["ю"][11] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'м'):
        dictStepSpace["ю"][12] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'н'):
        dictStepSpace["ю"][13] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'о'):
        dictStepSpace["ю"][14] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'п'):
        dictStepSpace["ю"][15] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'р'):
        dictStepSpace["ю"][16] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'с'):
        dictStepSpace["ю"][17] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'т'):
        dictStepSpace["ю"][18] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'у'):
        dictStepSpace["ю"][19] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["ю"][20] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'х'):
        dictStepSpace["ю"][21] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["ю"][22] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["ю"][23] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["ю"][24] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["ю"][25] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["ю"][26] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["ю"][27] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'э'):
        dictStepSpace["ю"][28] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["ю"][29] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'я'):
        dictStepSpace["ю"][30] += 1
# для я
for i in range(0, len(fileString) - 1, 2):
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'а'):
        dictStepSpace["я"][0] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'б'):
        dictStepSpace["я"][1] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'в'):
        dictStepSpace["я"][2] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'г'):
        dictStepSpace["я"][3] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'д'):
        dictStepSpace["я"][4] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'е'):
        dictStepSpace["я"][5] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ж'):
        dictStepSpace["я"][6] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'з'):
        dictStepSpace["я"][7] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'и'):
        dictStepSpace["я"][8] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'й'):
        dictStepSpace["я"][9] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'к'):
        dictStepSpace["я"][10] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'л'):
        dictStepSpace["я"][11] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'м'):
        dictStepSpace["я"][12] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'н'):
        dictStepSpace["я"][13] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'о'):
        dictStepSpace["я"][14] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'п'):
        dictStepSpace["я"][15] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'р'):
        dictStepSpace["я"][16] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'с'):
        dictStepSpace["я"][17] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'т'):
        dictStepSpace["я"][18] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'у'):
        dictStepSpace["я"][19] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ф'):
        dictStepSpace["я"][20] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'х'):
        dictStepSpace["я"][21] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ц'):
        dictStepSpace["я"][22] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ч'):
        dictStepSpace["я"][23] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ш'):
        dictStepSpace["я"][24] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'щ'):
        dictStepSpace["я"][25] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ы'):
        dictStepSpace["я"][26] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ь'):
        dictStepSpace["я"][27] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'э'):
        dictStepSpace["я"][28] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ю'):
        dictStepSpace["я"][29] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'я'):
        dictStepSpace["я"][30] += 1

#print()
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfSS = pd.DataFrame(dictStepSpace, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Кількість біграм без перетину (з пробілами):")
print(dfSS)

for key in dictStepSpace:
    for i in range(0, 31):
        dictStepSpace[key][i] = dictStepSpace[key][i] / len(charListSpace)

#Крок 1, з пробілами
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfSSF = pd.DataFrame(dictStepSpace, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Частота біграм без перетину (з пробілами):")
print(dfSSF)


dictCrossSpace = {
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
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["а"][0] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["а"][1] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["а"][2] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["а"][3] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["а"][4] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["а"][5] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["а"][6] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["а"][7] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["а"][8] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["а"][9] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["а"][10] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["а"][11] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["а"][12] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["а"][13] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["а"][14] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["а"][15] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["а"][16] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["а"][17] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["а"][18] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["а"][19] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["а"][20] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["а"][21] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["а"][22] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["а"][23] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["а"][24] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["а"][25] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["а"][26] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["а"][27] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["а"][28] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["а"][29] += 1
    if (charListSpace[i] == 'а' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["а"][30] += 1
# для б
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["б"][0] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["б"][1] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["б"][2] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["б"][3] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["б"][4] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["б"][5] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["б"][6] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["б"][7] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["б"][8] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["б"][9] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["б"][10] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["б"][11] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["б"][12] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["б"][13] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["б"][14] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["б"][15] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["б"][16] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["б"][17] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["б"][18] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["б"][19] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["б"][20] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["б"][21] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["б"][22] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["б"][23] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["б"][24] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["б"][25] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["б"][25] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["б"][26] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["б"][27] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["б"][28] += 1
    if (charListSpace[i] == 'б' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["б"][29] += 1
# для в
for i in range(0, len(fileString) - 1) :
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["в"][0] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["в"][1] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["в"][2] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["в"][3] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["в"][4] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["в"][5] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["в"][6] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["в"][7] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["в"][8] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["в"][9] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["в"][10] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["в"][11] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["в"][12] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["в"][13] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["в"][14] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["в"][15] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["в"][16] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["в"][17] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["в"][18] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["в"][19] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["в"][20] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["в"][21] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["в"][22] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["в"][23] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["в"][24] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["в"][25] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["в"][26] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["в"][27] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["в"][28] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["в"][29] += 1
    if (charListSpace[i] == 'в' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["в"][30] += 1
# для г
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["г"][0] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["г"][1] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["г"][2] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["г"][3] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["г"][4] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["г"][5] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["г"][6] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["г"][7] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["г"][8] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["г"][9] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["г"][10] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["г"][11] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["г"][12] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["г"][13] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["г"][14] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["г"][15] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["г"][16] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["г"][17] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["г"][18] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["г"][19] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["г"][20] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["г"][21] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["г"][22] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["г"][23] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["г"][24] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["г"][25] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["г"][26] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["г"][27] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["г"][28] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["г"][29] += 1
    if (charListSpace[i] == 'г' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["г"][30] += 1
# для д
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["д"][0] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["д"][1] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["д"][2] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["д"][3] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["д"][4] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["д"][5] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["д"][6] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["д"][7] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["д"][8] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["д"][9] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["д"][10] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["д"][11] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["д"][12] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["д"][13] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["д"][14] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["д"][15] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["д"][16] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["д"][17] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["д"][18] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["д"][19] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["д"][20] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["д"][21] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["д"][22] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["д"][23] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["д"][24] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["д"][25] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["д"][26] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["д"][27] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["д"][28] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["д"][29] += 1
    if (charListSpace[i] == 'д' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["д"][30] += 1
# для е
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["е"][0] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["е"][1] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["е"][2] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["е"][3] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["е"][4] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["е"][5] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["е"][6] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["е"][7] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["е"][8] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["е"][9] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["е"][10] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["е"][11] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["е"][12] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["е"][13] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["е"][14] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["е"][15] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["е"][16] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["е"][17] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["е"][18] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["е"][19] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["е"][20] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["е"][21] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["е"][22] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["е"][23] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["е"][24] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["е"][25] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["е"][26] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["е"][27] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["е"][28] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["е"][29] += 1
    if (charListSpace[i] == 'е' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["е"][30] += 1
# для ж
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ж"][0] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ж"][1] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ж"][2] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ж"][3] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ж"][4] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ж"][5] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ж"][6] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ж"][7] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ж"][8] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ж"][9] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ж"][10] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ж"][11] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ж"][12] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ж"][13] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ж"][14] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ж"][15] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ж"][16] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ж"][17] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ж"][18] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ж"][19] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ж"][20] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ж"][21] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ж"][22] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ж"][23] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ж"][24] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ж"][25] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ж"][26] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ж"][27] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ж"][28] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ж"][29] += 1
    if (charListSpace[i] == 'ж' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ж"][30] += 1
# для з
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["з"][0] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["з"][1] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["з"][2] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["з"][3] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["з"][4] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["з"][5] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["з"][6] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["з"][7] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["з"][8] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["з"][9] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["з"][10] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["з"][11] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["з"][12] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["з"][13] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["з"][14] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["з"][15] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["з"][16] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["з"][17] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["з"][18] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["з"][19] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["з"][20] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["з"][21] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["з"][22] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["з"][23] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["з"][24] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["з"][25] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["з"][26] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["з"][27] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["з"][28] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["з"][29] += 1
    if (charListSpace[i] == 'з' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["з"][30] += 1
# для и
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["и"][0] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["и"][1] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["и"][2] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["и"][3] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["и"][4] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["и"][5] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["и"][6] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["и"][7] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["и"][8] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["и"][9] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["и"][10] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["и"][11] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["и"][12] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["и"][13] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["и"][14] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["и"][15] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["и"][16] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["и"][17] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["и"][18] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["и"][19] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["и"][20] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["и"][21] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["и"][22] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["и"][23] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["и"][24] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["и"][25] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["и"][26] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["и"][27] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["и"][28] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["и"][29] += 1
    if (charListSpace[i] == 'и' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["и"][30] += 1
# для й
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["й"][0] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["й"][1] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["й"][2] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["й"][3] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["й"][4] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["й"][5] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["й"][6] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["й"][7] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["й"][8] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["й"][9] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["й"][10] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["й"][11] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["й"][12] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["й"][13] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["й"][14] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["й"][15] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["й"][16] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["й"][17] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["й"][18] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["й"][19] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["й"][20] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["й"][21] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["й"][22] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["й"][23] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["й"][24] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["й"][25] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["й"][26] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["й"][27] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["й"][28] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["й"][29] += 1
    if (charListSpace[i] == 'й' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["й"][30] += 1
# для к
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["к"][0] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["к"][1] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["к"][2] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["к"][3] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["к"][4] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["к"][5] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["к"][6] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["к"][7] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["к"][8] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["к"][9] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["к"][10] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["к"][11] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["к"][12] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["к"][13] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["к"][14] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["к"][15] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["к"][16] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["к"][17] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["к"][18] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["к"][19] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["к"][20] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["к"][21] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["к"][22] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["к"][23] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["к"][24] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["к"][25] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["к"][26] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["к"][27] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["к"][28] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["к"][29] += 1
    if (charListSpace[i] == 'к' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["к"][30] += 1
# для л
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["л"][0] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["л"][1] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["л"][2] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["л"][3] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["л"][4] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["л"][5] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["л"][6] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["л"][7] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["л"][8] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["л"][9] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["л"][10] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["л"][11] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["л"][12] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["л"][13] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["л"][14] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["л"][15] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["л"][16] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["л"][17] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["л"][18] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["л"][19] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["л"][20] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["л"][21] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["л"][22] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["л"][23] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["л"][24] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["л"][25] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["л"][26] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["л"][27] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["л"][28] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["л"][29] += 1
    if (charListSpace[i] == 'л' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["л"][30] += 1
# для м
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["м"][0] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["м"][1] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["м"][2] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["м"][3] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["м"][4] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["м"][5] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["м"][6] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["м"][7] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["м"][8] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["м"][9] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["м"][10] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["м"][11] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["м"][12] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["м"][13] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["м"][14] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["м"][15] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["м"][16] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["м"][17] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["м"][18] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["м"][19] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["м"][20] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["м"][21] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["м"][22] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["м"][23] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["м"][24] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["м"][25] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["м"][26] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["м"][27] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["м"][28] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["м"][29] += 1
    if (charListSpace[i] == 'м' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["м"][30] += 1
# для н
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["н"][0] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["н"][1] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["н"][2] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["н"][3] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["н"][4] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["н"][5] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["н"][6] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["н"][7] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["н"][8] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["н"][9] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["н"][10] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["н"][11] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["н"][12] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["н"][13] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["н"][14] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["н"][15] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["н"][16] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["н"][17] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["н"][18] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["н"][19] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["н"][20] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["н"][21] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["н"][22] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["н"][23] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["н"][24] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["н"][25] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["н"][26] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["н"][27] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["н"][28] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["н"][29] += 1
    if (charListSpace[i] == 'н' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["н"][30] += 1
# для о
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["о"][0] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["о"][1] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["о"][2] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["о"][3] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["о"][4] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["о"][5] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["о"][6] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["о"][7] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["о"][8] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["о"][9] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["о"][10] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["о"][11] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["о"][12] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["о"][13] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["о"][14] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["о"][15] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["о"][16] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["о"][17] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["о"][18] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["о"][19] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["о"][20] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["о"][21] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["о"][22] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["о"][23] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["о"][24] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["о"][25] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["о"][26] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["о"][27] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["о"][28] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["о"][29] += 1
    if (charListSpace[i] == 'о' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["о"][30] += 1
# для п
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["п"][0] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["п"][1] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["п"][2] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["п"][3] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["п"][4] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["п"][5] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["п"][6] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["п"][7] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["п"][8] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["п"][9] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["п"][10] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["п"][11] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["п"][12] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["п"][13] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["п"][14] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["п"][15] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["п"][16] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["п"][17] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["п"][18] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["п"][19] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["п"][20] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["п"][21] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["п"][22] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["п"][23] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["п"][24] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["п"][25] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["п"][26] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["п"][27] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["п"][28] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["п"][29] += 1
    if (charListSpace[i] == 'п' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["п"][30] += 1
# для р
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["р"][0] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["р"][1] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["р"][2] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["р"][3] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["р"][4] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["р"][5] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["р"][6] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["р"][7] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["р"][8] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["р"][9] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["р"][10] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["р"][11] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["р"][12] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["р"][13] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["р"][14] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["р"][15] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["р"][16] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["р"][17] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["р"][18] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["р"][19] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["р"][20] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["р"][21] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["р"][22] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["р"][23] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["р"][24] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["р"][25] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["р"][26] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["р"][27] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["р"][28] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["р"][29] += 1
    if (charListSpace[i] == 'р' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["р"][30] += 1
# для с
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["с"][0] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["с"][1] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["с"][2] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["с"][3] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["с"][4] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["с"][5] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["с"][6] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["с"][7] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["с"][8] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["с"][9] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["с"][10] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["с"][11] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["с"][12] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["с"][13] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["с"][14] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["с"][15] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["с"][16] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["с"][17] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["с"][18] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["с"][19] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["с"][20] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["с"][21] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["с"][22] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["с"][23] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["с"][24] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["с"][25] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["с"][26] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["с"][27] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["с"][28] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["с"][29] += 1
    if (charListSpace[i] == 'с' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["с"][30] += 1
# для т
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["т"][0] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["т"][1] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["т"][2] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["т"][3] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["т"][4] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["т"][5] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["т"][6] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["т"][7] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["т"][8] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["т"][9] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["т"][10] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["т"][11] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["т"][12] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["т"][13] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["т"][14] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["т"][15] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["т"][16] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["т"][17] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["т"][18] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["т"][19] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["т"][20] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["т"][21] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["т"][22] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["т"][23] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["т"][24] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["т"][25] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["т"][26] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["т"][27] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["т"][28] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["т"][29] += 1
    if (charListSpace[i] == 'т' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["т"][30] += 1
# для у
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["у"][0] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["у"][1] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["у"][2] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["у"][3] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["у"][4] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["у"][5] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["у"][6] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["у"][7] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["у"][8] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["у"][9] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["у"][10] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["у"][11] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["у"][12] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["у"][13] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["у"][14] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["у"][15] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["у"][16] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["у"][17] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["у"][18] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["у"][19] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["у"][20] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["у"][21] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["у"][22] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["у"][23] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["у"][24] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["у"][25] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["у"][26] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["у"][27] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["у"][28] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["у"][29] += 1
    if (charListSpace[i] == 'у' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["у"][30] += 1
# для ф
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ф"][0] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ф"][1] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ф"][2] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ф"][3] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ф"][4] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ф"][5] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ф"][6] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ф"][7] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ф"][8] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ф"][9] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ф"][10] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ф"][11] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ф"][12] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ф"][13] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ф"][14] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ф"][15] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ф"][16] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ф"][17] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ф"][18] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ф"][19] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ф"][20] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ф"][21] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ф"][22] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ф"][23] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ф"][24] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ф"][25] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ф"][26] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ф"][27] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ф"][28] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ф"][29] += 1
    if (charListSpace[i] == 'ф' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ф"][30] += 1
# для х
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["х"][0] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["х"][1] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["х"][2] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["х"][3] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["х"][4] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["х"][5] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["х"][6] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["х"][7] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["х"][8] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["х"][9] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["х"][10] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["х"][11] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["х"][12] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["х"][13] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["х"][14] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["х"][15] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["х"][16] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["х"][17] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["х"][18] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["х"][19] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["х"][20] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["х"][21] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["х"][22] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["х"][23] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["х"][24] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["х"][25] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["х"][26] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["х"][27] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["х"][28] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["х"][29] += 1
    if (charListSpace[i] == 'х' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["х"][30] += 1
# для ц
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ц"][0] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ц"][1] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ц"][2] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ц"][3] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ц"][4] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ц"][5] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ц"][6] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ц"][7] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ц"][8] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ц"][9] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ц"][10] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ц"][11] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ц"][12] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ц"][13] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ц"][14] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ц"][15] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ц"][16] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ц"][17] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ц"][18] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ц"][19] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ц"][20] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ц"][21] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ц"][22] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ц"][23] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ц"][24] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ц"][25] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ц"][26] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ц"][27] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ц"][28] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ц"][29] += 1
    if (charListSpace[i] == 'ц' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ц"][30] += 1
# для ч
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ч"][0] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ч"][1] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ч"][2] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ч"][3] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ч"][4] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ч"][5] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ч"][6] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ч"][7] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ч"][8] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ч"][9] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ч"][10] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ч"][11] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ч"][12] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ч"][13] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ч"][14] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ч"][15] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ч"][16] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ч"][17] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ч"][18] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ч"][19] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ч"][20] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ч"][21] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ч"][22] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ч"][23] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ч"][24] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ч"][25] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ч"][26] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ч"][27] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ч"][28] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ч"][29] += 1
    if (charListSpace[i] == 'ч' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ч"][30] += 1
# для ш
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ш"][0] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ш"][1] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ш"][2] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ш"][3] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ш"][4] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ш"][5] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ш"][6] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ш"][7] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ш"][8] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ш"][9] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ш"][10] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ш"][11] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ш"][12] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ш"][13] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ш"][14] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ш"][15] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ш"][16] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ш"][17] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ш"][18] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ш"][19] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ш"][20] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ш"][21] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ш"][22] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ш"][23] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ш"][24] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ш"][25] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ш"][26] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ш"][27] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ш"][28] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ш"][29] += 1
    if (charListSpace[i] == 'ш' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ш"][30] += 1
# для щ
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["щ"][0] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["щ"][1] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["щ"][2] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["щ"][3] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["щ"][4] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["щ"][5] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["щ"][6] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["щ"][7] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["щ"][8] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["щ"][9] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["щ"][10] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["щ"][11] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["щ"][12] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["щ"][13] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["щ"][14] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["щ"][15] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["щ"][16] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["щ"][17] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["щ"][18] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["щ"][19] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["щ"][20] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["щ"][21] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["щ"][22] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["щ"][23] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["щ"][24] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["щ"][25] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["щ"][26] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["щ"][27] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["щ"][28] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["щ"][29] += 1
    if (charListSpace[i] == 'щ' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["щ"][30] += 1
# для ы
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ы"][0] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ы"][1] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ы"][2] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ы"][3] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ы"][4] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ы"][5] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ы"][6] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ы"][7] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ы"][8] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ы"][9] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ы"][10] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ы"][11] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ы"][12] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ы"][13] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ы"][14] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ы"][15] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ы"][16] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ы"][17] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ы"][18] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ы"][19] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ы"][20] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ы"][21] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ы"][22] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ы"][23] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ы"][24] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ы"][25] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ы"][26] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ы"][27] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ы"][28] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ы"][29] += 1
    if (charListSpace[i] == 'ы' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ы"][30] += 1
# для ь
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ь"][0] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ь"][1] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ь"][2] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ь"][3] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ь"][4] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ь"][5] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ь"][6] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ь"][7] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ь"][8] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ь"][9] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ь"][10] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ь"][11] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ь"][12] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ь"][13] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ь"][14] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ь"][15] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ь"][16] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ь"][17] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ь"][18] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ь"][19] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ь"][20] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ь"][21] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ь"][22] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ь"][23] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ь"][24] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ь"][25] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ь"][26] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ь"][27] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ь"][28] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ь"][29] += 1
    if (charListSpace[i] == 'ь' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ь"][30] += 1
# для э
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["э"][0] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["э"][1] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["э"][2] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["э"][3] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["э"][4] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["э"][5] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["э"][6] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["э"][7] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["э"][8] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["э"][9] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["э"][10] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["э"][11] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["э"][12] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["э"][13] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["э"][14] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["э"][15] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["э"][16] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["э"][17] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["э"][18] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["э"][19] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["э"][20] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["э"][21] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["э"][22] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["э"][23] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["э"][24] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["э"][25] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["э"][26] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["э"][27] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["э"][28] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["э"][29] += 1
    if (charListSpace[i] == 'э' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["э"][30] += 1
# для ю
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["ю"][0] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["ю"][1] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["ю"][2] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["ю"][3] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["ю"][4] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["ю"][5] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["ю"][6] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["ю"][7] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["ю"][8] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["ю"][9] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["ю"][10] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["ю"][11] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["ю"][12] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["ю"][13] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["ю"][14] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["ю"][15] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["ю"][16] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["ю"][17] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["ю"][18] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["ю"][19] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["ю"][20] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["ю"][21] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["ю"][22] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["ю"][23] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["ю"][24] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["ю"][25] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["ю"][26] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["ю"][27] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["ю"][28] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["ю"][29] += 1
    if (charListSpace[i] == 'ю' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["ю"][30] += 1
# для я
for i in range(0, len(fileString) - 1):
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'а'):
        dictCrossSpace["я"][0] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'б'):
        dictCrossSpace["я"][1] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'в'):
        dictCrossSpace["я"][2] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'г'):
        dictCrossSpace["я"][3] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'д'):
        dictCrossSpace["я"][4] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'е'):
        dictCrossSpace["я"][5] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ж'):
        dictCrossSpace["я"][6] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'з'):
        dictCrossSpace["я"][7] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'и'):
        dictCrossSpace["я"][8] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'й'):
        dictCrossSpace["я"][9] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'к'):
        dictCrossSpace["я"][10] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'л'):
        dictCrossSpace["я"][11] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'м'):
        dictCrossSpace["я"][12] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'н'):
        dictCrossSpace["я"][13] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'о'):
        dictCrossSpace["я"][14] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'п'):
        dictCrossSpace["я"][15] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'р'):
        dictCrossSpace["я"][16] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'с'):
        dictCrossSpace["я"][17] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'т'):
        dictCrossSpace["я"][18] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'у'):
        dictCrossSpace["я"][19] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ф'):
        dictCrossSpace["я"][20] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'х'):
        dictCrossSpace["я"][21] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ц'):
        dictCrossSpace["я"][22] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ч'):
        dictCrossSpace["я"][23] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ш'):
        dictCrossSpace["я"][24] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'щ'):
        dictCrossSpace["я"][25] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ы'):
        dictCrossSpace["я"][26] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ь'):
        dictCrossSpace["я"][27] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'э'):
        dictCrossSpace["я"][28] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'ю'):
        dictCrossSpace["я"][29] += 1
    if (charListSpace[i] == 'я' and charListSpace[i + 1] == 'я'):
        dictCrossSpace["я"][30] += 1

print()
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfCS = pd.DataFrame(dictCrossSpace, index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                  columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Кількість біграм з перетином (з пробілами):")
print(dfCS)

for key in dictCrossSpace:
    for i in range(0, 31):
        dictCrossSpace[key][i] = dictCrossSpace[key][i] / len(charListSpace)

# Крок 2, з пробілами
pd.set_option("display.max_rows", None, "display.max_columns", None)
dfCSF = pd.DataFrame(dictCrossSpace,
                     index=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                     columns=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                              'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
print()
print("Частота біграм з перетином (з пробілами):")
print(dfCSF)


digits = {
"а": 0,
"б": 0,
"в": 0,
"г": 0,
"д": 0,
"е": 0,
"ж": 0,
"з": 0,
"и": 0,
"й": 0,
"к": 0,
"л": 0,
"м": 0,
"н": 0,
"о": 0,
"п": 0,
"р": 0,
"с": 0,
"т": 0,
"у": 0,
"ф": 0,
"х": 0,
"ц": 0,
"ч": 0,
"ш": 0,
"щ": 0,
"ы": 0,
"ь": 0,
"э": 0,
"ю": 0,
"я": 0
}

for i in range(0, len(charList)):
    if(charList[i] == 'а'):
        digits["а"] += 1
    if (charList[i] == 'б'):
        digits["б"] += 1
    if (charList[i] == 'в'):
        digits["в"] += 1
    if (charList[i] == 'г'):
        digits["г"] += 1
    if (charList[i] == 'д'):
        digits["д"] += 1
    if (charList[i] == 'е'):
        digits["е"] += 1
    if (charList[i] == 'ж'):
        digits["ж"] += 1
    if (charList[i] == 'з'):
        digits["з"] += 1
    if (charList[i] == 'и'):
        digits["и"] += 1
    if (charList[i] == 'й'):
        digits["й"] += 1
    if (charList[i] == 'к'):
        digits["к"] += 1
    if (charList[i] == 'л'):
        digits["л"] += 1
    if (charList[i] == 'м'):
        digits["м"] += 1
    if (charList[i] == 'н'):
        digits["н"] += 1
    if (charList[i] == 'о'):
        digits["о"] += 1
    if (charList[i] == 'п'):
        digits["п"] += 1
    if (charList[i] == 'р'):
        digits["р"] += 1
    if (charList[i] == 'с'):
        digits["с"] += 1
    if (charList[i] == 'т'):
        digits["т"] += 1
    if (charList[i] == 'у'):
        digits["у"] += 1
    if (charList[i] == 'ф'):
        digits["ф"] += 1
    if (charList[i] == 'х'):
        digits["х"] += 1
    if (charList[i] == 'ц'):
        digits["ц"] += 1
    if (charList[i] == 'ч'):
        digits["ч"] += 1
    if (charList[i] == 'ш'):
        digits["ш"] += 1
    if (charList[i] == 'щ'):
        digits["щ"] += 1
    if (charList[i] == 'ы'):
        digits["ы"] += 1
    if (charList[i] == 'ь'):
        digits["ь"] += 1
    if (charList[i] == 'э'):
        digits["э"] += 1
    if (charList[i] == 'ю'):
        digits["ю"] += 1
    if (charList[i] == 'я'):
        digits["я"] += 1

print()
print()
print("Довжина тексту без пробілів:", len(charList))
print("Кількість літер: ")
print(digits)

print("Частота літер без пробілу: ")
for key in digits:
    digits[key] = digits[key] / len(charList)
    print(key, ":", digits[key])


digitsWithSpace = {
"_": 0,
"а": 0,
"б": 0,
"в": 0,
"г": 0,
"д": 0,
"е": 0,
"ж": 0,
"з": 0,
"и": 0,
"й": 0,
"к": 0,
"л": 0,
"м": 0,
"н": 0,
"о": 0,
"п": 0,
"р": 0,
"с": 0,
"т": 0,
"у": 0,
"ф": 0,
"х": 0,
"ц": 0,
"ч": 0,
"ш": 0,
"щ": 0,
"ы": 0,
"ь": 0,
"э": 0,
"ю": 0,
"я": 0
}
print()
print()
print("Довжина тексту з пробілами:", len(charListSpace))
print("Кількість літер і пробілів: ")
for i in range(0, len(charListSpace)):
    if (charListSpace[i] == ' '):
        digitsWithSpace["_"] += 1
    if(charListSpace[i] == 'а'):
        digitsWithSpace["а"] += 1
    if (charListSpace[i] == 'б'):
        digitsWithSpace["б"] += 1
    if (charListSpace[i] == 'в'):
        digitsWithSpace["в"] += 1
    if (charListSpace[i] == 'г'):
        digitsWithSpace["г"] += 1
    if (charListSpace[i] == 'д'):
        digitsWithSpace["д"] += 1
    if (charListSpace[i] == 'е'):
        digitsWithSpace["е"] += 1
    if (charListSpace[i] == 'ж'):
        digitsWithSpace["ж"] += 1
    if (charListSpace[i] == 'з'):
        digitsWithSpace["з"] += 1
    if (charListSpace[i] == 'и'):
        digitsWithSpace["и"] += 1
    if (charListSpace[i] == 'й'):
        digitsWithSpace["й"] += 1
    if (charListSpace[i] == 'к'):
        digitsWithSpace["к"] += 1
    if (charListSpace[i] == 'л'):
        digitsWithSpace["л"] += 1
    if (charListSpace[i] == 'м'):
        digitsWithSpace["м"] += 1
    if (charListSpace[i] == 'н'):
        digitsWithSpace["н"] += 1
    if (charListSpace[i] == 'о'):
        digitsWithSpace["о"] += 1
    if (charListSpace[i] == 'п'):
        digitsWithSpace["п"] += 1
    if (charListSpace[i] == 'р'):
        digitsWithSpace["р"] += 1
    if (charListSpace[i] == 'с'):
        digitsWithSpace["с"] += 1
    if (charListSpace[i] == 'т'):
        digitsWithSpace["т"] += 1
    if (charListSpace[i] == 'у'):
        digitsWithSpace["у"] += 1
    if (charListSpace[i] == 'ф'):
        digitsWithSpace["ф"] += 1
    if (charListSpace[i] == 'х'):
        digitsWithSpace["х"] += 1
    if (charListSpace[i] == 'ц'):
        digitsWithSpace["ц"] += 1
    if (charListSpace[i] == 'ч'):
        digitsWithSpace["ч"] += 1
    if (charListSpace[i] == 'ш'):
        digitsWithSpace["ш"] += 1
    if (charListSpace[i] == 'щ'):
        digitsWithSpace["щ"] += 1
    if (charListSpace[i] == 'ы'):
        digitsWithSpace["ы"] += 1
    if (charListSpace[i] == 'ь'):
        digitsWithSpace["ь"] += 1
    if (charListSpace[i] == 'э'):
        digitsWithSpace["э"] += 1
    if (charListSpace[i] == 'ю'):
        digitsWithSpace["ю"] += 1
    if (charListSpace[i] == 'я'):
        digitsWithSpace["я"] += 1
print(digitsWithSpace)

print("Частота літер і пробілу: ")
for key in digitsWithSpace:
    digitsWithSpace[key] = digitsWithSpace[key] / len(charListSpace)
    print(key, ":", digitsWithSpace[key])


print()
print("Обчислення H1 (без пробілу):")
H1 = 0.0000
for key in digits:
        H1 = H1 + (abs(digits[key]) * abs(math.log(digits[key], 2)))
print("H1", H1)

print()
print("Обчислення H1 (з пробілом):")
H1 = 0.0000
for key in digitsWithSpace:
        H1 = H1 + (abs(digitsWithSpace[key]) * abs(math.log(digitsWithSpace[key], 2)))
print("H1", H1)


print()
H2S = 0.0000
for key in dictStep:
    for i in range (0, 30):
        if (dictStep[key][i] != 0):
            temp = abs(dictStep[key][i] * math.log(dictStep[key][i], 2))
            H2S = H2S + temp
        else:
            temp = 1*dictStep[key][i]
            H2S = H2S + temp



print()
H2SS = 0.0000
for key in dictStepSpace:
    for i in range (0, 30):
        if (dictStepSpace[key][i] != 0):
            temp = abs(dictStepSpace[key][i] * math.log(dictStepSpace[key][i], 2))
            H2SS = H2SS + temp
        else:
            temp = 1*dictStepSpace[key][i]
            H2SS = H2SS + temp



print()
H2C = 0.0000
for key in dictCross:
    for i in range (0, 30):
        if (dictCross[key][i] != 0):
            temp = abs(dictCross[key][i] * math.log(dictCross[key][i], 2))
            H2C = H2C + temp
        else:
            temp = 1*dictCross[key][i]
            H2C = H2C + temp


print()
H2CS = 0.0000
for key in dictCrossSpace:
    for i in range (0, 30):
        if (dictCrossSpace[key][i] != 0):
            temp = abs(dictCrossSpace[key][i] * math.log(dictCrossSpace[key][i], 2))
            H2CS = H2CS + temp
        else:
            temp = 1*dictCrossSpace[key][i]
            H2CS = H2CS + temp

