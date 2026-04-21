box = []
num_of_stuff = int(input("How many numbers do you want to store?"))
for i in range(num_of_stuff):
    kangaroos = int(input("Enter the number to add to the list here :) ---> "))
    box.append(kangaroos)
print(box)

#applying linear search to find data in a list

super_sticky_duct_tape = int(input("Enter a number (again) to search it in the list ----> "))
print(super_sticky_duct_tape)
for element in box:
    if element == super_sticky_duct_tape:
        print("The number exists in the list :D")