//########################################
// fin_arc.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../fin_data.scad>

use <MMlib/circular_arc_spar.scad>

module fin_arc(r=fin_radius, size=spar_size) {
    circular_arc_spar(r, 180,270, size,size);
}

fin_arc();

