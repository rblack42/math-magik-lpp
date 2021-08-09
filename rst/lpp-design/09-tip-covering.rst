Tip Covering Logic
##################

Covering the center section of the wing and stab is a snap. That covering is
actually a simple slice out of a very thing cylinder since we are using
circular arc airfoils. I chose the generate the points on a grid that covers
the center section and use the *Bezier Surface* function to generate the actual
covering shape.

The tips are another matter. If we keep the outer ribs of the center section
vertical and raise the wing tip up to form the dihedral, the inner edge of the
covering is not a straight line. Mathematically, it is a piece of an ellipse
formed by cutting a cylinder with an angled plane. We can extract the
coordinates of the outer edge of the center section covering and use those points
as our starting point for the tip covering. However, we need to account for the
dihedral angle we will be using and adjust those points to find the correct
starting points for the tip covering. (Remember, there is no actual rib here.

This is not going to be too hard if we make one simple assumption.

Tip Airfoil
***********

The tip has no ribs, only the tip outline as a structure. If we cover an actual
model with this structure, something modelers typically do by building the wing
flat, then the covering assumes some shape other than out circular arc as we
move toward the tip. The actual height of this shape tapers off to zero as we
approach the tip.

I am simply going to assume that we can draw a straight line between the tip
center point and a corresponding point on the tip for form our grid. I have a
function set up that lets me calculate the **X** offset of the leading and
trailing edges, and the number of points along the chord I am using. I set up
needed points at he tip rib, then calculate new points ar virtual ribs
positioned along the tip span. The needed height is a simple calculation
calculated from the straight line running from the center virtual rib to the
tip rib.

Time for Some Math
******************

We need tome math to figure all of this out.

Inner Covering Points
=====================

At each point on the center section outer rib, we have a height value
available. Tat point in the coordinate system of the outer tip panlw wen it is
tipped up to form the dihedral can be calculated as follows:

..  math::

    y = z_r \sin{\theta}

    z = z_r \cos(\theta)

Where $\theta$ is the dihedral angle.




