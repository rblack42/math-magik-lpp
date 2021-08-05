MMlpp Motor Stick
#################

The motor stick is a simple piece. However, I decided to taper it at the front
and rear, and add a brace for the rear hook. For those reasons, I elected to
generate this piece using a 2D polygon, that gets extruded to form the final
shape.

The rules limit the distance from the length of the  motor, and this gas an
effect on the length of the motor stick. We will need to generate the
propeller, and the prop shaft to figure out the actual motor stick length.

Here is the code containing the polygon shape.

..  literalinclude::    ../../../../scad/fuselage/motor_stick/motor_stick_data.scad
    :linenos:

And here is the code that generates the shape:

..  literalinclude::    ../../../../scad/fuselage/motor_stick/motor_stick.scad
    :linenos:

Finally, here is our basic motor stick:

..  image:: motor_stick.png
    :align: center


