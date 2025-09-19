import string

class Spreadsheet:

    def __init__(self, rows: int):
        # self.sheet = {char: [0]*rows for char in string.ascii_uppercase}
        self.sheet = {}

    def setCell(self, cell: str, value: int) -> None:
        # key, idx = cell[0], int(cell[1:])
        # self.sheet[key][idx-1] = value
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        # key, idx = cell[0], int(cell[1:])
        # self.sheet[key][idx-1] = 0
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        key1, key2 = formula.replace("=","").split("+")
        # if key1.isdigit():
        #     val1 = int(key1)
        # else:
        #     key, idx = key1[0], int(key1[1:])
        #     val1 = self.sheet[key][idx-1]
        # if key2.isdigit():
        #     val2 = int(key2)
        # else:
        #     key, idx = key2[0], int(key2[1:])
        #     val2 = self.sheet[key][idx-1]
        # return val1+val2
        if key1.isdigit():
            val1 = int(key1)
        elif key1 in self.sheet:
            val1 = self.sheet[key1]
        else:
            val1 = 0
        if key2.isdigit():
            val2 = int(key2)
        elif key2 in self.sheet:
            val2 = self.sheet[key2]
        else:
            val2 = 0
        return val1+val2
            


# ["Spreadsheet","getValue","setCell","getValue","setCell","getValue","resetCell","getValue"]
# [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

# spread_sheet = Spreadsheet(3)
# print(spread_sheet.sheet)