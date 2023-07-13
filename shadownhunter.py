#!/usr/bin/python3
"""ShadowHunter - is a pack of programs for interacting with the Internet, for conducting penetration testing, working with Linux and OSINT
Copyright (C) 2022, 2023 Okulus Dev (Alexeev Bronislav)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
# Импорт стандартных модулей
import sys														# Импорт библиотеки sys
import os 														# Импорт библиотеки os

# Импорт локальных модулей
from modules import machanger


def cls():
	os.system('clear')


def interactive_mode():
	print('''ShadowHunter, интерактивный режим интерфейса командной строки''')


def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == 'changemac':
			cls()
			try:
				interface = sys.argv[2]
				machanger.main(interface)
			except IndexError:
				print(machanger.ifconfig())
				machanger.main(input('Введите интерфейс > '))
	else:
		interactive_mode()


if __name__ == '__main__':
	main()
