Math-Magick-lpp Code
####################

This model is designed to compete in the AMA Li|LPP| class. The rulebook
defines come basic design constraints we must follow to be legal in this class:

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

..  literalinclude    ../../scad/math_magok_lpp_pos.scad
    :linenos:

Here is the final assembly file that builds the entire model.

..  literalinclude    ../../scad/math-magik_lpp.scad
    :linenos:

The challenge in this final assembly is making sure everything lines up. This
is the point in time when you really ned to think through how parts relate to
each other when bringing the model together.

Animation
*********

|OSC| supportsanimating shapes. I decided to generate an animated **GIF** file using this feature. It appears on the project website. To get this running, click on :menuselection:`design -> Animate` and set in ta **FPS value of 30, and a **Step** value of 10. The anitation should start up. There are controls that let you generate animation images that can be combined to build the **GIF** file.


