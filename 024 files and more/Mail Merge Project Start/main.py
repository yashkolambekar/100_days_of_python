#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(file="Input/Names/invited_names.txt", mode="r") as names:
    names = names.readlines()

for i in range(len(names) - 1):
    names[i] = names[i].strip("\n")

with open(file="Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

for i in names:
    with open(file=f"Output/ReadyToSend/letter_for_{i.lower().replace(' ', '_')}.txt", mode="w") as new_letter:
        letter_content = letter.replace("[name]", i)
        new_letter.write(letter_content)
