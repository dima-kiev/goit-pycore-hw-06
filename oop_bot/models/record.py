from oop_bot.models.name import Name


class Record:

    def __init__(self, name, phones):
        self.name = Name(name)
        if phones:
            self.phones = phones
        else:
            self.phones = []


    def add_phone(self, phone):
        self.phones.append(phone)
        return self


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
