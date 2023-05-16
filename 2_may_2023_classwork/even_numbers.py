number = 0
for number in range(1, 51,):
      if number % 2 & number == 0:
        number.append(number)
        print(number)
        print(number[::-1])


even_number = list(range(0, 51,2))
print(even_number)
print(number[-1])

numbers = [1, 2, 3, 4, 5]
numbers[4] = 550
print(numbers)
print(len(numbers))
variable1 = numbers[1]
# LIST UNPACKING
a, e, u, o, i = numbers
print(variable1)
# LIST UNPACKING
a, e, *others = numbers
print(a, e, others)
a, *others, i = numbers
print(a, others, i)
letters = list("Hello c16")
print(letters)
for index, letters in enumerate(letters):
    print(index, letters)

letter = ['p', 'r', 'g', 'y']
letter.append('e')
print(letter)
letter.append('f')
print(letter)
letter.insert(0, 'l')
print(letter)
letter[2] = 4
letter.remove("g")
print(letter)
del letter[0:2]
print(letter)
