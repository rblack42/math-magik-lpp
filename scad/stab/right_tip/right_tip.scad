//#####################################
// right-tip.scad
// (c) 2021 by Roie R. Black
//=====================================
use <../left_tip/left_tip.scad>

module right_tip() {
  mirror([0,1,0]) left_tip();
}

//--------------------------------------
// debug display

right_tip();

