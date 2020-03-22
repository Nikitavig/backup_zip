from datetime import datetime
import os
import time
import shutil


# Пути откуда бэкапить файлы
LIST_PATH_FROM = [
				'C:/Project/alarm',
				]

# Пути куда бэкапить файлы
LIST_PATH_TO = [
				'C:/Backup',
				'D:/Backup',
				'E:/Backup',
				'F:/Backup',
				'//backup/sda1/backup',
				]

# Тут хранится информация о дате последнего быкапа
PATH_RESOURCES = 'resources'


def zip_(path_to, path_from):
	try:
		shutil.make_archive(path_to, 'zip', path_from)
	except Exception as e:
		raise e


def check_date():
	"""
	
	Функция для проверки даты
	Если наступил следующий день, то необходимло сделать бэкап

	"""


	def get_date_fropm_file():
		"""

		Функция для чтения даты из файла
		"""		
		with open(PATH_RESOURCES + '/' + 'date', 'r') as file:
			return datetime.strptime(file.read(), "%Y-%m-%d").date()

	def write_date_now():
		"""

		Функция для записи даты в файла
		"""		
		with open(PATH_RESOURCES + '/' + 'date', 'w') as file:
			file.write(str(datetime.now().date()))

	# Проверка, если текущая дата > чем дата последнего бэкапа,
	if datetime.now().date() > get_date_fropm_file():
		# Записываем текущую дату в файла 
		write_date_now()
		# тогда возвращаем True
		return True
	else:
		# иначе False
		return False


def backup():
	"""
	
	Функция для копирования файлов
	"""

	# Перебираем все пути куда надо скопировать файлы
	for path_to in LIST_PATH_TO:
		print(f"Копирвоание в: {path_to}")
		
		# Перебираем все пути откуда надо скопировать файлы
		for path_from in LIST_PATH_FROM:
			
			# Сохраняем в переменную наименование коневой папки
			root_dir = path_from.split('/')[-1]

			# Архивируем директорию
			try:
				zip_(path_to=path_to + "/" + root_dir, path_from=path_from)
			except Exception as e:
				print(f"Error: {e}")
			

def main():
	"""
	
	Главная main функци
	"""

	# Проверка нужно ли делать бэкап или нет
	if check_date():
		# Если нужно сделать бэкап, то вызываем функцию backup()
		backup()


if __name__ == '__main__':
	main()
		