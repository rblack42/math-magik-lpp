//######################################
// wire-shaft.scad
// (c) 2021 Roie R. Black
//**************************************
include <colors.scad>
include <wire_shaft_data.scad>
$fn=100;


module wire_shaft() {
  r = wire_diameter/2;
  translate([length,0,0]) {
    rotate([0,90,-90])
      color(METAL_Steel) {
        // hook
        translate([-hook_radius/2,1.5*hook_radius,0])
        rotate_extrude(angle=270, convexity=10)
          translate([hook_radius, 0])
            circle(r);

        // 90 degree bend
        translate([-hook_radius/2,0,0])
          rotate_extrude(angle=90, convexity=10)
            translate([hook_radius/2, 0])
              circle(r);

        // straight shaft
        translate([0,0,0])
          rotate([90,0,0])
            cylinder(r=r,h=length);

        // 90 degree bend
        translate([-hook_radius/2,-length,0])
          rotate_extrude(angle=-90, convexity=10)
            translate([hook_radius/2,0])
              circle(r);

        // final straight
        translate([-hook_radius/2,-length- hook_radius/2,0])
          rotate([0,-90,0])
            cylinder(r=r,h=stub_length);
    }
  }
}

//-------------------------------------
// debug display

wire_shaft();
