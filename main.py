#TODO 1. Create a dictionary in this format:
import pandas
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_alpha = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
code_talker = True
while code_talker:
    user_input = input("\nWhat word do you need help spelling? \nType 'exit' to quit: ")
    try:
        user_input.upper()
        if user_input.upper() == "EXIT":
            code_talker = False
        else:
            result = [dict_alpha[letter] for letter in list(user_input.upper())]
            print(result)
    except:
        print("\nPlease, only one word at a time and no punctuation or special characters.")
