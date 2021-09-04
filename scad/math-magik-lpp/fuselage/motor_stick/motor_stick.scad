//#####################################
// motor-stick.scad
// (c) 2021 - Roie R. Black
//*************************************
include <colors.scad>
include <motor_stick_data.scad>


module motor_stick() {
  color(WOOD_Balsa)
	  linear_extrude(
	      height = ms_thickness,
	      center=false,
	      convexity=10
	  )
        polygon(ms_points);
}

//-------------------------------------
// debug display

motor_stick();
