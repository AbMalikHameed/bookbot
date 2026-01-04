def main():
    book = get_book_text("books/frankenstein.txt")
    
    print(word_count(book))

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(book):
    words = book.split()
    count = 0
    
    for word in words:
        count +=1
    
    return f"Found {count} total words"


main()