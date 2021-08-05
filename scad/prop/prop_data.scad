//#####################################
// prop-blade-data.scad
// (c) 2021 by Roie R. Black
//*************************************
include <colors.scad>
include <../constraints.scad>

// Propeller dimensions
prop_radius = max_prop_diameter/2;
prop_pitch_angle = 40;
prop_blade_offset = 0.5;

// prop spar dimensions
prop_spar_inner_radius = 1/32;
prop_spar_outer_radius = 1/64;
prop_spar_length = 4;

prop_spar_color = WOOD_Balsa;

// prop blade dimensions
prop_blade_thickness = 1/64;
prop_max_chord = 1.85;

// prop form dimensions
prop_form_radius = 2.5;
prop_form_height = prop_radius + 2;
prop_form_angle = 14;

// elliptic form data
s = prop_radius - 1;
c = 2.5;
f = 2;
s1 = 1;
s2 = s - s1;
s3 = 1;
s4 = 1;

prop_blade_color = WOOD_Balsa;

//-------------------------------------
// calculated by analysis
prop_forward_x = -1.3287;


