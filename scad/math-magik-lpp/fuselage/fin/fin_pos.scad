//########################################
// arc_pos.scad
// (c) 2021 - Roie R. Black
//****************************************
include <./fin_data.scad>

le_pos = [0,-fin_le_length/2-spar_size,0,0,0,0];
te_pos = [fin_chord - spar_size,-fin_te_length/2 - spar_size,0,0,0,0];
arc_pos = [fin_radius, -fin_span + fin_radius, 0,0,0,0];
rib1_pos = [fin_chord/2,-spar_size,0,0,0,90];
rib2_pos = [(fin_chord+fin_radius)/2-spar_size/2,-fin_span,0,0,0,90];
covering_pos = [0,0,0,0,0,0];
