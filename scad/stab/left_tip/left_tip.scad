//#####################################
// left_tip.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>
use <MMlib/position.scad>
include <./left_tip_pos.scad>

use <./tip_arc/tip_arc.scad>
use <./leading_edge/leading_edge.scad>
use <./trailing_edge/trailing_edge.scad>
use <./tip_rib/tip_rib.scad>
use <./tip_arc/tip_arc.scad>
//use <./covering/covering.scad>


module left_tip() {
  color(WOOD_Balsa) {
    align(le_pos) leading_edge();
    align(te_pos) trailing_edge();
    align(arc_pos) tip_arc();
    align(rib1_pos) tip_rib();
  }
  //rotate([180,0,0]) right_tip_covering();
}

//--------------------------------------
// debug display

left_tip();

