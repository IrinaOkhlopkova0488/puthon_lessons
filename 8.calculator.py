# *** Пример. Калькулятор ***


# * Алгорим работы разработки калькулятора *

# - функция-обработчик
# - цикл программы
# - ввод данных
# - обработка данных
# - вывод данных 


# функция-обработчик
def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    else:
        result = f"что это такое: {op}? :("

    return result

# цикл программы
while True:
    # ввод данных
    command = input("введите команду ")
    if command == "стоп":
        print("Buy buy!")
        break
    
    num_1 = int(input("введите 1 число: "))
    num_2 = int(input("введите 2 число: "))
    op = input("введите символ операции: ")

    # обработка данных
    result = calculate(num_1, num_2, op)

    #  вывод данных
    print(f"результат: {result}")


