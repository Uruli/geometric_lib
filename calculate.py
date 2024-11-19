"""Импортируем модули для работы с кругом и квадратом."""
import circle
import square
import triangle


"""Список доступных фигур и функций."""
figs = ['circle', 'square']
"""Список доступных функций для вычислений."""
funcs = ['perimeter', 'area', 'triangle']
sizes = {
	'circle-area': 1, 'circle-perimeter': 1,
    'square-area': 1, 'square-perimeter': 1,
    'triangle-area': 3, 'triangle-perimeter': 3
}


def calc(fig, func, size):
	"""
    Функция для вычисления периметра или площади фигуры.

    Параметры:
    fig (str): Название фигуры ('circle' или 'square', 'triangle').
    func (str): Название функции ('perimeter' или 'area').
    size (list): Список размеров фигуры.

    Возвращает:
    Результат вычисления периметра или площади фигуры.
    """

	assert fig in figs 
	"""Проверка, что фигура доступна."""

	assert func in funcs
	"""Проверка, что фигура доступна."""

	# Проверка на количество аргументов.
	key = f'{fig}-{func}'
	expected_args = sizes.get(key)
	assert expected_args is not None
	assert len(size) == expected_args

	# Проверка на положительные аргументы.
	assert all(s >= 0 for s in size)

	# Проверка, что треугольник существует.
	if fig == 'triangle':
		a, b, c = size
		assert a + b > c and a + c > b and c + b > a

	"""Вычисляем результат с помощью eval,
	  передавая размеры в качестве аргументов."""
	result = eval(f'{fig}.{func}(*{size})')
	"""Выводим результат."""
	return result


if __name__ == "__main__":
	"""Инициализируем переменные для
	хранения ввода пользователя."""
	func = ''
	fig = ''
	size = list()
    
	"""Ввод названия фигуры."""
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")

	"""Ввод названия фигуры."""
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")

	"""Ввод названия фигуры."""
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

	"""Вызов функции для вычисления и вывода результата."""
	calc(fig, func, size)
	"""Описание:
	Функция для вычисления периметра или площади фигуры.

	Аргументы:
	fig (str): Название фигуры ('circle' или 'square').
	func (str): Название функции ('perimeter' или 'area').
	size (list): Список размеров фигуры.
	"""