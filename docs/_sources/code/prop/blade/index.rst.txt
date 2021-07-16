MMlpp Prop Blade
################

The prop blade design took a big of thought. I decided to create a basic blade
shape using simple elliptical segments, and set up the shape to provide for
"flair". The values selected are not flight tested yet, but they show the basic
idea.

Constructing the blade was an interesting exercise. I pondered this issue until
it occurred to me that I could form this blade using the same idea modelers use
when they take a flat blade section and form it around a cylinder. I decided to
generate the blade shape as a 2D surface, then extrude is into a long section.
I then create a thin walled cylinder, formed by subtracting an inner cylinder
from an outer cylinder. I then oriented the blade shape and generated the
intersection of these two shapes. The result is a thin blade that looks about
right.

It should be apparent that this is not quite right. Normal blade construction
warps a flat surface around the cylinder. BY cutting out my blade using this
scheme, I do not get the same blade shape. Perhaps I will figure out a
correction to the blade shape I use at a later time!

Here is the file for the blade shape:

..  literalinclude::    ../../../../MMlib/elliptic_blade_blank.scad
    :linenos:

And here is the code used to generate the blade:

..  literalinclude::    ../../../../scad/prop/blade/blade.scad
    :linenos:

The final result looks fairly nice!

..  image:: blade.png
    :align: center


