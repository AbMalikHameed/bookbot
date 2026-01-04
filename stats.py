#FUNCTIONS TO COUNT HOW MANY WORDS IN A BOOK
#GIVEN A BOOK AS AN INPUT
def word_count(book):
    words = book.split()
    count = 0
    
    for word in words:
        count +=1
    
    return f"Found {count} total words"

#FUNCTION TO CREATE A DICTIONARY OF HOW MANY TIME
#EACH CHARACTER APPEARS IN THE BOOK GIVEN A BOOK AS INPUT
def get_character_count(book):
    unique_characters = {}

#ITTERATES OVER ALL CHARCTERS IN THE BOOK
    for char in book:
        #MAKES CHARCTERS LOWER CASE
        char = char.lower()

        #BUILD DICTIONARY OF CHARACTERS AND COUNTS
        if char in unique_characters:
            unique_characters[char] += 1
        else:
            unique_characters[char] = 1
    

    return unique_characters