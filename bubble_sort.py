python = [3,6,2,99,102,33,5550,6,33,5]

swapped = True

while swapped:
    swapped = False
    for i in range(0,9):
        if python[i] > python[i+1]:
            python[i],python[i+1] = python[i+1],python[i]
            # python[i] had been assigned to python[i+i]; e.g. x,y = 4,9
            # x=4 and y=9
            swapped = True
print(f"Sorted list: {python}")