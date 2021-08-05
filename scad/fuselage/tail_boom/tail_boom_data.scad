//#####################################
// tail-boom.data
// (c) 2021 by Roie R. Black
//*************************************
include <colors.scad>
include <../fuselage_data.scad>

density = 6;
tb_color = WOOD_Balsa;

tb_front_height = 3/16;
tb_rear_height = 1/16;
tb_thickness = 3/32;

//-------------------------------------
// calculated values

tail_boom_angle = atan2(tb_front_height - tb_rear_height,tail_boom_length);
