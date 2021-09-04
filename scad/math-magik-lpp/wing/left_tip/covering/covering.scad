use <function_grapher.scad>;
include <./cover_points.scad>
include <colors.scad>

thickness = 0.001;
style = "FACES";  // LINES to show surface grid

module covering() {
  color(GLASS_Blue)
  function_grapher(g_pts, thickness, style);
}


covering();
