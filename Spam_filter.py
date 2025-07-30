import csv #importing required libraries
import re
from collections import Counter

spam_word={} #dictionary for storing spam words and their frequency counts
n_spam_word={} #dictionary for storing non-spam words and their frequency counts

with open('SMS_list.csv',newline='') as data_file: #opening the sms csv file as datafile
    data_set=list(csv.reader(data_file,delimiter='\t')) #setting the readin procedure to data_set as a list of rows
    
    for row in data_set: #loop running for each row of the csv file
       
        words=row[1] #message is stored in words

        words=re.sub(r'[0-9]'," ",words) #number are removed from words
        words=re.sub(r'[()*.!-+/:;@$%?<=>Â£,~`€_Éˆ¥Â”¾Ã‰Â»™]'," ",words) #symbolic characters are removed from words
        words=re.sub(r'[-]',' ',words)
        words=words.upper() #whole string is capitalized
        words=words.split() #all words are splitted and stored in a list
        
        if(row[-1]==''): #'removing any '' character
            row.pop()
            
        if(row[0]=='spam'): #if spam then the word and frequency counts gets updated in spam_word dictionary
            for char in words:
                if char not in spam_word:
                    spam_word[char]=1
                else:
                    spam_word[char]+=1
                    
        elif(row[0]=='notspam'): #if non-spam then the word and frequency counts gets updated in n_spam_word dictionary
            for char in words:
                if char not in n_spam_word:
                    n_spam_word[char]=1
                else:
                    n_spam_word[char]+=1

    
    #list of words to be not considered 
    rmv=['M','P','U','I','S','A','AND','THE','TO','IN','IS','OF','FOR','ON','FROM','WITH','OR','AT','ARE','BY','OFF','DOWN','NEAR','ON','UPON','AS','INTO','IS','IT','SO','DO','T']
    for c in rmv: #for loop for removing the words in the above list
        
        if c in list(n_spam_word.keys()): #removing the words from n_spam_word list
            del n_spam_word[c]
            
        if c in list(spam_word.keys()): #removing the words from spam_word list
            del spam_word[c]
    
#     #new1 is basically spam_word dictionary in an order sorted according to decreasing value of frequency counts of words
#     new1=dict(sorted(spam_word.items(), key=lambda item: item[1],reverse=True))
#     #new2 is basically n_spam_word dictionary in an order sorted according to decreasing value of frequency counts of words
#     new2=dict(sorted(n_spam_word.items(), key=lambda item: item[1],reverse=True))
    
#     print('Top ten spam words') #printing the top ten spam words
#     for i in range(10):
#         print(list(new1.keys())[i],':',new1[list(new1.keys())[i]])
    
#     print('\nTop ten non-spam words') #printing the top ten non-spam words
#     for k in range(10):
#         print(list(new2.keys())[k],':',new2[list(new2.keys())[k]])

f_total= sum(list(n_spam_word.values())+list(spam_word.values())) #total number of words

def spam_prob(W): #function declaration for conditional probability of a word given it is spam
    
    global f_total #f_total as a global variable
    num1=0
    total1=sum(list(spam_word.values())) #total number of words in spam list
    
    if(W in list(spam_word.keys())): #counting the total instances of the word in spam list
        num1+=spam_word[W]

    if(num1!=0): #calculating the conditional probability given a spam message
        prob=num1/total1 
        
    else: #if the total instances of the word is 0
        prob=1/f_total
    
    return prob #returning the conditional probability

def non_spam_prob(W): #function declaration for conditional probability of a word given it is non-spam
    
    global f_total #f_total as a global variable
    num2=0
    total2=sum(list(n_spam_word.values())) #total number of words in non-spam list
    
    if(W in list(n_spam_word.keys())): #counting the total instances of the word in non-spam list
        num2+=n_spam_word[W]
    
    if(num2!=0): #calculating the conditional probability given a non-spam message
        prob=num2/total2
        
    else: #if the total instances of the word is 0
        prob=1/f_total
    
    return prob #returning the conditional probability

def classifier(M): #function declaration for a classifier which checks if a message is spam or not 
    
    global p_spam #p(spam) as a global variable
    global p_non_spam #p(non-spam) as a global variable
    
    tp_spam=1 #total probability of a message being spam given some message
    tp_non_spam=1 #total probability of a message being non-spam given some message
    
    M=re.sub(r'[0-9]'," ",M) #number are removed from words
    M=re.sub(r'[()*.!-+/:;@$%?<=>Â£,~`€_Éˆ¥Â”¾Ã‰Â»™]'," ",M) #symbolic characters are removed from words
    M=re.sub(r'[-]',' ',M)
    M=M.upper()
    M=M.split()
    
    for ch in M: #loop for finding conditional probability for a message given either spam or non-spam
        tp_spam*=spam_prob(ch)
        tp_non_spam*=non_spam_prob(ch)
    
    tp_spam*=p_spam #finding the total probability of a message being spam given some message
    tp_non_spam*=p_non_spam #finding the total probability of a message being non-spam given some message
    
    if(tp_spam>=tp_non_spam): #checks if the message being spam is more likely than non-spam
        return True
    #if the message being non-spam is more likely than spam
    return False

M=input('Enter the message: ') #message M as input

p_spam=(sum(list(spam_word.values())))/f_total #calculating p(spam)
p_non_spam=(sum(list(n_spam_word.values())))/f_total #calculating p(non-spam)

if(classifier(M)): #call to classifier function for message M
    print('m is spam')
else:
    print('m is not a spam') 
