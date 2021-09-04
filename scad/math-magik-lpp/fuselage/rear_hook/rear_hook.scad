//#######################################
// rear_hook.scad
// (c) 2021 - Roie R. Black
//***************************************
include <rear_hook_data.scad>
$fn=100;


module rear_hook() {
  color(rear_hook_color) {
    // rear of ms
    cylinder(r=r,h=b);

    // top  bend
    translate(p1)
    rotate([90,0,0])
      rotate_extrude(angle=90, convexity=10)
        translate([bend_radius, 0])
          circle(r);
    // top stub
    translate(p1 + [-stub_length,0,bend_radius])
      rotate([0,90,0])
        cylinder(r=r, h=stub_length);

    // lower ms  bend
    translate(p2)
      rotate([90,0,0])
        rotate_extrude(angle=-45, convexity=10)
          translate([bend_radius, 0])
            circle(r);


    // upper hook side
    translate(p3)
      rotate([0,-135,0])
        cylinder(r=r,h=hook_side);

    // hook bend
    translate(p4)
      rotate([90,-135,0])
        rotate_extrude(angle=90, convexity=10)
          translate([bend_radius, 0])
            circle(r);

    // lower hook side
    translate(p5)
      rotate([0,135,0])
        cylinder(r=r,h=hook_side);
  }
}

rear_hook();
