//#################################################
// wing_mount.scad
// (c) 2021 Roie R. Black
//=================================================
include <../../materials.scad>
use <MMlib/paper_tube.scad>

module wing_mount() {
  color("Yellow")
	  paper_tube(post_diameter/2,tube_height,tube_thickness);
}

wing_mount();
