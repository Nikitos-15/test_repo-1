#Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#Примеры:
# - 5, 25 -> да 
#- 4, 16 -> да
#- 25, 5 -> да
#  - 8,9 -> нет

a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
if a == b*b :
    print( a, "первое число являеться квадратом числа ", b )
elif  b ==a*a:
    print( b, "первое число являеться квадратом числа ", a )
else:
    print(" нет квадратов ")