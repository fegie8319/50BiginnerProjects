# Program an advanced calculator in Python.
# You can make a console application or a GUI.
# Implement not only basic arithmetic operations but also more complex functions like trigonometry, square root, memory and so on.

# Target: Clone a windows build-in calculator with tkinter


import tkinter as tk

window = tk.Tk()

window.title('Calculator')
window.geometry('320x472')
window.resizable(True, True)

num_list = range(0, 10)


# Function Declare
def palce(text):
    print(text)


# Button Declare
# number
num0 = tk.Button(window, text=0, command=lambda: palce(0))
num1 = tk.Button(window, text=1, command=lambda: palce(1))
num2 = tk.Button(window, text=2, command=lambda: palce(2))
num3 = tk.Button(window, text=3, command=lambda: palce(3))
num4 = tk.Button(window, text=4, command=lambda: palce(4))
num5 = tk.Button(window, text=5, command=lambda: palce(5))
num6 = tk.Button(window, text=6, command=lambda: palce(6))
num7 = tk.Button(window, text=7, command=lambda: palce(7))
num8 = tk.Button(window, text=8, command=lambda: palce(8))
num9 = tk.Button(window, text=9, command=lambda: palce(9))

# operation
dot = tk.Button(window, text='.', command=lambda: palce('.'))
plus = tk.Button(window, text='+', command=lambda: palce('+'))
minus = tk.Button(window, text='-', command=lambda: palce('-'))
times = tk.Button(window, text='x', command=lambda: palce('*'))
divide = tk.Button(window, text='/', command=lambda: palce('/'))
sign = tk.Button(window, text='士', command=lambda: palce('-'))
# Button Pack
num0.pack()
num1.pack()
num2.pack()
num3.pack()
num4.pack()
num5.pack()
num6.pack()
num7.pack()
num8.pack()
num9.pack()
dot.pack()
plus.pack()
minus.pack()
times.pack()
divide.pack()
sign.pack()
window.mainloop()
