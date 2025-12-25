class Browser:
    def __init__(self, id, name, version, computer_id):
        self.id = id
        self.name = name
        self.version = version
        self.computer_id = computer_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BrowserComputer:
    def __init__(self, computer_id, browser_id):
        self.computer_id = computer_id
        self.browser_id = browser_id
