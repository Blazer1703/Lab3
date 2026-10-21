# Задание 1
# def greet(name):
#     print(f"Здравствуйте, {name}!")

# def square(number):
#     return number ** 2

# def max_of_two(a, b):
#     if a > b:
#         return a
#     return b

# greet("Иван")
# greet("Анна")
# print("Квадрат:", square(4), square(7))
# print("Максимум:", max_of_two(10, 5), max_of_two(3, 8))

# Задание 2
# def calculate_rectangle(width, height):
#     return width * height

# def calculate_perimeter(width, height):
#     return 2 * (width + height)

# def describe_rectangle(width, height, unit="см"):
#     area = calculate_rectangle(width, height)
#     print(f"Прямоугольник {width}x{height}. Площадь: {area} {unit}²")

# describe_rectangle(5, 10)
# describe_rectangle(5, 10, "м")

# Задание 3
# value = 10

# def example():
#     value = 20
#     local_var = "Секрет"
#     print("Внутри функции:", value)

# example()
# print("Вне функции:", value)
# print(local_var)

# Задание 4
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print("Первый, третий, последний:", nums[0], nums[2], nums[-1])

# nums[1] = 999
# nums.append(200)
# nums.remove(40) # или nums.pop()

# print("Итог:", nums, "| Элементов:", len(nums))

# Задание 5
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Первые три:", numbers[:3])
# print("Последние три:", numbers[-3:])
# print("С 3-го по 7-й:", numbers[2:7]) 
# print("Каждый второй:", numbers[::2])
# print("В обратном порядке:", numbers[::-1])

# Задание 6
# measurements = (12.5, 14.1, 10.0, 9.8, 15.2, 11.4, 13.0, 12.1)
# print("Первый и последний:", measurements[0], measurements[-1])
# print("Срез:", measurements[2:5])

# val1, val2 = measurements[:2]

# temp_list = list(measurements)
# temp_list[0] = 99.9
# measurements = tuple(temp_list)

# measurements[0] = 99.9

# Задание 7
# nums = [15, 2, 8, 24, 5]
# print(f"Кол-во: {len(nums)}, Сумма: {sum(nums)}")
# print(f"Мин: {min(nums)}, Макс: {max(nums)}, Среднее: {sum(nums)/len(nums)}")

# sorted_copy = sorted(nums)
# nums.sort()

# Задание 8
# def calculate_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# def find_min(numbers):
#     minimum = numbers[0]
#     for num in numbers:
#         if num < minimum:
#             minimum = num
#     return minimum

# def find_max(numbers):
#     maximum = numbers[0]
#     for num in numbers:
#         if num > maximum:
#             maximum = num
#     return maximum

# # Тестовый список
# my_numbers = [15, 3, 8, 42, 4, 23, 16]

# # Вывод результатов работы собственных функций
# print("--- Собственные функции ---")
# print("Сумма:", calculate_sum(my_numbers))
# print("Минимум:", find_min(my_numbers))
# print("Максимум:", find_max(my_numbers))

# # Вывод результатов встроенных функций Python для сравнения
# print("\n--- Встроенные функции Python ---")
# print("Сумма (sum):", sum(my_numbers))
# print("Минимум (min):", min(my_numbers))
# print("Максимум (max):", max(my_numbers))

# Задание 9
# def find_element(numbers, target):
#     for index, value in enumerate(numbers):
#         if value == target:
#             return index
#     return -1

# print("Индекс числа 20:", find_element([10, 20, 30], 20))
# print("Индекс числа 99:", find_element([10, 20, 30], 99))

# Задание 10
# def analyze(numbers):
#     return min(numbers), max(numbers), sum(numbers)/len(numbers)

# minimum, maximum, average = analyze([10, 20, 30, 40])
# print(f"Мин: {minimum}, Макс: {maximum}, Сред: {average}")

# Задание 11
# numbers = [-10, 32, 8, -5]
# print("Обычная сортировка:", sorted(numbers))
# print("По модулю:", sorted(numbers, key=lambda x: abs(x)))

# Задание 12
# def calculate_average(measurements):
#     s = 0
#     for m in measurements: s += m
#     return s / len(measurements)

# def find_minimum(measurements):
#     m = measurements[0]
#     for val in measurements:
#         if val < m: m = val
#     return m

# def find_maximum(measurements):
#     m = measurements[0]
#     for val in measurements:
#         if val > m: m = val
#     return m

# def count_above_average(measurements):
#     avg = calculate_average(measurements)
#     count = 0
#     for val in measurements:
#         if val > avg: count += 1
#     return count

# def find_value(measurements, target):
#     for i in range(len(measurements)):
#         if measurements[i] == target: return i
#     return -1

# def analyze_measurements(measurements):
#     return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)

# data = [12.0, 15.5, 8.2, 22.1, 14.0, 10.0, 9.8, 18.4, 20.1, 11.0]

# print("Всего измерений:", len(data))
# min_v, max_v, avg_v = analyze_measurements(data)
# print(f"Мин: {min_v} | Макс: {max_v} | Среднее: {avg_v:.2f}")
# print("Значений выше среднего:", count_above_average(data))
# print("Индекс значения 14.0:", find_value(data, 14.0))