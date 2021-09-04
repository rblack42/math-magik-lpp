//########################################
// arc_pos.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../wing_data.scad>

le_pos = [0,0,0,0,0,-90];
te_pos = [max_wing_chord - spar_size,0,0,0,0,-90];
arc_pos = [tip_radius, -tip_span + tip_radius, 0,0,0,0];
rib1_pos = [tip_rib_chord/2 + tip_radius,-tip_span,0,0,0,90];
left_tip_cover_pos = [0,0,0,0,0,0];
