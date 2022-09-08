class StringConverter:
    def __init__(self, stroka):
        self.stroka = stroka
        self.changedstr = stroka

    def converter(self):
        if not self.changedstr.endswith("!"):
            self.changedstr = self.changedstr + "!"
        return self.changedstr.capitalize()
