#IMPORT FUNCTIONS FROM STATS.PY
from stats import word_count
from stats import get_character_count
from stats import generate_sorted_list

#PRINTS PUT WORD COUNT AND THE COUNT OF ALL CHARACTERS OF A BOOK
def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)

    dictionary = get_character_count(book)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ---------")
    print(word_count(book))
    print ("--------- Character Count -------")

    sorted_character_list = generate_sorted_list(dictionary)
    #print(sorted_character_list)

    for word_counts in sorted_character_list:
        if word_counts["char"].isalpha() == True:
            print(f"{word_counts["char"]}: {word_counts["num"]}")

    print("============= END ===============")
    





#GETS ALL TEXT FROM A BOOK
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

main()