import pandas

student_dict = {
    "student": ["kitty","bobo","benny"],
    "score": [80, 78, 81]
}

# for (key, value) in student_dict.items():
#     # print(key)
#     # print(value)


student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     # print(key)
#     # print(value)

# Loop through rows of a data frame
# Each of these rows is a pandas series object
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    print(row.student)
    print(row.score)