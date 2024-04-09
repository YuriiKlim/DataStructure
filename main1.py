class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

print(node1)

####################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next is not None:
            tail = tail.next

        tail.next = new_node


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print(my_list)

######################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node



my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print(my_list)

##############################################

# Клас Node - представляє вузол списку з певними даними та посиланням на наступний (і попередній у двосв'язному) вузол
class Node:
    def __init__(self, data):
        self.data = data  # Зберігаємо дані у вузлі
        self.next = None  # Посилання на наступний вузол у списку
        self.prev = None  # Посилання на попередній вузол у двосв'язному списку


# Клас для черги реєстрації пасажирів
class RegistrationQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next


# Клас для черги посадки пасажирів
class BoardingQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def move_forward(self, data):
        # Знайти node з потрібним data
        node = self.head

        while node is not None and node.data != data:
            node = node.next

        if node is None:
            print('Немає пасажира в черзі')
            return

        # Переміщення вперед

        red = node.prev
        green = node
        blue = node.next
        black = node.next.next # blue.next

        # змінюємо посилання вперед
        red.next, green.next, blue.next = blue, black, green

        # змінюємо посилання назад
        green.prev, blue.prev, black.prev = blue, red, green

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next


my_list = BoardingQueue()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print()
print()

my_list.move_forward(3)
my_list.print()
print()

my_list.move_forward(5)
my_list.print()
print()

###########################################

# Клас Node - представляє вузол списку з певними даними та посиланням на наступний (і попередній у двосв'язному) вузол
class Node:
    def __init__(self, data):
        self.data = data  # Зберігаємо дані у вузлі
        self.next = None  # Посилання на наступний вузол у списку
        self.prev = None  # Посилання на попередній вузол у двосв'язному списку


# Клас для черги реєстрації пасажирів
class RegistrationQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next


# Клас для черги посадки пасажирів
class BoardingQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def move_forward(self, data):
        # Знайти node з потрібним data
        node = self.head

        while node is not None and node.data != data:
            node = node.next

        if node is None:
            print('Немає пасажира в черзі')
            return

        # Переміщення вперед

        red = node.prev
        green = node
        blue = node.next
        black = node.next.next # blue.next

        # змінюємо посилання вперед
        red.next, green.next, blue.next = blue, black, green

        # змінюємо посилання назад
        green.prev, blue.prev, black.prev = blue, red, green

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next


my_list = BoardingQueue()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print()
print()

my_list.move_forward(3)
my_list.print()
print()

my_list.move_forward(5)
my_list.print()
print()

##########################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head

        while node is not None:
            print(node.data, end='->')
            node = node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next is not None:
            tail = tail.next

        tail.next = new_node
        new_node.prev = tail


my_list = DoubleLinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.print()

#######################################

