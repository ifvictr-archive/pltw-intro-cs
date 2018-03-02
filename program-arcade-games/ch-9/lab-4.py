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