imput = int(input("Please type a random number to calculate the sum of the chosen number:"))
print(imput)

def sum(number):
    if number == 1:
        print("Calculating the sum of 1...")
        print("IT'S LITERALLY 1")
        return 1
    elif number == 0:
        print("Calculating the sum of 0...")
        print("IT'S 0 WHY ARE YOU ASKING ME")
        return 0
    else:
        answer = number + sum(number-1) 
        print(f"The answer is: {answer}")
        return answer

answered = sum(imput)