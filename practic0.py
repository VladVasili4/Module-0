
# Задача 1: Арифметика
# Возводим число 9 в степень 0.5 и умножаем на 5
print(9 ** 0.5 * 5)


# Задача 2: Логика
# Проверяем, что 9.99 больше 9.98 и 1000 не равно 1000.1
print(9.99 > 9.98 and 1000 != 1000.1)


# Задача 3: Школьная загадка
# 2 * 2 + 2 без приоритета
print(2 * 2 + 2)
# 2 * 2 + 2 с приоритетом для сложения
print(2 * (2 + 2))
# Сравниваем оба результата
print((2 * 2 + 2) == (2 * (2 + 2)))


# Задача 4: Первый после точки
# Дана строка '123.456'
s = '123.456'
# Преобразуем строку в число с плавающей точкой
num = float(s)
# Умножаем на 10, чтобы сдвинуть дробную часть
num *= 10
# Получаем целую часть после умножения, чтобы отделить первую цифру после запятой
first_digit = int(num) % 10
print(first_digit)