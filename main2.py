stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(f'{stack=}')

print(f'Дістанемо останній елемент {stack.pop()}')
print(f'{stack=}')

##############################


from collections import deque


stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(f'{stack=}')

print(f'Дістанемо останній елемент {stack.pop()}')
print(f'{stack=}')

####################################

from queue import LifoQueue

stack = LifoQueue()

stack.put(1)
stack.put(2)
stack.put(3)

print(f'{stack=}')

print(f'Дістанемо останній елемент {stack.get()}')
print(f'{stack=}')

#######################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        self.size += 1

        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError('stack is empty')

        self.size -= 1

        data = self.head.data
        self.head = self.head.next

        return data

    def peek(self):
        if self.head is None:
            raise IndexError('stack is empty')

        return self.head.data

    def get_size(self):
        return self.size

    def print(self):
        node = self.head

        while node:
            print(node.data, end=' ')
            node = node.next
        print()


stack = Stack()

stack.append(1)
stack.append(2)
stack.append(3)

stack.print()

print(f'Дістанемо останній елемент {stack.pop()}')
stack.print()

print(f'Подивемось на останній елемент {stack.peek()}')
stack.print()

#################################

examples = ['2 + (1-5)', '(2*[10-5] + (8-4))*(2-1)']


def naive(text):
    num_type1 = 0
    num_type2 = 0
    num_type3 = 0

    for char in text:
        if char == '(': num_type1 += 1
        elif char == '{': num_type2 += 1
        elif char == '[': num_type3 += 1

        if char == ')':
            if num_type1 == 0:
                return False
            else:
                num_type1 -= 1

        elif char == '}':
            if num_type2 == 0:
                return False
            else:
                num_type2 -= 1

        elif char == ']':
            if num_type3 == 0:
                return False
            else:
                num_type3 -= 1

    return num_type1 == 0 and num_type2 == 0 and num_type3 == 0


def check_with_stack(text):
    stack = []

    for char in text:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if len(stack) == 0:
                return False
            item = stack.pop()
            pair = item + char

            if pair not in ('()', '{}', '[]'):
                return False

    return len(stack) == 0


for example in examples:
    print(f'{example} - {check_with_stack(example)}')

#############################################

def infix_to_postfix(text):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -100}
    charecters = text.split()
    stack = []
    result = ''

    for char in charecters:
        if char.isdigit():
            result += ' ' + char

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack[-1] != '(':
                result += ' ' + stack.pop()

            stack.pop()

        else:
            while stack and priority[stack[-1]] >= priority[char]:
                result += ' ' + stack.pop()

            stack.append(char)

    result += ' ' + ' '.join(stack)

    return result


example = '3 + 4 * ( 2 - 5 )'

print(infix_to_postfix(example))

#######################################

