# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

nquarter = int(input('Введите номер четверти (от 1 до 4): '))
while(nquarter<1 or nquarter>4):
    print ('Вы ввели не верный номер, введите номер четверти (от 1 до 4): ')
    nquarter = int(input())
if nquarter == 1:
    print ('Х+ У+')
elif nquarter == 2:
    print ('Х- У+')
elif nquarter == 3:
    print ('Х- У-')
else:
    print ('Х+ У-')