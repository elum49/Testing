# Модуль для работы с комплексными числами
# Предоставлен для задания по МДК.01.02

import math

class ComplexNumber:
    """
    Класс для представления и арифметических операций с комплексными числами.
    Комплексное число представлено в виде a + bi, где a - действительная часть, b - мнимая часть.
    """
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # Исправлено: добавлена проверка типа
        if not isinstance(other, ComplexNumber):
            raise TypeError("Операнд должен быть ComplexNumber")
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        # Исправлено: добавлена проверка типа
        if not isinstance(other, ComplexNumber):
            raise TypeError("Операнд должен быть ComplexNumber")
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        # Исправлено: добавлена проверка типа и исправлена формула умножения
        if not isinstance(other, ComplexNumber):
            raise TypeError("Операнд должен быть ComplexNumber")
        # Правильная формула: (a+bi) * (c+di) = (ac-bd) + (ad+bc)i
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        # Исправлено: улучшено форматирование с учетом знака мнимой части
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

    def magnitude(self):
        # Исправлено: правильная формула модуля комплексного числа
        return math.sqrt(self.real**2 + self.imaginary**2)

# --- Исправленная функция с логической ошибкой ---
def find_largest_magnitude(numbers_list):
    """
    Находит комплексное число с наибольшим модулем (величиной) в списке.
    Возвращает это число.
    """
    if not numbers_list:
        return None  # Исправлено: корректная обработка пустого списка

    largest = numbers_list[0]
    for num in numbers_list:
        # Исправлено: используется правильный метод magnitude
        if num.magnitude() > largest.magnitude():
            largest = num
    return largest

# --- Исправленная функция с синтаксической ошибкой ---
def print_summary(real_part, imag_part):
    # Исправлено: добавлена закрывающая скобка
    print(f"Действительная часть: {real_part}, Мнимая часть: {imag_part}")

# --- Пример использования (исправленный) ---
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

# Теперь функция работает корректно
print_summary(10, 20)
