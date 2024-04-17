# Завдання 2
# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний
# час доби;
# 2. Середній час між появою катерів на причалі у різний час
# доби;
# 3. Тип зупинки катера (кінцева або інша).
# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно
import random
from queue import Queue


class Dock:
    def __init__(self, passenger_timing, boat_timing, dock_type):
        self.passenger_timing = passenger_timing
        self.boat_timing = boat_timing
        self.dock_type = dock_type

    def calculate_boat_capacity(self):
        return random.randint(10, 50)

    def average_passenger_timing(self):
        total_wait_time = 0
        count_periods = len(self.passenger_timing)
        for time in self.passenger_timing.values():
            total_wait_time += time
        average_passenger_timing = total_wait_time / count_periods
        return  average_passenger_timing

    def calculate_average_wait_time(self):
        total_boat_time = 0
        count_periods = len(self.passenger_timing)
        average_passenger_timing = self.average_passenger_timing()
        for boat_time in self.boat_timing.values():
            total_boat_time += boat_time
        average_boat_timing = total_boat_time / count_periods
        average_wait = average_boat_timing / average_passenger_timing
        print(f"Середній час очікування на причалі: {average_wait:.2f} хвилин")
        return average_wait

    def optimal_boat_interval(self, max_people):
        self.max_people = max_people
        optimal_intervals = {}
        for period, interval in self.passenger_timing.items():
            time_to_fill_boat = (max(self.max_people, self.calculate_boat_capacity()) * interval)
            optimal_intervals[period] = time_to_fill_boat
        print(f"Оптимальні часи пррибуття{optimal_intervals}")
        return optimal_intervals


passenger_timing = {'Ранок': 5, 'День': 3, 'Вечір': 7, 'Ніч': 15}
boat_timing = {'Ранок': 20, 'День': 15, 'Вечір': 10, 'Ніч': 30}

dock = Dock(passenger_timing, boat_timing, 'Кінцева')
dock.calculate_average_wait_time()
dock.optimal_boat_interval(20)
