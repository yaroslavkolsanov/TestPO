import unittest
from logic import MathExecutor


# class TestDivision(unittest.TestCase):
#     """Тест 1: Проверка операции деления"""
#
#     def test_zero_division(self):
#         executor = MathExecutor(1, ":", 0, False)  # Деление на ноль
#         result = executor.execute()
#         self.assertEqual(result, "Вы попытались поделить на 0. К сожалению, это ещё не определено!")
#
#     def test_str_division(self):
#         executor = MathExecutor(1, ":", 'Два', False)  # Строка вместо числа
#         result = executor.execute()
#         self.assertEqual(result, "Операнд не является числом")
#
#     def test_base_division(self):
#         executor = MathExecutor(2, ":", 1, False)  # Базовое деление
#         result = executor.execute()
#         self.assertEqual(result, "2.0")
#
#     def test_float_division(self):
#         executor = MathExecutor(2, ":", 0.5, False)  # Деление на десятичную дробь
#         result = executor.execute()
#         self.assertEqual(result, "4.0")
#
#     def test_neg_division(self):
#         executor = MathExecutor(10, ":", -5, False)  # Деление на отрицательное число
#         result = executor.execute()
#         self.assertEqual(result, "-2.0")


# class TestTrigonometric(unittest.TestCase):
#     """Тест 2: Проверка тригонометрических функций"""
#
#     def test_not_defined_value(self):
#         executor = MathExecutor(90, "tg", None, True)  # Тангенс 90 градусов не определен
#         result = executor.execute()
#         self.assertEqual(result, "Тангенс не определен")
#
#     def test_str_value(self):
#         executor = MathExecutor("Угол", "ctg", None, True)  # Строка вместо числа
#         result = executor.execute()
#         self.assertEqual(result, "Операнд не является числом")
#
#     def test_neg_degree(self):
#         executor = MathExecutor(-30, "cos", None, True)  # Косинус отрицательного угла
#         result = executor.execute()
#         self.assertEqual(round(float(result), 3), round(3 ** 0.5 / 2, 3))
#
#     def test_base_func_value(self):
#         executor = MathExecutor(30, "sin", None, True)  # Синус обычного угла
#         result = executor.execute()
#         self.assertEqual(round(float(result), 1), 0.5)
#
#     def test_period_func_value(self):
#         executor_1 = MathExecutor(30, "cos", None, True)  # Косинус обычного угла
#         executor_2 = MathExecutor(30 + 360, "cos", None, True)  # Косинус обычного угла с периодом 2pi
#         result_1 = executor_1.execute()
#         result_2 = executor_2.execute()
#         self.assertEqual(round(float(result_1), 3), round(float(result_2), 3))
#
#
# class TestFactorial(unittest.TestCase):
#     """Тест 3: Проверка факториала числа"""
#
#     def test_factorial_of_null(self):
#         executor = MathExecutor(0, "n!", None, False)  # Факториал нуля
#         result = executor.execute()
#         self.assertEqual(result, "1")
#
#     def test_factorial_of_str_value(self):
#         executor = MathExecutor("Число", "n!", None, True)  # Строка вместо числа
#         result = executor.execute()
#         self.assertEqual(result, "Операнд не является целочисленным числом (integer)")
#
#     def test_factorial_of_neg(self):
#         executor = MathExecutor(-5, "n!", None, False)  # Факториал отрицательного числа
#         result = executor.execute()
#         self.assertEqual(result, "Операнд не является целочисленным числом (integer)")
#
#     def test_base_factorial(self):
#         executor = MathExecutor(5, "n!", None, False)  # Факториал натурального числа
#         result = executor.execute()
#         self.assertEqual(result, "120")
#
#
# class TestPercents(unittest.TestCase):
#     """Тест 4: Проверка перевода числа в проценты"""
#
#     def test_str_value_percents(self):
#         executor = MathExecutor("Процент", "%", None, False)  # Строка вместо числа
#         result = executor.execute()
#         self.assertEqual(result, "Операнд не является числом")
#
#     def test_float_value_percents(self):
#         executor = MathExecutor(0.5, "%", None, False)  # Десятичная дробь
#         result = executor.execute()
#         self.assertEqual(result, "50.0%")
#
#     def test_natural_value_percents(self):
#         executor = MathExecutor(10, "%", None, False)  # Обычное число
#         result = executor.execute()
#         self.assertEqual(result, "1000.0%")
#
#     def test_null_value_percents(self):
#         executor_3 = MathExecutor(0, "%", None, False)  # Ноль
#         result_3 = executor_3.execute()
#         self.assertEqual(result_3, "0.0%")
#
#     def test_neg_value_percents(self):
#         executor_4 = MathExecutor(-0.5, "%", None, False)  # Отрицательное число
#         result_4 = executor_4.execute()
#         self.assertEqual(result_4, "-50.0%")
#

class TestDecimalSystem(unittest.TestCase):
    """Тест 5: Проверка перевода числа в десятичную систему счисления"""

    def test_str_value_percents(self):
        executor = MathExecutor("Двоичное число", "n to10", 2, False)  # Строка вместо числа
        result = executor.execute()
        self.assertEqual(result, "Операнд не является целочисленным числом (integer) "
                                 "или такое число невозможно в данной системе")

    def test_natural_value_from_binary_to_decimal_system(self):
        executor = MathExecutor(10, "n to10", 2, False)  # Обычное двоичное число
        result = executor.execute()
        self.assertEqual(result, "2")

    def test_natural_value_from_decimal_to_binary_system(self):
        executor = MathExecutor(10, "n to10", 10, False)  # Десятичное число
        result = executor.execute()
        self.assertEqual(result, "10")

    def test_neg_value_from_binary_to_decimal_system(self):
        executor_3 = MathExecutor(-10, "n to10", 2, False)  # Отрицательное двоичное число
        result_3 = executor_3.execute()
        self.assertEqual(result_3, "-2")

    def test_float_value_from_binary_to_decimal_system(self):
        executor_4 = MathExecutor(10.11, "n to10", 2, False)  # Двоичное дробное число
        result_4 = executor_4.execute()
        self.assertEqual(result_4, "2.75")


if __name__ == '__main__':
    unittest.main()
