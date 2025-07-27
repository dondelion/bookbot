from stats import (count_words,count_char,sort_char) 
import sys
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = count_words(text)
        num_chars = count_char(text)
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print(f"----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print(f"--------- Character Count -------")
        for member in sort_char(num_chars):
            print(f"{member["char"]}: {member["num"]}")
        print(f"============= END ===============")
def get_book_text(path):
    with open(path) as f:
        return f.read()

main ()