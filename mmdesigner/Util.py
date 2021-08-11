import math

def xle(y, span, radius):
    """ calculate x location of tip le"""
    py = y * span
    yarc = span - radius
    if py < yarc:
        return 0;
    else:
        dy = py - yarc
        rad = radius**2 - dy**2
        if rad<0: return 0
        x = radius - math.sqrt(rad)
        return x

def zle(y, span, radius, height1, height2):
    py = y * span
    ztaper = height1 - height2
    ytaper = span - radius
    if py > ytaper:
        return height2
    else:
        return height2 + (ytaper - py)/ytaper * ztaper

def xte(y, span, height1, height2):
    pass

def zte(y, span, height1, height2):
    y = y * span
    ztaper = height1 - height2
    return height2 + (span - y) / span + taper

def zchord(x, height1, height2):
    dh = height1 - height2
    return height1 - x * dh

def ytip(x, radius, span):
    if x > radius:
        return span
    else:
        return span - (radius - math.sqrt(x * (2 * radius - x)))

