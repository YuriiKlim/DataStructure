# Завдання 1
# Реалізуйте базу даних зі штрафами податкової
# інспекції. Ідентифікувати кожну конкретну людину буде
# персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання
from bintrees import AVLTree


class TaxFineDatabase:
    def __init__(self):
        self.data = AVLTree()

    def print_all(self):#1
        for id_code, info in self.data.items():
            print(f"Код: {id_code}, Інформація: {info['personal_info']}, Штрафи: {info['fines']}")

    def print_by_code(self, id_code):#2
        if id_code in self.data:
            info = self.data[id_code]
            print(f"Код: {id_code}, Інформація: {info['personal_info']}, Штрафи: {info['fines']}")
        else:
            print("Особу не знайдено.")

    def print_by_fine_type(self, fine_type):#3
        for id_code, info in self.data.items():
            fines = [fine for fine in info['fines'] if fine['type'] == fine_type]
            if fines:
                print(f"Код: {id_code}, Штрафи: {fines}")

    def print_by_city(self, city):#4
        for id_code, info in self.data.items():
            if info['personal_info']['city'] == city:
                print(f"Код: {id_code}, Інформація: {info['personal_info']}, Штрафи: {info['fines']}")

    def add_person(self, id_code, personal_info):#5
        if id_code not in self.data:
            self.data[id_code] = {'personal_info': personal_info, 'fines': []}
            print("Нова особа додана.")
        else:
            print("Особа з таким кодом уже існує.")

    def add_fine(self, id_code, fine_info):#6
        if id_code in self.data:
            self.data[id_code]['fines'].append(fine_info)
            print("Штраф додано.")
        else:
            print("Особу не знайдено.")

    def delete_fine(self, id_code, fine_index):#7
        if id_code in self.data and len(self.data[id_code]['fines']) > fine_index:
            del self.data[id_code]['fines'][fine_index]
            print("Штраф видалено.")
        else:
            print("Штраф або особу не знайдено.")

    def update_person_info(self, id_code, new_info):#8.1
        if id_code in self.data:
            self.data[id_code]['personal_info'] = new_info
            print("Особиста інформація оновлена.")
        else:
            print("Особу не знайдено.")

    def update_fine(self, id_code, fine_index, new_fine_info):#8.2
        if id_code in self.data and 0 <= fine_index < len(self.data[id_code]['fines']):
            self.data[id_code]['fines'][fine_index] = new_fine_info
            print("Штраф оновлено.")
        else:
            print("Штраф або особу не знайдено.")


def main_menu():
    db = TaxFineDatabase()
    db.add_person('0001', {'name': 'Юрій Клім', 'city': 'Тернопіль'})
    db.add_fine('0001', {'type': 'перевищення швидкості', 'amount': 500})
    while True:
        print("\n1. Повний друк бази даних")
        print("2. Друк даних за конкретним кодом")
        print("3. Друк даних за конкретним типом штрафу")
        print("4. Друк даних за конкретним містом")
        print("5. Додавання нової людини з інформацією про неї")
        print("6. Додавання нових штрафів для вже існуючого запису")
        print("7. Видалення штрафу;")
        print("8. Заміна інформації про людину та її штрафи")
        print("enter для виходу")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            db.print_all()
        elif choice == "2":
            db.print_by_code(input("Введіть ID"))
        elif choice == "3":
            db.print_by_fine_type(input("Введіть тип штрафу"))
        elif choice == "4":
            db.print_by_city(input("Введіть місто"))
        elif choice == "5":
            db.add_person(input("Введіть ID"), {'name': input("Введіть ім'я"), 'city': input("Введіть місто")})
        elif choice == "6":
            db.add_fine(input("Введіть ID"), {'type': input("Введіть тип штрафу"), 'amount': input("Введіть суму штрафу")})
        elif choice == "7":
            while True:
                try:
                    db.delete_fine(input("Введіть ID"), int(input("Введьть номер штрафу"))-1)
                    break
                except: print("Неправильне значення номеру!")
        elif choice == "8":
            id_code = input("Введіть ID: ")
            new_info = {'name': input("Введіть ім'я: "), 'city': input("Введіть місто: ")}
            db.update_person_info(id_code, new_info)

            if id_code in db.data and db.data[id_code]['fines']:
                print("Існуючі штрафи:")
                for idx, fine in enumerate(db.data[id_code]['fines'], start=1):
                    print(f"{idx}. Тип: {fine['type']}, Сума: {fine['amount']}")

                while True:
                    try:
                        fine_input = int(
                            input("Введіть номер штрафу для оновлення (0 - якщо не бажаєте оновлювати штрафи): "))
                        if fine_input == 0:
                            break
                        if 0 < fine_input <= len(db.data[id_code]['fines']):
                            fine_choice = fine_input - 1
                            new_type = input("Введіть новий тип штрафу: ")
                            new_amount = float(input("Введіть нову суму штрафу: "))
                            new_fine_info = {'type': new_type, 'amount': new_amount}
                            db.update_fine(id_code, fine_choice, new_fine_info)
                            break
                        else:
                            print("Невірний номер штрафу.")
                    except ValueError:
                        print("Неправильне значення, спробуйте ще раз.")
            else:
                print("Штрафи відсутні або особу не знайдено.")
        elif choice == "":
            break
        else:
            print("Невірний вибір")


main_menu()


