# Use recursion to calculate the factorial of any number as efficient as possible.

u_input = int(input("Please enter an integer"))

init = 1

if u_input == 1:
    print(1)
else:
    for i in range(1, u_input + 1):
        init = init * i

    print(init)
