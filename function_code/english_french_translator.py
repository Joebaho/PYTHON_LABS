import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='translator.log',
    filemode='a'
)

def english_french(word):
    """Translate English to French with logging"""
    vocabulary = {
        "hello": "bonjour",
        "goodbye": "au revoir",
        "apple": "pomme",
        "banana": "banane",
        "prune": "cerise",
        "cloud": "nuage",
        "space": "espace",
        "dog": "chien",
        "hand": "main",
        "word": "mot",
        "enter": "entrer",
        "distance": "distance",
        "first": "premier",
        "person": "personne",
        "grape": "raisin",
        "orange": "orange",
        "pear": "poire",
        "peach": "pêche"
    }
    
    logging.info(f"Attempting English->French translation for: '{word}'")
    
    if word in vocabulary:
        translation = vocabulary.get(word)
        logging.info(f"Successful translation: '{word}' -> '{translation}'")
        return translation
    else:
        error_msg = f"'{word}' not in memory"
        logging.warning(error_msg)
        return f"Sorry {error_msg}. Try another word."

def french_english(word):
    """Translate French to English with logging"""
    vocabulary = {
        "bonjour": "hello",
        "au revoir": "goodbye",
        "pomme": "apple",
        "banane": "banana",
        "cerise": "prune",
        "nuage": "cloud",
        "espace": "space",
        "chien": "dog",
        "main": "hand",
        "mot": "word",
        "entrer": "enter",
        "distance": "distance",
        "premier": "first",
        "personne": "person",
        "raisin": "grape",
        "orange": "orange",
        "poire": "pear",
        "pêche": "peach"
    }
    
    logging.info(f"Attempting French->English translation for: '{word}'")
    
    if word in vocabulary:
        translation = vocabulary.get(word)
        logging.info(f"Successful translation: '{word}' -> '{translation}'")
        return translation
    else:
        error_msg = f"'{word}' not in memory"
        logging.warning(error_msg)
        return f"Sorry {error_msg}. Try another word."

def main():
    """Main program execution with logging"""
    logging.info("=== Translator application started ===")
    print("Welcome to the English-French Translator!")
    
    try:
        language = input("Select language (English/French): ").capitalize()
        logging.info(f"User selected language: {language}")
        
        if language == "English":
            word = input('Enter French word to translate to English: ').lower()
            logging.debug(f"User input word: {word}")
            translation = french_english(word)
            
        elif language == "French":
            word = input('Enter English word to translate to French: ').lower()
            logging.debug(f"User input word: {word}")
            translation = english_french(word)
            
        else:
            error_msg = "Invalid language selection"
            logging.error(error_msg)
            print(f"Error: {error_msg}. Please choose English or French.")
            return
            
        print(translation)
        logging.info("Translation displayed successfully")
        
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        print("An error occurred. Please check the logs.")
        
    finally:
        logging.info("=== Translator session ended ===\n")
        print("Thank you for using our Translator App!")

if __name__ == "__main__":
    main()





