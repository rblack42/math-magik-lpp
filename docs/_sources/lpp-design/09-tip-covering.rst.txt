Tip Covering Logic
##################

Covering the center section of the wing and stab is a snap. That covering is
actually a simple slice out of a very thin cylinder since we are using
circular arc airfoils. I chose the generate the points on a grid that covers
the center section and use the *Function Grapher* logic created by `Justin
lin`_ to generate the actual covering shape.

The tips are another matter. If we keep the outer ribs of the center section
vertical and raise the wing tip up to form the dihedral, the inner edge of the
tip covering is not a straight line. Mathematically, it is a piece of an ellipse
formed by cutting a cylinder with an angled plane. We can extract the
coordinates of the outer edge of the center section covering and use those points
as our starting point for the tip covering. However, we need to account for the
dihedral angle we will be using and adjust those points to find the correct
starting points for the tip covering. (Remember, there is no actual rib here.

Tip Airfoil
***********

The tip has no ribs, only the tip outline as a structure. If we cover an actual
model with this structure, something modelers typically do by building the wing
flat, then the covering assumes some shape other than out circular arc as we
move toward the tip. The actual height of this shape tapers off to zero as we
approach the tip.

Here is a basic diagram showing the tip design:

..  tikz::
    :libs: calc, intersections

    \makeatletter
    \newcommand{\gettikzxy}[3]{%
        \tikz@scan@one@point\pgfutil@firstofone#1\relax
        \edef#2{\the\pgf@x}%
        \edef#3{\the\pgf@y}%
    }
    \makeatother

    \coordinate (o) at (0,0); % name the origin
    \coordinate (le) at (5,5); % inner leading edge
    \coordinate (te) at (5,0); % inner trailing edge
    \coordinate (s) at (2,5); % start of rib arc
    \coordinate (c) at (2,3); % center of rib arc
    \coordinate (t) at (0,3);  % top of outer rib


    % draw dihedral angle
    \draw[thick] (te) -- (o) -- (t);
    \draw[thick] (s) -- (le);
    \draw[thick, name path=arc] (2,5) arc (90:180:2);
    \draw[thin] (t) --  (0,6);
    \draw[thin, name path=grid] (0,4.5) -- (5,4.5);
    \draw[thin] (t) -- (c);
    \path [name intersections={of=arc and grid, by=E}];
    \draw[black,fill] (E) circle [radius=0.05];
    \gettikzxy{(E)}{\dx}{\dy}
    \draw [thin] (E) -- (\dx,1.5);
    \draw[thin, ->] (3,5.5) -- (3,5);
    \draw[thin, ->] (3,4) node[below]{$x$} -- (3,4.5) ;
    \draw[thin, ->] (-0.25,2) -- (0,2);
    \draw[thin, <-] (\dx,2) -- (1.2,2) node [right] {$\delta$};
    \draw[thin] (2,3) -- node [left] {$r$} (E) node [above] {$p$};
    \draw [thin] (s) -- (-0.75,5);
    \draw[thin, <->] (-0.5,5) -- node [left] {$C$} (-0.5,0);
    \draw[thin] (-0.75,0) -- (0,0);

In this figure, we are going to pick points on the outer part of the tip, along
the arc and the outer tip rib, that represent the intersection of a vertical
plane parallel to the **Y** axis drawn from the inner tip rib points to the
outer tip structure. We calculate the **Y** offset of the tip at the
intersection ($\delta$ in the figure above) and draw a straight 3D line between
the inner point and this outer tip structure. We will distribute points along
this line using the number of points selected in the **Y** direction for our
grid.

Since there are no supporting ribs along the tip span, I am going to assume
that the covering can be modeled as a set of straight lines from a point on the
center section outer rib to the tip outline. The selected points on the outline
will be chosen so that these tip covering lines are all parallel to the wing
axis (**Y**). This is not "real" in any sense, but should look fine visually,
and give us something close to right in weight and balance calculations.
Furthermore, the tip covering grid will need involves far fewer data points
than we might need with other ideas.

It is important to note that there will be visual problems as the covering
approaches the circular arc. The generated covering uses straight lines between
data points, and that means the tip outline will not be covered correctly. The
fewer the points we set up in the chord wise direction, the worse things will
look.

iWe are generating the grid for our covering using evenly distributed points
along the span and chord. In that code **x**, and **y** range from zero to one
and must be scaled to determine physical values.

The equations needed for calculating the coordinates of our tip grid point
(point **p** in the figure) are given here:

..  math::

    x_p = x * C

    y_p = span - \delta

    z_p =  tip_spar_size


We can determine $\delta$ using the equation of the circular arc centered as
shown in the figure:



..  mathcode::
   import sympy

   x,r,delta,c = sympy.symbols('x r delta c')
   eq1 = (r - delta)**2 + (r - x)**2 - r**2
   sol = sympy.solve(eq1, delta)
   sol[0]

And here is an image showing the grid on the wing tip:

Virtual Tip Rib
***************

There is no physical rib at the tip inner line. Instead the covering attaches
to the outer center section rib. When the tip is placed in its final position,
raised up to form the dihedral, the inner most edge of the tip covering must be
trimmed off to join nicely. Actually, we can use those center section rib
elevation values to form the correct starting points for the tip covering. The
calculations are pretty simple:

..  math::

    x_0 = x_c

    y_y = - z_c \sin{\theta}

    z_o = z_c \cos{\theta}

Here, the **0** subscript refers to the tip coordinate values at the "virtual
starting rib point, and **c** refers to the point values on the outer center
section rib. $\theta$ is the dihedral angle.

Python Covering Code
********************

All of the calculations needed to generate covering grids are included in the
**Covering.py** code file. This code creates a **covering.scad** file that cna
be *included* in other |OSC| files to generate the actual covering surface.


