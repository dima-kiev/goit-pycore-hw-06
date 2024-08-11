from oop_bot.services.commands.cmd_add import Cmd_add
from oop_bot.services.commands.cmd_del import Cmd_del
from oop_bot.services.commands.cmd_edit import Cmd_edit
from oop_bot.services.commands.cmd_exit import Cmd_exit
from oop_bot.services.commands.cmd_find import Cmd_find
from oop_bot.services.commands.cmd_list import Cmd_list
from oop_bot.services.commands.cmd_not_found import Cmd_not_found


class CmdFactory:

    def __init__(self, storage):
        self.storage = storage
        self.__init_commands()

    def find_command(self, user_inp: str):
        for cmd_name in self.commands:
            if user_inp.find(cmd_name) != -1:
                return self.commands[cmd_name]
        return self.commands.get(Cmd_not_found.CMD_NAME)

    def __init_commands(self):
        self.commands = dict()
        self.commands[Cmd_not_found.CMD_NAME] = Cmd_not_found()
        self.commands[Cmd_add.CMD_NAME] = Cmd_add(self.storage)
        self.commands[Cmd_find.CMD_NAME] = Cmd_find(self.storage)
        self.commands[Cmd_list.CMD_NAME] = Cmd_list(self.storage)
        self.commands[Cmd_del.CMD_NAME] = Cmd_del(self.storage)
        self.commands[Cmd_edit.CMD_NAME] = Cmd_edit(self.storage)
        self.commands[Cmd_exit.CMD_NAME] = Cmd_exit()
        self.commands["close"] = self.commands.get(Cmd_exit.CMD_NAME)
