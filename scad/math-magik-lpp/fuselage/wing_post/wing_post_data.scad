//#####################################
// wing_post_data.scad
// (c) 2021 by Roie R. Black
//*************************************
include <../fuselage_data.scad>
include <colors.scad>
include <../../materials.scad>

density = 5;

wing_post_color = WOOD_Balsa;
wing_post_height = wing_elevation + tube_height;
