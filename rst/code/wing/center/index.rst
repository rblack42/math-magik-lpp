MMlpp Wing Center Section
#########################

The wing center section is a simple rectangular structure with square spars at
the leading ans trialing edges. There will be five ribs with a four percent
camber.

The dimensions needed for this structure are all defined in the
w**wing_data.scad** file.

Note that we only have one rib defined here. That rib is used five times, and
each will be positioned along the center section span. This complicates the
analysis a bit, but we will deal with that in the code.

Here is the assembly file that constructs this section:

..  literalinclude::    ../../../../scad/wing/center/center.scad
    :linenos:

And, here are the details on the components used in this code:

..  toctree::
    :maxdepth: 2

    spar/index
    rib/index

Finally, here is the positioning code needed to assemble this section:

..  literalinclude::    ../../../../scad/wing/center/center_pos.scad
    :linenos:

