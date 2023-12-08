def read_file_to_string(path):
    with open(path) as f:
        return f.read()    

def print_no_of_words_in_string(string):
    words = string.split()
    print(f"{len(words)} were found in the document")

def count_chars_in_string(string):
    char_dict = {}
    for char in string:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in char_dict:
                char_dict[lower_char] += 1
            else:
                char_dict[lower_char] = 1
    char_list = list(char_dict.items())
    char_list.sort()
    for char in char_list:
        print(f"The '{char[0]}' character was found {char[1]} times")

def print_book_report(path):
    print(f"--- Begin report of {path} ---")
    file_content_as_string = read_file_to_string(path)
    print_no_of_words_in_string(file_content_as_string)
    print()
    count_chars_in_string(file_content_as_string)
    print("--- End report ---")

def main():
    print_book_report("books/frankenstein.txt")

main()