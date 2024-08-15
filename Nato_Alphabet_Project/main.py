# Compare numbers in text1 with those in text2
# list comprehension

# First method:
# with open("text1.txt") as text1:
#     file1 = text1.readlines()
#     list1 = [int(i.strip()) for i in file1]
#
# with open("text2.txt") as text2:
#     file2 = text2.readlines()
#     list2 = [int(i.strip()) for i in file2]
#
# new_list = [num for num in list1 if num in list2]
# print(new_list)

# Second method:
# with open("text1.txt") as text1:
#     file1 = text1.readlines()
#
# with open("text2.txt") as text2:
#     file2 = text2.readlines()
#
# new_list = [int(num.strip()) for num in file1 if num in file2]
# print(file1)
# print(file2)
# print(new_list)