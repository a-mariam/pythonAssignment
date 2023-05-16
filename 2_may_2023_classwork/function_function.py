list2 = [1, 2, 3, 4, 5, 6]

def square(number):
   squares = number ** 2
   return squares

ints = int(input("Enter a number: "))
print(square(ints))

ans = list(map(square, list2))
print(ans)
