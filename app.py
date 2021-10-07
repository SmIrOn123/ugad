from time import sleep
from random import randint
from os import system

print('Если консоль ничего не показалось значит число не угадано')

while True:
	a1 = randint(0, 30)
	a2 = randint(0, 30)
	a3 = randint(0, 30)
	a4 = randint(0, 30)
	vib = int(float(input('Сколько нужно секунд для запоминание?: ')))

	print(f'{a1} {a2} {a3} {a4} ')
	sleep(vib)
	system('cls')
	otvet = int(input('Напишите любую цифру которую вы запомнили: '))
	if(otvet == a1):
		print('Вы запомнили 1 цифру')
	if(otvet == a2):
		print('Вы запомнили 2 цифру')
	if(otvet == a3):
		print('Вы запомнили 3 цифру')	
	if(otvet == a4):
		print('Вы запомнили 4 цифру')
	else:
		print()
