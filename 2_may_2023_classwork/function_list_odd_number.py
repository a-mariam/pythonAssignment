odd_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def odd_number(lst):
  lst2 = []
  for n in lst:
     if n % 2 != 0:
        lst2.append(n)
     return lst2

lists = [2, 5,4]
print(odd_number(odd_num))


def num1(n):
    for nn in n:
        if nn % 2 != 0:
            return nn

lists = [2, 5,4, 2]
print(odd_number(lists))
#print(num1(5))
