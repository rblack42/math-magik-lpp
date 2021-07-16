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
        translate([0,width/2,0])
          rotate([90,0,0])
            linear_extrude(width)
              prop_bearing_2D(
                length,
                height,
                front_height,
                top_length,
                thickness
              );
        // front lower cap
        rotate([0,90,0])cylinder(r=width/2,h=thickness);
        // rear cap
        translate([length-thickness,0,0])
          rotate([0,90,0])
            cylinder(r=width/2, h=thickness);
      }
      translate([-0.1,0,0])
        rotate([0,90,0])
          cylinder(r=wire_size/2,length + 0.2);
    }
}

thrust_bearing();
