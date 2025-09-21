from my_nlp_tools import tokenize_text, get_file_content, count_vowels, to_vertical, get_tokens_freqs, calculate_ttr

slovo = "koloběžka"
veta = "ahoj, jak se máš"
soubor = 'example.txt'

def main():
    # příklad použití jednotlivých funkcí
    print(tokenize_text(veta))
    ###
    print(get_file_content(soubor))
    ###
    print(count_vowels(slovo))
    ###
    print(to_vertical(soubor))
    dict_with_count = get_tokens_freqs(soubor)
    print(dict_with_count)
    ###
    print(calculate_ttr(dict_with_count))


if __name__ == "__main__":
    main()
