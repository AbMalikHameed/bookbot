def word_count(book):
    words = book.split()
    count = 0
    
    for word in words:
        count +=1
    
    return f"Found {count} total words"