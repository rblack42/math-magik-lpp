# -*- coding: utf8 -*-
"""
    ArcAirfoil
    ~~~~~~~~~~

    height function for circular arc airfoil
"""
import math


class ArcAirfoil(object):
    """manage circular arc airfoil"""

    def __init__(self,chord, camber, spar_size):
        self.chord = chord
        c = chord - 2 * spar_size
        self.camber = camber
        self.spar_size = spar_size
        self.thickness = self.chord * self.camber/100
        self.radius = c**2 / (8 * self.thickness) + self.thickness/2

    def height(self,x):

        t = self.thickness
        r = self.radius
        ct = self.chord
        c = ct - 2 * self.spar_size
        x = x * ct
        if x < self.spar_size: return 0
        if x > ct - self.spar_size: return 0
        h = -r + t + math.sqrt((-c/2 + r + x)*(c/2 + r - x))
        return h

if __name__ == "__main__":

    print("Check circular arc airfoil height")
    a = ArcAirfoil(5,5,1/16)
    print("x=0 ->",a.height(0))
    print("x=0.5 ->",a.height(0.5))
    print("x=1 ->",a.height(1.0))
