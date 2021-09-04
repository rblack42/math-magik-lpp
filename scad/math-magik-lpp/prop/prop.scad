//######################################
// prop.scad
// (c) 2021 - Roie R. Black
//**************************************
include <MMlib/position.scad>
include <prop_pos.scad>

use <./blade/blade.scad>
use <./wire_shaft/wire_shaft.scad>
use <./spar/spar.scad>


module prop() {
  align(pos_blade1) blade();
  align(pos_blade2) blade();
  align(pos_spar) spar();
  align(pos_wire_shaft) wire_shaft();
}

//---------------------------------------
// debug display
prop();
