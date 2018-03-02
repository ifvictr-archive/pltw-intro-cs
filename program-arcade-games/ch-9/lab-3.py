def find(list, target_num):
    for i in range(len(list)):
        if list[i] == target_num:
            print("Found %d at position %d" % (target_num, i))

# Test case
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)