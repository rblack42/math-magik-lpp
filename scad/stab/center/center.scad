//#####################################
// center.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>
include <./center_pos.scad>

use <MMlib/position.scad>
use <./spar/spar.scad>
use <./rib/rib.scad>
//use <./covering/covering.scad>

module center() {
  color(WOOD_Balsa) {
    align(le_pos) spar();
    align(rib1_pos) rib();
    align(rib2_pos) rib();
    align(rib3_pos) rib();
    align(te_pos) spar();
  }
  //align(covering_pos) covering();
}


//====================================
// display this shape
center();
