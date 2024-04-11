class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return "Стек пустий. Повернення неможливе."

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return "Стек пустий."

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def main():
    history = Stack()
    pop_history = Stack()
    while True:
        print("\n1. Відвідати сторінку")
        print("2. Назад")
        print("3. Вперед")
        print("3. Поточна сторінка")
        print("4. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            url = input("Введіть URL сторінки: ")
            history.push(url)
            print(f"Відвідано {url}")

        elif choice == "2":
            if not history.is_empty():
                last_page = history.pop()
                pop_history.push(last_page)
                current_page = history.peek()
                print(f"Повернення на: {current_page}")
            else:
                print("Історія відвідувань пуста.")

        elif choice == "3":
            if not pop_history.is_empty():
                next_page = pop_history.pop()
                history.push(next_page)
                print(f"Повернення на попередню сторінку: {next_page}")
            else:
                print("Історія відвідувань пуста.")

        elif choice == "3":
            print(f"Поточна сторінка: {history.peek()}")

        elif choice == "4":
            print("Вихід з програми.")
            break

        else:
            print("Невідома опція.")


if __name__ == "__main__":
    main()
