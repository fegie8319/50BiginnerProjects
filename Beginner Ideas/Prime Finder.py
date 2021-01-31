# # Code a script which finds the nth prime number for you. You just enter a number and it gives you the respective prime number. Example: Input an 11 and get a 31.

user_input = input("請輸入想找第幾個質數: ")
cal = int(user_input)
init_num = 2
listx = [2]

while True:
    if len(listx) == cal:
        ans = listx[-1]
        print(ans)
        break
    init_num += 1

    for i in range(2, init_num):
        if init_num % i == 0:
            break

        if i == init_num -1:
            listx.append(init_num)
            break
