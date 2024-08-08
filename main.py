def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(sort(chars_dict))
    print("\n--- End report ---")

def sort(dict):
    sorted_list = []
    sorted_string = ""
    for d in dict:
        if d.isalpha() == True:
            sorted_list.append({"char": d, "num": dict[d]})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    for l in sorted_list:
        sorted_string += f"\nThe '{l['char']}' character was found {l['num']} times"
    return  sorted_string

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()