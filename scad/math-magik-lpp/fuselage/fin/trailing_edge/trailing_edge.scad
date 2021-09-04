//#####################################
// te.scad = wing center section
// (c) 2021 by Roie R. Black
//=====================================
include <../fin_data.scad>
use <MMlib/square_spar.scad>

module trailing_edge() {
		square_spar(fin_te_length,spar_size);
}

//====================================
// display this shape
trailing_edge();


