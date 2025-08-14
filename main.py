from stats import count_words, count_characters, sort_char_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def get_book_text(filepath: str) -> str:
    with open(filepath, 'r') as file:
        return file.read()

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_char_count = sort_char_count(num_characters)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_char_count:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
        
    
main()
