//###################################################
// stab.scad
// (c) 2021 - Roie R. Black
//***************************************************
include <./stab_data.scad>
include <./stab_pos.scad>

use <MMlib/position.scad>

use <./center/center.scad>
use <./right_tip/right_tip.scad>
use <./left_tip/left_tip.scad>
use <./stab_mount/stab_mount.scad>


module stab() {
    align(right_tip_pos) right_tip();
    align(center_pos) center();
    align(left_tip_pos) left_tip();
    align(stab_le_mount_pos) stab_mount();
    align(stab_te_mount_pos) stab_mount();

}

stab();

