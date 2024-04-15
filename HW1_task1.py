from queue import LifoQueue


class StringStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = LifoQueue(maxsize=capacity)
        self.temp_stack = LifoQueue(maxsize=capacity)

    def push(self, string):
        if not self.stack.full():
            self.stack.put_nowait(string)
        else:
            print("Стек повний!")

    def pop(self):
        try:
            return self.stack.get_nowait()
        except self.stack.empty():
            print("Стек порожній!")
            return None

    def size(self):
        return self.stack.qsize()

    def is_empty(self):
        return self.stack.empty()

    def is_full(self):
        return self.stack.full() if self.capacity != 0 else False

    def clear(self):
        while not self.stack.empty():
            self.stack.get()

    def peek(self):
        if not self.is_empty():
            item = self.stack.get()
            self.stack.put(item)
            return item
        print("Стек порожній!")
        return None

    def get_specific_item(self, index):
        if index < 0 or index >= self.size():
            print("Індекс поза межами стеку.")
            return None
        for _ in range(index -1):
            self.temp_stack.put_nowait(self.stack.get_nowait())

        item = self.stack.get_nowait()
        print(f"Елемент на індексі {index}: {item}")

        self.stack.put_nowait(item)
        while not self.temp_stack.empty():
            self.stack.put_nowait(self.temp_stack.get_nowait())

        return item


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
        print("3. Показати вміст стеку")
        print("4. Перевірити, чи порожній стек")
        print("5. Перевірити, чи повний стек")
        print("6. Очистити стек")
        print("7. Показати верхній елемент")
        print("8. Отримати елемент за індексом")
        print("9. Вийти з програми")

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
            print(f"Верхній елемент: {stack.peek()}")
        elif choice == "8":
            while True:
                try:
                    index = int(input("Введіть індекс елемента для отримання: "))
                    break
                except ValueError:
                    print("Неправильне значення")
            stack.get_specific_item(index)
        elif choice == "9":
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте знову.")


if __name__ == "__main__":
    main()
