# Завдання 1
# Створіть клас черги для роботи із символьними значеннями. Ви маєте створити реалізації для операцій над
# елементами:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.

from queue import Queue


class CharQueue:
    def __init__(self, size):
        self.size = size
        self.queue = Queue(maxsize=size)

    def is_empty(self):
        return self.queue.empty()

    def is_full(self):
        return self.queue.full()

    def enqueue(self, char):
        if not self.is_full():
            self.queue.put(char)
            print(f"Символ '{char}' додано до черги.")
        else:
            print("Черга повна.")

    def dequeue(self):
        if not self.is_empty():
            char = self.queue.get()
            print(f"Символ '{char}' видалено з черги.")
        else:
            print("Черга порожня.")

    def show(self):
        if self.is_empty():
            print("Черга порожня.")
        else:
            print("Елементи черги:")
            for item in list(self.queue.queue):
                print(item, end=" ")
            print()


def main_menu():
    queue_size = int(input("Введіть розмір черги: "))
    queue = CharQueue(queue_size)

    while True:
        print("\n1. Додати елемент до черги")
        print("2. Видалити елемент з черги")
        print("3. Показати вміст черги")
        print("4. Перевірити, чи черга пуста")
        print("5. Перевірити, чи черга повна")
        print("0. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            if queue.is_full():
                print("Черга повна. Неможливо додати новий елемент.")
            else:
                char = input("Введіть символ для додавання: ")
                queue.enqueue(char)
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.show()
        elif choice == "4":
            print("Черга порожня." if queue.is_empty() else "В черзі є елементи.")
        elif choice == "5":
            print("Черга повна." if queue.is_full() else "В черзі є місце для елементів.")
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")


main_menu()
