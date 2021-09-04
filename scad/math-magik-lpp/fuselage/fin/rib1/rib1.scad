//########################################
// fin_rib1.scad
// (c) 2021 - Roie R. Black
//****************************************
include <../fin_data.scad>

use <MMlib/square_spar.scad>

module rib1() {
  square_spar(fin_chord, spar_size);
}

rib1();
