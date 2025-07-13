a = int(input("Enter your markes and get to know about your Grade: "))   #all input provided by user will be converted in integer
if a > 90:                             #here starts the if conditions for each condition given in the assignment
    print("Excellent! Your grade is A")
elif a >= 80 and a < 90:
    print("Good Job! Your grade is B")
elif a >= 70 and a < 80:
    print("Keep it up! Your grade is C")
elif a >= 60 and a < 70:
    print("You can do better! Your grade is D")
elif a < 60:
    print("Sorry! Your grade is F")
