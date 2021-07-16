//#####################################
// left_tip.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>
include <./left_tip_pos.scad>

use <MMlib/position.scad>


use <./arc/arc.scad>
use <./le/le.scad>
use <./te/te.scad>
use <./rib1/rib1.scad>
use <./arc/arc.scad>
//use <./covering/covering.scad>


module left_tip() {
  color(WOOD_Balsa) {
    align(le_pos) le();
    align(te_pos) te();
    align(arc_pos) arc();
    align(rib1_pos) rib1();
  }
  //rotate([180,0,0]) right_tip_covering();
}

//--------------------------------------
// debug display

left_tip();

