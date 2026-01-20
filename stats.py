def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
    return book_text

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    normalized_text = book_text.lower()
    characters = {}
    for char in normalized_text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    characters_dict_list = [{"char": k, "num": v} for k, v in characters.items()]
    return characters_dict_list

def sort_on(characters_dict_list):
    return characters_dict_list["num"]
    
def sort_character_dict(characters_dict_list):
    characters_dict_list.sort(reverse=True, key=sort_on)
    return characters_dict_list