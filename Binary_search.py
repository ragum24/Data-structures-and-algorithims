numbers = [1,9,34,67,89,100,344,765,876,987]
#binary serching always works on a sorted list
start_index = 0
num_of_items = len(numbers)
print(num_of_items)
end_index = num_of_items-1
middle_index = (start_index+end_index)//2
found = False

num_2_search = int(input("What number would you like to search for, potato?"))

#repeat until starting index is less than the ending index and found = True
while start_index <= end_index and found == False:
    middle_index = (start_index+end_index)//2
    if numbers[middle_index] == num_2_search:             #index is in square brackets
        found = True
    elif numbers[middle_index] > num_2_search:
        end_index = middle_index-1
    else:
        start_index = middle_index+1
#checking if the number was found (while loop)
if found == True:
    print(f"The number {num_2_search} has been found at {middle_index}, potato.")
else:
    print(f"The number {num_2_search} has not been found, potato.")