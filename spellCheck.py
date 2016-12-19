'''
Created on December 18, 2016
@author: Anusha Bilakanti
'''

def anagramWord(word_list):
    if(len(word_list)==0):
        return []
    elif(len(word_list)==1):
        return [word_list]
    else:
        l=[]
        for i in range(len(word_list)):            
            x = word_list[i]
            xs = word_list[:i] + word_list[i+1:]
            for p in anagramWord(xs):
                l.append([x]+p)
        return l

def spellCheck(word,dict_file):

    misspelt=0
    word_in_dict=0
    for i in dict_file:
        if word==i: 
            word_in_dict=1
            break

    if word_in_dict==0:
        word=word.strip()
        word_list=[]
        replace_list=[]
        word_list=list(word)
        anagram_list=anagramWord(word_list)
        for temp in anagram_list:
            for x in dict_file:
                x=x.strip()
                x=list(x)
                if x==temp and misspelt==0:
                    misspelt=1
                    x=''.join(x)
                    print "WORD '",word,"' is misspelled"
                    print "Replacement word", x
                    replace_list.append(x)
                elif x==temp and misspelt==1:
                    x=''.join(x)
                    for replace_word in replace_list:
                        if x!=replace_word:
                            replace_list.append(x)
                            print "Replacement word", x
                            break                 

lst=[]
dict_file=open("dictionary.txt","r")
for line in dict_file.readlines():
    for dict_word in line.split():
        dict_word=dict_word.lower()
        lst.append(dict_word)
ip_file=open("input.txt","r")
for line in ip_file.readlines():
    for ip_word in line.split():
        ip_word=ip_word.lower()
        spellCheck(ip_word,lst)













