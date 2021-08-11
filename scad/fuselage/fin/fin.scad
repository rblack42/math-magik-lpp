//#####################################
// fin.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>
use <MMlib/position.scad>
include <./fin_pos.scad>

use <./arc/fin_arc.scad>
use <./leading_edge/leading_edge.scad>
use <./trailing_edge/trailing_edge.scad>
use <./rib1/fin_rib1.scad>
use <./rib2/fin_rib2.scad>
use <./arc/fin_arc.scad>
use <./covering/fin_covering.scad>


module fin() {
  color(WOOD_Balsa) {
    align(le_pos) leading_edge();
    align(te_pos) trailing_edge();
    align(arc_pos) fin_arc();
    align(rib1_pos) fin_rib1();
    align(rib2_pos) fin_rib2();
  }
  align(covering_pos) fin_covering();
}

//--------------------------------------
// debug display

fin();

