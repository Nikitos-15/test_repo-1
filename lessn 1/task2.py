Lst = [1, 2, 3, 9, 4]
max = Lst[0]

for i in range(1, len(Lst)):
    if Lst[i]> max:
        max = Lst[i]
print(f"Максимальное число {max}")