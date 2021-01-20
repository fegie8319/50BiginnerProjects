# Code a script which finds the nth prime number for you. You just enter a number and it gives you the respective prime number. Example: Input an 11 and get a 31.

user_input = input("請輸入想找第幾個質數: ")
cal = int(user_input)


init_num = 2
prime_list = [2]

def main_find(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


while True:

    init_num += 1
    print(init_num)
    if main_find(init_num):
        prime_list.append(init_num)
        print(prime_list)

    if len(prime_list) == cal:
        print("Yes")
