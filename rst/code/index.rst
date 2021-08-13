Math-Magick-lpp Code
####################

This model is designed to compete in the AMA |LPP| class. The rulebook
defines some basic design constraints we must follow to be legal in this class:

..  _constraints-scad:

..  figure: constraints.scad
    ..  literalinclude::    ../../scad/constraints.scad
        :linenos:


This file defines a few named values that can be used in other **.SCAD** files by *including* this file. This pattern is used extensively in defining various dimensions that are needed to set material sizes and part locations in the model.

As |OSC| code files are presented, the actual code will be displayed, followed by links to any data files needed to build the part or assembly.

..  note::

    My current documentation system does not provide a way for me to display
    code with links directly in that code, but I am working on that. The
    provided links will at least give the reader quick access to any data they
    wish to explore further.

Final Model Assembly
********************

The top-level model directory contains the |OSC| file used to generate the
complete model. This file relies on a positioning data file to properly locate
each major assembly that makes up that model. In addition, a basic data file is
located here defining a number of dimensions used in this final assembly.  i
Let's start off by looking at the top-level model code file:

..  literalinclude::    ../../scad/math_magik_lpp.scad
    :linenos:
    :language: c
    :caption: math_magik_lpp.scad

This file is laid out in a pattern that will be used throughout the design. The
top-level file defines an *assembly* of other components. We position those
components using the **math_magik_lpp_pos.scad** data file shown below. The
data in that file is used by the **align** method defined in the
**position.scad** library file.

When we **use** a file, we make any methods defined in that file available in
the current file. This mechanism only provides access to method names, not any
other data defined in those files.

When we **include** another file, the effect is to produce code that could be
written by copying the *included* file in place here. Since **include** files
often *include* other files, we can control what variables are available to
code in the current file easily. One of the challenges in setting up code this
way is making sure all needed names are available, even if those names are
defined inn other places.

My coding convention is to place as much data as possible in data files
containing no modules. I am trying to name all variables so you should see no
"bare" numbers in module files

..  note::

    I am constantly working to clean up this code, so be warned that
    thingsmight change in the future. If you work on this code by "cloning" a
    copy of this project using Git_, you can run a **git pull** command to
    update your code to the most current version.

Here is the positioning data file used to build the full model:

..  literalinclude::    ../../scad/math_magik_lpp_pos.scad
    :linenos:
    :language: c
    :caption:    math_magik_lpp_pos.scad

Finally, here is the data file needed fr the full model assembly:

..  literalinclude::    ../../scad/math_magik_lpp_data.scad
    :linenos:
    :language: c
    :caption: math_magik_lpp_data.scad


The model is constructed using the following assemblies/parts:

..  toctree::
    :maxdepth: 1

    fuselage/index
    wing/index
    stab/index
    prop/index
    rubber_motor/index

Animation
*********

|OSC| supports animating shapes. I decided to generate an animated **GIF** file
using this feature. It appears on the project website. To get this running,
click on :menuselection:`design -> Animate` and set in ta **FPS value of 30,
and a **Step** value of 10. The animation should start up. There are controls
that let you generate animation images that can be combined to build the
**GIF** file.


