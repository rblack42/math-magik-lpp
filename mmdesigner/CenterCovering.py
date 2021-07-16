# -*- coding: utf8 -*-
"""
    CenterCovering
    ~~~~~~~~

    Generate center section covering surface
"""
# system library imports
import math

# local application imports
from ArcAirfoil import ArcAirfoil

class Covering(object):

    def __init__(self, span, chord, camber, nx, ny):
        self.span = span
        self.chord = chord
        self.camber = camber
        self.nx = nx
        self.ny = ny
        self.airfoil = ArcAirfoil(self.chord,self.camber, 1/16)
        self.callback = self.airfoil.height


    def grid_builder(self):
        dx = 1.0 / self.nx
        dy = 1.0 / self.ny
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
                ph = self.callback(x)
                xpoints.append([px,py,ph])
            points.append(xpoints)
        self.points = points

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


    def run(self, fname):
        self.fname = fname
        self.grid_builder()
        self.grid_writer()



if __name__ == "__main__":
    # generate wing center covering
    c = Covering(12,5,5,20,20)
    c.run("../scad/wing/center/covering/cover-points.scad")

    c = Covering(6,4,2,20,20)
    c.run("../scad/stab/center/covering/cover-points.scad")
