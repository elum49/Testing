import unittest
import math
from main import ComplexNumber, find_largest_magnitude

class TestComplexNumber(unittest.TestCase):
    
    def test_initialization(self):
        """Тест инициализации комплексного числа"""
        num = ComplexNumber(3, 4)
        self.assertEqual(num.real, 3)
        self.assertEqual(num.imaginary, 4)
    
    def test_str_representation(self):
        """Тест строкового представления"""
        num1 = ComplexNumber(3, 4)
        num2 = ComplexNumber(3, -4)
        num3 = ComplexNumber(0, 5)
        num4 = ComplexNumber(2, 0)
        
        self.assertEqual(str(num1), "3 + 4i")
        self.assertEqual(str(num2), "3 - 4i")
        self.assertEqual(str(num3), "0 + 5i")
        self.assertEqual(str(num4), "2 + 0i")
    
    def test_addition(self):
        """Тест сложения комплексных чисел"""
        num1 = ComplexNumber(3, 4)
        num2 = ComplexNumber(1, -2)
        result = num1 + num2
        
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imaginary, 2)
    
    def test_addition_with_invalid_type(self):
        """Тест сложения с некорректным типом"""
        num1 = ComplexNumber(3, 4)
        with self.assertRaises(TypeError):
            num1 + "invalid"
    
    def test_subtraction(self):
        """Тест вычитания комплексных чисел"""
        num1 = ComplexNumber(5, 6)
        num2 = ComplexNumber(2, 3)
        result = num1 - num2
        
        self.assertEqual(result.real, 3)
        self.assertEqual(result.imaginary, 3)
    
    def test_multiplication(self):
        """Тест умножения комплексных чисел"""
        num1 = ComplexNumber(3, 4)
        num2 = ComplexNumber(1, -2)
        result = num1 * num2
        
        # (3+4i)*(1-2i) = 3*1 + 3*(-2i) + 4i*1 + 4i*(-2i) = 3 -6i +4i -8i² = 3 -2i +8 = 11 -2i
        self.assertEqual(result.real, 11)
        self.assertEqual(result.imaginary, -2)
    
    def test_magnitude(self):
        """Тест расчета модуля"""
        num1 = ComplexNumber(3, 4)
        num2 = ComplexNumber(0, 0)
        num3 = ComplexNumber(-3, -4)
        
        self.assertAlmostEqual(num1.magnitude(), 5.0)
        self.assertAlmostEqual(num2.magnitude(), 0.0)
        self.assertAlmostEqual(num3.magnitude(), 5.0)
    
    def test_edge_cases(self):
        """Тест граничных случаев"""
        # Нулевое число
        zero = ComplexNumber(0, 0)
        self.assertEqual(zero.real, 0)
        self.assertEqual(zero.imaginary, 0)
        self.assertEqual(zero.magnitude(), 0)
        
        # Только действительная часть
        real_only = ComplexNumber(5, 0)
        self.assertEqual(real_only.real, 5)
        self.assertEqual(real_only.imaginary, 0)
        
        # Только мнимая часть
        imag_only = ComplexNumber(0, 5)
        self.assertEqual(imag_only.real, 0)
        self.assertEqual(imag_only.imaginary, 5)

class TestFindLargestMagnitude(unittest.TestCase):
    
    def test_normal_case(self):
        """Тест поиска числа с наибольшим модулем"""
        num1 = ComplexNumber(3, 4)    # модуль = 5
        num2 = ComplexNumber(6, 8)    # модуль = 10
        num3 = ComplexNumber(1, 1)    # модуль ≈ 1.414
        
        numbers = [num1, num2, num3]
        result = find_largest_magnitude(numbers)
        
        self.assertEqual(result.real, 6)
        self.assertEqual(result.imaginary, 8)
    
    def test_empty_list(self):
        """Тест пустого списка"""
        result = find_largest_magnitude([])
        self.assertIsNone(result)
    
    def test_single_element(self):
        """Тест списка с одним элементом"""
        num = ComplexNumber(3, 4)
        result = find_largest_magnitude([num])
        self.assertEqual(result, num)
    
    def test_negative_numbers(self):
        """Тест с отрицательными числами"""
        num1 = ComplexNumber(-3, -4)  # модуль = 5
        num2 = ComplexNumber(-1, -1)  # модуль ≈ 1.414
        num3 = ComplexNumber(-6, -8)  # модуль = 10
        
        numbers = [num1, num2, num3]
        result = find_largest_magnitude(numbers)
        
        self.assertEqual(result.real, -6)
        self.assertEqual(result.imaginary, -8)

if __name__ == '__main__':
    unittest.main()
