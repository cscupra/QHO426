print("What is your name, human?")
name = input()
print("How old are you (in years)?")
age = int(input())
print("How tall are you (in m)?")
height = float(input())
print("How much do you weight (in kg)?")
weight = float(input())
bmi = weight/(height*height)
print(f"{name} you are {age} years old. Your BMI is {bmi:.2f}")


