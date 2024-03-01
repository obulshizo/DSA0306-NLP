import spacy

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")
def syntax_semantic_analysis(sentence):
    # Process the input sentence using spaCy
    doc = nlp(sentence)
    # Extract noun phrases and their meanings
    noun_phrases_and_meanings = []
    for chunk in doc.noun_chunks:
        # Get the head (main word) of the noun phrase
        head_word = chunk.root.text

        # Extract the meaning (definition) of the head word
        head_meaning = get_word_meaning(head_word)

        # Store the noun phrase and its meaning
        noun_phrases_and_meanings.append({
            'noun_phrase': chunk.text,
            'meaning': head_meaning
        })

    return noun_phrases_and_meanings
def get_word_meaning(word):
    # Placeholder function to get the meaning of a word
    # In a real-world scenario, you would use a lexical database or an API
    # For simplicity, we'll return a dummy meaning here
    return f"Dummy meaning for {word}"

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
results = syntax_semantic_analysis(sentence)

# Display the results
for result in results:
    print(f"Noun Phrase: {result['noun_phrase']}, Meaning: {result['meaning']}")
