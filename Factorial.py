#IMPORTANT POINTS FOR RECUSION:
#funcion calling itself 
#it will always have an dead end (spiral)
#it will always have a return key word

store = int(input("Please type a number to calculate the factorial of the chosen number:"))
print(store)


def factorial(keep): #keep id a copy of the variable store
    if keep == 1:
        print("Calculating the factorial of 1:")
        print("Answer:1")
        return 1
    else:
        print(f"Calculating factorial of {keep}:")
        answer = keep * factorial(keep-1)
        print(f"Answer:{answer}")
        return answer
final_answer = factorial(store)

print(f"The final answer is: {final_answer}")

#       :)