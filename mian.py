from collections import Counter



strText = open('ciphertext.txt','r').read()

#generate a dictionary that has all char counting, delete white space from the dictionary
wordCount = Counter(strText)
del wordCount[' ']
del wordCount['\n']
print(wordCount)

sum = 0
for i in wordCount.values():
    sum += i

#total number of char is needed to calculate percentage
print(sum)

