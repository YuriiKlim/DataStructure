# Завдання 3
# Розробіть додаток, який дозволяє зберігати інформацію
# про логіни і паролі користувачів. Кожному користувачеві
# відповідає пара «логін — пароль». При старті додатку
# відображається меню:
# ■ Додати нового користувача;
# ■ Видалити існуючого користувача;
# ■ Перевірити, чи існує такий користувач;
# ■ Змінити логін існуючого користувача;
# ■ Змінити пароль існуючого користувача.
# Для реалізації завдання обов’язково застосуйте одну
# із структур даних. При виборі структури керуйтеся постановкою завдання.
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, login, password):
        if login in self.users:
            print("Користувач вже існує.")
        else:
            self.users[login] = password
            print("Новий користувач доданий.")

    def delete_user(self, login):
        if login in self.users:
            del self.users[login]
            print("Користувач видалений.")
        else:
            print("Користувач не знайдений.")

    def check_user_exists(self, login):
        if login in self.users:
            print("Користувач існує.")
        else:
            print("Користувач не знайдений.")

    def change_login(self, old_login, new_login):
        if old_login in self.users:
            if new_login in self.users:
                print("Новий логін вже використовується.")
            else:
                self.users[new_login] = self.users.pop(old_login)
                print("Логін змінено.")
        else:
            print("Старий логін не знайдений.")

    def change_password(self, login, new_password):
        if login in self.users:
            if new_password in self.users:
                print("Новий пароль вже використовується.")
            else:
                self.users[login] = new_password
                print("Пароль змінено.")
        else:
            print("Користувач не знайдений.")

    def menu(self):
        while True:
            print("\nМеню:")
            print("1. Додати нового користувача")
            print("2. Видалити існуючого користувача")
            print("3. Перевірити, чи існує такий користувач")
            print("4. Змінити логін існуючого користувача")
            print("5. Змінити пароль існуючого користувача")
            print("0. Вихід")

            choice = input("Виберіть опцію: ")
            if choice == "1":
                login = input("Введіть логін: ")
                password = input("Введіть пароль: ")
                self.add_user(login, password)
            elif choice == "2":
                login = input("Введіть логін для видалення: ")
                self.delete_user(login)
            elif choice == "3":
                login = input("Введіть логін для перевірки: ")
                self.check_user_exists(login)
            elif choice == "4":
                old_login = input("Введіть поточний логін: ")
                new_login = input("Введіть новий логін: ")
                self.change_login(old_login, new_login)
            elif choice == "5":
                login = input("Введіть логін: ")
                new_password = input("Введіть новий пароль: ")
                self.change_password(login, new_password)
            elif choice == "0":
                print("Вихід із програми.")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    user_manager = UserManager()
    user_manager.menu()

