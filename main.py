#define main executable
#seting variable book_path to frankenstein.txt
#setting text to run get_book_text() passing the book_path variable as the arguement
#setting num_words to run count_words with text as the argument
#setting variable for count_letters function
#setting vaiable for chars_sorted function

#print string with book path
#print string stating the number of words
#print loop for each character in the list.
#'char' is pulled from dict, defined in char_sorted function
#'num pulled from dict, defined in char_sorted function
#printing string
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letters(text)
    chars_sorted_list = chars_sorted(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words are found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

#setting get_book_text from main executable file
#path is the argument being passed through.
#opening path passed through and setting it as the variable f
#returning f.read() to read the book
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
#setting count_words for main exe
#running text as the passing argument
#setting words variable to split the text file
#returning the number of words
def count_words(text):
    words = text.split()
    return len(words)

#Passing text in as an argument to
#Setting letters as an empty dictionary
#for loop looking at characters in test
#setting a variable that makes all characters lower case
#if loggic for lowered variable in the letters dictionary.
#if letters exist in dictionary incrment count by 1
#otherwise set the letter in the dictionary value to 1
#return the letters dictionary
def count_letters(text):
    letters = {}
    for c in text:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

#setting a function with a list.
def sort_on(d):
    return d["num"]


#a function with num_chars_dict passed in as the arguement
#creating an empty list
#for loop adding the dictionary to sorted_list. the prefix 'char' is the variable ch
#num is is the num_chars_dict
#sorted_list.sort is taking 2 arguments 1 boolean; 1 that seems to be calling the sort_on function
#not 100% sure as this was never explained
#returning the list.
def chars_sorted(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
#running main executeable
main()