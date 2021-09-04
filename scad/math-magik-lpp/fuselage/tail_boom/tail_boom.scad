//#########################################
// tail_boom.scad
// (c) 2021 - Roie R. Black
//*****************************************
include <tail_boom_data.scad>

use <MMlib/single_taper_spar.scad>


module tail_boom() {
  color(tb_color) {
    translate([0,tb_thickness/2,tb_front_height])
      rotate([180,0,0])
        single_taper_spar(
          l=tail_boom_length,
          z1=tb_front_height,
          z2=tb_rear_height,
          t=tb_thickness
        );
  }
}

//-----------------------------------------
// debug display

tail_boom();
