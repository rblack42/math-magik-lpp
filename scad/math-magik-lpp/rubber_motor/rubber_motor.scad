//##################################################
// rubber_motor.scad - Math-Magik-LPP
// (c) 2021 by Roie R Black
//==================================================
$fn=100;
include <MMlib/colors.scad>

// alignment: centered along X axis

module rubber_motor() {
	rotate([0,90,0])
		color("Tan") cylinder(h=10, r=1/8);
}

//=================================================
rubber_motor();
