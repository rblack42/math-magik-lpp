Positioning Components
######################

One of the issues with designing with |OSC| is getting things positioned
correctly. In a traditional *CAD* program, you just drag things around and
things pop into place. Not so with |OSC|. You need to think through exactly where
things need to go, and that involves knowing exactly where the parts are
located in the coordinate system.

Coordinate Systems
******************

Every individual part and assembly is created in its own coordinate system.
When moving parts around, the part or assembly is translated and/or rotated
into the proper position within this coordinate system.

You are in charge of the system used to design any part or assembly! All of
this is a mental exercise. The important part of this process is being able to
mentally visualize the gadget you are about to design, then identify points
within that coordinate system that will be important in your design work. As
much as possible, I try to think about each component the way a builder thinks
and works. Most models are built on some kind of flat surface, so I make that
surface the **X-Y** plane, and place the part the origin of the coordinate
system. When assembling the model, I switch to a "pilot's" view of the world. I
place the origin of this system at some point on the front of the model and run
the **X** axis down the fuselage to the tail. The wings are aligned along the
**Y** axis, and the **Z** axis ends up aligned vertically .


For example, when designing an individual rib for an indoor model, I set up the
coordinate system with the origin located at bottom front of the leading edge
of the rib. The rib is constructed flat on the **X-Y** plane, and the lower
point on the rib sits flat on the **X-Z** plane.

When we use this rib in the wing assembly, the coordinate system is different.
For the wing, the leading and trailing edge spars should end up sitting on the
**X-Y** plane, and the wing is centered relative to the **X-Z** plane.

That means we need to position the rib within the wing's coordinate system.
That will involve rotating it so it is oriented correctly, then translating
that rib into its proper position within the wing structure.

..  note::

    Of course, there is the issue of properly trimming the rib sit it fits
    nicely against a wing spar. There are a lot of details modelers never think
    about while building. I am working on ideas to streamline a lot of these
    details as I work on this project!

Visualizing Components
======================

|OSC| make it easy to see the results of your work. You tweak the code, then
generate a display that shows the results. (Of course, you never make typos,
but if you do, you can fix then quickly!).

There is an interesting way to use |OCS| that I find handy.

I write a lot on my computer. Some of my writings are just normal text, some is
code. Long ago I settled on a nice editing tool called **vim** that I have used
for ll kinds of textual work. I really do not like working on some editing tool
that is not as smart as my favorite editor. Fortunately, |OSC| lets me write
code in my favorite editor, then save that work on my system. |OCS| can monitor
a file you are editing, and then it sees a saved change, it will automatically
regenerate your design so you can see it easily. That save a lot of time!

Using this scheme, I open up my favorite editor and |OSC| at the same time and
position the screen windows as i like. I then set up |OSC| to use this feature,
and turn off the |OSC| editor.

To do this,
The
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

