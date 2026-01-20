import sys
from pathlib import Path
from stats import get_book_text, get_word_count, get_character_count, sort_character_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = sort_character_dict(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_character_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()