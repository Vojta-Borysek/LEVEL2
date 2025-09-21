import string
from collections import Counter


def tokenize_text(text):
    # Rozdělení textu podle mezer
    tokens = text.split()
    # Vytvoření seznamu tokenů s odstraněnou interpunkcí na začátku a konci
    clean_tokens = []
    for token in tokens:
        # Odstranění interpunkce z obou stran tokenu
        cleaned_token = token.strip(string.punctuation)
        # Přidání neprázdného tokenu do seznamu
        if cleaned_token:
            clean_tokens.append(cleaned_token)
    return clean_tokens


def get_file_content(file_name):
    with open(file_name, encoding='utf-8') as open_file:
        return open_file.read()


def count_vowels(word):
    vowels = 'aeiouyáéíóúůýě'
    return sum(1 for ch in word.lower() if ch in vowels) or 1


def to_vertical(file_name):
    # načtení textu
    text = get_file_content(file_name)
    tokens = tokenize_text(text)
    # vytvoření nového souboru s příponou .vertical.txt
    out_file = file_name + ".vertical.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        for token in tokens:
            length = len(token)
            syllables = count_vowels(token)
            # print(f"{token.lower()}\t{length}\t{syllables}") --> print pro kontrolu
            f.write(f"{token.lower()}\t{length}\t{syllables}\n")
    return "successfully put to vertical"


def get_tokens_freqs(file):
    text = get_file_content(file)
    tokens = tokenize_text(text)
    tkns = []
    for t in tokens:
        tkns.append(t.lower())
    # print(dict(Counter(tkns))) --> print pro kontrolu
    return dict(Counter(tkns))


def calculate_ttr(dict_with_freqs):
    # počet unikátních slov
    uni = len(dict_with_freqs)
    # celkový počet slov v textu
    words_summarry = sum(dict_with_freqs.values())
    if words_summarry == 0:
        return 0
    return uni/words_summarry
