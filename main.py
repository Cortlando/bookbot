from stats import get_num_words, num_of_letter, seperate_words, sort_letter_by_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    filepath = sys.argv[1]
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    contents = get_book_text(filepath)
   
    print('----------- Word Count ----------')
    num_words = get_num_words(contents)
    print(f'Found {num_words} total words')
    
    print('--------- Character Count -------')
    num_of_letters = num_of_letter(seperate_words(contents))
    # print(num_of_letters)
    sorted_list = sort_letter_by_count(num_of_letters)
    for dict in sorted_list:
        print(f'{dict['char']}: {dict['num']}')
    print('============= END ===============')
    
main()