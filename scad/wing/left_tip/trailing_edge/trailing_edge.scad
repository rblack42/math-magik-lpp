//#####################################
// te.scad = wing center section
// (c) 2021 by Roie R. Black
//=====================================
include <../../wing_data.scad>
use <MMlib/double_taper_spar.scad>

s1 = spar_size;
s2 = spar_size/2;


module trailing_edge() {
		double_taper_spar(tip_span,s1,s2,s1,s2);
}

//====================================
// display this shape
trailing_edge();


