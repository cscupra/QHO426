import random

#Defined a function - I specified what it is, what it does and what name is attached to it
#Parameter - data given into the function
#Default Parameters - some data that would be used, if not given an argument
def calc_area(h = 4, b = 6):
    area = h*b*0.5
    return area

def run():
    print(calc_area(random.randint(1, 10), 4))
    a1 = calc_area(10, 9)
    a2 = calc_area(2, 2)
    if a1>a2:
        print("Area 1 was larger")
    print(calc_area(100))
    calc_area(b=20)
    calc_area()

