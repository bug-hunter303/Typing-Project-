import random
import time 
import MAIN



def sentence_extract():
    list_sentence = [] 

    with open("sentences.csv" , 'r') as f:
        sentence = f.read()
        sentence_nospace = sentence.replace('\n','')
        list_sentence = [s.strip() for s in sentence_nospace.split(',')]
    return list_sentence

def sentence_select():
    sentence = sentence_extract()
    random_number = random.randint(0,14)
    return sentence[random_number]        

def user_input():
    original_sentence = sentence_select()
    print(f'Type this :\n{original_sentence}\n')
    input("**PRESS ENTER TO START**\n")
    start_time = time.time()
    user_sentence = input()
    end_time = time.time()
    
    return (original_sentence,user_sentence,start_time,end_time)

def character_accuracy(original, user):
    match_count = 0
    min_length = min(len(original), len(user))

    for i in range(min_length):
        if user[i] == original[i]:
            match_count += 1
    
    total_char = len(original)
    character_accuracy_percentage = round((match_count/total_char) * 100,2)

    return character_accuracy_percentage

def word_accuracy(original,user,start,end):
    correct_words = 0
    original_words = original.split()
    user_words = user.split()

    elapsed_time = round(end - start , 2)

    for i in range(len(original_words)):
        if i < len(user_words):
            if original_words[i] == user_words[i]:
                correct_words += 1
    
    wpm = int((correct_words/elapsed_time) * 60)
    return wpm,elapsed_time

def display(accuracy,time,words_per_min):
    print(f'\nAccuracy : {accuracy}')
    print(f'Time Taken : {time} s')
    print(f'WPM : {words_per_min}')




original , user , start , end = user_input()
a = character_accuracy(original,user)
b,c = word_accuracy(original,user,start,end)
display(a,b,c)

