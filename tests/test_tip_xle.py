import math
from pytest import approx

from mmdesigner.Util  import xle, zle, xte, zte, zchord, ytip

def test_tip_xle():
    x = 0
    span = 3.5
    radius = 2.0
    assert xle(0.0, span, radius) == 0.0
    assert xle(1.0, span, radius) == radius

def test_tip_zle():
    x = 0
    span = 3.5
    radius = 2
    height1 = 1/16.0
    height2 = 1/32.0
    assert zle(0.0, span, radius, height1, height2) == height1
    assert zle((span-radius/span), span, radius, height1, height2) == height2
    assert zle(1.0, span, radius, height1, height2) == height2

def test_zchord():
    span = 5
    h1 = 1
    h2 = 0.5
    assert zchord(0,h1,h2) == h1
    assert zchord(1.0,h1,h2) == h2
    assert zchord(0.5,h1,h2) == (h1 + h2)/2

def test_y_tip():
    span = 3.5
    chord = 5
    radius = 2
    assert ytip(0, radius, span) == span - radius
    assert ytip(radius, radius, span) == span
    assert ytip(radius, radius, span) == span
    testx = radius - radius / math.sqrt(2)
    assert ytip(testx, radius, span) == approx(span - testx, rel=1e-3)
