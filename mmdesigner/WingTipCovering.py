# -*- coding: utf8 -*-
"""
    Covering
    ~~~~~~~~

    Generate covering surface for models
"""
# system library imports
import math

# local application imports
import Airfoil

class Covering(object):

    def __init__(self, span, chord, radius, nx, ny, height_function):
        self.span = span
        self.chord = chord
        self.radius = radius
        self.nx = nx
        self.ny = ny
        self.callback = height_function


    def grid_builder(self):
        dx = 1.0 / self.nx
        dy = 1.0 / self.ny
        points = []
        # loop over cord-wise points (x)
        for i in range(self.nx + 1):
            x = i * dx
            xpoints = []
            # loop over span-wise points (y)
            for j in  range(self.ny + 1):
                y = j * dy
                px, py, ph = self.callback(self.span, self.chord, self.radius, x, y)
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



def flat(span, chord, radius, x, y):
    """
        return x,y,height for tip outline
        x and y are percentages
    """
    py = y * span
    y_tip = span - radius
    c_tip = chord - radius
    if py <= y_tip:
        x0 = 0
        ych = chord
    else:
        sf = (py-y_tip)/radius
        alpha = math.asin(sf)
        x0 =  radius*(1 - math.cos(alpha))
        ych = chord - x0
    px = x0 + x * ych
    height = 0
    return px, py, height;

def circular_arc_airfoil(span, chord, radius, x, y):
    """
        return x,y,height for tip outline
        x and y are percentages
        Airfoils is circular arc
    """
    py = y * span
    y_tip = span - radius
    c_tip = chord - radius
    if py <= y_tip:
        x0 = 0
        ych = chord
    else:
        sf = (py-y_tip)/radius
        alpha = math.asin(sf)
        x0 =  radius*(1 - math.cos(alpha))
        ych = chord - x0
    px = x0 + x * ych
    height = 0
    return px, py, height;

if __name__ == "__main__":
    # generate fin covering
    c = Covering(2,4,1.5,10,10, flat)
    c.run("../scad/math-magik-lpp/fuselage/fin/fin-covering/fin-covering-points.scad")

    # wing center section covering
    c = Covering(12,5,0,10,10, circular_arc_airfoil)
    c.run("../scad/math-magik-lpp/wing/center/center-covering/center-cover-points.scad")

    # stab center section covering
    c = Covering(6,4,0,10,10, circular_arc_airfoil)
    c.run("../scad/math-magik-lpp/stab/center/center-covering/center-cover-points.scad")

    # stab - left tip covering
    c = Covering(3,4,2,10,10, flat)
    c.run("../scad/math-magik-lpp/stab/left-tip/left-tip-covering/left-tip-covering-points.scad")

    # stab right tip covering
    c = Covering(3,4,2,10,10, flat)
    c.run("../scad/math-magik-lpp/stab/right-tip/right-tip-covering/right-tip-covering-points.scad")

    tip_angle = math.atan2(1.75,3)
    tip_span = 3/math.cos(tip_angle)

    # wing left tip covering
    c = Covering(tip_span,5,2,10,10, flat)
    c.run("../scad/math-magik-lpp/wing/left-tip/left-tip-covering/left-tip-covering-points.scad")

    # wing right tip covering
    c = Covering(tip_span,5,2,10,10, flat)
    c.run("../scad/math-magik-lpp/wing/right-tip/right-tip-covering/right-tip-covering-points.scad")

