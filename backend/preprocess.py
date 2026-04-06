import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)

    verbs, nouns, adverbs, adjectives = [], [], [], []

    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.lemma_.lower())
        elif token.pos_ == "NOUN":
            nouns.append(token.lemma_.lower())
        elif token.pos_ == "ADV":
            adverbs.append(token.lemma_.lower())
        elif token.pos_ == "ADJ":
            adjectives.append(token.lemma_.lower())

    return {
        "verbs": verbs,
        "nouns": nouns,
        "adverbs": adverbs,
        "adjectives": adjectives
    }