MMlpp Wing Right Tip
####################

Since the tips are basically flat sections with no ribs except at the tip,
building the right tip is a much easier exercise. |OSC| has a m*mirror*
function that can be used to generate a mirror image shape. This is exactly
what we need!

Here is the code that generates the right tip:

..  literalinclude::    ../../../../scad/wing/right_tip/right_tip.scad
    :linenos:

After building this part, it occurred to me that the entire right section of
the wing could have been constructed as a mirror image of the left side. Of
course, that means I need to rework the center section. Maybe in a future
model!


