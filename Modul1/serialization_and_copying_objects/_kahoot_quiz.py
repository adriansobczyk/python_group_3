'''
 Omówienie pytań z kahoota
'''

# 3. Co będzie znajdować się w pliku tekstowym "salary.txt" po wykonaniu programu?
# salary = {"Jhon": 2300, "Steve": 1300, "Liza": 1700}
# with open("salary.txt", "w") as fh:
#     for key, value in salary.items():
#         fh.write(f"{key} {value}/n")


# 5. Co zostanie wyświetlone na konsoli przez program?
# import pickle
# some_data = {
#     (1, 3): 3.145,
#     2: ["apple", "pineaple", "peach", "lemon"],
#     "name": "Python",
# }

# byte_stream = pickle.dumps(some_data)
# unpacked = pickle.loads(byte_stream)

# print(unpacked is some_data)
# print(unpacked == some_data)


# 10. Co program zapisze w pliku json?
# import json

# numbers = [2, 3, 4, 7, 11, 13]

# with open("numbers.json", "w") as f_obj:
#     json.dump(numbers, f_obj)


# 12. Co będzie znajdować się w pliku CSV po wykonaniu programu?
# import csv

# users = [
#     {"name": "Tom", "age": 28},
#     {"name": "Bob", "age": 34},
# ]

# with open("users.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "age"])
#     writer.writeheader()
#     writer.writerows(users)
#     writer.writerow({"name": "Sam", "age": 41})


# 14. Co zostanie wyświetlone na konsoli przez program?
# lst= [1, 2, 3]
# copy_lst = lst
# copy_lst.append(4)
# print(lst)


# 15. Co zostanie wyświetlone na konsoli przez program?

# dct = {"id": 345}
# dct_copy = {**dct}
# dct_copy[2] = 567

# print(dct)


# 16. Co zostanie wyświetlone na konsoli przez program?
import copy

lst = [1, 2, {2: 567}]

copy_lst = copy.deepcopy(lst)
copy_lst.append(4)
print(lst)
