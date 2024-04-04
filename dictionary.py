import json
from difflib import get_close_matches

def load_data():
    with open("data.json") as file:
        data = json.load(file)
    return data

def find_definition(word, data):
    word = word.lower()  # Convert input word to lowercase
    if word in data:
        return data[word]
    elif word.title() in data:  # Check for title case
        return data[word.title()]
    elif word.upper() in data:  # Check for uppercase
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        # If there's a close match, ask user if they meant the suggested word
        suggestion = get_close_matches(word, data.keys())[0]
        confirm = input("Did you mean '{}' instead? Enter Y if yes, or N if no: ".format(suggestion))
        if confirm.upper() == 'Y':
            return data[suggestion]
        else:
            return "Word not found. Please double check it."
    else:
        return "Word not found. Please double check it."

def main():
    data = load_data()
    while True:
        word = input("Enter a word to get its definition (type 'q' to quit): ")
        if word.lower() == 'q':
            break
        else:
            definition = find_definition(word, data)
            if type(definition) == list:
                for item in definition:
                    print("-", item)
            else:
                print(definition)

if __name__ == "__main__":
    main()
