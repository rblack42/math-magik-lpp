//###########################################################
// prop_pos.scad - prop positioning data
// (c) 2021 by Roie R. Black
//===========================================================
include <prop_data.scad>

pos_spar = [0,0,0,0,0,0];

pos_blade1 = [0,0,prop_blade_offset,0,0,prop_pitch_angle];
pos_blade2 = [0,0,-prop_blade_offset,180,0,-prop_pitch_angle];

pos_wire_shaft = [-1/64,0,0,0,0,0];
