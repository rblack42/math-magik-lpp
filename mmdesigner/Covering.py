# -*- coding: utf8 -*-
"""
    Covering
    ~~~~~~~~

    Generate covering surfaces
"""
# system library imports
import math
import json

# local application imports
from ArcAirfoil import ArcAirfoil

class Covering(object):

    def __init__(self):
        jdata = None
        with open("covering_data.json") as fin:
            jdata = json.load(fin)
        #print(jdata)
        if jdata is None:
            print("Error reading data file")
            sys.exit(1)
        self.jdata = jdata
        #self.airfoil = ArcAirfoil(self.chord,self.camber, 1/16)
        #self.callback = self.airfoil.height
        for part in self.jdata:
            print("generating covering for ", part)
            for segment in self.jdata[part]:
                if segment == "base": continue
                print("\t", segment)

    def run(self):
        print("generating covering data files:")
        for part in self.jdata:
            print("\tpart;", part)
            self.nx = self.jdata[part]["base"]["nx"]
            self.ny = self.jdata[part]["base"]["ny"]
            for seg in self.jdata[part]:
                if seg == "base": continue
                print("\t\tsegment:", seg)
                if seg == "center":
                    self.span = self.jdata[part][seg]["span"]
                    self.camber = self.jdata[part][seg]["camber"]
                    self.chord = self.jdata[part][seg]["chord"]
                    self.center_covering()
                    self.fname = "%s_%s_cover_points.scad" % (part,seg)
                    self.grid_writer()
                if seg == "tip":
                    self.span = self.jdata[part][seg]["span"]
                    dihedral = self.jdata[part][seg]["dihedral"]
                    # calculate real tip span
                    self.span =math.sqrt(self.span**2 + dihedral**2)
                    self.le_height1 = self.jdata[part][seg]["height1"]
                    self.le_height2 = self.jdata[part][seg]["height2"]
                    self.chord = self.jdata[part][seg]["chord"]
                    self.radius = self.jdata[part][seg]["radius"]
                    self.tip_covering()
                    self.fname = "%s_%s_cover_points.scad" % (part,seg)
                    self.grid_writer()

    def _xle(self, y):
        """ calculate x location of tip le"""
        yarc = self.span - self.radius
        if y < yarc:
            return 0;
        else:
            dy = y - yarc
            rad = self.radius**2 - dy**2
            if rad<0: return 0
            x = self.radius - math.sqrt(rad)
            return x

    def center_covering(self):
        dx = 1.0 / self.nx  # percentage of chord
        dy = 1.0 / self.ny  # percentage of span
        points = []
        # loop over cord-wise points (x)
        for i in range(self.nx + 1):
            x = i * dx
            px = x * self.chord
            xpoints = []
            # loop over span-wise points (y)
            py = 0
            for j in  range(self.ny + 1):
                y = j * dy
                py = y* self.span
                ph = self.circular_arc_airfoil(x)
                xpoints.append([px,py,ph])
            points.append(xpoints)
        self.points = points

    def tip_covering(self):
        dx = 1.0 / self.nx  # percentage of chord
        dy = 1.0 / self.ny  # percentage of span
        points = []
        # loop over span-wise points (y)
        for i in range(self.ny + 1):
            y = i * dy * self.span
            xle = self._xle(y)
            xte = self.chord
            xpoints = []
            # loop over chord-wise points (x)
            for j in  range(self.nx + 1):
                x = j * dy * (xte - xle)
                xpoints.append([x,y,0.0])
            points.append(xpoints)
        self.points = points

    def circular_arc_airfoil(self, x):
        """
            return height for rib
            x is percentage of chord
        """
        px = x * self.chord
        t = self.camber * self.chord/100.0
        r = self.chord**2/(8.0*t) + t/2.0
        beta = math.asin((px - self.chord/2)/r)
        beta_degrees = beta * 180.0 / math.pi
        height = r * math.cos(beta) - (r - t)
        return height;

    def grid_writer(self):
        with open(self.fname,"w") as fout:
            fout.write("g_pts = [\n")
            p = self.points
            ny = len(p)

            # loop over grid rows
            for i in range(ny):
                fout.write("    [\n")
                xp = p[i]
                nx = len(xp)

                # loop over grid columns
                fout.write("        ")
                for j in range(nx):
                    pt = xp[j]
                    g_pt = "[{0:.2f}, {1:.2f}, {2:.2f}]".format(pt[0], pt[1], pt[2])
                    fout.write(g_pt)
                    if j < nx-1: fout.write(",")
                fout.write("\n    ]")
                if i<ny-1: fout.write(",")
                fout.write("\n")
            fout.write("];\n")





if __name__ == "__main__":
    c = Covering()
    c.run()
    #c.run("../scad/wing/center/covering/cover-points.scad")

    #c = Covering(6,4,2,20,20)
    #c.run("../scad/stab/center/covering/cover-points.scad")
