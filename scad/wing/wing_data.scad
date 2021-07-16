//#####################################
// wing.data
// (c) 2021 by Roie R. Black
//=====================================
include <../constraints.scad>

// center section dimensions
center_span = 12;
spar_size = 1/16;
rib_chord = max_wing_chord - 2 * spar_size;
rib_camber = 4;
num_center_ribs = 5;

// tip section dimensions
tip_dihedral = 1.75;
tip_radius = 2;
a = tip_dihedral;
b = (max_projected_wing_span - center_span)/2;
tip_span = sqrt(a*a + b*b);
tip_dihedral_angle = atan2(a,b);
tip_le_span = tip_span - tip_radius;
tip_rib_chord = max_wing_chord - tip_radius - spar_size;

echo(tip_dihedral_angle);