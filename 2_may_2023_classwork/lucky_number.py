lucky_number = 7
user_input = int(input("Enter your lucky number: "))
while user_input != lucky_number:
    user_input = int(input("Enter your lucky number: "))
else:
    print("Congratulation, You are correct")
