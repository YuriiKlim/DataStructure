# Завдання 1
# Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
# чого покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def remove(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return True
            current = current.next
        return False


def menu():
    ll = LinkedList()
    while True:
        try:
            numbers = input("Введіть набір чисел, розділених пробілом: ").split()
            for num in numbers:
                ll.append(int(num))
            break
        except:
            print("Введіть лише числа")


    while True:
        print("\n1. Додати елемент до списку.")
        print("2. Видалити елемент зі списку.")
        print("3. Показати вміст списку.")
        print("4. Перевірити, чи є значення у списку.")
        print("5. Замінити значення у списку.")
        print("6. Вийти.")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            while True:
                try:
                    data = int(input("Введіть елемент для додавання: "))
                    ll.append(data)
                    break
                except:
                    print("Введіть лише числа")
        elif choice == "2":
            while True:
                try:
                    data = int(input("Введіть елемент для видалення: "))
                    if not ll.remove(data):
                        print("Елемент не знайдено.")
                    break
                except:
                    print("Введіть лише числа")
        elif choice == "3":
            ll.show()
        elif choice == "4":
            while True:
                try:
                    data = int(input("Введіть елемент для перевірки: "))
                    print(
                        f"Так, {data} міститься у списку" if ll.contains(data) else f"Ні, {data} не міститься у списку")
                    break
                except:
                    print("Введіть лише числа")

        elif choice == "5":
            while True:
                try:
                    old_data = int(input("Введіть елемент для заміни: "))
                    new_data = int(input("Введіть новий елемент: "))
                    if not ll.replace(old_data, new_data):
                        print("Елемент для заміни не знайдено.")
                    break
                except:
                    print("Введіть лише числа")
        elif choice == "6":
            break
        else:
            print("Невідомий вибір.")


if __name__ == "__main__":
    menu()
