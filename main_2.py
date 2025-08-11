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


price = float(input("what is ypur purchase amount ?\n"))

if price > 100.00:
    print(f'your total ampount is : { price * 0.8 } ')

elif price > 50.00:
    print(f' your total payment is: {price * 0.9}')

else:
    print(f'your total  is {price}')




