# Ask user to input integer
# Determine the modulo of the integer
# if the modulo is equal to 2 print Even
# Else print odd

# number=int(input("Please input a counting number "))
# if (number) % 2 == 0:
#  print({number}, f"is an even number")
# else:
#      print({number}, f"is an odd number")

# Ask user to input their score as a number
# if the score is between 90 to 100 (inclusive) print
# if the score is between 80 to 89 (inclusive) print
# if the score is between 70 to 79 (inclusive) print
# if the score is between 60 to 69 (inclusive) print
# if the score is between 0 to 59 (inclusive) print

# score = int(input("What was your score?\n"))
# if score>=90 and score <=100:
#    print("your Had Grad A - Excellent")
# if score >=80 and score <=89:
#     print("your Had Grad B - Good")
# if score >=70 and score <=79:
#     print("your Had Grad C - Good")
# if score >=60 and score <=69:
#     print("your Had Grad D - Pass")
# if score >=0 and score <=59:
#     print("your Had Grad F - Fail")

# Ask user to enter the purchase amount as float
# if amount is mor than 100 cedis apply a 20% discount and print amount to pay
# if amount is 50 cedis apply 10% discount and print amount to pay
# if the purchase amount is less than 50 allpy no discount and print amount to pay


# price = float(input("what is ypur purchase amount ?\n"))

# if price > 100.00:
#     print(f'your total ampount is : { price * 0.8 } ')

# elif price > 50.00:
#     print(f' your total payment is: {price * 0.9}')

# else:
#     print(f'your total  is {price}')






# # Ask user to input the length of the 3 sides of a triangle
# x=int(input("Enter first side:\n"))
# y=int(input("Enter second side:\n"))
# z=int(input("Enter third side:\n"))
# # If all sides are equal print Equilateral
# if x==y and y==z :
#     print( "This is an Equilateral triangle")
# # If 2 sides are equal print Isosceles
# elif z==y or y==x or z==x:
#     print("This is an Isosceles triangle")
# # If no sides are equal print Scalene
# else:
#     print ("This is a Scalene")
    

# file = open( https://docs.google.com/document/d/1tL0f-ESR8x9HwcU2WNlqE6hqu6C97yaUzE2gESeBqt0/edit?usp=sharing , "r")
# print(file.read())

# file = open( "tasks.txt" , "r")
# tasks = (file.read().split("\n"))
# for task in tasks:
#   print(f"{tasks.index(task) +1}. {task}")

# response = register_user("prince amankwah", "amankwahp@apcgh.com", "0244449489")
# #print(response)


# # define a register user function


import add
import show
import update
import delete

add_task_response = add.add_Task("sleep")
print(add_task_response)

show_task_response = show.show_task()
print(show_task_response)

update_task_response = update.update_task()
print(update_task_response)

delete_task_response = update.update_task()
print(delete_task_response)


