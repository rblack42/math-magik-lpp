//###################################################
// rib.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <../../wing_data.scad>

use <MMlib/circle_template_rib.scad>

module rib() {
    circle_template_rib(rib_chord, rib_camber, spar_size, spar_size);
}

rib();

