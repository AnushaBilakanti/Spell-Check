'''
Created on December 17, 2016
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
    # print "DICT IN FUNC"
    misspelt=0
    if word in dict_file:
        print "FOUND"
    else:
        word=word.strip()
        word_list=[]
        word_list=list(word)
        # print "WORD CHAR",word_list
        anagram_list=anagramWord(word_list)
        for temp in anagram_list:
            for x in dict_file:
                x=x.strip()
                x=list(x)
                if x==temp and misspelt==0:
                    misspelt=1
                    x=''.join(x)
                    print "WORD",word,"is misspelled"
                    print "Replacement word", x
                if x==temp and misspelt==1:
                    x=''.join(x)
                    print "Replacement word", x

lst=[]
dict_file=open("words.txt","r")
for i in dict_file:
    lst.append(i)
ip_file=open("input.txt","r")
for i in ip_file:
    spellCheck(i,lst)
