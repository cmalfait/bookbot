from stats import get_letters, get_num_words
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(sys.argv[1])
    letters = get_letters(file_contents)
    counter = get_num_words(file_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {counter} total words")
    print("--------- Character Count -------")
    for key, value in letters.items():
        print(f"{key}: {value}")
    print("============== END ==============")

main()
