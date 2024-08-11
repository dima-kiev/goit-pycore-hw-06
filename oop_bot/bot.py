from oop_bot.services.adress_book import AddressBook
from services.cmd_factory import CmdFactory
from views.view import View
from controllers.controller import Controller


def main():
    View(
        Controller(
            CmdFactory(
                AddressBook()
            )
        )
    ).start()


if __name__ == '__main__':
    main()
