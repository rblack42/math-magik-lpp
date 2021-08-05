//#####################################
// fin.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>
use <MMlib/position.scad>
include <./fin_pos.scad>

use <./fin_arc/fin_arc.scad>
use <./leading_edge/leading_edge.scad>
use <./trailing_edge/trailing_edge.scad>
use <./fin_rib1/fin_rib1.scad>
use <./fin_rib2/fin_rib2.scad>
use <./fin_arc/fin_arc.scad>
//use <./covering/covering.scad>


module fin() {
  color(WOOD_Balsa) {
    align(le_pos) leading_edge();
    align(te_pos) trailing_edge();
    align(arc_pos) fin_arc();
    align(rib1_pos) fin_rib1();
    align(rib2_pos) fin_rib2();
  }
  //rotate([180,0,0]) right_tip_covering();
}

//--------------------------------------
// debug display

fin();

