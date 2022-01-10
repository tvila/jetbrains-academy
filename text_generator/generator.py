from nltk.tokenize import WhitespaceTokenizer
from nltk.util import ngrams
from collections import Counter
import random
import re

file_name = str(input())
file = open(file_name, 'r', encoding='utf-8')
tk = WhitespaceTokenizer()
text = tk.tokenize(file.read())


# Creating N_GRAMS lists
n_grams2 = list(ngrams(text, 2))
n_grams3 = list(ngrams(text, 3))
n_grams_list = []
full_sentence = []

for i in range(len(n_grams3)):
    n_grams_list.append(" ".join(n_grams3[i][0:2]))
    n_grams_list.append(n_grams3[i][2])

n_grams_bride = list(ngrams(n_grams_list, 2))

# starting head
template = '[!?,.]'
template2 = '[!?.]'


# PROCESS
for i in range(10):
    full_sentence = []
    while True:
        head = " ".join(random.choice(n_grams2))
        if head[0].isupper() and re.search(template, head.split()[0]) == None:
            full_sentence.append(head.split()[0])
            full_sentence.append(head.split()[1])
            break

    while True:
        if len(full_sentence) >= 5 and re.search(template2, full_sentence[-1]) != None:
            break
        else:
            tail_list = []
            for i in range(len(n_grams_bride)):
                if n_grams_bride[i][0] == " ".join(full_sentence[-2:]):
                    tail_list.append(n_grams_bride[i][1])
            full_sentence.append(Counter(tail_list).most_common()[0][0])

    print(*full_sentence)
