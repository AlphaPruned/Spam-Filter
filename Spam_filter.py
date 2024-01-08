# import the required libraries
import csv
from collections import Counter
import re

sms = []            # sms list store whether the message is spam or not
message = []          # message store the message of both spam and not spam
s_spam = []
s_nonspam = []          
with open("./sms.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter="\t")
  for row in csvreader:
    sms.append(row[0])
    message.append(row[1])

ns = []
s1 = ''  # string of all strings with nonspam messages together
s2 = ''    # string of all strings with spam messages together
a = len(sms)
b = len(message)
# making two different lists s_nonspam and s_spam having string as element of messages of nonspam and spam resp.
for i in range(a):
    if sms[i] == 'notspam':
        s_nonspam.append(message[i])
        ns.append(i)
    else:
        s_spam.append(message[i])
        
for j in range(len(s_nonspam)):
    s1 = s1 + ' ' + s_nonspam[j]

for j in range(len(s_spam)):
    s2 = s2 + ' ' + s_spam[j]
    
# removing all the exclamotory signs and numeric values
s1 = re.sub(r'[^\w\s]',"",s1)
s2 = re.sub(r'[^\w\s]',"",s2)
s1 = re.sub(r'[0-9]',"",s1)
s2 = re.sub(r'[0-9]',"",s2)

# making all the elements in lowercase
s1 = s1.lower()
s2 = s2.lower()
# print(s1)
s1 = s1.split()          #nonspam
s2 = s2.split()          #spam

s1new = []
s2new = []
# list that need to remove
to_rmv = ['and','a','â','the','at','by','for','down','from','in','into','near','of','off','on','to','upon','with','As','as','The','And','A','&','or','2','is','I','i','it','4','me','my','but','your','if','so','are','we','not','&lt;#&gt;','we','do','can','be','ur','im','will','ltgt','i','m','no','its','ok','go','up','u']

for word in s1:
    if word in to_rmv:
        continue
    else:
        s1new.append(word)
for word in s2:
    if word in to_rmv:
        continue
    else:
        s2new.append(word)

counts = Counter(s1new)
counts_spam = Counter(s2new)
def find_prob(word):
    total_words = len(s1new) + len(s2new)
    s_new = s1new + s2new
    w = word
        # p1 for given non-spam
    if counts[w] != 0:
        p1 = (counts[w]/len(s1new))
    else:
        p1 = 1/len(s_new)
        #p2 for spam
    if counts_spam[w] != 0:
        p2 = (counts_spam[w]/len(s2new))
    else:
        p2 = 1/len(s_new)
    return p1,p2

m = input()           # taking input of the message
m = re.sub(r'[^\w\s]',"",m)
m = re.sub(r'[0-9]',"",m)
m = m.lower()
li = m.split()
linew = []
for word in li:
    if word in to_rmv:
        continue
    else:
        linew.append(word)

pm_spam = 1    # pm_spam means probability of m given spam
for word in linew:
    p = find_prob(word)
    pm_spam = pm_spam*p[1]
p_spam = len(s2new)
pspam_m = pm_spam*p_spam     # probability of m given spam

pm_nonspam = 1
for word in linew:
    p = find_prob(word)
    pm_nonspam = pm_nonspam*p[0]
p_nonspam = len(s1new)
pnonspam_m = pm_nonspam*p_nonspam         #probability of m given nonspam

if pspam_m > pnonspam_m:
    print("The given message fall into Spam")
else:
    print("The given message fall into NonSpam")
