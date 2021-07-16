//##########################################
// spar.scad = wing center section
// (c) 2021 by Roie R. Black
//==========================================
include <../../wing_data.scad>
use <MMlib/square_spar.scad>

module spar() {
		square_spar(center_span, spar_size);
}

//==========================================
// display this shape
spar();


