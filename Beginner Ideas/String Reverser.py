# Implement a script which reverses a string, while still retaining the upper- or lower-case of the individual characters.
from retrying import retry

workflow = True


@retry
def main():
    old_input = input("Please enter a word: ")
    string_list = []
    return_string = ""
    for i in old_input:
        string_list.append(i)

    string_list.reverse()

    for x in string_list:
        return_string += x

    print(return_string)


while workflow:
    main()
