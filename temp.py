import math

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return math.sqrt(Number)


def calc(your_number):
    """Check inserted number and call CalculateSquareRoot func."""
    if your_number <= 0:
        return 0
    root = CalculateSquareRoot(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


print(message)
calc(25.5)
