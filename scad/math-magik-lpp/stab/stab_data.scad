//#####################################
// stab.data
// (c) 2021 by Roie R. Black
//=====================================
include <../constraints.scad>

// center section dimensions
center_span = 6;
spar_size = 1/16;
rib_chord = max_stab_chord - 2 * spar_size;
rib_camber = 2;
num_center_ribs = 3;

// tip section dimensions
tip_span = (max_stab_span - center_span)/2;
tip_radius = 1.5;
tip_le_span = tip_span - tip_radius;
tip_rib_chord = max_stab_chord - tip_radius - spar_size;
