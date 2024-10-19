'''
PYTHON LAB: french_english_translator.py

- Create an English to french and French to english translator program. Use function to complete this program
- The programs takes a word from the user as an input and translates it using a dictionary data type as a vocabulary word.
- Please add the translation of "prune" in your homework.
- If the word is not in the French code, print "[word]" is not in memory)
***The user will select the language that he/she would like to translate to*** (optional)
'''
def english_french(word):
    vocabulary = {
        "hello": "bonjour",
        "goodbye": "au revoir",
        "apple": "pomme",
        "banana": "banane",
        "prune": "cerise",
        "cloud" :"nuage",
        "space" : "espace",
        "dog" : "chien",
        "hand" : "main",
        "word" : "mot",
        "enter" : "entrer",
        "distance" : "distance",
        "first" : "premier",
        "person" : "personne",
        "grape": "raisin",
        "orange": "orange",
        "pear": "poire",
        "peach": "pêche"
    }
    if word in vocabulary:
        return vocabulary.get(word)
    else:
        return f"Sorry '{word}' is not in memory now. Let try another word."

def french_english(word):
    vocabulary = {
        "bonjour": "hello",
        "au revoir": "goodbye",
        "pomme": "apple",
        "banane": "banana",
        "cerise": "prune",
        "nuage" :"cloud",
        "espace" : "space",
        "chien" : "dog",
        "main" : "hand",
        "mot" : "word",
        "entrer" : "enter",
        "distance" : "distance",
        "premier" : "first",
        "personne" : "person",
        "raisin": "grape",
        "orange": "orange",
        "poire": "pear",
        "pêche": "peach"
    }
    if word in vocabulary:
        return vocabulary.get(word)
    else:
        return f"Sorry '{word}' is not in memory now. Let try another word."

def main():
    print("Welcome to the both English and French Translator!")
    language = input("Select the language (English/French): ").capitalize()

    if language == "English":
        word = input('Please enter the French word to be translate in English:  ')
        translation = french_english(word.lower())
        #print(f"The English translation of '{word}' is : {translation}")
        print(translation)
        print("Thank you for using our Translator App! Feel free to come back!")
           
    elif language == "French":
        word = input('Please enter the English word to be translate in French:  ')
        translation = english_french(word.lower())
        #print(f"The French translation of '{word}' is : {translation}")
        print(translation)
        print("Thank you for using our Translator App! Feel free to come back!")
    else:
        print("Invalid language selection. Please choose between English or French")
        print("Thank you for using our Translator App! Feel free to come back!")

if __name__ == "__main__":
    main()