import os

MODEL = "../scad"

class DataCataloger(object):

    def __init__(self, path):
        self.path = path

    def catalog(self):
        design_files = []
        data_files = []
        position_files = []

        for dirpath, dirnames, filenames in os.walk(MODEL):
            for f in filenames:
                fn = os.path.join(dirpath,f)
                if not f.endswith(".scad"): continue
                if "data" in f:
                    data_files.append(fn)
                elif "pos" in f:
                    position_files.append(fn)
                else:
                    design_files.append(fn)
        self.position_files = position_files
        self.data_files = data_files
        self.design_files = design_files;

    def dump(self):
        print("Design Files:")
        for f in self.design_files:
            print("\t",f)
        print("\nData Files:")
        for f in self.data_files:
            print("\t",f)
        print("\nPositionFiles:")
        for f in self.position_files:
            print("\t",f)

    def gen_data_index(self):
        index = {}
        for f in self.data_files:
            try:
                fin = open(f,"r")
                lines = fin.readlines()
            except:
                print("opening failed:",f)
                lines = {}
            for l in lines:
                if "//" in l: continue
                if "=" in l:
                    d,v = l.split("=")
                    index[d.strip()] = v.strip()

        for i in sorted(index.keys()):
            print(i,index[i])


if __name__ == '__main__':
    c = DataCataloger(MODEL)
    c.catalog()
    c.dump()
    c.gen_data_index()
