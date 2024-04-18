from queue import Queue
from queue import PriorityQueue


# queue = Queue()
#
# queue.put(1)
# queue.put(2)
# queue.put(3)
#
# print(queue.get())
# print(queue.get())
# print(queue.get())
# print(queue.empty())

###############################

# class BankQueue:
#     def __init__(self):
#         self.queue = Queue()
#
#     def put_client(self, client):
#         self.queue.put(client)
#         print(f"{client} is come")
#
#     def serve_next_client(self):
#         if self.queue.empty():
#             print("no clients")
#             return None
#
#         client = self.queue.get()
#
#         print(f"you serve client {client}")
#
#     def number_clients(self):
#         return self.queue.qsize()
#
#     def is_empty_queue(self):
#         return self.queue.empty()
#
#     def print(self):
#         temp_queue = Queue()
#
#         while not self.queue.empty():
#             client = self.queue.get()
#             print(client, end=' -> ')
#
#         print()
#         self.queue = temp_queue
#
#
# bank_clients = BankQueue()
# bank_clients.put_client("mary")
# bank_clients.put_client("sofy")
# bank_clients.print()
#
# bank_clients.serve_next_client()
# bank_clients.print()
# bank_clients.put_client("max")
# bank_clients.print()
# bank_clients.serve_next_client()
# bank_clients.serve_next_client()
# bank_clients.serve_next_client()
# bank_clients.print()

#################################################

queue = PriorityQueue()

queue.put((1, "Mary"))
queue.put((3, "Sophy"))
queue.put((2, "John"))
queue.put((2, "Max"))
queue.put((2, "Julia"))

while not queue.empty():
    priority, client = queue.get()
    print(client, priority)

##################################################

class TaskSolver:
    def __init__(self):
        self.queue = PriorityQueue()

    def add_task(self, task, priority):
        self.queue.put((priority, task))

    def solve_next_task(self):
        if self.queue.empty():
            print("Всі завдання виконані")
            return

        priority, task = self.queue.get()

        print(f'Виконую {task}')


solver = TaskSolver()

solver.add_task('Завдання 2', 2)
solver.add_task('Завдання 3', 3)
solver.add_task('Завдання 1', 1)

solver.solve_next_task()
solver.solve_next_task()
solver.solve_next_task()

#############################################


