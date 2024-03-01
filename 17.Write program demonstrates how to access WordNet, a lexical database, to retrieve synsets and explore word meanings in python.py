import nltk
from nltk.corpus import wordnet

def explore_word(word):
    synsets = wordnet.synsets(word)

    if synsets:
        print(f"Word: {word}")
        for synset in synsets:
            print(f"Synset: {synset.name()}")
            print(f"Definition: {synset.definition()}")
            print(f"Examples: {synset.examples()}")
            print()

    else:
        print(f"No synsets found for the word: {word}")

# Example usage
word_to_explore = "happy"
explore_word(word_to_explore)
