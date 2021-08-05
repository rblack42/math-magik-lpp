//#####################################
// leading_edge.scad = wing center section
// (c) 2021 by Roie R. Black
//=====================================
include <../fin_data.scad>
use <MMlib/square_spar.scad>

module leading_edge() {
		square_spar(fin_le_length,spar_size);
}

//====================================
// display this shape
leading_edge();
