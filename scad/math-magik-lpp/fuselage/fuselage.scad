//##########################################
// fuselage.scad
// (c) 2021 - Roie R. Black
//******************************************
include <./fuselage_pos.scad>

use <./motor_stick/motor_stick.scad>
use <./tail_boom/tail_boom.scad>
use <./rear_hook/rear_hook.scad>
use <./thrust_bearing/thrust_bearing.scad>
use <./wing_post/wing_post.scad>
use <./stab_post/stab_post.scad>
use <./fin/fin.scad>

use <MMlib/position.scad>

module fuselage() {
  align(ms_pos) motor_stick();
  align(tb_pos) tail_boom();
  align(rh_pos) rear_hook();
  align(thb_pos) thrust_bearing();
  align(fin_pos) fin();
  align(fwp_pos) wing_post();
  align(rwp_pos) wing_post();
  align(fsp_pos) stab_post();
  align(rsp_pos) stab_post();
}

//----------------------------------------------
// debug display
fuselage();
