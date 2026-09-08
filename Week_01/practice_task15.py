# 15. Write a program to count the frequency of each word in a sentence using a dictionary.
sentence="python is easy and python is powerful"
words=sentence.split()
frequency={}
for word in words:
    frequency[word]=frequency.get(word,0)+1
print(frequency)