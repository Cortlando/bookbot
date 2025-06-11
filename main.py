from stats import get_num_words, num_of_letter, seperate_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    filepath = 'books/frankenstein.txt'
    contents = get_book_text(filepath)
    # print(contents)
    num_words = get_num_words(contents)
    print(f'{num_words} words found in the document')
    num_of_letters = num_of_letter(seperate_words(contents))
    print(num_of_letters)
    
    
main()