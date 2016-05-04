#!/usr/bin/python
# coding: utf-8

import os
import sys
import argparse
import random

reload(sys).setdefaultencoding("utf-8")

enl = list("""abcdefghijklmnopqrstuvwxyz""")
ENl = list("""ABCDEFGHIJKLMNOPQRSTUVWXYZ""")
dig = list("""0123456789""")
smb = list("""~!@#[]$%^&*()_+=-"'|\/`<>?,.{};:№""")
rul = list("""абвгдеёжзийклмнопрстуфхцчшщъыьэюя""")
RUl = list("""АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ""")
isl = list("""O0СсОоНКХхЗЕУуВАаТМРр""")

def ArgParse():
	parser = argparse.ArgumentParser()

	# -l	Задать длину паролей
	parser.add_argument("-l", type=int, default=8, help="Длина паролей", dest='Length')

#	# -M	Генерация паролей по шаблону
#	parser.add_argument("-M", type=str, default="", help="Генерация паролей по шаблону", dest='Mask')

	# -c	Включить в пароль хотя бы одну прописную (большую) букву
	parser.add_argument('-c', action='store_true', default=False, dest='OneLargeLetters', help='Включить в пароль хотя бы одну прописную (большую) букву')
	# ^ Если флаг не выставлен, большие буквы могут отсутствовать

	# -A	Не использовать прописные (большие) буквы при создании пароля
	parser.add_argument('-A', action='store_true', default=False, dest='NoLargeLetters', help='Не использовать прописные (большие) буквы при создании пароля')

	# -n	Включить в пароль хотя бы одну цифру
	parser.add_argument('-n', action='store_true', default=False, dest='OneDigit', help='Включить в пароль хотя бы одну цифру')
	# ^ Если флаг не выставлен, цифры могут отсутствовать

	# -0	Не использовать цифры при создании пароля
	parser.add_argument('-0', action='store_true', default=False, dest='NoOneDigit', help='Не использовать цифры при создании пароля')

	# -y	Включить в пароль хотя бы один специальный символ
	parser.add_argument('-y', action='store_true', default=False, dest='SpecialSymbols', help='Включить в пароль хотя бы один специальный символ')

	# -B	Не включать в пароль неоднозначные символы (т.е., которые легко перепутать, например, "0" и "О")
	parser.add_argument('-B', action='store_true', default=False, dest='NoAmbiguous', help='Не включать в пароль неоднозначные символы (т.е., которые легко перепутать, например, "0" и "О")')

	# -1	Вывод сгенерированных паролей в один столбец
	parser.add_argument('-1', action='store_true', default=False, dest='OneColumn', help='Вывод сгенерированных паролей в один столбец')

	# -R	Включить в пароль хотя бы один символ из русского алфавита
	parser.add_argument('-R', action='store_true', default=False, dest='RussianLetters', help='Включить в пароль хотя бы один символ из русского алфавита')

	#
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')
	results = parser.parse_args()

	minlit = 1

	if (results.OneDigit) and (results.NoOneDigit):
		parser.error("Что делать с цифрами?")
	if (results.OneLargeLetters) and (results.NoLargeLetters):
		parser.error("Что делать с большими буквами?")

	if results.OneLargeLetters:
		minlit += 1
	if results.OneDigit:
		minlit += 1
	if results.SpecialSymbols:
		minlit += 1
	if results.RussianLetters:
		minlit += 1

	if results.Length + 1 < minlit:
		parser.error("Нужно увеличить длину пароля")
	if results.Length < 1:
		parser.error("Ошибочный параметр -l")
	return results

def printPasswordList(pList, rows, columns):
	line = 0;
	for pasword in pList:
		sys.stdout.write(pasword)
		line += len(pasword) + 2
		if (line + len(pasword) + 1) >= columns:
			sys.stdout.write("\n")
			line = 0
		else:
			sys.stdout.write("  ")
	sys.stdout.flush()

def genpwd(count, param, dl):
	plist = []
	for i in xrange(count):
		pstr = ""
		for j in xrange(param.Length):
			pstr += random.choice(dl)
		plist.append(pstr)
	return plist

def main():
	rows, columns = os.popen('stty size', 'r').read().split()
	rows = int(rows)
	columns = int(columns)
	Params = ArgParse()
	
#	if Params.
	
	pascount = ((columns) / (Params.Length+2)) * (rows-1)
	pwlist = genpwd(pascount, Params, dig+enl+ENl)
	printPasswordList(pwlist, rows, columns)
	return




if __name__ == '__main__':
	core = getattr(sys.modules["__main__"], "__file__", None)
	if core:
		root = os.path.dirname(os.path.abspath(core))
		if root:
			os.chdir(root)
	main()
