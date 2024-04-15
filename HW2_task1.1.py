# Завдання 1, 2
# Реалізуйте клас стеку для роботи з рядками (стек рядків).
# Стек має бути фіксованого розміру. Реалізуйте набір операцій
# для роботи зі стеком:
# o розміщення рядка у стек;
# o виштовхування рядка зі стеку;
# o підрахунок кількості рядків у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього рядка зі стеку.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.
class StringStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
        self.peeked_item = 0

    def push(self, string):
        if not self.is_full():
            self.stack.append(string)
        else:
            print("Стек повний!")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Стек порожній!")
            return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity if self.capacity != 0 else False

    def clear(self):
        self.stack.clear()

    def peek(self):
        if not self.is_empty():
            return self.stack[self.peeked_item]
        else:
            print("Стек порожній!")
            return None


def main():
    while True:
        try:
            capacity = int(input("Введіть максимальну місткість стеку (введіть 0 для необмеженого розміру): "))
            if capacity >= 0:
                break
            else:
                print("Місткість стеку не може бути від'ємною")
        except ValueError:
            print("Неправильне значення")
    stack = StringStack(capacity)

    while True:
        print("\n1. Додати рядок до стеку")
        print("2. Видалити рядок зі стеку")
        print("3. Перевірити кількість рядків у стеку")
        print("4. Перевірити, чи порожній стек")
        print("5. Перевірити, чи повний стек")
        print("6. Очистити стек")
        print("7. Показати елемент стеку")
        print("8. Вийти з програми")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            string = input("Введіть рядок для додавання у стек: ")
            stack.push(string)
        elif choice == "2":
            print(f"Видалено: {stack.pop()}")
        elif choice == "3":
            print(f"Кількість рядків у стеку: {stack.size()}")
        elif choice == "4":
            print("Стек порожній." if stack.is_empty() else "Стек не порожній.")
        elif choice == "5":
            print("Стек повний." if stack.is_full() else "Стек не повний.")
        elif choice == "6":
            stack.clear()
            print("Стек очищено.")
        elif choice == "7":
            if capacity != 0 and capacity != 1:
                StringStack.peeked_item = int(input(f"Введіть  номер елементу у стеку від 1 до {capacity}: ")) - 1
                print(f"{StringStack.peeked_item} елемент у стеку {stack.peek()}")
            elif capacity == 1:
                print(f"У стеку лише удин елемент {stack.peek()}")
            elif capacity == 0:
                StringStack.peeked_item = int(input(f"Введіть  номер елементу у стеку: ")) - 1
                print(f"{StringStack.peeked_item - 1} елемент у стеку {stack.peek()}")
        elif choice == "8":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
