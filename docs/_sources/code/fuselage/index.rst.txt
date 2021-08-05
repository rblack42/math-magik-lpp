MMlpp Fuselage
##############

The model fuselage has a lot of parts to assemble. These are detailed below.

..  toctree::
    :maxdepth: 2

    motor_stick/index
    tail_boom/index
    fin/index
    wing_posts/index
    stab_posts/index
    fin_post/index
    thrust_bearing/index
    rear_hook/index

The positioning data needed to assembly this component are shown next.

..  literalinclude::    ../../../scad/fuselage/fuselage_data.scad
    :linenos:

Here is the assembly code:

..  literalinclude::    ../../../scad/fuselage/fuselage.scad
    :linenos:

The assembly is shown below:

..  image:: fuselage.png
    :align: center

