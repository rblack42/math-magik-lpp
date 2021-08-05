//####################################
// math-magik-lpp_data.scad
// (c) 2021 - Roie R. Black
//************************************
include <constraints.scad>

// calculated prop width
prop_x_width = 1.3287;
prop_x_offset = -1/4 - 1/32;
prop_z_offset = -3/16;

// fuselage data
thrust_bearing_x_offset = -1/4;

// wing design constants
wing_x_offset = 1.625;
wing_elevation = 3;
wing_rib_camber = 4;
wing_center_span = 12;
wing_tip_radius = 2;
wing_spar_size = 1/16;


// stab dimensions
stab_x_offset = max_overall_length - prop_x_width - max_stab_chord;
stab_center_span = 6;
stab_rib_camber = 2;
stab_tip_radius = 1.5;
stab_elevation = 0.5;

// motor stick dimensions
motor_stick_thickness = 1/8;

// post size
post_size = 1/16;


