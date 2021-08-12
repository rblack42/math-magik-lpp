//########################################
// wing_pos.scad
// (c) 2021 - Roie R. Black
//****************************************
include <./wing_data.scad>
include <../materials.scad>


center_pos = [0,0,0,0,0,0];
left_tip_pos = [0, -center_span/2, 0, -tip_dihedral_angle,0,0];
right_tip_pos = [0, center_span/2, 0, tip_dihedral_angle,0,0];
wing_le_mount_pos = [-post_diameter/2-tube_thickness,0,0,0,0,0];
wing_te_mount_pos = [max_wing_chord+post_diameter/2+tube_thickness,0,0,0,0,0];
