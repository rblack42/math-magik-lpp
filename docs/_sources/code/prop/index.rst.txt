MMlpp Propeller
###############

The propeller is a bit involved. The basic idea in this construction is to build a thin walled cylinder thrn slice out the blades from that cylinder. The prop spar is just two tapered cylinders. The wire shaft is a bit more complex, but models a bent chunk of wire.


..  toctree::
    :maxdepth: 2

    blade/index
    spar/index
    wire_shaft/index

These parts are assembled in the usual way. Here is the prop data file:

..  literalinclude::    ../../../scad/prop/prop_data.scad
    :linenos:

The parts are positioned as follows:

..  literalinclude::    ../../../scad/prop/prop_pos.scad
    :linenos:

And, here is the assembly code:

..  literalinclude::    ../../../scad/prop/prop.scad
    :linenos:

Running this code produces this shape:

..  image:: prop.png
