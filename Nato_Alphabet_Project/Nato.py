import pandas

# Create a dictionary in this format: {'A': 'Alfa', 'B': 'Bravo'}
pd = pandas.read_csv("alphabet.csv")
# print(pd)
# for (index, row) in pd.iterrows():
#     print(row.code)
new_dict = {row.letter:row.code for (index,row) in pd.iterrows()}
# print(new_dict)

spelling_on = True

while spelling_on:
    # Create a list of the phonetic code words from a word that the user inputs
    user_input = input("Enter a word: ").upper()
    output = [new_dict[letter] for letter in user_input]
    print(output)

    again = input("Run again (Y/N): ").upper()
    if again == "N":
        spelling_on = False




