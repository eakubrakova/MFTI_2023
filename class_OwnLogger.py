
class OwnLogger:
    def __init__(self):
        self.logs = {"info": None, "warning": None, "error": None, "all": None}

    def log(self, message, level):
        self.logs[level] = message

    def show_last(self, level="all"):
        if level == "all":
            return self.logs["all"]
        else:
            return self.logs[level]
