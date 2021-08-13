Data Catalog
################

..  csv-table::
    :header: Name, Value, File

    a,,
    ,"stub_length",fuselage/rear_hook/rear_hook_data.scad
    ,"tip_dihedral",wing/wing_data.scad
    b,,
    ,"ms_height - wire_diameter",fuselage/rear_hook/rear_hook_data.scad
    ,"(max_projected_wing_span - center_span)/2",wing/wing_data.scad
    bend_radius,,
    ,"1.5*wire_diameter",fuselage/rear_hook/rear_hook_data.scad
    c,,
    ,"2.5",prop/prop_data.scad
    ,"hook_side",fuselage/rear_hook/rear_hook_data.scad
    center_span,,
    ,"6",stab/stab_data.scad
    ,"12",wing/wing_data.scad
    density,,
    ,"501.12",fuselage/rear_hook/rear_hook_data.scad
    ,"168.77",fuselage/thrust_bearing/thrust_bearing_data.scad
    ,"6",fuselage/tail_boom/tail_boom_data.scad
    f,,
    ,"2",prop/prop_data.scad
    fin_chord,,
    ,"4",fuselage/fin/fin_data.scad
    fin_color,,
    ,"WOOD_Balsa",fuselage/fin/fin_data.scad
    fin_le_length,,
    ,"fin_span - fin_radius - spar_size",fuselage/fin/fin_data.scad
    fin_radius,,
    ,"1.5",fuselage/fin/fin_data.scad
    fin_span,,
    ,"2",fuselage/fin/fin_data.scad
    fin_te_length,,
    ,"fin_span -2*spar_size",fuselage/fin/fin_data.scad
    fp_offset,,
    ,"wing_offset - post_diameter/2 - tube_thickness",fuselage/fuselage_data.scad
    fuse_offset,,
    ,"thb_length - thb_top_length - 3 * tube_thickness",fuselage/fuselage_data.scad
    hook_offset,,
    ,"thb_height",fuselage/rear_hook/rear_hook_data.scad
    hook_side,,
    ,"(hook_offset - 2*bend_radius*ka)/ka",fuselage/rear_hook/rear_hook_data.scad
    ka,,
    ,"sin(45)",fuselage/rear_hook/rear_hook_data.scad
    motor_stick_rear_height,,
    ,"0.1875",fuselage/motor_stick/motor_stick_data.scad
    motor_stick_thickness,,
    ,"1/8",math_magik_lpp_data.scad
    ms_height,,
    ,"motor_stick_rear_height",fuselage/rear_hook/rear_hook_data.scad
    ms_length,,
    ,"10",fuselage/motor_stick/motor_stick_data.scad
    ms_points,,
    ,"",fuselage/motor_stick/motor_stick_data.scad
    ms_thickness,,
    ,"1/8",fuselage/motor_stick/motor_stick_data.scad
    num_center_ribs,,
    ,"3",stab/stab_data.scad
    ,"5",wing/wing_data.scad
    p1,,
    ,"[-bend_radius,0,b]",fuselage/rear_hook/rear_hook_data.scad
    p2,,
    ,"[-bend_radius,0,0]",fuselage/rear_hook/rear_hook_data.scad
    p3,,
    ,"p2 + [bend_radius*ka,0,-bend_radius*ka]",fuselage/rear_hook/rear_hook_data.scad
    p4,,
    ,"p3 + [-hook_side*ka, 0,-hook_side*ka] + [bend_radius*ka,0,-bend_radius*ka]",fuselage/rear_hook/rear_hook_data.scad
    p5,,
    ,"p4 + [-bend_radius*ka,0,-bend_radius*ka]",fuselage/rear_hook/rear_hook_data.scad
    post_size,,
    ,"1/16",math_magik_lpp_data.scad
    prop_blade_color,,
    ,"WOOD_Balsa",prop/prop_data.scad
    prop_blade_offset,,
    ,"0.5",prop/prop_data.scad
    prop_blade_thickness,,
    ,"1/64",prop/prop_data.scad
    prop_form_angle,,
    ,"14",prop/prop_data.scad
    prop_form_height,,
    ,"prop_radius + 2",prop/prop_data.scad
    prop_form_radius,,
    ,"2.5",prop/prop_data.scad
    prop_forward_x,,
    ,"-1.3287",prop/prop_data.scad
    prop_max_chord,,
    ,"1.85",prop/prop_data.scad
    prop_pitch_angle,,
    ,"40",prop/prop_data.scad
    prop_radius,,
    ,"max_prop_diameter/2",prop/prop_data.scad
    prop_spar_color,,
    ,"WOOD_Balsa",prop/prop_data.scad
    prop_spar_inner_radius,,
    ,"1/32",prop/prop_data.scad
    prop_spar_length,,
    ,"4",prop/prop_data.scad
    prop_spar_outer_radius,,
    ,"1/64",prop/prop_data.scad
    prop_x_offset,,
    ,"-1/4 - 1/32",math_magik_lpp_data.scad
    ,"1/16",fuselage/fuselage_data.scad
    prop_x_width,,
    ,"1.3287",math_magik_lpp_data.scad
    prop_z_offset,,
    ,"-3/16",math_magik_lpp_data.scad
    ,"thb_height",fuselage/fuselage_data.scad
    r,,
    ,"wire_diameter/2",fuselage/rear_hook/rear_hook_data.scad
    rear_hook_color,,
    ,"METAL_Steel",fuselage/rear_hook/rear_hook_data.scad
    rib_camber,,
    ,"2",stab/stab_data.scad
    ,"4",wing/wing_data.scad
    rib_chord,,
    ,"max_stab_chord - 2 * spar_size",stab/stab_data.scad
    ,"max_wing_chord - 2 * spar_size",wing/wing_data.scad
    rp_offset,,
    ,"wing_offset + max_wing_chord + post_diameter/2 + tube_thickness",fuselage/fuselage_data.scad
    rubber_motor_length,,
    ,"10",rubber_motor/rubber_motor_data.scad
    rubber_motor_radius,,
    ,"1/8",rubber_motor/rubber_motor_data.scad
    s,,
    ,"prop_radius - 1",prop/prop_data.scad
    s1,,
    ,"1",prop/prop_data.scad
    s2,,
    ,"s - s1",prop/prop_data.scad
    s3,,
    ,"1",prop/prop_data.scad
    s4,,
    ,"1",prop/prop_data.scad
    sfp_offset,,
    ,"srp_offset - max_stab_chord - post_diameter - tube_thickness-1/64",fuselage/fuselage_data.scad
    spar_size,,
    ,"1/16",stab/stab_data.scad
    ,"1/32",fuselage/fin/fin_data.scad
    ,"1/16",wing/wing_data.scad
    srp_offset,,
    ,"tail_boom_rear_x - post_diameter - tube_thickness-1/16",fuselage/fuselage_data.scad
    stab_center_span,,
    ,"6",math_magik_lpp_data.scad
    stab_elevation,,
    ,"0.5",math_magik_lpp_data.scad
    stab_post_color,,
    ,"WOOD_Balsa",fuselage/stab_post/stab_post_data.scad
    stab_post_height,,
    ,"0.5 + tube_height",fuselage/stab_post/stab_post_data.scad
    stab_rib_camber,,
    ,"2",math_magik_lpp_data.scad
    stab_tip_radius,,
    ,"1.5",math_magik_lpp_data.scad
    stab_x_offset,,
    ,"max_overall_length - prop_x_width - max_stab_chord",math_magik_lpp_data.scad
    stub_length,,
    ,"1/8",fuselage/rear_hook/rear_hook_data.scad
    tail_boom_angle,,
    ,"atan2(tb_front_height - tb_rear_height,tail_boom_length)",fuselage/fuselage_data.scad
    ,"atan2(tb_front_height - tb_rear_height,tail_boom_length)",fuselage/tail_boom/tail_boom_data.scad
    tail_boom_length,,
    ,"max_overall_length -ms_length + prop_forward_x + tail_boom_overlap",fuselage/fuselage_data.scad
    tail_boom_overlap,,
    ,"1/8",fuselage/fuselage_data.scad
    tail_boom_rear_x,,
    ,"max_overall_length + prop_x_offset",fuselage/fuselage_data.scad
    tb_color,,
    ,"WOOD_Balsa",fuselage/fuselage_data.scad
    ,"WOOD_Balsa",fuselage/tail_boom/tail_boom_data.scad
    tb_front_height,,
    ,"3/16",fuselage/fuselage_data.scad
    ,"3/16",fuselage/tail_boom/tail_boom_data.scad
    tb_rear_height,,
    ,"1/16",fuselage/fuselage_data.scad
    ,"1/16",fuselage/tail_boom/tail_boom_data.scad
    tb_thickness,,
    ,"3/32",fuselage/fuselage_data.scad
    ,"3/32",fuselage/tail_boom/tail_boom_data.scad
    thb_front_height,,
    ,"thb_height/3",fuselage/thrust_bearing/thrust_bearing_data.scad
    thb_height,,
    ,"3/16",fuselage/thrust_bearing/thrust_bearing_data.scad
    thb_length,,
    ,"1/2",fuselage/thrust_bearing/thrust_bearing_data.scad
    thb_thickness,,
    ,"1/32",fuselage/thrust_bearing/thrust_bearing_data.scad
    thb_top_length,,
    ,"3/16",fuselage/thrust_bearing/thrust_bearing_data.scad
    thb_width,,
    ,"1/16",fuselage/thrust_bearing/thrust_bearing_data.scad
    thb_wire_size,,
    ,"0.025",fuselage/thrust_bearing/thrust_bearing_data.scad
    thrust_bearing_color,,
    ,"METAL_Aluminium",fuselage/thrust_bearing/thrust_bearing_data.scad
    thrust_bearing_x_offset,,
    ,"-1/4",math_magik_lpp_data.scad
    tip_dihedral,,
    ,"1.75",wing/wing_data.scad
    tip_dihedral_angle,,
    ,"atan2(a,b)",wing/wing_data.scad
    tip_le_span,,
    ,"tip_span - tip_radius",stab/stab_data.scad
    ,"tip_span - tip_radius",wing/wing_data.scad
    tip_radius,,
    ,"1.5",stab/stab_data.scad
    ,"2",wing/wing_data.scad
    tip_rib_chord,,
    ,"max_stab_chord - tip_radius - spar_size",stab/stab_data.scad
    ,"max_wing_chord - tip_radius - spar_size",wing/wing_data.scad
    tip_span,,
    ,"(max_stab_span - center_span)/2",stab/stab_data.scad
    ,"sqrt(a*a + b*b)",wing/wing_data.scad
    wing_center_span,,
    ,"12",math_magik_lpp_data.scad
    wing_elevation,,
    ,"3",math_magik_lpp_data.scad
    ,"3",fuselage/fuselage_data.scad
    wing_offset,,
    ,"1.625",fuselage/fuselage_data.scad
    wing_post_color,,
    ,"WOOD_Balsa",fuselage/wing_post/wing_post_data.scad
    wing_post_height,,
    ,"wing_elevation + tube_height",fuselage/wing_post/wing_post_data.scad
    wing_rib_camber,,
    ,"4",math_magik_lpp_data.scad
    wing_spar_size,,
    ,"1/16",math_magik_lpp_data.scad
    wing_tip_radius,,
    ,"2",math_magik_lpp_data.scad
    wing_x_offset,,
    ,"1.625",math_magik_lpp_data.scad
    wire_diameter,,
    ,"0.025",fuselage/rear_hook/rear_hook_data.scad
