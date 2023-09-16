class Board:
    def __init__(self,lenght):
        self.high = lenght
        self.widh = lenght
    def  rtrboard(self):
        a = [[None for i in range(self.high)] for j in range(self.widh)]
        return a