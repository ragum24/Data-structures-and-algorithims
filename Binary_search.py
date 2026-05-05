numbers = [1,2,3,4,5,6,7,8,9,100]
#binary serching always works on a sorted list
start_index = 0
num_of_items = len(numbers)
print(num_of_items)
end_index = num_of_items-1
middle_index = (start_index+end_index)/2
found = False

#repeat until starting index is less than the ending index and found = True
while start_index <= end_index and found == False:
    