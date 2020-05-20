# 1
# class Menu(object):

#     def __init__(self, text):
#         self.text = text
#         char = ""
#         s_char = ""
#         num = []
#         for i in self.text:
#             if i.isdigit():
#                 num.append(int(i))
#             elif i.isalpha():
#                 char += i
#             else:
#                 s_char += i
#                 print("No.of characters: {0}, No.of special characters: {1}, No.of digits: {2}".format(len(char), len(s_char), len(num)))
#         if sum(num) % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#         for _ in sorted(char, reverse=True):
#             print(_, end="")


# m = Menu("12bsD$")


# # 2
# class Password(object):

#     def __init__(self, password):
#         self.password = password
#         if 8 <= len(self.password) <= 10 and self.password[0].islower() and self.password[-1].islower() and self.password[0].isalpha() and self.password[-1].isalpha() and self.alphanum(self.password):
#         		print("Entered password is valid")
#         else:
#             print("Entered password is not valid")

# # https://www.tutorialspoint.com/How-to-check-if-a-string-has-at-least-one-letter-and-one-number-in-Python

#     def alphanum(self,text):
#     	alpha_flag = False
#     	num_flag = False
#     	for j in text:
#     		if j.isalpha():
#     			alpha_flag = True
#     		if j.isdigit():
#     			num_flag = True
#     	return alpha_flag and num_flag


# p = Password("oorewtu")

# 4
# for i in ['a','b','c']:
# 	try:
# 		print(i**2)
# 	except TypeError:
# 		print("Not a number")

# while True:
# 	print("Enter 'q' to exit")
# 	num = input("Enter a number: ")
# 	if num != "q":
# 		try:
# 			print(int(num) ** 2)
# 		except Exception:
# 			print("Enter a valid entry")
# 	else:
# 		break

# 5
# metro = [("Mumbai",), ("Chennai",), ("Delhi",), ("Gujrat",), ("Kolkata",), ("Hydrabad",), ("Banglore",)]
# metro_dict = {}

# for i in metro:
#     a = int(input(f"Enter positive cases in {i[0]}: "))
#     metro_dict[i[0]] = a

# avg_pos_case = sum(metro_dict.values()) // 7

# for x, y in metro_dict.items():
#     if y >= avg_pos_case:
#         print(x, "Red Zone Need to be sealed")
#     elif y == avg_pos_case // 2:
#         print(x, "Orange Zone... Need to be Quarantine")
#     if y < avg_pos_case // 2:  # changed the condition here
#         print(x, "Stay home Stay safe")

# 6
# https://www.tutorialspoint.com/generating-random-number-list-in-python
# from random import randint
# n = randint(1000, 9999)
# user = input("Enter a 4 digit number: ")
# bulls = cows = 0
# for i in user:
#     if i in str(n):
#     	bulls += 1
#     else:
#     	cows += 1
# print("{0} cows, {1} bulls".format(cows,bulls))


# 7
# def check_prime(num):
#     flag = True
#     for k in range(2, num):
#         if num % k == 0:
#             return False
#     return flag

# one_v = []
# two_v = []
# res = set()
# with open("One.txt", "r") as one_t:
#     for i in one_t:
#         one_v.append(i)
# with open("Two.txt", "r") as two_t:
#     for j in two_t:
#         two_v.append(j)
# for l in one_v[0].split(","):
#     if check_prime(int(l)):
#         res.add(int(l))
# for o in two_v[0].split(","):
#     if check_prime(int(o)):
#         res.add(int(o))
# for r in res:
#     print(r, sep=",")


# 8
# from itertools import product
# one_v = []
# two_v = []

# with open("One.txt", "r") as one_t:
#     for i in one_t:
#         one_v.append(i)
# with open("Two.txt", "r") as two_t:
#     for j in two_t:
#         two_v.append(j)
# with open("Output.txt", "a") as op_t:
#     for x, y in product(one_v[0].split(","), two_v[0].split(",")):
#         print(int(x) / int(y), file=op_t)

# 9
# def swapnum(num):
#     t_l = []
#     for i in num:
#         t_l.append(i)
#     if len(t_l) == 4:
#         (t_l[1], t_l[2]) = (t_l[2], t_l[1])
#         print("Swapped number", "".join(t_l))
#     else:
#         print(num)


# a = input("Enter a number: ")
# swapnum(a)
