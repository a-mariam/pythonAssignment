
def cohort16_register():
    registers = {"esther": 23, "rotimi": 45, "lateef": 34, "mariam": 20}
    name = input("What's your name?").lower()
    if name in registers:
        age = registers[name]
        return f"Hi,{name}, you are {age} years old"
    else:
        age = int(input("your name is not in the register,please enter your age? "))
        registers[name] = age
        print(f"Hi,{name},you are {age} years old.")


cohort16_register()
