//#####################################
// stab_post.scad
// (c) 2021 by Roie R. Black
//*************************************
include <stab_post_data.scad>
$fn=100;
use <MMlib/rounded_post.scad>

module stab_post() {
  color(stab_post_color)
    translate([0,0,0])
      rounded_post(
        z1=stab_post_height,
        z2= stab_post_height-tube_height,
        t = post_diameter
      );
}

//---------------------------------------
// debug display

stab_post();


