letter = ("a", "b", "c")
print(letter)
number = 1, 5, 7, 8,
print(number)
list1 = [1, 3, 5, 6]
list2 = [2, 3, 43, 5]
print(list1 + list2)
print(letter + number)
ttuple = tuple(range(1, 500))
print(ttuple)
odd = ttuple[0:-1:2]
print(odd)
even = ttuple[1:-1:2]
print(even)
print(even + odd)
r, o, p, *other = ttuple
print(r, o, p, other)
t, u, i, *remaining, i, p = ttuple
print(t, u, i, *other)
#for num in ttuple:
 #   if number % 2 == 0:

