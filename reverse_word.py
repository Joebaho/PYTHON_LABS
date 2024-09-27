'''
PYTHON LAB:reversing_a_word.py

Write a program that will ask for a word as reverse the word.

Display on the screen: Your word is: word, and the reverse is: reverse_word.'''

#This Code we will be using string format and flows work to request for a word and the write the reserve of it! 
word=input('What is your favorite word:  ')
#Declaration of Variables
reverse_word=word[:: -1]
sentence = f" Your word is {word}, and the reverse is {reverse_word}."
# Print the sentence
print(sentence)