# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с
# единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно
# два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_columns):
    for x in range(1, num_rows+1):
        for y in range (1, num_columns+1):
            print(*list(map(operation, [x],[y])), end=' ')
        print()
operation = lambda x,y: x * y
print_operation_table(operation, 6, 6)












# # sum (lambda x, y: x + y, 4, 6)
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# print(res) # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))

