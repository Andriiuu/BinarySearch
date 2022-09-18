import random
def binary_search(list_e,searh_element):
    low = 0
    high = len(list_e) - 1
    mid = 0
    counter_of_operations = 0
    search_result = False

    while low<= high and not search_result:
        mid = (low + high) // 2
        guess = list_e[mid]
        if guess == searh_element:
            search_res = True
            return search_res, counter_of_operations
        counter_of_operations = counter_of_operations + 1
        if guess > searh_element:
            high = mid - 1
        else:
            low = mid + 1

    return search_result, counter_of_operations

def input_list():
    while True:
        try:
            print("Choose one of three options (1, 2 or 3)  ")
            print("1. Enter list by keybord: ")
            print("2. Generate random list in range [a,b] ")
            print("3. Exit\n")
            choose = int(input())
            if choose > 3 or choose < 1:
                print("Choose 1,2 or 3!")
                continue
            if choose == 1:
                n = int(input("Enter the size of list : "))
                new_list =[]
                for i in range(0, n):
                    print(i + 1,'- element :')
                    elem = int(input())
                    new_list.append(elem)
                new_list.sort()
                return new_list, True
            if choose == 2:
                new_list = []
                n = int(input("Enter the size of list : "))
                a = int(input("Eneter a : "))
                b = int(input("Eneter b : "))
                for i in range(0, n):
                    elem = random.randint(a, b)
                    new_list.append(elem)
                print("Generated random list : ")
                print(new_list)
                new_list.sort()
                return new_list, True
            if choose == 3:
                new_list = []
                return new_list, False
        except ValueError:
            print("This is not an int type!")



true_or_fasle= True
while true_or_fasle:
    lst, true_or_fasle = input_list()
    if true_or_fasle != True:
        continue
    value = int(input("Enter the value you want to find :"))
    result, counter_of_operations = binary_search(lst,value)
    if result:
        print("Element is found!",counter_of_operations, " were made operations" )
    else:
        print("Element is not found!")
