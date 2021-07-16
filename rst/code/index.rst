Math-Magick-lpp Code
####################

This model is designed to compete in the AMA Li|LPP| class. The rulebook defines come basic design constraints we must follow to be legal in this class:

..  literalinclude::    ../../scad/constraints.scad
    :linenos:

The model will be constructed using the following assemblies/parts"

..	toctree::
	:maxdepth: 2

	fuselage/index
	wing/index
	stab/index
	prop/index
	rubber_motor/index

Placing these parts is done with another position data file:

..  literalinclude    ../../scad/model_pos.scad
    :linenos:

Here is the final assembly file that builds the entire model.
