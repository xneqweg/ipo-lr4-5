# Запрашиваем число
n = int(input("Введите число: "))

# Инициализируем сумму
sum = 0

# Используем цикл for для нахождения суммы чисел от 1 до n
for i in range(1, n + 1):
    sum += i

print("Сумма всех чисел от 1 до", n, "равна", sum)