MODEL = "../scad/fuselage/fuselage_data.scad"

class Parser(object):

    def __init__(self, path):
        self.path = path
        self.line = None
        self.index = 0
        try:
            self.fin = open(path)
            self.line = self.fin.readline()
            if self.line == "":
                self.line = None
        except:
            pass

    def get_ch(self):
        if self.line is None:
            self.line = self.fin.readline()
            if self.line =="":
                self.line = None
                return None
            self.index = 0
        c = self.line[self.index]
        self.index += 1
        if self.index >= len(self.line):
            self.line = None
        return c

    def display(self):
        c = self.get_ch()
        while not c is None:
            print(self.index,c)
            c = self.get_ch()



if __name__ == "__main__":
    p = Parser(MODEL)
    p.display()



