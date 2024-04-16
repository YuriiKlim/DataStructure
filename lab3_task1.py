# 1. Система обробки замовлень в ресторані:
# Черга для зберігання замовлень в ресторані,
# де замовлення обробляються за порядком їх надходження.
from queue import Queue


class OrderSystem:
    def __init__(self):
        self.orders = Queue()

    def place_order(self, order_details):
        self.orders.put(order_details)
        print(f"Замовлення прийнято: {order_details}")

    def process_order(self):
        if not self.orders.empty():
            current_order = self.orders.get()
            print(f"Замовлення оброблено: {current_order}")
        else:
            print("Немає замовлень для обробки.")

    def show_orders(self):
        print("Замовлення в черзі:")
        for order in list(self.orders.queue):
            print(order)


restaurant_orders = OrderSystem()


restaurant_orders.place_order("Піца Маргарита")
restaurant_orders.place_order("Салат Цезар")
restaurant_orders.show_orders()
restaurant_orders.process_order()
restaurant_orders.process_order()
restaurant_orders.process_order()
