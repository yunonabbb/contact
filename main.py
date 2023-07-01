class Contact:
    def __init__(self, name, phone_numbers):
        self.name = name
        self.phone_numbers = phone_numbers

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Контакт успешно добавлен!")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Контакт успешно удален!")
                return
        print("Контакт с таким именем не найден.")

    def edit_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_name = input("Введите новое имя: ")
                new_phone_numbers = input("Введите новые номера телефонов (разделите их запятыми): ").split(",")
                contact.name = new_name
                contact.phone_numbers = new_phone_numbers
                print("Контакт успешно отредактирован!")
                return
        print("Контакт с таким именем не найден.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Имя: {contact.name}")
                print("Номера телефонов:")
                for number in contact.phone_numbers:
                    print(number)
                return
        print("Контакт с таким именем не найден.")

# Создание экземпляра контактной книги
contact_book = ContactBook()

# Добавление контактов
contact1 = Contact("василий", ["111111111", "222222222"])
contact_book.add_contact(contact1)

contact2 = Contact("виктор", ["333333333"])
contact_book.add_contact(contact2)

# Удаление контакта
contact_book.remove_contact("василий")

# Редактирование контакта
contact_book.edit_contact("виктор")

# Поиск контакта
contact_book.search_contact("виктор")










