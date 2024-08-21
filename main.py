from string import ascii_lowercase

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_letters_counts(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There are {word_count} words in this book.\n\n")
    report_formatting(char_counts)
    print("--- END REPORT ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    text_split = text.split()
    words = len(text_split)
    return words

def get_letters_counts(text):
    alpha_dict = {}
    for letter in text:
        lower = letter.lower()
        if alpha_dict.get(lower) == None:
            alpha_dict[lower] = 1
        else:
            alpha_dict[lower] = alpha_dict.get(lower) + 1
    return alpha_dict

def report_formatting(char_counts_raw):
    sorted_dict = dict(sorted(char_counts_raw.items(), reverse=True, key=lambda i: i[1]))
    for key in sorted_dict:
        if key.isalpha() == True:
            print(f"The letter {key} appears {sorted_dict[key]} times.")



main()
