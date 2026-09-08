# 19. Given a sentence, reverse the order of words using split() and join().
sentence="Python is very easy"
result=" ".join(sentence.split()[::-1])
print(result)