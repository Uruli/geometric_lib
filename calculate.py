'''Импортируем модули для работы с кругом и квадратом'''
import circle
import square

'''Список доступных фигур и функций'''
figs = ['circle', 'square']
'''Список доступных функций для вычислений'''
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''
    Функция для вычисления периметра или площади фигуры.

    Параметры:
    fig (str): Название фигуры ('circle' или 'square').
    func (str): Название функции ('perimeter' или 'area').
    size (list): Список размеров фигуры.

    Возвращает:
    None: Выводит результат вычисления на экран.
    '''
	assert fig in figs 
	'''Проверка, что фигура доступна'''
	assert func in funcs
	'''Проверка, что фигура доступна'''
	'''Вычисляем результат с помощью eval,
	  передавая размеры в качестве аргументов'''
	result = eval(f'{fig}.{func}(*{size})')
	'''Выводим результат на экран'''
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	'''Инициализируем переменные для
	хранения ввода пользователя'''
	func = ''
	fig = ''
	size = list()
    
	'''Ввод названия фигуры'''
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	'''Ввод названия фигуры'''
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	'''Ввод названия фигуры'''
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	'''Вызов функции для вычисления и вывода результата'''
	calc(fig, func, size)
	'''Описание:
	Функция для вычисления периметра или площади фигуры.

	Аргументы:
	fig (str): Название фигуры ('circle' или 'square').
	func (str): Название функции ('perimeter' или 'area').
	size (list): Список размеров фигуры.

	Возвращает: None'''



