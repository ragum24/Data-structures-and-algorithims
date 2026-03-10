store=[]
#this loop will run 10 times (it will run what evers given in it 10 times)
# i is a variable that counts the number of times that the loop has run
#I AND ITEM ARE TWO DIFFERENT VARIABLES
#i = iteration is repetition 
for i in range(10):
    numbers = int(input("Give a number pls:"))
    store.append(numbers)
    print(numbers)
print(store)

#printing each item of the list one by one
#for loop will start from the first element of the list and will automatically 
#stop at the end of the list
for item in store:
    print(item)
    #item is a variable recieves each list element one by one

