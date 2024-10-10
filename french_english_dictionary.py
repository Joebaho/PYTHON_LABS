'''
PYTHON LAB: french_english_dictionary.py

- Create an English to french translator program.
- The programs takes a word from the user as an input and translates it using a dictionary data type as a vocabulary word.
- Please add the translation of "prune" in your homework.
- If the word is not in the French code, print "[word]" is not in memory)
***The user will select the language that he/she would like to translate to*** (optional)
'''

#get user input language
user_language = input('Please enter language the word to be translate to: ')

# declare of the dictionary
english_french = {
    "prune" :"élaguer",
    "cloud" :"nuage",
    "space" : "espace",
    "dog" : "chien",
    "hand" : "main",
    "word" : "mot",
    "enter" : "entrer",
    "distance" : "distance",
    "first" : "premier",
    "person" : "personne",
    "apple": "pomme",
    "banana": "banane",
    "grape": "raisin",
    "prune": "prune",  # Translation of "prune"
    "orange": "orange",
    "pear": "poire",
    "peach": "pêche"
}
language ={
    "english" : "English",
    "french" :  "French"
}
# Perform translation based on the user input language
if user_language == "English":
    user_input = input('Please enter the French word to be translate in English:  ')
    #declaration for word not in memory
    not_in_memory = f'\nSorry, the word "{user_input.capitalize()}" is not in memory today.'
    # Look for the word in the values (French) and get the English key
    english_result = [k for k, v in english_french.items() if v == user_input]
    if english_result:
        print(f'\nThe English translation of the French word "{user_input.capitalize()}" is: "{english_result[0]}"')
    else:
        print(not_in_memory)

elif user_language == "French":
    # user input 
    user_input = input('Please enter the English word to be translate in French:  ')
    #declaration for word not in memory
    not_in_memory = f'\nSorry, the word "{user_input.capitalize()}" is not in memory today.'
    # Look for the word in the keys (English)
    french_result = english_french.get(user_input)
    if french_result:
        print(f'\nThe French translation of the English word "{user_input.capitalize()}" is: "{french_result.capitalize()}"')
    else:
        print(not_in_memory)

else:
    print(f'\nSorry, the language {user_language.capitalize()} is not available in my memory.')


