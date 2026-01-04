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

#TAKES A DICTIONARY AND RETURNS "num"
def sort_on(word_counts):
        return word_counts["num"]

#FUNCTION TO GENERATE SORTED LIST OF WORDS AND COUNTS
def generate_sorted_list(characters):

    #initialise a list to contain the dictionaries
    character_counts = []

    #loop through the dictionary of character counts and populate the new list
    for character in characters:
        temp ={"char" : character, "num" : characters[character]}
        character_counts.append(temp)

    character_counts.sort(reverse=True, key=sort_on)

    return character_counts
    