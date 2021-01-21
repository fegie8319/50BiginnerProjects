# # Code a script which finds the nth prime number for you. You just enter a number and it gives you the respective prime number. Example: Input an 11 and get a 31.
#
# # user_input = input("請輸入想找第幾個質數: ")
# # cal = int(user_input)
#
init_num = 2
prime_list = [2]

while True:
    i = 2
    for i in range(2, init_num):
        print(i)
        if init_num % i == 0:
            break
        else:
            prime_list.append(init_num)
            break
    if len(prime_list) == 10:
        print(prime_list)
        break
    init_num += 1

# list1 = []
# i = 2
# for i in range(2,101):
#     j = 2
#     for j in range (2,i):
#         if i%j == 0:
#             break
#     else:
#         list1.append(i)
#
# print(list1)
