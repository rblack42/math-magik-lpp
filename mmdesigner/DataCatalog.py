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
                    'dirname': "",
                    'cname': ""
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
                elif "pos" in f and not "post" in f:
                    design_dirs[dirpath]['pos'].append(f)
                    position_files.append(mmfn)
                else:
                    #print("design file:",f)
                    b,e = f.split('.')
                    design_dirs[dirpath]['design'].append(f)
                    design_dirs[dirpath]['cname'] = b
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
        print("generating design file docs")
        # generate design code doc files

        for d in self.design_dirs:
            print(d)
            # generate component path for this component file
            parts = d.split('/')
            if len(parts) == self.path_parts:
                cpath = ""
                depth = 0
                depth_leadin = ""
            else:
                cpath_parts = parts[self.path_parts:]
                depth = len(cpath_parts)
                cpath = '/'.join(parts[self.path_parts:])
            depth_leadin = "../" * (depth + 2)
            print("\t",depth, depth_leadin, cpath)

            # extract data dictionary for this component
            data = self.design_dirs[d]
            for cd in data:
                print("\t",cd, data[cd])

            # set code and doc file paths
            code_path = os.path.join(depth_leadin, "scad", cpath)
            doc_path = os.path.join("../", "rst", "design_docs", cpath)
            print("\tcode_path:", code_path)
            print("\tdoc_path:", doc_path)

            cname = self.design_dirs[d]['cname']
            ctype = self.design_dirs[d]['dftype']

            print("creating:", cname, " path:", code_path, " type:", ctype)
            components = self.design_dirs[d]['parts']
            print("components",components)
            print("")

            # create component directory
            os.makedirs(doc_path, exist_ok=True)

            # generate the index file
            ifn = os.path.join(doc_path,'index.rst')
            with open(ifn,'w') as fout:
                title = ctype + ": " + cname
                underbar = '#' * len(title)
                fout.write("%s\n" % title)
                fout.write("%s\n\n" % underbar)

                # set up the include for this component file
                fout.write("This %s is created with the following file:\n\n" % ctype)
                scadpath = os.path.join(code_path, cname+'.scad')
                fout.write("..  literalinclude::  %s\n" % scadpath)
                captext = os.path.join(cpath, cname + '.scad')
                fout.write("    :linenos:\n    :caption: %s\n\n" % captext)

                # show any data files
                data_files = self.design_dirs[d]['data']
                if len(data_files) > 0:
                        fout.write("Component Data File(s)\n")
                        fout.write("**********************\n\n")
                        for df in data_files:
                            scadpath = os.path.join(code_path, df)
                            fout.write("..  literalinclude::  %s\n\n" % scadpath)

                # show components, if any
                if len(components) > 0:
                    fout.write("\nComponents\n**********\n\n")
                    fout.write("..  toctree::\n    :maxdepth: 1\n\n")
                    for c in components:
                        fout.write("    %s/index\n" % c)

            print(cpath, cname)


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

    #for d in data:
    #    print(d)
    #    print("\tdesign:",data[d]['design'])
    #    print("\tdata:",data[d]['data'])
    #    print("\tpos:",data[d]['pos'])
