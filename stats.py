def get_num_words(book_text):
    full_book = book_text.split()
    num_words = len(full_book)
    return num_words

def get_chars_dict(book_text):
    count_characters = {}
    for char in book_text:
        char = char.lower()
        if char in count_characters:
            count_characters[char] += 1
        else:
            count_characters[char] = 1
    return count_characters

def chars_dict_to_sorted_list(count_characters):
    result = []
    for char, count in count_characters.items():
        result.append({"char": char, "num": count})
    result.sort(key=lambda x: x["num"], reverse=True)
    return result