def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def seperate_words(book_text):
    return book_text.split()


def num_of_letter(book_text):
    letter_count = {}
    
    for word in book_text:
        for letter in word.lower():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    
    return letter_count
            
    