########################################################### LIST COMPREHENSION

# original_list = [1, 2, 3, 4, 5, 6]

# new_list = [i + 10 for i in original_list]

# print(new_list)


# list_with_words = ["Yash", "Sai", "Siddhi", "Bhakti"]

# new_list_with_words = [f"The {i}" for i in list_with_words]

# print(new_list_with_words)


########################################################### SQUARING NUMBERS WITH LIST COMPREHENSION

# numbers = [1, 1, 2 ,3 ,5 ,8 ,13 ,21 ,34 ,55]

# squared = [n ** 2 for n in numbers]
# print(squared)


########################################################### FILTERING NUMBERS WITH LIST COMPREHENSION

# numbers = [1, 1, 2 ,3 ,5 ,8 ,13 ,21 ,34 ,55]

# evens = [n for n in numbers if (n % 2 == 0)]
# print(evens)


########################################################### DATA OVERLAP

# list_1 = [1, 2, 3, 4, 5]
# list_2 = [3, 4, 5, 6, 7]

# overlapping = [num for num in list_1 if (num in list_2)]
# print(overlapping)


########################################################### DICTIONARY COMPREHENSION FROM LIST

# numbers = [1, 1, 2 ,3 ,5 ,8 ,13 ,21 ,34 ,55]

# new_dict = {f"entry_{i}": i for i in numbers}

# print(new_dict)


########################################################### DICTIONARY COMPREHENSION FROM DICTIONARY

# dict = {
#     "smallest" : "Sai",
#     "middle": "Yash",
#     "eldest": "Siddhi"    
# }

# new_dict = {f"The_{key}" : f"The {value}" for (key, value) in dict.items()}

# print(new_dict)


########################################################### DICTIONARY COMPREHENSION EXERCISE

# sentence = "What is Airspeed Velocity of an Unladen Swallow?"

# result = [f"{word} : {len(word)}" for word in sentence.split(" ")]

# print(result)


########################################################### DICTIONARY COMPREHENSION EXERCISE 2

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# weather_k = {key: ((value * 9/5) + 32) for (key, value) in weather_c.items()}

# print(weather_k)


########################################################### ITERATING OVER PANDAS DATAFRAME

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# for (index, row) in student_data_frame.iterrows():
#     print(row["student"])


########################################################### NATO