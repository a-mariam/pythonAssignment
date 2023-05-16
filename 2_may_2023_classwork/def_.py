from math import pi


def area_calc(number):
    try:
        return pi * (number ** 2)
    except:
        return f"The input must be a number"


print(area_calc("e"))

# def area(r):
#     try:
#         return pi * (r ** 2)
#     except (TypeError,  ValueError):
#         print("Eye dey pain you?, Enter an integer")
