lst = [25, 10, 15, 5, 30, 55, 35, 45, 20]
print(lst)
for num in range(len(lst)):
    for j in range(num + 1, len(lst)):
        if lst[num] > lst[j]:
            lst[num], lst[j], = lst[j], lst[num]

print(lst)
 