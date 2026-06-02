nums = [4,6,2,7,0,11,411,5,10,7]

def insertion_sort(list2sort):
    for i in range(1,len(list2sort)):
        value2compare = list2sort[i]
        j = i-1
        while j >= 0 and list2sort[j] > value2compare:
            list2sort[j+1] = list2sort[j]
            j = j-1
            print(list2sort)
        list2sort[j+1] = value2compare
    print("\n\nFinal sorted list:")
    print(list2sort)
insertion_sort(nums)