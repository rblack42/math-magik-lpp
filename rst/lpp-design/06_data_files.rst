Data Files
##########

We need to define dimensions for all the parts that make up the model. We also
need to define placement values that place each part or assembly in the proper
position in the model. Using |OSC|, we will define parts individually, then
assemble parts into assemblies. These may be further combined to produce the
final model. Al l of that means we need to set up these constants and do some
calculations to get things right.

Rather than place dimensions directly in the files where they are needed, I
elected to factor them out into separate data files that get included as
needed. The scheme I came up with to organize these data files is outlined
here.

Part Data Files
***************

Within each part directory (no subdirectories in these), the part data file
contains values needed to create the part. These data files may include other
data files as needed to fully define the part. For that reason, all data items
include the part name to avois conflicts in other places.

Assembly Data Files
*******************

When combining parts (or other assemblies) we need data that helps properly
place all components to create the assembly. Data needed for assemblies is
located in an assembly data file.

Position Data Files
*******************

In order to facilitate design analysis, all positioning data items are located
in position data files. These are only located in assembly directories.

Naming Data
***********

All data items have a distinct name. As much as possible, no "bare" numbers
should be found in shape design files. Instead, we include the necessary data
files to create each component.

Hopefully, changes to the design can be made by adjusting data item values.
Changes in the shape design files should not be needed, unless you are changing
that shape in some fundamental way.

Data Catalog
************

..	todo::

    Add a catalog of all defined data. This will be generated using a Python
    script that scans all data files.
