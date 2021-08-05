//########################################
// wing_pos.scad
// (c) 2021 - Roie R. Black
//****************************************
include <./wing_data.scad>

center_pos = [0,0,0,0,0,0];
left_tip_pos = [0, -center_span/2, 0, -tip_dihedral_angle,0,0];
right_tip_pos = [0, center_span/2, 0, tip_dihedral_angle,0,0];
