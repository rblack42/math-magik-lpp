//######################################
// prop.scad
// (c) 2021 - Roie R. Black
//**************************************
include <MMlib/position.scad>
include <prop_pos.scad>

use <./prop_blade/prop_blade.scad>
use <./wire_shaft/wire_shaft.scad>
use <./prop_spar/prop_spar.scad>


module prop() {
  align(pos_blade1) prop_blade();
  align(pos_blade2)  prop_blade();
  prop_spar();
  position(pos_wire_shaft) wire_shaft();
}

//---------------------------------------
// debug display
prop();
