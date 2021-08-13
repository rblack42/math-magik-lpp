MMlpp  Wing
###########

The wing is constrained by a maximum chord, and maximum projected wing span. We
need to decide on the wing layout and calculate some dimensions.

For this design, I decided to use a flat center section, with tips raised to
generate the dihedral needed for stability. The leading edge of the tip will be
a circular arc.

The tip span will be defined as an elevation at the tip. The actual span can be
calculated using the |OSC| *atan2* function.

Here is the data generated for the wing:

..  literalinclude::    ../../../scad/wing/wing_data.scad
    :linenos:
    :caption: wing/wing_data.scad

Here are the assemblies used to construct the wing:

..  toctree::
    :maxdepth: 2

    center/index
    left_tip/index
    right_tip/index

Finally, here is the code that creates the wing assembly:

..  literalinclude::    ../../../scad/wing/wing.scad
    :linenos:
    :caption: wing/wing.scad



