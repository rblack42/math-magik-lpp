//#####################################
// fin.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>
use <MMlib/position.scad>
include <./fin_pos.scad>

use <./arc/arc.scad>
use <./leading_edge/leading_edge.scad>
use <./trailing_edge/trailing_edge.scad>
use <./rib1/rib1.scad>
use <./rib2/rib2.scad>
use <./arc/arc.scad>
use <./covering/covering.scad>


module fin() {
  color(WOOD_Balsa) {
    align(le_pos) leading_edge();
    align(te_pos) trailing_edge();
    align(arc_pos) arc();
    align(rib1_pos) rib1();
    align(rib2_pos) rib2();
  }
  align(covering_pos) covering();
}

//--------------------------------------
// debug display

fin();

