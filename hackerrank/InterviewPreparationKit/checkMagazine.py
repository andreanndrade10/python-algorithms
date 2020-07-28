#https://www.hackerrank.com/challenges/ctci-ransom-note/
from collections import Counter

'''
def checkMagazine(magazine, note):
    dictMagazine = list_to_dict(magazine)
    dictNote = list_to_dict(note)
    ok=[]
    for i in dictNote:
        if i not in dictMagazine:
            ok.append('not ok')
        if i in dictMagazine:
            if dictNote[i]>dictMagazine[i]:
                ok.append('not ok')
            else:
                ok.append('ok')

    if 'not ok' in ok:
        print('No') 
    else:
        print('Yes')

def list_to_dict(my_list):
    freq = {} 
    for items in my_list: 
        freq[items] = my_list.count(items)
    return freq 
''' 


def checkMagazine(magazine, ransom):
    word_counts = Counter(magazine)
    for word in ransom:
        if word_counts[word] > 0:
            word_counts[word] -= 1
        else:
            return 'No'   
    return 'Yes'


if __name__ == "__main__":
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    print(checkMagazine(magazine, note))

   