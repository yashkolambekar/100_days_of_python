########################################################### THE CLASSIC WAY OF WRITING TO FILE

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


############################################################ THE BETTER WAY OF WRITING TO FILE

# with open(file="my_new.txt", mode="w") as file:
#     file.write("New line lol")


############################################################ OPENING THE FILE

# with open(file="my_new.txt", mode="r")as file:
#     print(file.read())


########################################################### 