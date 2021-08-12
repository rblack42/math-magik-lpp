//#####################################
// fuselage_pos.scad
// (c) 2021 by Roie R. Black
//*************************************
include <./motor_stick/motor_stick_data.scad>
include <./tail_boom/tail_boom_data.scad>
include <./thrust_bearing/thrust_bearing_data.scad>
include <../materials.scad>

// motor stick positioning
ms_pos = [0,ms_thickness/2,0,90,0,0];

// tail boom positioning
tb_pos = [ms_length - 1/8, -ms_thickness/2-tb_thickness/2,0,0,0,0];

// rear hook positioning
rh_pos = [ms_length,0,0,0,0,0];

// thrust bearing positioning
thb_pos = [-thb_length+1/4,0,-thb_height,0,0,0];


xf = ms_length + tail_boom_length - 1/8 - max_stab_chord;
xt = (ms_thickness + tb_thickness-thb_thickness)/2;
fin_pos = [xf,-xt,5/64,90,-tail_boom_angle,0];

// wing post positioning
fwp_pos = [fp_offset,-ms_thickness/2-post_diameter/2,0,0,0,0];
rwp_pos = [rp_offset,-ms_thickness/2-post_diameter/2,0,0,0,0];

// stab post positioning
xfsp = xf-post_diameter/2;
xrsp = xf+max_stab_chord+post_diameter/2;
ysp = -ms_thickness/2-tb_thickness-post_diameter/2;
fsp_pos = [xfsp,ysp,0,0,0,0];
rsp_pos = [xrsp,ysp,0,0,0,0];
