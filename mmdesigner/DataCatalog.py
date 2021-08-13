import os

MODEL = "../scad"

class DataCataloger(object):

    def __init__(self, path):
        self.path = path
        self.path_parts = len(path.split('/'))

    def catalog(self):
        design_dirs = {}
        design_files = []
        data_files = []
        position_files = []

        for dirpath, dirnames, filenames in os.walk(MODEL):
            if len(dirnames) > 0:
                dftype="assembly"
            else:
                dftype='part'
            design_dirs[dirpath] = {
                    'dftype': dftype,
                    'design': [],
                    'data': [],
                    'pos': [],
                    'parts': [],
                    'dirname': ""
            }

            for d in dirnames:
                design_dirs[dirpath]['parts'].append(d)

            for f in filenames:

                fn = os.path.join(dirpath,f)
                fn_parts = fn.split('/')
                component_dir = fn_parts[-2]
                design_dirs[dirpath]['dirname'] = component_dir
                mmfn = '/'.join(fn_parts[self.path_parts:])
                if not f.endswith(".scad"): continue
                print("processing:",f, dirpath)
                if "data" in f or \
                        'points' in f \
                            or f == 'constraints.scad' \
                            or f == 'materials.scad':
                    design_dirs[dirpath]['data'].append(f)
                    data_files.append(mmfn)
                elif "pos" in f:
                    design_dirs[dirpath]['pos'].append(f)
                    position_files.append(mmfn)
                else:
                    print("design file:",f)
                    b,e = f.split('.')
                    design_dirs[dirpath]['design'].append(f)
                    design_files.append(fn)
        self.position_files = position_files
        self.data_files = data_files
        self.design_files = design_files;
        self.design_dirs = design_dirs

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
        print("Design files")
        for d in self.design_dirs:
            print("\t", self.design_dirs[d])

    def gen_data_index(self):
        index = {}
        for f in self.data_files:
            fn = os.path.join(self.path, f)
            try:
                fm = os.path.join(self.path, fn)
                fin = open(fn,"r")
                lines = fin.readlines()
            except:
                print("opening failed:",fn)
                lines = {}
            for l in lines:
                if "//" in l: continue
                if "=" in l:
                    d,v = l.split("=")
                    tag = d.strip()
                    val = v.strip()[:-1]
                    if not tag in index:
                        index[tag] = []
                    index[tag].append((f,val))

        # generate data catalog file
        outfn = '../rst/data_catalog.rst'
        with open(outfn,'w') as fout:
            fout.write("Data Catalog\n")
            fout.write("################\n\n")
            fout.write("..  csv-table::\n")
            fout.write("    :header: Name, Value, File\n\n")

            for i in sorted(index.keys()):
                val = index[i]
                fout.write("    %s,,\n" % i)
                for j in val:
                    p = j[0]
                    v = j[1]
                    fout.write('    ,"%s",%s\n' % (v,p))


    def gen_pos_index(self):
        index = {}
        for f in self.position_files:
            fn = os.path.join(self.path, f)
            try:
                fin = open(fn,"r")
                lines = fin.readlines()
            except:
                print("opening failed:",fn)
                lines = {}
            for l in lines:
                if "//" in l: continue
                if "=" in l:
                    d,v = l.split("=")
                    tag = d.strip()
                    val = v.strip()[:-1]
                    if not tag in index:
                        index[tag] = []
                    index[tag].append((f,val))

        # generate catalog file
        outfn = '../rst/position_catalog.rst'
        with open(outfn,'w') as fout:
            fout.write("Position Catalog\n")
            fout.write("################\n\n")
            fout.write("..  csv-table::\n")
            fout.write("    :header: Name, Value, File\n\n")

            for i in sorted(index.keys()):
                val = index[i]
                fout.write("    %s,,\n" % i)
                for j in val:
                    p = j[0]
                    v = j[1]
                    fout.write('    ,"%s",%s\n' % (v,p))


    def gen_design_code_file_docs(self):
        # generate design code doc files
        print("generating design file docs")
        for d in self.design_dirs:
            parts = d['design_file.split('/')
            df_path = '/'.join(parts[self.path_parts:-1])
            df_path = os.path.join('../rst/design_docs',df_path)
            design_file = parts[-1]
            os.makedirs(df_path)
            ifn = os.path.join(df_path,'index.rst")
            with open(ifn,'w') as fout:
                title = self.design_dirs['dirname']'
                fout.write("%s\n" % title)
                fout.write("%s\n" % '#' * len(title))
            print(df_path, design_file)

        return
        outfn = '../design_code/rst/data_catalog.rst'
        with open(outfn,'w') as fout:
            fout.write("Data Catalog\n")
            fout.write("################\n\n")
            fout.write("..  csv-table::\n")
            fout.write("    :header: Name, Value, File\n\n")

            for i in sorted(index.keys()):
                val = index[i]
                fout.write("    %s,,\n" % i)
                for j in val:
                    p = j[0]
                    v = j[1]
                    fout.write('    ,"%s",%s\n' % (v,p))

    def get_design_dirs(self):
        return self.design_dirs


if __name__ == '__main__':
    c = DataCataloger(MODEL)
    c.catalog()
    c.dump()
    #c.gen_data_index()
    #c.gen_pos_index()
    c.gen_design_code_file_docs()
    data = c.get_design_dirs()
    for d in data:
        print(d)
        print("\tdesign:",data[d]['design'])
        print("\tdata:",data[d]['data'])
        print("\tpos:",data[d]['pos'])
