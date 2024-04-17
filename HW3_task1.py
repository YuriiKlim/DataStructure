# Завдання 1
# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.
from queue import PriorityQueue
import time


class ServerQueue:
    def __init__(self):
        self.requests = PriorityQueue()
        self.stats = []

    def add_request(self, client_name, priority):
        request_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.requests.put((priority, client_name, request_time))
        self.stats.append((client_name, request_time))

    def process_request(self):
        if not self.requests.empty():
            priority, client_name, request_time = self.requests.get()
            print(f"Оброблено запит: {client_name} час: {request_time} з пріоритетом: {priority}")
        else:
            print("Черга запитів порожня.")

    def show_statistics(self):
        print("Статистика запитів:")
        for client_name, request_time in self.stats:
            print(f"Клієнт: {client_name}, Час запиту: {request_time}")


server = ServerQueue()


server.add_request('Клієнт1', 1)
server.add_request('Клієнт2', 2)
server.add_request('Клієнт3', 3)


server.process_request()
server.process_request()


server.show_statistics()
