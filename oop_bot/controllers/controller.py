class Controller:
    def __init__(self, cmd_factory):
        self.cmd_service = cmd_factory

    def consume(self, user_inp):
        cmd_line = user_inp.strip().lower()
        command = self.cmd_service.find_command(cmd_line)
        return command.apply(cmd_line)
