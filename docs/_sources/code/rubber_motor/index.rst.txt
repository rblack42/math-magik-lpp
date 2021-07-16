MMlpp Rubber Motor
##################

We do not need an accurate model of the motor we will use for this design.
Therefore, we will simply model it as a cylinder running between with propeller
shaft hook, and the rear hook. The chosen density of this cylinder will make
the motor weight about what it should. That will be used in center of gravity
calculations. Visually, it might look a bit silly, but YMMV!

Design SCAD File
****************

..  literalinclude::   ../../../scad/rubber_motor/rubber_motor.scad
    :linenos:

Design data
***********

..  literalinclude::    ../../../scad/rubber_motor/rubber_motor_data.scad
    :linenos:

Since this motor is modeled as a simple skinny cylinder, I am omitting the
image! It will appear in the final model image.

