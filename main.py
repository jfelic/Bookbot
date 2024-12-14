def main():
    frankenstein_txt = get_book_text("books/frankenstein.txt")

    report("Frankenstein", frankenstein_txt)

# Report
def report(name_of_text, text):
    print(f"--- Begin report of {name_of_text} ---")
    print(f"{get_word_count(text)} words found in the document")
    print()

    char_count = get_char_count(text)

    # Sort the character count dictionary by values (number of occurrences) in descending order
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    for (char, count) in sorted_char_count:
        if char.isalpha(): 
            print(f"The '{char}' character was found {count} times")

    print()
    print("--- End report ---")


# Get word count
def get_word_count(text):
    text = text.split()
    return len(text)

# Get char count
def get_char_count(text):
    lowered_text = text.lower()

    countDict = {}

    for c in lowered_text: 
        if c in countDict:
            countDict[c] += 1
        else:
            countDict[c] = 1
    
    return countDict

# Get book text
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
