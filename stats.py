
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    low_text = text.lower()
    for char in low_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    dict_list = []
    for char, count in char_count.items():
        list = {}
        list["char"] = char
        list["num"] = count
        dict_list.append(list)

    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list
