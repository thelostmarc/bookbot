import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        text = get_book_text(book_path)  # read once
    except FileNotFoundError:
        print(f"Error: file not found at '{book_path}'. Make sure the file exists and the path is correct.")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    text_chars = get_chars_dict(text)
    sorted_list = chars_dict_to_sorted_list(text_chars)
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()