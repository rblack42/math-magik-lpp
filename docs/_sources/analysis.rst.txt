Analysis of Design
##################

In this section, we will use the analysis toold presented in the main |MM| project at https://rblack42/github.io/math-magik to get an estimate of the model weight and center of gravity location.

Material Densities
******************

|OSC| will generate a |STL| file for each part we need to construct to build an
actual model. Typically, builders select wood with properties appropriate fpr
that part. We need to record the material density for each part so we can
calculate the weight and balance data.

Model Weight
************

THis calculation is simple. A |PY| program will run |OSC| and automatically
generate the part **STL** file. It will then run a *mass properties* assessment
to determine the volume and center of mass for each part. The total weight of
the model can be determined by multiplying the part volume by the material
density, then summing up the weights of all parts.

Center of Gravity
*****************

Locating the center of gravity is more difficult. The *mass properties*
analysis will give us the center of mass for each part. We need to follow the
alignment transformations made on that part as it is located in the final model
to determine the center of gravity. These alignments are sequential. A rib it
aligned within a wing, and the wing is aligned within the model. By placing all
positioning data in a separate **name_pos.scad** file, we can use Python to
calculate the final position of the center of mass for a part in the model. The
center of gravity calculation can be made using this information.



