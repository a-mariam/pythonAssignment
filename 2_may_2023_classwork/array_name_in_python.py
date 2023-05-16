names = []
for n in range(1, 6):
    add = (input("Enter a name: "))
    if len(add) <= 5 and len(add) > 0:
        if len(add) != " ":
         names.append(add)

print(names)
