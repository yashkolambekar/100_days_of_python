# Today is 21-08-2023 and we are 4 days ahead 

# weather_data_list = []
# with open(file="weather_data.csv", mode="r") as weather_data_file:
#     while weather_data_file.readline():
#         data = weather_data_file.readline()
#         data = data.removesuffix("\n")
#         temp_list = data.split(",")
#         weather_data_list.append(temp_list)

#     print(weather_data_list)


########################################################### CSV MODULE

# import csv

# with open(file="weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)

#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))

#     print(tempratures)


########################################################### PANDAS

# import pandas

# data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
# # print(type(data["day"]))

# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# total_temp = 0
# for temprature in temp_list:
#     total_temp += temprature
# avg_temp = total_temp / len(temp_list)

# print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()]["condition"])

# print(data[data.day == "Monday"]["temp"] * 9/5 + 32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)

# print(data)

# data.to_csv("student_data.csv")


########################################################### SQUIRREL DATA WITH PANDAS

# import pandas

# squirrel_data = pandas.read_csv("squirrel_data.csv")

# fur_color_data = squirrel_data["Primary Fur Color"]

# fur_count = fur_color_data.value_counts()

# fur_count.to_csv("fur_color_count.csv")


########################################################### ABOVE THING IN TWO LINES

# import pandas
# pandas.read_csv("squirrel_data.csv")["Primary Fur Color"].value_counts().to_csv("new_fur_color_count.csv")


########################################################### 