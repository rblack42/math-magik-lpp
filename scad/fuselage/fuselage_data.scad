//###########################################
// fuselage-data.scad
// (c) 2021 - Roie R. Black
//*******************************************
include <../constraints.scad>
include <../materials.scad>
include <thrust_bearing/thrust_bearing_data.scad>
include <motor_stick/motor_stick_data.scad>
include <../prop/prop_data.scad>

// prop adjustment
prop_x_offset = 1/16;

// wing position dimensions
wing_offset = 1.625;
wing_elevation = 3;

// tail boom data
tb_color = WOOD_Balsa;

tb_front_height = 3/16;
tb_rear_height = 1/16;
tb_thickness = 3/32;

tail_boom_overlap = 1/8;
tail_boom_length = max_overall_length -ms_length + prop_forward_x + tail_boom_overlap;
tail_boom_rear_x = max_overall_length + prop_x_offset;


//adjust motor stick to fit bearing
fuse_offset = thb_length - thb_top_length - 3 * tube_thickness;
prop_z_offset = thb_height;

// front post position
fp_offset = wing_offset - post_diameter/2 - tube_thickness;

// rear post position
rp_offset = wing_offset + max_wing_chord + post_diameter/2 + tube_thickness;


//-------------------------------------
// calculated values

tail_boom_angle = atan2(tb_front_height - tb_rear_height,tail_boom_length);

// stab positioning data
srp_offset = tail_boom_rear_x - post_diameter - tube_thickness-1/16;
sfp_offset = srp_offset - max_stab_chord - post_diameter - tube_thickness-1/64;
