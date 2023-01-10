#### A.
# x = 1
# y = 2
#
# if x > y:
#     print("BIG")
# elif x < y:
#     print("small")


#### B.

# for i in range(5):
#     print(i+1)

#### C.
#
# var = 1
# for i in range(4):
#     if var == 1:
#         print("summer")
#     elif var == 2:
#         print("winter")
#     elif var == 3:
#         print("fall")
#     elif var == 4:
#         print("spring")
#     var += 1

#### D.

# count = 1
# while count < 11:
#     print(count)
#     count = count +1


#### E.

# age = 34
# first_letter = 'g'
# shekel_dollar_currency = 3.43
# flew_abroad = True
# aprtment_num = 15
#
# print(age,first_letter,shekel_dollar_currency,flew_abroad,aprtment_num)
# print(age+shekel_dollar_currency)

#### F.

# phone_number = input("Type your phone number: ")
# print(phone_number)

#### G.

# def printHello():
#     print("Hello")
#
# def calculate():
#     print(5+3.2)
#
#
# printHello()
# calculate()

#### H.
# def get_name(name):
#     print(name)
# def get_half(num):
#     print(num/2)
#
# get_name('gal')
# get_half(9)

#### I.
# def get_sum(num1, num2):
#     result = num1 + num2
#     return result
#
#
# def get_string(str1, str2):
#     result = str1 + " " + str2
#     return result
#
# print(get_sum(4,7))
# print(get_string('gal','abc'))

#### J.
# lst = [1,'asd', False]
# for i in lst:
#     print(i)

#### K.
# def get_list_sum(lst):
#     result = 0
#     for i in lst:
#         result += i
#     print(result)
#
# get_list_sum([1,5,9,3,2])

#### L.
# my_dict = {'Name': 'Gal',
#            'Date': '22/08',
#            'add': '24 aprt 15'}
#
# for i in my_dict:
#     print(i)

#### M.

# for i in range(5):
#     str = "*"
#     for j in range(i):
#         str += '*'
#     print(str)

#### N.

# for i in range(7):
#     for j in range(7):
#         if (i == j) or ((7 - j - 1) == i):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

#### O.

# def get_num():
#     num = input("num: ")
#     get_dig_sum(num)
#
#
# def get_dig_sum(num):
#     sum = 0
#     for i in range(len(num)):
#         sum += int(num[i])
#     print(sum)
#
# get_num()

#### P.
# def get_tup_to_str(str):
#     result = ''
#     for i in range(len(str)):
#         result += str[i]
#     return result
#
# tup = ('h','e','l','l','o')
# print(get_tup_to_str(tup))

#### Q.

# def get_smallest(lst):
#     small_num = lst[0]
#     for i in range(len(lst)):
#         if lst[i] < small_num:
#             small_num = lst[i]
#     return small_num
#
# my_list = [8,44,31,5,888,23,645,11,345]
# print(get_smallest(my_list))
