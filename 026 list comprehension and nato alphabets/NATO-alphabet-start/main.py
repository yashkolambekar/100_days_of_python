import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {}
for (row, data) in nato_data.iterrows():
    alphabet[data["letter"]] = data["code"]

def name_to_nato():
    print([alphabet.get(i.upper()) for i in input("Enter your name: ")])

name_to_nato()