Introduction
************

In this section you fill find listings of all |OSC| code used to generate the
|MM| |LPP| model. All documentation pages were generated automatically from the
current code in this project.

This documentation includes code blocks showing the actual |OSC| code created
for this model.

..	note::

    You *could* copy and paste these code blocks directly from these wen pages,
    but that would be silly. Instead, go to the project site on |GH|_ and you
    can see everything I have generated for this project, uncluding the |OSC|
    code and supporting |PY| code.


The design code documentation is organized in the same way as the |OSC| file
themselves. Each part ot assembly has its own directory and there is one
documentation page describing all of the files within that directory. The
pattern of the documentation is described below.

File Naming Convention
======================

I am using a simple naming convention for this project. All files used by |OSC|
to generate the complete model end with a **.scad** extension. Each part of
assembly is defined within a directory with that part or assembly name. Inside
that directory you will find a file with the same name as the directory, and
the **.scad** extension. This design file can be loaded into |OSC| and it will
generate that part or assembly for you to examine.

If and dimensions are needed to create a component, thse data values will be
located in files with names that look like this: **name_data.scad**. There are
two data files that do not follow this convention, both in the tip level code
directory: **constraints.scad** defines dimensions from the AMA rules for this
class, and **materials.scad** contains basic material dimensions.used in the
design.

Finally, positioning data needed t properly place each part or assembly in a
larger assembly are named with a pattern that looks like this:
**name_pos.scad**.

Design Notes
============

Information needed to describe how this component was designed will be
presented here.

Design File
===========

The code for the part or assembly is shown here. The caption at the tip of each
listing indicates where in the actual code directory tree this file can be
located.

Data Files
==========

If data is needed to create this component, the data files used are shown next.
These files *include* other |OSC| files as needed to fully define all values
defined.

Components
==========

Assemblies gather other components together to create a larger component. In
the design file, we *use* these component files so we can refer to the needed
part or assembly. These will be placed properly using position data shown in
the next section. (This section will not be present for part documentation).

The list of components needed for the current assembly is shown as links that
will take you to the documentation for that component.

Component Position Data
=======================

All components needed to create the current assembly need to be oriented
properly in the new assembly's coordinate system. I created a simple **align**
function that will place each component using translations and rotations as
needed. The position data for each component is a vector with six values, three
for translations, and three for rotations. (This section will not be present
for part documentation)
