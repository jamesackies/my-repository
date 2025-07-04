# my_list = ['a', 'b', 'c', 'd', 'e']

# a = 0 

# while a < len(my_list):
#     print("square of {} is : {}". format(a, a**2))
#     a +=1



# age = input("Enter Your age:")

# while not age.isdigit():
#     print("ERROR:Provide only integers as input")
#     age = input("enter your age")

# print("great Your age is", age22)




# answer = 30 

# print("lets play the guessing game")

# while True:
#     guess = int(input("what number am i thinking of?"))

#     if guess < answer:
#         print("little higher")
#     elif guess > answer:
#         print("little lower")
#     else:
#         print("you read my mind")
#         break




# for abcd in [1, 2, 3, 4, 5]:
#     print(abcd)

# numbers = []

# for num in range(1,6):
#     numbers.append(num)
# print(numbers)



# word = input("give me a word-")

# count = 0 

# for i in word:
#     count += 1
#     if count < len(word): 
#         i = i + '-'
#     print(i, end='')


#!/bin/bash

echo "Looping through 1 to 10 but will break at 5"

for ((i=1; i<=10; i++))
do      
        echo "Number is $i"
        if [ "$i" -eq 5 ]; then
                echo "Reached 5, breaking the loop"
                break
        fi      
done    

echo "Loop Ended! Command after Loop execution"