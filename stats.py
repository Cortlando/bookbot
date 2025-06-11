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
 
 
def sort_on(dict):
    return dict["num"]
           
def sort_letter_by_count(letter_count):
    # print(letter_count)
    letter_list= []
    
    for letter in letter_count:
        if letter.isalpha():
            temp = {
                "char" : letter,
                "num" : letter_count[letter]
            }
            letter_list.append(temp)
    
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
    
        
    