'''times = []
number = int(input("EntEr A NumERal:"))
for i in range(1,13): # 1: what number it should start with    13: what number it should end
    multiply= number*i
    times.append(multiply)
print(times)

# printing multiples without multiplying

for i in range(number,13,number): # for i in range(starting number, limit, steps)
    print(i)                    #steps = how many numbers you are skipping each time the loop runs

#Imagine a student is preparing for an exam and wants to print all 
# even numbers from 2 to 20 to practice patterns in mathematics.

for i in range(2,22,2):  #   :D
    print(i)

#A shopkeeper wants to generate bill numbers starting from 1000 up to 1020, 
#increasing by 5 each time for special customers.

for i in range(1000,1020,5):
    print(i)'''

#Suppose a fitness tracker records steps 
#taken every 3 hours in a day, starting from hour 0 up to 24
for i in range(0,27,3):
    print(i)