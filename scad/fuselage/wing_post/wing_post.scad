//#####################################
// wing_post.scad
// (c) 2021 by Roie R. Black
//*************************************
include <wing_post_data.scad>
$fn=100;
use <MMlib/rounded_post.scad>

module wing_post() {
  color(wing_post_color)
    translate([0,0,0])
      rounded_post(
        z1=wing_post_height,
        z2= wing_post_height-tube_height,
        t = post_diameter
      );
}

//---------------------------------------
// debug display

wing_post();


