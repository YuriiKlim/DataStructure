# Завдання
# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача,
# покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи
# замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після
# чого меню з’являється знову.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.find(data):
            print(f"Число {data} вже існує у списку.")
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                temp = current
                current = current.next
                del temp
            else:
                current = current.next

    def show(self, reverse=False):
        if reverse:
            current = self.tail
            while current:
                print(current.data, end=" ")
                current = current.prev
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
        print()

    def replace(self, old_data, new_data, replace_all=False):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                if not replace_all:
                    return
            current = current.next


def menu():
    dll = DoublyLinkedList()
    while True:
        try:
            numbers = input("Введіть набір чисел, розділених пробілом: ").split()
            for num in numbers:
                dll.append(int(num))
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
                    dll.append(data)
                    break
                except:
                    print("Введіть лише числа")

        elif choice == "2":
            while True:
                try:
                    data = int(input("Введіть елемент для видалення: "))
                    if not dll.delete(data):
                        print("Елемент не знайдено.")
                    break
                except:
                    print("Введіть лише числа")

        elif choice == "3":
            while True:
                reverse = input("Показати список з кінця? (y/n): ").lower()
                if reverse == "y":
                    dll.show(reverse)
                    break
                elif reverse == "n":
                    dll.show()
                    break
                else:
                    print("Невірний вибір")

        elif choice == "4":
            while True:
                try:
                    data = int(input("Введіть елемент для перевірки: "))
                    print(
                        f"Так, {data} міститься у списку" if dll.find(data) else f"Ні, {data} не міститься у списку")
                    break
                except:
                    print("Введіть лише числа")

        elif choice == "5":
            while True:
                try:
                    old_data = int(input("Введіть елемент для заміни: "))
                    new_data = int(input("Введіть новий елемент: "))
                    if not dll.replace(old_data, new_data):
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
