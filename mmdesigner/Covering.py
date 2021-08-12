# -*- coding: utf8 -*-
"""
    Covering
    ~~~~~~~~

    Generate covering surfaces
"""
# system library imports
import math
import json
import os
import sys

# local application imports
from .ArcAirfoil import ArcAirfoil
from .Util import ytip


class Covering(object):

    def __init__(self, fname):
        self.fname = fname

        # load model data file
        jdata = None
        if not os.path.isfile(fname):
            print("Data file not found:", fname)
            sys.exit(1)

        with open(fname) as fin:
            jdata = json.load(fin)
        #print(jdata)
        if jdata is None:
            #print("Error reading data file")
            sys.exit(1)
        self.jdata = jdata

    def run1(self):
        part = "wing"
        seg = "center"
        self.nx = 20
        self.span = self.jdata[part][seg]["span"]
        self.camber = self.jdata[part][seg]["camber"]
        self.chord = self.jdata[part][seg]["chord"]
        self.center_covering()
        self.center_elevation = self.points
        self.grid_writer(part, seg)

        seg = "tip"
        self.nx = 40
        self.span = self.jdata[part][seg]["span"]
        self.dihedral = self.jdata[part][seg]["dihedral"]
        # calculate real tip span
        self.span = math.sqrt(self.span**2 + self.dihedral**2)
        self.dihedral_angle = math.asin(self.dihedral / self.span)
        #print("Angle:", self.dihedral_angle * 180.0 / math.pi)
        #print(self.tip_elevation)
        self.height1 = self.jdata[part][seg]["height1"]
        self.height2 = self.jdata[part][seg]["height2"]
        self.chord = self.jdata[part][seg]["chord"]
        self.radius = self.jdata[part][seg]["radius"]
        self.tip_covering()
        self.grid_writer(part, seg)

    def run(self):
        #print("generating covering data files:")
        for part in self.jdata:
            self.nx = self.jdata[part]["grid"]["nx"]
            self.ny = self.jdata[part]["grid"]["ny"]
            for seg in self.jdata[part]:
                if seg == "grid": continue
                if seg == "center":
                    self.span = self.jdata[part][seg]["span"]
                    self.camber = self.jdata[part][seg]["camber"]
                    self.chord = self.jdata[part][seg]["chord"]
                    self.center_covering()
                    self.tip_elevation = self.points[0]
                    self.grid_writer(part, seg)

                if seg == "tip":
                    self.span = self.jdata[part][seg]["span"]
                    self.dihedral = self.jdata[part][seg]["dihedral"]
                    # calculate real tip span
                    self.span = math.sqrt(self.span**2 + self.dihedral**2)
                    self.dihedral_angle = math.asin(self.dihedral / self.span)
                    #print("Angle:", self.dihedral_angle * 180.0 / math.pi)
                    #print(self.tip_elevation)
                    self.height1 = self.jdata[part][seg]["height1"]
                    self.height2 = self.jdata[part][seg]["height2"]
                    self.chord = self.jdata[part][seg]["chord"]
                    self.radius = self.jdata[part][seg]["radius"]
                    self.tip_covering()
                    self.grid_writer(part, seg)

    def center_covering(self):
        dx = 1.0 / self.nx  # percentage of chord
        points = []
        # loop over chord-wise points (x)
        for j in  range(self.nx + 1):
            xpoints = []
            x = j * dx
            px = x * self.chord
            y0 = 0
            y1 = self.span
            z0 = self.circular_arc_airfoil(x)
            z1 = z0
            xpoints.append([px,y0,z0])
            xpoints.append([px,y1,z1])
            points.append(xpoints)
        self.points = points

    def tip_covering(self):
        dx = 1.0 / self.nx  # percentage of chord
        points = []
        # loop over chordwise points (x)
        for i in range(self.nx + 1):
            xpoints = []
            x = i * dx
            px = x * self.chord
            h = self.circular_arc_airfoil(x)
            y0 = -h * math.sin(self.dihedral_angle)
            y1 = -ytip(px, self.radius, self.span)
            z0 = h * math.cos(self.dihedral_angle) + self.height1
            z1 = self.height2
            xpoints.append([px,y0,z0])
            xpoints.append([px,y1,z1])
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

    def cover_path(self, part, seg):
        """return file path for specified covering"""
        if seg == "tip":
            seg = "left_tip"
        # get path to project root
        cfile = os.path.abspath(__file__)
        path_parts = cfile.split('/')
        project_root = '/'.join(path_parts[:-2])
        if part == "fin":
            fname = os.path.join(
                    project_root,
                    "scad",
                    "fuselage",
                    part,
                    "covering",
                    "cover_points.scad")
        else:
            fname = os.path.join(
                        project_root,
                        "scad",
                        part,
                        seg,
                        "covering",
                        "cover_points.scad")

        return fname

    def grid_writer(self, part, seg):
        fname = self.cover_path(part, seg)
        #print("Writing point file:", fname)
        with open(fname,"w") as fout:
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
    c = Covering("../scad/covering_data.json")
    c.run()
