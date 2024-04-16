# Завдання 2
# Створіть клас черги з пріоритетами для роботи із
# символьними значеннями.
# Ви маєте створити реалізації для операцій над елементами черги:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ InsertWithPriority — додати елемент з пріоритетом у
# чергу;
# ■ PullHighestPriorityElement — видалення елемента з
# найвищим пріоритетом із черги;
# ■ Peek — повернення найбільшого за пріоритетом елемента. Зверніть увагу, що елемент не видаляється з
# черги;
# ■ Show — відображення на екрані всіх елементів черги.
# Показуючи елемент, також необхідно вказати і його
# пріоритет.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.
from queue import PriorityQueue


class PriorityCharQueue:
    def __init__(self, max_size):
        self.queue = PriorityQueue(maxsize=max_size)

    def is_empty(self):
        return self.queue.empty()

    def is_full(self):
        return self.queue.full()

    def insert_with_priority(self, priority, char):
        if not self.is_full():
            self.queue.put((priority, char))
        else:
            print("Черга повна.")

    def pull_highest_priority_element(self):
        if not self.is_empty():
            return self.queue.get()[1]
        else:
            print("Черга порожня.")
            return None

    def peek(self):
        if not self.is_empty():
            item = self.queue.get()
            self.queue.put(item)
            return item[1]
        else:
            print("Черга порожня.")
            return None

    def show(self):
        temp_queue = PriorityQueue(maxsize=self.queue.maxsize)
        print("Вміст черги:")
        while not self.queue.empty():
            item = self.queue.get()
            print(f"Елемент: {item[1]}, Пріоритет: {item[0]}")
            temp_queue.put(item)
        self.queue = temp_queue


def menu():
    max_size = int(input("Введіть максимальний розмір черги: "))
    pq = PriorityCharQueue(max_size)

    while True:
        print("\n1. Додати елемент з пріоритетом")
        print("2. Видалити елемент з найвищим пріоритетом")
        print("3. Показати елемент з найвищим пріоритетом")
        print("4. Показати вміст черги")
        print("5. Перевірити, чи порожня черга")
        print("6. Перевірити, чи повна черга")
        print("0. Вийти")

        choice = int(input("Виберіть опцію: "))

        if choice == 1:
            if pq.is_full():
                print("Черга повна.")
            else:
                element = input("Введіть символ: ")
                priority = int(input("Введіть пріоритет: "))
                pq.insert_with_priority(priority, element)
        elif choice == 2:
            print("Видалено елемент:", pq.pull_highest_priority_element())
        elif choice == 3:
            print("Елемент з найвищим пріоритетом:", pq.peek())
        elif choice == 4:
            pq.show()
        elif choice == 5:
            print("Черга порожня:" if pq.is_empty() else "Черга не порожня")
        elif choice == 6:
            print("Черга повна:" if pq.is_full() else "Черга не повна")
        elif choice == 0:
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")


menu()
