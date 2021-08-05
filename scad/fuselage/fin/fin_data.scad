//#####################################
// fin-data.scad
// (c) 2021 by Roie R. Black
//=====================================
include <colors.scad>

fin_span = 2;
fin_chord = 4;
fin_radius = 1.5;
spar_size = 1/32;
fin_color = WOOD_Balsa;

//-------------------------------------
// calculated values

fin_le_length = fin_span - fin_radius - spar_size;
fin_te_length = fin_span -2*spar_size;

