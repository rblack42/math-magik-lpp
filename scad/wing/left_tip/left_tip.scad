//#####################################
// left_tip.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>
include <./left_tip_pos.scad>

use <MMlib/position.scad>


use <./tip_arc/tip_arc.scad>
use <./leading_edge/leading_edge.scad>
use <./trailing_edge/trailing_edge.scad>
use <./tip_rib/tip_rib.scad>
use <./covering/left_tip_covering.scad>


module left_tip() {
  color(WOOD_Balsa) {
    align(le_pos) leading_edge();
    align(te_pos) trailing_edge();
    align(arc_pos) tip_arc();
    align(rib1_pos) tip_rib();
  }
  //align(left_tip_cover_pos) 
  left_tip_covering();
}

//--------------------------------------
// debug display

left_tip();

