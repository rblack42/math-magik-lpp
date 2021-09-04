//########################################
// fin_rib2.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../fin_data.scad>

use <MMlib/square_spar.scad>

module rib2() {
  square_spar(fin_chord-fin_radius+spar_size, spar_size);
}

rib2();

