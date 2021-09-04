//########################################
// center_pos.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../stab_data.scad>

le_pos = [0,0,0,0,0,0];
te_pos = [max_stab_chord - spar_size,0,0,0,0,0];
rib1_pos = [spar_size,-center_span/2+spar_size/2,0,0,0,0];
rib2_pos = [spar_size,0,0,0,0,0];
rib3_pos = [spar_size,center_span/2-spar_size/2,0,0,0,0];
covering_pos = [0,-center_span/2,spar_size,0,0,0];
