#IMPORT FUNCTIONS FROM STATS.PY
from stats import word_count
from stats import get_character_count

#PRINTS PUT WORD COUNT AND THE COUNT OF ALL CHARACTERS OF A BOOK
def main():
    book = get_book_text("books/frankenstein.txt")

    dictionary = get_character_count(book)
    
    print(word_count(book))
    print(dictionary)


#GETS ALL TEXT FROM A BOOK
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

main()