# Завдання 3
# Дано три вежі та n дисків різного розміру, відсортованих
# за зростанням, розміщених на першій вежі у вигляді піраміди.
# Потрібно перемістити всі диски на третю вежу,
# використовуючи проміжну вежу, за умови, що можна
# переміщати тільки один диск за раз та диск завжди можна
# покласти лише на диск більшого розміру або на порожню
# вежу.
# Ця задача може бути вирішена за допомогою
# рекурсивного алгоритму, використовуючи стек для
# зберігання проміжних ходів при переміщенні дисків між
# вежами.
def hanoi_with_stack(n, source, helping, target, moves=None):
    if moves is None:
        moves = []

    if n == 1:
        moves.append((source, target))
        print(f"Перемістити диск 1 з вежі {source} на вежу {target}")
    else:
        hanoi_with_stack(n - 1, source, target, helping, moves)
        moves.append((source, target))
        print(f"Перемістити диск {n} з вежі {source} на вежу {target}")
        hanoi_with_stack(n - 1, helping, source, target, moves)

    return moves


hanoi_moves = hanoi_with_stack(5, 'A', 'B', 'C')
print(hanoi_moves)


