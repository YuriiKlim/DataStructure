from bintrees import AVLTree


class Dictionary:
    def __init__(self):
        self.data = AVLTree()
        self.access_count = {}

    def initialize_data(self, initial_words):
        for english, ukrainian in initial_words.items():
            self.data.insert(english, ukrainian)
            self.access_count[english] = 0

    def display_word(self, word):
        translation = self.data.get(word, None)
        if translation:
            self.access_count[word] += 1
            print(f"{word}: {translation}")
        else:
            print("Word not found.")

    def add_or_update_word(self, word, translation):
        self.data.insert(word, translation)
        if word not in self.access_count:
            self.access_count[word] = 0

    def delete_word(self, word):
        self.data.discard(word)
        if word in self.access_count:
            del self.access_count[word]

    def add_or_update_translation(self, word, new_translation):
        if word in self.data:
            self.data[word] = new_translation
            print("Переклад оновлено.")
        else:
            print("Слово незнайдене.")

    def delete_translation(self, word):
        if word in self.data:
            self.data.pop(word)
            print("Переклад видалено.")
        else:
            print("Слово незнайдене.")

    def top_words(self, n=10):
        sorted_words = sorted(self.access_count.items(), key=lambda item: item[1], reverse=True)
        print(f"\nТоп {n} найпопулярніших слів:")
        for i, (word, count) in enumerate(sorted_words[:n], start=1):
            print(f"{i}. {word} - {count} запитів")

    def run(self):
        initial_data = {
            "hello": "привіт",
            "world": "світ",
            "computer": "комп'ютер",
            "language": "мова",
            "python": "пайтон"
        }
        self.initialize_data(initial_data)

        self.display_word("hello")
        self.display_word("world")
        self.display_word("world")
        self.add_or_update_word("tree", "дерево")
        self.add_or_update_word("cat", "кіт")
        self.display_word("tree")
        self.delete_word("computer")
        self.add_or_update_translation("world", "світ (планета)")
        self.delete_translation("python")

        self.top_words()


dictionary = Dictionary()
dictionary.run()
