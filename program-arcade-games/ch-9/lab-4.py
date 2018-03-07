import random

def create_list(size):
    list = []
    for _ in range(size):
        list.append(random.randint(1, 6))
    return list

def count_list(list, target_num):
    count = 0
    for num in list:
        if num == target_num:
            count += 1
    return count

def average_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum / len(list)

# `create_list` test case
my_list = create_list(5)
print(my_list)
# `count_list` test case
count = count_list([1, 2, 3, 3, 3, 4, 2, 1], 3)
print(count == 3)
# `average_list` test case
avg = average_list([1, 2, 3])
print(avg == 2)
print()

# Main program
list = create_list(10000)
for i in range(1, 7):
    print("%d's in list: %d" % (i, count_list(list, i)))
print("List average: %f" % average_list(list))

# Extra stuff
while True:
    user_input = input("""
What would you like to do?

a) Create a list filled with random numbers
b) Count the amount of numbers in a given list
c) Find the average of a list of numbers
q) Quit this program

> """).lower()
    if user_input == "a":
        while True:
            size = input("What size do you want the list to be? ").lower()
            if size == "q":
                print("Bye")
                break
            try:
                size = int(size)
                if type(size) is int:
                    print(create_list(size))
            except:
                print("Invalid input")
    elif user_input == "b":
        list = []
        while True:
            num = input("Enter a number, or press 'n' to proceed: ")
            try:
                if not num:
                    print("Please specify a number!")
                elif num.lower() == "n":
                    while True:
                        try:
                            target = input("Which number do you want to look for? ")
                            target = int(target)
                            if not target:
                                print("Please specify a number!")
                            elif type(target) is int:
                                print("There were %d %d's in the list" % (count_list(list, int(target)), target))
                                break
                            elif target.lower() == "q":
                                print("Bye")
                                break
                        except:
                            print("Invalid input")
                elif int(num):
                    list.append(int(num))
                    print(list)
            except:
                print("Invalid character entered")
            # When user enters 'n', move to prompt which number to find
    elif user_input == "c":
        list = []
        print("Enter all your numbers. Type 'q' when finished: ")
        while True:
            data_input = input("> ")
            try:
                if not data_input:
                    print("Please specify a number!")
                elif data_input.lower() == "q":
                    print("List average was %f" % average_list(list))
                    break
                elif int(data_input):
                    list.append(int(data_input))
            except:
                print("Invalid character entered")
    elif user_input == "q":
        print("Bye!")
        break