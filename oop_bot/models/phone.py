from oop_bot.models.field import Field


def validate(value: str):
    if len(value) != 10 and not value.isalnum():
        raise ValueError


class Phone(Field):

    def __init__(self, phone):
        validate(phone)
        super().__init__(phone)
