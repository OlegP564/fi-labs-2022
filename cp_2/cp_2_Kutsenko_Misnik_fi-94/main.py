import codecs
import random


def parseFile(name):
    parsed = ""
    file = codecs.open(name,"r","utf-8")
    for line in file:
        for ch in line.lower():
            #print(ord(ch),end=" ")
            temp = ord(ch)
            if 1072<=temp<1104:
                parsed+=ch
            if temp == 1105:
                parsed+='е'
    return parsed
def keyText(text,key):
    keyedText = ""
    counter =0
    for i in text:
        inext = ord(i)+key[counter % len(key)] - 1072*2
        counter+=1
        inext %=(1103-1072)
        inext+=1072
        keyedText+=chr(inext)
    return keyedText
def dekeytext(text,key):
    dekeyedText = ""
    counter = 0
    for i in text:
        inext = ord(i) - key[counter % len(key)]
        counter += 1
        if inext < 0:
            inext+=32
        inext += 1072
        dekeyedText += chr(inext)
    return dekeyedText

def Ir(text):
    Nt = []
    n = 0
    for i in range(0,32):
        Nt.append(0)
    for ch in text:
        temp = ord(ch)
        temp -= 1072
        Nt[temp] += 1
        n += 1
    sum = 0
    for i in range(0,32):
        sum += (Nt[i]-1)*Nt[i]/(n*(n-1))
    return sum
def Dr(text, r):
    sum = 0
    for i in range(len(text)-r):
        if text[i] == text[i+r]:
            sum+=1
    return sum
def cesar(text, ch0):
    Nt = []
    for i in range(0, 32):
        Nt.append(0)
    for ch in text:
        temp = ord(ch)
        temp -= 1072
        Nt[temp] += 1
    max = 0
    tempi = 0
    for i in range(0,32):
        if max < Nt[i]:
            max = Nt[i]
            tempi = i
    step = tempi - ch0
    if step < 0:
        step+=32
    return step+1072
def Mig(text,p,tmp,ic):
    Nt = []
    for i in range(0, 32):
        Nt.append(0)
    for ch in text:
        temp = ord(ch)
        temp -= 1072
        Nt[temp] += 1
    maxSum = 0
    g0 = 0
    for g in range(0,32):
        sum = 0
        for i in range(0,32):
            sum += p[i]*Nt[(i+g)%32]
        if sum > maxSum:
            maxSum = sum
            g0 = g
        tmp[g][ic]=sum
    return g0

if __name__ == '__main__':
    opentext = (parseFile("Open.txt"))
    text = parseFile("text.txt")
    print("Open text Ir = "+str(Ir(opentext)))
    for i in range(2,21):
        key = []
        keyprnt = []
        for j in range(0, i):
            t = random.randint(1072, 1103)
            while t in key:
                t = random.randint(1072, 1103)
            key.append(t)
            keyprnt.append(chr(t))
        temptext = keyText(opentext, key)
        Iri = Ir(temptext)
        print(i)
        print("key = " + str(keyprnt))
        print(Iri)
    print("Dr:")
    for i in range(2,30):
        print(str(i) + " " + str(Dr(text,i)))
    r = 17
    slisedText = []
    key1 = []
    key1prnt =[]
    for i in range(0,r):
        slisedText.append("")
    for i in range(0,int(len(text)/r)):
        for j in range(0,r):
            slisedText[j]+=text[i*r+j]
    for el in slisedText:
        temp = cesar(el,ord('о')-1072)
        key1.append(temp)
        key1prnt.append(chr(temp))
    print(key1prnt)
    print(dekeytext(text,key1))
    frequencies = [0.0843887, 0.0152686, 0.0404102, 0.0195458, 0.032045, 0.0801951, 0.0115769, 0.0165079
                   , 0.0655562, 0.0133974, 0.031389, 0.0530833, 0.0335155, 0.0701812, 0.113803, 0.0285009
                   , 0.0515864, 0.0526673, 0.0557051, 0.0262115, 0.00318095, 0.00770912, 0.00311711, 0.0125829
                   , 0.00744496, 0.0027737, 0.000154094, 0.0164617, 0.0188435, 0.00324259, 0.00467787, 0.0195061]
    key2 = []
    key2prnt = []
    tempprint = []
    for i in range(0,32):
        tempprint.append([])
        for j in range(0,r):
            tempprint[i].append(0)


    for i in range(0,r):
        temp = Mig(slisedText[i],frequencies,tempprint,i)
        key2.append(temp+1072)
        key2prnt.append(chr(temp+1072))

    for i in range(-1, 32):
        if i == -1:
            print("")
        else:
            print(chr(1072+i), end = " ")
        for j in range(0,r):
            if i == -1:
                if j <10:
                    print("   "+ str(j)+"   ", end = " ")
                else:
                    print("   " + str(j) + "   ", end="")
            else:
                tmp0 = str(round(tempprint[i][j],4))
                while len(tmp0)<7:
                    tmp0+=" "
                print(tmp0,end = " ")
        if i >=0:
            print(chr(1072 + i), end=" ")
        print()

    print(key2prnt)
    print(dekeytext(text, key2))
    print(text[0:1000])
    print(dekeytext(text,key2)[0:1000])
