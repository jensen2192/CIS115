def main():
    list = [1, 6, 8, 15, 23, 64, 734, 5839, 999999999]
    print("Displaying numbers in list greater than 'n'")
    n = int(input("Provide a value for 'n': "))
    larger_than(n, list)

def larger_than(the_num, the_list):
    for value in the_list:
        if value > the_num:
            print(value)

main()