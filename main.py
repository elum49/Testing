# Модуль для работы с комплексными числами
# Предоставлен для задания по МДК.01.02

class ComplexNumber:
    """
    Класс для представления и арифметических операций с комплексными числами.
    Комплексное число представлено в виде a + bi, где a - действительная часть, b - мнимая часть.
    """
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # Ошибка: не проверяется, является ли 'other' экземпляром ComplexNumber
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        # Ошибка: не проверяется, является ли 'other' экземпляром ComplexNumber
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        # Ошибка: не проверяется, является ли 'other' экземпляром ComplexNumber
        # Ошибка: неправильная формула умножения комплексных чисел (a+bi) * (c+di) = (ac-bd) + (ad+bc)i
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        # Ошибка: не учитывается знак мнимой части для красивого вывода
        return f"{self.real} + {self.imaginary}i"

    def magnitude(self):
        # Ошибка: неправильная формула (должна быть sqrt(a^2 + b^2))
        return self.real**2 + self.imaginary**2 # Пропущен sqrt

# --- Функция с логической ошибкой ---
def find_largest_magnitude(numbers_list):
    """
    Находит комплексное число с наибольшим модулем (величиной) в списке.
    Возвращает это число.
    """
    if not numbers_list:
        return None # Ошибка: не обрабатывается случай пустого списка в логике цикла

    largest = numbers_list[0]
    for num in numbers_list:
        # Ошибка: используется неправильный метод magnitude (см. класс)
        if num.magnitude() > largest.magnitude():
            largest = num
    return largest

# --- Функция с синтаксической ошибкой ---
def print_summary(real_part, imag_part):
    # Ошибка: синтаксическая ошибка (лишний символ)
    print(f"Действительная часть: {real_part}, Мнимая часть: {imag_part}"
    # Пропущена закрывающая скобка у print

# --- Пример использования (с ошибками) ---
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, -2)
num3 = ComplexNumber(0, 5)

print("Число 1:", num1)
print("Число 2:", num2)
print("Сложение:", num1 + num2)
print("Вычитание:", num1 - num2)
print("Умножение:", num1 * num2)
print("Модуль числа 1:", num1.magnitude())

numbers = [num1, num2, num3]
largest_num = find_largest_magnitude(numbers)
print("Число с наибольшим модулем:", largest_num)

# print_summary(10, 20) # Вызовите эту функцию, чтобы увидеть синтаксическую ошибку