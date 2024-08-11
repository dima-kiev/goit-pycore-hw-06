class AbstractCmd:
    CMD_NAME = None

    def __init__(self):
        self.user_input = None

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "THIS IS DECORATOR HANDLED ERROR"

        return inner

    @input_error
    def apply(self, user_input):
        self.user_input = user_input
        return self.action()

    def action(self):
        pass
