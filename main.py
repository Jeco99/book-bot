def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_letters(word):
     letterCount = {}
     for char in word.lower():
          if char in letterCount:
               letterCount[char] += 1
          else:
               letterCount[char] = 1
     return letterCount

def count_words(fileContent):
    words = fileContent.split()
    return len(words)

def read_path(path):
    with open(path, "r") as f:
        return f.read()
   
def main():
    path = "books/frankenstein.txt"
    readFile = read_path(path)
    countWord = count_words(readFile)
    countLetter = count_letters(readFile)
    chars_sorted_list = chars_dict_to_sorted_list(countLetter)

    print(f"--- Begin report of {path} ---")
    print(f"{countWord} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

main()
