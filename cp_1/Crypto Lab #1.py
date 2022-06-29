import re
import math

monograms = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')

bigrams = [i+j for i in monograms for j in monograms]

def read_file(filename: str):
    text = open(filename, 'r', encoding='utf-8')
    texts = str(text.read())
    return texts

def count_substring(big_string,substring):
    count = 0 
    for char in range(len(big_string)):
        count += big_string[char: char + len(substring)] == substring
    return count

def frequency_monograms(message):
    return [[i, message.count(i)/len(message)] for i in monograms]

def frequency_bigrams_no_overlap(message):
    return [[i, message.count(i)/len(message)] for i in bigrams]

def frequency_bigrams_overlap(message):
    return [[i, count_substring(message,i)/len(message)] for i in bigrams]

def H1(ProbabilitiesMono):
    s = 0
    for P in ProbabilitiesMono:
        if P[1] != 0:
            s += P[1]*math.log2(P[1])
    return -1*s
           
def H2(ProbabilitiesBi):
    s = 0
    for P in ProbabilitiesBi:
        if P[1] != 0:
            s += P[1]*math.log2(P[1])
    return -1*s/2

def main():
    text = read_file('ourtext.txt').replace('\n', '')
    text_without_spaces = (''.join(filter(str.isalpha, text))).lower()
    text_with_spaces = (re.sub(r'[^Z0-9А-Яа-я- -]', '', text)).lower()
    
    probabilities_monograms_no_spaces = frequency_monograms(text_without_spaces)
    probabilities_monograms_with_spaces  = frequency_monograms(text_with_spaces)
    
    probabilities_bigrams_no_spaces_no_overlap = frequency_bigrams_no_overlap(text_without_spaces)
    probabilities_bigrams_no_spaces_with_overlap = frequency_bigrams_overlap(text_without_spaces)
    
    probabilities_bigrams_with_spaces_no_overlap = frequency_bigrams_no_overlap(text_with_spaces)
    probabilities_bigrams_with_spaces_with_overlap = frequency_bigrams_overlap(text_with_spaces)
    
    H1_no_spaces = H1(probabilities_monograms_no_spaces)
    H1_with_spaces = H1(probabilities_monograms_with_spaces)
    
    H2_no_spaces_no_overlap = H2(probabilities_bigrams_no_spaces_no_overlap)
    H2_no_spaces_overlap = H2(probabilities_bigrams_no_spaces_with_overlap)
    
    H2_with_spaces_no_overlap = H2(probabilities_bigrams_with_spaces_no_overlap)
    H2_with_spaces_overlap = H2(probabilities_bigrams_with_spaces_with_overlap)
    
    print('probabilities_monograms_no_space')
    for i in probabilities_monograms_no_spaces:
        print(f'Letter = {i[0]} Pr = {i[1]}')
        
    print('probabilities_monograms_with_space')
    for j in probabilities_monograms_with_spaces:
            print(f'Letter = {j[0]} Pr = {j[1]}')
    
   # print('probabilities_monograms_with_space')
    #for k in probabilities_monograms_with_spaces:
     #       print(f'Letter = {k[0]} Pr = {k[1]}')
    
    print(f'H1 no spaces = {H1_no_spaces}\nH1 with spaces = {H1_with_spaces}')
    print(f'H2 no spaces no overlap = {H2_no_spaces_no_overlap}\nH2 no spaces with overlap = {H2_no_spaces_overlap}')
    print(f'H2 with spaces no overlap = {H2_with_spaces_no_overlap}\nH2 with spaces with overlap = {H2_with_spaces_overlap}')


    
if __name__ == '__main__':
    main()
    
