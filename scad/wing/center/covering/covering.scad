use <MMlib/covering_generator.scad>;
include <cover_points.scad>
include <MMlib/colors.scad>


thickness = 0.001;

module covering() {
    color(GLASS_Blue)
      covering_generator(g_pts, thickness);
}

covering();
