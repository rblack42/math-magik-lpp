Getting Started
***************

To get started on this project, you need to make sure you have |OSC| installed.
The project website has installers for all major platforms (Windows, Mac, and
Linux). For an overview of using this program, see the |MM| project
documentation. I highly recommend that you print out a copy of the |OSC| "cheat
sheet" available at https://openscad.org/cheatsheet

|LPP| Rules
***********

We cannot get much design work done without a clear understanding of the class
rules. These are published in the `AMA Rulebook`_ under "Event 208".

Basically, we need to respect a few model dimensions and weights in order to
compete in this class. All of these are specified in a single |OSC| data file
placed at the top of the model design directory:

..  literalinclude::    ../../scad/constraints.scad
    :language: c
    :caption:   math-magic-lpp/scad/constraints.scad
    :linenos:

Note that in this design, all dimensions are in inches. |OSC| supports doing
simple math when defining constants, so I am using things like **1/16** to
indicate a standard modeling dimension, rather than using the actual decimal
value.

Also note that I name data files with a **.data** extension. |OSC| will handle
these files just fine. All files with an **.scad** extension will define actual
model parts or assemblies.

Parts and Assemblies
********************

In this design, a *part* is a single component constructed out of some building
material. When we analyze the properties of a part, we will need to specify the
density of the material. In order to simplify the design, and set up useful
components that might be useful in other designs, some *part* code files will
be placed in a library folder. The *library parts* generally use parameters
that need to be set to construct an actual physical part. We will see this
concept in action soon in our design work.

An *assembly* is a collection of parts combined to form a higher level
component of the model. Assemblies can join simple parts, or other assemblies
as needed to complete the model.

|OSC| is generally used by folks building things using 3d printers. In those
applications, it is common to "fuse" parts together so generating files needed
by a 3D printer can be constructed. in our design work, we will not be doing
that. Instead, we need to carefully align parts so they end up placed in
exactly the right spot. Fortunately, you can do simple calculations in |OSC|
code to simplify this process.

Design Process
**************

In the pages that follow, we will work on model parts in no particular order.
We will initially focus on building a few parts, then set up assemblies that
use those parts. The last thing we will be doing is assembling the complete
model. This process is much the same as the one you would use to build any
model using real parts. There is not one "correct" way to do this, although
some things get pretty obvious.

In the next section, we will start off by building the wing.

