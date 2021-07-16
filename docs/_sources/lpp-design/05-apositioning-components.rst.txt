Positioning Components
######################

One of the issues with designing wit |OSC| is getting things positioned
correctly. In a traditional *CAD* program, you just drag things arond and
things pop into place. Not so with OSC. You need to think through exactly where
things need to go, and that involves knowing exactly where the parts are
located in the coordinate system.

Coordinate Systems
******************

Every individual part and assembly is created in its own coordinate system.
When moving parts around, the part or assembly is translated and/or rotated
into the proper position within this coordinate system.

For example, when designing an individual rib, the coordinate ssystem is
located at the leading edge. The rib is centered in the **X_Z** plane, and the
lower point on the rib sits flat on the **X-Y** plane.

When we use this rib in the wing assembly, the coordinate system is different.
For the wing, the leading and trailing edge spars should end up sitting on the
**X-Y** plane, ans the wing is centered relative t the **X-Z** plane.

That means we need to position the rib within the wing's coordinate system. The
critical point we need to remember is the location of the origin of the rib's
coordinate system (bottom of the leading edge, right in the middle of the rib).
That point must me moved into the proper position in the wing's coordinate
system. The translations need to slide the rib to the right spot, and any
rotations needed to properly align the rib need ot happen before moving.

Align Function
**************

To make this a bit easier, I wrote an *align* function that takes a list of six
values:

..	math::

	[x_y, y_t, z_t, x_r, y_r, z_r]

Using this function involves calculating exactly what translations and
rotations are needed to properly position that part. Since individual parts do
not need to be aligned (unless you need to do that to properly create the
part, I set up a file named *partname_pos.scad* within each assembly directory. This file lists the alignment values need to build the assembly out of the required components.

Using this concept, constructing an assembly is as simple as listing the
components and aligning each one:

..	literalinclude::	../../scad/wing/wing.scad
	:linenos:
	:language: c

Calculating Alignment Values
****************************

In setting up the alignment values, you need to access design values.
The dimensions of each component are important in figuring this out. There is
no easy to avoid needing to do some annoying calculations. For instance, when
positioning the wing posts on the side of the motor stick, we need to know how
thick the motor-stick is and how thick the wing posts are. The offset needed is
one half the sum of these two values:

..	code-block::

	post_x_offset = (motor_stick_thickness + wing_post_size)/2;

I have tried to name these dimensions to make it clear what the calculations
involve. Unfortunately, some calculations need access to dimensional values
defined in other directories. To make this a bit easier to manage, I am placing
a data file in each directory where these values are either defined, of
calculated as needed to define the component in the associated directory.

