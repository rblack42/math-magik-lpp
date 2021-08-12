//####################################
// math-magik-lpp_pos.scad
// (c) 2021 - Roie R. Black
//************************************
include <math_magik_lpp_data.scad>
include <materials.scad>
include <fuselage/thrust_bearing/thrust_bearing_data.scad>
include <fuselage/motor_stick/motor_stick_data.scad>
include <fuselage/tail_boom/tail_boom_data.scad>


fuse_pos = [0,0,0,0,0,0];
wing_pos = [wing_x_offset,-ms_thickness/2-post_diameter/2,wing_elevation,0,0,0];

stab_y_offset = ms_thickness/2 + tb_thickness + post_diameter/2;
stab_pos = [stab_x_offset,-stab_y_offset,stab_elevation,0,0,0];
prop_pos = [prop_x_offset, 0, prop_z_offset, -40,0,0];
