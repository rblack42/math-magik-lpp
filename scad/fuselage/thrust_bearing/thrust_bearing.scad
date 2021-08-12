//#####################################
// thrust-bearing.scad
// (c) 2021 - Roie R. Black
//=====================================
include <thrust_bearing_data.scad>

use <MMlib/prop_bearing_2D.scad>
$fn=100;

module thrust_bearing() {
  color(thrust_bearing_color)
    difference() {
      union() {
        translate([0,thb_width/2,0])
          rotate([90,0,0])
            linear_extrude(thb_width)
              prop_bearing_2D(
                thb_length,
                thb_height,
                thb_front_height,
                thb_top_length,
                thb_thickness
              );
        // front lower cap
        rotate([0,90,0])cylinder(r=thb_width/2,h=thb_thickness);
        // rear cap
        translate([thb_length-thb_thickness,0,0])
          rotate([0,90,0])
            cylinder(r=thb_width/2, h=thb_thickness);
      }
      translate([-0.1,0,0])
        rotate([0,90,0])
          cylinder(r=thb_wire_size/2,thb_length + 0.2);
    }
}

thrust_bearing();
