import json
import random

from pyparsing import Word
states = [
    "     -----",
    "     -----\n      0",
    "     -----\n      0\n      |",
    "     -----\n      0\n      |\n     /",
    "     -----\n      0\n      |\n     / \ ",
    "     -----\n    \ 0 \n      |\n     / \ ",
    "     -----\n    \ 0 /\n      |\n     / \ ",
    "     -----\n    \ 0 /|\n      |\n     / \ ",
    "     -----\n    \ 0 /_|\n      |\n     / \ ",
    "     -----\n      0_|\n     /|\ \n     / \ ",
]
def checker(str1,q):
    listof = list()
    sw = 0
    ind =0
    for w in str1:
        if(w == q):
            listof.append(ind)
            sw = 1
        ind += 1
    if (sw == 0):
        return -1
    else:
        return listof
file = open("words.json","r",encoding='utf8')
datas = json.load(file)
w = []
amount =0
print("Zorluk seçin (kolay: max 4 harf, orta: max 6 harf, zor: limit yok, otomatik zorluk: orta): ")
diff = input()
max = 6
if(diff == "kolay"):
    max = 4
elif(diff == "zor"):
    max=90

for data in datas:
    if(len(data)<=max):
        w.append(data)
        amount +=1
print("{} words loaded".format(amount))
r = random.randint(0,amount-1)
sword = w[r]
l = len(sword)
l2 = list()
for i in range(l):
    l2.append("_ ")
sayi = 0
current_s = 0

while (1):
    if (sayi == l):
        print(sword)
        print("You won!!")
        break
    if (current_s > 8):
        print(sword)
        print("Game over!")
        break
    str1 = "Guess the word: " + "".join(l2) + " "
    quess = input(str1)
    res = checker(sword,quess)
    if res == -1:
        current_s += 1
        print(states[current_s])
    else:
        for i in res:
            sayi +=1
            l2[i] = quess
    str1 = ""


