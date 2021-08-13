Position Catalog
################

..  csv-table::
    :header: Name, Value, File

    $fn,,
    ,"100",fuselage/wing_post/wing_post.scad
    ,"100",fuselage/stab_post/stab_post.scad
    arc_pos,,
    ,"[tip_radius, -tip_span + tip_radius, 0,0,0,0]",stab/left_tip/left_tip_pos.scad
    ,"[fin_radius, -fin_span + fin_radius, 0,0,0,0]",fuselage/fin/fin_pos.scad
    ,"[tip_radius, -tip_span + tip_radius, 0,0,0,0]",wing/left_tip/left_tip_pos.scad
    ,"[tip_radius, -tip_span + tip_radius, 0,0,0,0]",wing/left_tip/tip_arc/tip_arc_pos.scad
    center_pos,,
    ,"[0,0,0,0,0,0]",stab/stab_pos.scad
    ,"[0,0,0,0,0,0]",wing/wing_pos.scad
    covering_pos,,
    ,"[0,-center_span/2,spar_size,0,0,0]",stab/center/center_pos.scad
    ,"[0,0,0,0,0,0]",fuselage/fin/fin_pos.scad
    ,"[0,-center_span/2,spar_size,0,0,0]",wing/center/center_pos.scad
    fin_pos,,
    ,"[xf,-xt,5/64,90,-tail_boom_angle,0]",fuselage/fuselage_pos.scad
    fsp_pos,,
    ,"[xfsp,ysp,0,0,0,0]",fuselage/fuselage_pos.scad
    fuse_pos,,
    ,"[0,0,0,0,0,0]",math_magik_lpp_pos.scad
    fwp_pos,,
    ,"[fp_offset,-ms_thickness/2-post_diameter/2,0,0,0,0]",fuselage/fuselage_pos.scad
    le_pos,,
    ,"[0,0,0,0,0,0]",stab/center/center_pos.scad
    ,"[0,0,0,0,0,-90]",stab/left_tip/left_tip_pos.scad
    ,"[0,-fin_le_length/2-spar_size,0,0,0,0]",fuselage/fin/fin_pos.scad
    ,"[0,0,0,0,0,0]",wing/center/center_pos.scad
    ,"[0,0,0,0,0,-90]",wing/left_tip/left_tip_pos.scad
    left_tip_cover_pos,,
    ,"[0,0,0,0,0,0]",stab/left_tip/left_tip_pos.scad
    ,"[0,0,0,0,0,0]",wing/left_tip/left_tip_pos.scad
    left_tip_pos,,
    ,"[0, -center_span/2, 0, 0,0,0]",stab/stab_pos.scad
    ,"[0, -center_span/2, 0, -tip_dihedral_angle,0,0]",wing/wing_pos.scad
    ms_pos,,
    ,"[0,ms_thickness/2,0,90,0,0]",fuselage/fuselage_pos.scad
    pos_blade1,,
    ,"[0,0,prop_blade_offset,0,0,prop_pitch_angle]",prop/prop_pos.scad
    pos_blade2,,
    ,"[0,0,-prop_blade_offset,180,0,-prop_pitch_angle]",prop/prop_pos.scad
    pos_spar,,
    ,"[0,0,0,0,0,0]",prop/prop_pos.scad
    pos_wire_shaft,,
    ,"[-1/64,0,0,0,0,0]",prop/prop_pos.scad
    prop_pos,,
    ,"[prop_x_offset, 0, prop_z_offset, -40,0,0]",math_magik_lpp_pos.scad
    rh_pos,,
    ,"[ms_length,0,0,0,0,0]",fuselage/fuselage_pos.scad
    rib1_pos,,
    ,"[spar_size,-center_span/2+spar_size/2,0,0,0,0]",stab/center/center_pos.scad
    ,"[tip_rib_chord/2 + tip_radius,-tip_span,0,0,0,90]",stab/left_tip/left_tip_pos.scad
    ,"[fin_chord/2,-spar_size,0,0,0,90]",fuselage/fin/fin_pos.scad
    ,"[spar_size,-center_span/2+spar_size/2,0,0,0,0]",wing/center/center_pos.scad
    ,"[tip_rib_chord/2 + tip_radius,-tip_span,0,0,0,90]",wing/left_tip/left_tip_pos.scad
    rib2_pos,,
    ,"[spar_size,0,0,0,0,0]",stab/center/center_pos.scad
    ,"[(fin_chord+fin_radius)/2-spar_size/2,-fin_span,0,0,0,90]",fuselage/fin/fin_pos.scad
    ,"[spar_size,-center_span/4,0,0,0,0]",wing/center/center_pos.scad
    rib3_pos,,
    ,"[spar_size,center_span/2-spar_size/2,0,0,0,0]",stab/center/center_pos.scad
    ,"[spar_size,0,0,0,0,0]",wing/center/center_pos.scad
    rib4_pos,,
    ,"[spar_size,center_span/4,0,0,0,0]",wing/center/center_pos.scad
    rib5_pos,,
    ,"[spar_size,center_span/2-spar_size/2,0,0,0,0]",wing/center/center_pos.scad
    right_tip_pos,,
    ,"[0, center_span/2, 0, 0,0,0]",stab/stab_pos.scad
    ,"[0, center_span/2, 0, tip_dihedral_angle,0,0]",wing/wing_pos.scad
    rsp_pos,,
    ,"[xrsp,ysp,0,0,0,0]",fuselage/fuselage_pos.scad
    rwp_pos,,
    ,"[rp_offset,-ms_thickness/2-post_diameter/2,0,0,0,0]",fuselage/fuselage_pos.scad
    stab_le_mount_pos,,
    ,"[-post_diameter/2-tube_thickness,0,0,0,0,0]",stab/stab_pos.scad
    stab_pos,,
    ,"[stab_x_offset,-stab_y_offset,stab_elevation,0,0,0]",math_magik_lpp_pos.scad
    stab_te_mount_pos,,
    ,"[max_stab_chord+post_diameter/2+tube_thickness,0,0,0,0,0]",stab/stab_pos.scad
    stab_y_offset,,
    ,"ms_thickness/2 + tb_thickness + post_diameter/2",math_magik_lpp_pos.scad
    t,,
    ,"post_diamete",fuselage/wing_post/wing_post.scad
    ,"post_diamete",fuselage/stab_post/stab_post.scad
    tb_pos,,
    ,"[ms_length - 1/8, -ms_thickness/2-tb_thickness/2,0,0,0,0]",fuselage/fuselage_pos.scad
    te_pos,,
    ,"[max_stab_chord - spar_size,0,0,0,0,0]",stab/center/center_pos.scad
    ,"[max_stab_chord - spar_size,0,0,0,0,-90]",stab/left_tip/left_tip_pos.scad
    ,"[fin_chord - spar_size,-fin_te_length/2 - spar_size,0,0,0,0]",fuselage/fin/fin_pos.scad
    ,"[max_wing_chord - spar_size,0,0,0,0,0]",wing/center/center_pos.scad
    ,"[max_wing_chord - spar_size,0,0,0,0,-90]",wing/left_tip/left_tip_pos.scad
    thb_pos,,
    ,"[-thb_length+1/4,0,-thb_height,0,0,0]",fuselage/fuselage_pos.scad
    wing_le_mount_pos,,
    ,"[-post_diameter/2-tube_thickness,0,0,0,0,0]",wing/wing_pos.scad
    wing_pos,,
    ,"[wing_x_offset,-ms_thickness/2-post_diameter/2,wing_elevation,0,0,0]",math_magik_lpp_pos.scad
    wing_te_mount_pos,,
    ,"[max_wing_chord+post_diameter/2+tube_thickness,0,0,0,0,0]",wing/wing_pos.scad
    xf,,
    ,"ms_length + tail_boom_length - 1/8 - max_stab_chord",fuselage/fuselage_pos.scad
    xfsp,,
    ,"xf-post_diameter/2",fuselage/fuselage_pos.scad
    xrsp,,
    ,"xf+max_stab_chord+post_diameter/2",fuselage/fuselage_pos.scad
    xt,,
    ,"(ms_thickness + tb_thickness-thb_thickness)/2",fuselage/fuselage_pos.scad
    ysp,,
    ,"-ms_thickness/2-tb_thickness-post_diameter/2",fuselage/fuselage_pos.scad
    z1,,
    ,"wing_post_height",fuselage/wing_post/wing_post.scad
    ,"stab_post_height",fuselage/stab_post/stab_post.scad
    z2,,
    ,"wing_post_height-tube_height",fuselage/wing_post/wing_post.scad
    ,"stab_post_height-tube_height",fuselage/stab_post/stab_post.scad
