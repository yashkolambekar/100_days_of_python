# print(len(str(10000)));
# print("Hello"[-2]);
# print(int("10"));
# print(type(456.44))
# print("Your name has " + str(len(input("What is your name?\n"))) +" characters");
# print(6 / 2);
# print(2 ** 20);

############################## BODY MASS INDEX
# print((float(input("What is your weight? : ")) // (float(input("What is your height? : ")) ** 2)));

############################## Number of days, weeks and months left
# remaining_years = (90 - int(input("What is your age? : ")));
# print(f"You have {remaining_years * 365} days, {remaining_years * 52} and {remaining_years * 12} months remaining");

############################## Tip calculator
print(round((int(input("What is the bill amount? : ")) / int(input("How many people are going to pay? : ")) * 1.12), 2));