# dictionary comprehension

sentence = "What is the airspeed velocity of an unladen swallow?"
words = sentence.split()
# print(words)

word_dic = {word: len(word) for word in words}
print(word_dic)