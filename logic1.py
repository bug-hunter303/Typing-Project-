
import time
import random



def sentence_extract():
    list_sentence = [] 

    with open("sentences.csv" , 'r') as f:
        sentence = f.read()
        sentence_nospace = sentence.replace('\n','')
        list_sentence = [s.strip() for s in sentence_nospace.split(',')]

    return list_sentence

def sentence_select():
    sentence = sentence_extract()
    random_number = random.randint(0,12)
    return sentence[random_number]  