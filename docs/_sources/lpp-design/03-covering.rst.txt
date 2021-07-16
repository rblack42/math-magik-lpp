Generating Covering
###################

Building the basic framework of an indoor model airplane with |OSC| is fairly
easy. Covering is another matter entirely. There is no simple way to generate a
thin film that covers flying surface frameworks using just |OSC|. We need to
take another approach.

Since we are using math to figure out a lot of this design, let's see what we
can do if we think this through.

STL Files
*********

|OSC| is a 3D solid modeling tool most often used in generating 3D printer
products. Part of that generation process involves converting the 3D objects
into |STL| files. These files are then post-processed to generate input data
files for the 3D printer. An |STL| file is a (long) list of triangles that
"wrap" the surface in question. These triangles are all connected in such a way
that the surface is called water tight, meaning there are no gaps anywhere. If
the triangles are big, the surface will not resemble the original shape very
much, but if we make them tiny, he resulting surface will look very good. What
this means is that our entire model can be reduced to a giant list of triangles
surrounding the structure. The closer the points on these triangles are to each
other, the closer our approximation to the real shape gets.

For the covering the shape is a very thin film. Suppose we generate a grid of
points on that surface and use those points  and generate our own triangles,
each suitably thin, to represent the covering over any shape we need. The grid
will look like a rectangular mesh, but we an run a diagonal across each
four-point grid element producing two triangles. This is exactly what an |STL|
file looks like.

|OSC| can create an |STL| file, and it can load them for display. Perhaps the way
to generate a covering for our model involves creating our own |STL| file for
the covering, or something similar to that.

Function Grapher
****************

Suppose you can build a mathematical function describing the covering surface
you need:

..	math::

	Surface = f(x,y)


If we create a matrix of points covering the projected wing plan form, we can
use this function to generate the two-dimensional matrix of data points needed
for |OSC| work. Python can write these points out so that |OSC| can read the
file produced. Sounds simple enough for a Python programmer.

Once we have this matrix, we can use it to generate a 3D surface using |OSC|
code. `Justin Lin`_ created a tool for displaying a 3D function, input as a
collection of 3D points, using the **polyhedron** tool in |OSC|. His function
takes the rectangular array of 3D *X-Y* points and extrudes them to create an
identical surface some defined thickness in the **Z** direction. Justin has a
library that uses this scheme on his website, and I started off by extracting
just part of that code for use in this project. This scheme is suitable for
indoor models, but will not work for more general model building, so I plan on
replacing this code at a later time.

Generating Covering Points
**************************

The challenge in using this approach is generating the matrix of points. I
elected to do this work in Python, and created a function that generates the
needed point array we can use for the covering.

Let's start off by looking at the rib height function.

Rib Height
==========

Here is our basic geometry:

..  tikz::
    :libs:  arrows, calc

    \draw(0,0) -- (7,0);
    \draw[thick](3.5,0) -> node[above] {r} ++(45:2.5) coordinate (p1);
    \draw(3.5,0) -- ++(135:2.5) coordinate (p2);
    \draw(3.5,0) -- (3.5,3);
    \draw[ultra thick] (p1) arc (45:135:2.5);
    \draw (4.5,0) arc (0:45:1);
    \draw (p1) -- (p2);
    \node[right] at (p1) {te};
    \node[left] at (p2) {le};
    \coordinate (angle_label) at ($ (3.5,0) + (22.5:1.2) $);
    \node at (angle_label) {$\alpha$};
    \coordinate (p3) at ($(p1) + (0,1.5) $);
    \coordinate (p4) at ($ (p2) + (0,1.5) $);
    \draw[<->] (p3) -- node[above] {C} (p4);

From this figure, we can generate two equations:

..  math::

    t = r - r sin(\alpha)

    C = 2 r cos(\alpha)



Here **C** is the rib chord and **t** is the rib thickness. We need to figure out the radius, **r** and the angle :math`\alpha`.

Rather than doing this manually, let's introduce Python SymPy_, a neat tool you wish you had back in your school days.

Here is a piece of code that will give up the results we are after:

..  code-block:: python

   import sympy

    r,c,t,alpha = \
      sympy.symbols('r c t alpha')

    eq1 = 2 * r * sympy.cos(alpha) - c
    eq2 = r - r * sympy.sin(alpha) - t
    sol = sympy.solve([eq1,eq2],[r,alpha])
    print(sol)

SymPy_ requires that you name your equations, and set them up as expressions
that evaluate to zero. So we move the left-hand side of each equation over to
the right and come up with some usable name.

The neat feature is the line where we solve these two equations for the two
unknowns. SymPy_ will produce the solutions we are after!

Here they are, nicely formatted:

..  mathcode::

    import sympy
    r,c,t,alpha = \
      sympy.symbols('r c t alpha')

    eq1 = 2 * r * sympy.cos(alpha) - c
    eq2 = r - r * sympy.sin(alpha) - t
    sol = sympy.solve([eq1,eq2],[r,alpha])
    sol[1]

The first solution gives us the arc radius, the second on gives :math:`\alpha`.

Let's check these equations out with a little Python code.

..  code-block::    python

    import math

    c = 5.0       # chord
    camber = 5.0  # percent of c

    t = camber * c
    r = c**2/(8*t) + t/2
    alpha = math.acos(4*c*t'(c**2 + 4*t**2)) * 180.0/math.pi
    print(r, alpha)

Here is what we get:

..  mathcode::

    import math

    c = 5.0       # chord
    camber = 5.0  # percent of c

    t = camber * c
    r = c**2/(8*t) + t/2
    alpha = math.acos(4*c*t/(c**2 + 4*t**2)) * 180/math.pi
    (r,alpha)

As  check, let's calculate the thickness using these values:

..  code-block:: python

    thickness = r - r * math.sin(alpha * math.pi/180.0)
    print(thickness)

..  mathcode::

    thickness = r - r * math.sin(alpha * math.pi/180.0)
    thickness

That is what we expect, so things look fine.

Rib Height
==========

To generate the height function needed to create our covering data array, we
need a bit of geometry. Since we are using a circular arc airfoil, the figure
below show basically what we need to generate the function:

..  tikz::
    :libs:  arrows, calc

    \newcommand{\tikzAngleOfLine}{\tikz@AngleOfLine}
    \def\tikz@AngleOfLine(#1)(#2)#3{%
    \pgfmathanglebetweenpoints{%
    \pgfpointanchor{#1}{center}}{%
    \pgfpointanchor{#2}{center}}
    \pgfmathsetmacro{#3}{\pgfmathresult}%
    }

    \coordinate (o) at (0,0);
    \coordinate (c) at ($(o)+(-45:2)$);
    \coordinate (e) at ($(c)+(45:2)$);
    \coordinate (t) at ($(c)+(67.5:2)$);
    \coordinate (p) at ($(c)+(67.5,2)$);
    \coordinate (m) at ($(o)!0.5!(e)$);
    \coordinate (c1) at ($(o)+(0,1.5)$);
    \coordinate (c2) at ($(e)+(0,1.5)$);
    \coordinate (c3) at ($(e)+(0,1.25)$);
    \coordinate (m2) at ($(t)+(3,0)$);

    \tikzAngleOfLine(c)(o){\AngleStart}
    \tikzAngleOfLine(c)(t){\AngleEnd}
    \draw[<->] (c)+(\AngleStart:1cm) arc (\AngleStart:\AngleEnd:1 cm);
    \node at ($(c)+({(\AngleStart+\AngleEnd)/2}:0.75 cm)$) {$\beta$};

    \draw[thin] (o) -- node[below left] {$r$} (c) -- (e) -- cycle;
    \draw [ultra thick] (o) arc (135:45:2);
    \draw[thin,->] (e) -- +(1,0) node[right] {$x$};
    \draw[thin,->] (o) -- (0,2) node [above] {$z$};
    %\draw[thick,->] (m) -- (t) node[above] {$z_c$};
    %\draw[thick,->] (o) -- node[above right=0.05] {$x_c$} (m);
    \draw[thin, dotted] (c) -- (t) node[above] {$p$};
    \draw[thin] (e) -- (c2);
    \draw[thin,<->] (0,1.25) -- node[above] {$C$}(c3);
    \draw[thin] (t) -- (m2);
    %\draw[thin,<->] ($(e)+(0.5,0)$)-- node[left] {$t$} +($(t)-(m)$);

The height of the rib at some point :math:`P` is given as follows:

Given a camber, chord, and radius, we can come up with the following equations:

..  math::

    t = camber \frac{C}{100}

    w = \frac{C}{2}

    h = t - r

    r^2 = (x - w)^2 + (z - h)^2

That last equation is the general equation for a circle centered at :math:`(w,y)`.
We need to solve these equations for the height, :math:`z`. SymPy_ to the rescue!

For some specified :math:`x, r, w, and h` we want to find the height,
:math:`z`: SymPy_ to the rescue!

..  code-block::    python

    import sympy

    x,z,h,w,r,c,t,beta = sympy.symbols('x z h w r c t beta')
    eq3 = (x-w)**2 + (z-h)**2 - r**2
    sol2 = sympy.solve(eq3, z)
    print(sol2[1])

..  mathcode::

    x,z,h,w,r,c,t,beta = sympy.symbols('x z h w r c t beta')
    eq3 = (x-w)**2 + (z-h)**2 - r**2
    sol2 = sympy.solve(eq3, z)
    sol2[1]

Let's make some substitutions. First, we eliminate :math:`w`:

..  code-block::    python

    eq4 = sol2[1]
    eq5 = eq4.subs(w,c/2)
    print(eq5)

..  mathcode::

    eq4 = sol2[1]
    eq5 = eq4.subs(w,c/2)
    eq5

Next, we eliminate :math:`h`:

..  code-block::    python

    eq6 = eq5.subs(h,t-r)
    print(eq6)

..  mathcode::

    eq6 = eq5.subs(h,t-r)
    eq6

Now we have an equation we can use to build our height function.

Here it is:

..  code-block::    python

    def rib_height(chord, camber, x):
        """return the height for some fraction of the chord x"""

        c = chord
        x = x * c
        t = camber * chord / 100
        r = chord**2/(8*t) + t/2
        return -r +t + math.sqrt((-c/2 + r + x)*(c/2 + r - x))

Let's test this out. The height at the midpoint should be the thickness:

..  code-block::    python

    print(rib_height(5,5,0.5))

..  mathcode::
    :newcontext:


    def rib_height(chord, camber, x):
        """return the height for some fraction of the chord x"""
        import math
        c = chord
        t = camber * chord / 100
        r = chord**2/(8*t) + t/2
        return -r + t + math.sqrt((-c/2 + r + x)*(c/2 + r - x))

    rib_height(5,5,0.5)

This gives us the height function needed for the circular arc airfoil. Next we
need to work on the wing outline.

Wing Outline
============

The wing is constructed using s rectangular center section and two rectangular tip sections with a rounded leading edge. Here is the geometry we are using:


..  tikz::
   :libs:  arrows, calc

    \draw[ultra thick]  (0,0) -- (8,0) -- (8,3);
    \draw[ultra thick]  (8,3) arc[
    start angle=0,
    end angle=90,
    x radius=2,
    y radius=2] -- (0,5);

    \draw[thin] (0,5) -- (0,5.5);
    \draw[thin] (0,0) -- (0,5);
    \draw[thin,->] (0,0) -- (0,-0.5) node [below] {$x$};

    \draw[thin] (4,5) -- (4,0) node[below] {$y_t$};

    \draw[thin] (6,5) -- (6,0);
    \draw[thin] (6,3) -- (8,3);
    \draw[thin,->] (8,0) -- (8.5,0) node[right] {$y$};

    \draw[thin] (0,0) -- (-0.5,0);
    \draw[thin] (0,5) -- (-0.5,5);
    \draw[thin,<->] (-0.25,0) -- node[left] {$C$}(-0.25,5);

    \draw[thin,->] (6,3) --node[above left] {$r_t$}  +(45:2);

    \draw[thin] (8,3.5) -- (8,5.5);
    \draw[thin, <->] (0,5.25) -- node[above] {$S/2$}(8,5.25);


In this figure, we need to provide four parameters:

	* Which chord

	* Total wingspan

	* Center section span

	* Tip radius

..	note::

    In this figure, the total span is the flat span, not the span set by the
    rules. The rules ilmit the span with dihedral!

The leading edge offset, beginning where the circular section starts is defined
by another general circle equation. Let's consider a coordinate system
positioned at the start of the leading edge arc. Here is the equation for the tip arc:

..  math::

    (x -r)^2 + y^2 = r^2

SymPy_ will give us our equation:

..  code-block:: python

    import sympy

    x,y,r = sympy.symbols('x y r')
    eq7 = (x-r)**2 + y**2 - r**2
    sol3 = sympy.solve(eq7, x)
    print(sol3[0])

..  mathcode::

    import sympy

    x,y,r = sympy.symbols('x y r')
    eq7 = (x-r)**2 + y**2 - r**2
    sol3 = sympy.solve(eq7, x)
    sol3[0]


This equation gives us the leading edge offset along the arc. A function that
gives us that offset for some percentage of the wing span looks like this:

..  code-block::    python

    def xle(s, r, y):
        """s is the half span, r is the tip radius and Y ranges from 0 to 1"""
        if y < s - r:
            return 0
        yt = y = (s - r)
        return r - math.sqrt((r-yt)*(r + yt))

We now have all the pieces needed to generate the covering for our model.

Covering grid
=============

A simple way to generate the covering matrix is to divide up the chord into
**nx** points, and the span into **ny** points. Actually, we will be generating
covering shapes for each part of the model, not the assembled parts.

Wing and Stab Center Sections
-----------------------------

For the wing and stab, the grid is simple. We set up simple loops to generate
**X,Y** pairs, and use the height function to find the height.

..  note::

    There is a subtle point here. The ribs normally start at the inner edge of
    the leading edge and trailing edges. That means our airfoil is not really a
    pure circular arc. Rather than complicate things, I am gong to generate the
    covering as an arc, and position it so it connects to the leading and
    trailing edge outer points. Visually, this will be fine and the analysis
    will still be good. The covering will "float" above the actual framework a
    tiny amunt.

Tip sections
------------

The tip sections are more of a puzzle. They will be canted upward to generate
the dihedral. Modelers normally build and cover the wings flat, and deal with
the covering at the joint using a variety of schemes. To make thing look proper
in |OSC| we need to do better.

Here is a look at the junction of two circular arc sections joined at some
dihedral angle:

..  image:: tip-joint.png
    :align: center
    :width: 400

If you look closely, the intersection is along a plane cutting through this
joint at an angle (one half of the dihedral). That means the end rib should
really be canted on the center section, something builders do not so.

Therefore, the joint we are going to create will not be a circular arc on the
tip, but a slight ellipse. The tip covering starts at the edge of yhe center
section, which we can calculate easily. There will be no rib at the inner edge
of the tip, but we can use the center section rib points, suitably transformed
to figure out the tip covering edge.

Phew!.

Here is the geometry we are dealing with:

..  tikz::

    \draw[thick] (0,0) -- (6,0) -- (9,1.75);
    \draw([thick] (0,0.25) -- (6,0.25) -- (9,1.75);

In this figure, we assume the tip covering runs in a straight line from the
center section to the flat tip rib. (Close enough for this study!)

But this means that our rib height function will not work for the tips. Instead, we need to use a straight line running from center section o the the tip and find the height of that line as needed. More math work!

Consider the general equation defining a line in 3D space:

Given two points in 3D space:

..  math::

    p1 = (x1,y1,z2)
    p2 = (x2,y2,z2)

Now, we define these constants:

..  math::

    l = (x2 - x1)
    m = (y2 - y1)
    n = (z2 - z1)

Then this equation defines the line:

..  math::

    (\frac{x - x1}{l} = \frac{y - y1}{m} = \frac{z - z1}{n}

If we set one coordinate value we can calculate the other two from this.

The only remaining problem is finding the set of points that represent the
inner edge of the tip covering surface. For this, we need to do a simple
transformation.

..  tikz::
    :libs:  arrows, calc

    \draw[thick]   (0,0) -- (3,0);
    \draw[thick] (0,1) -- (3,1) -- (3,0);
    \draw (3,0) -- (5,0);
    \draw (3,0) -- ++(30:2);
    \draw (3,1) -- ++(25:2);
    \draw (3,1) -- ++(-60:0.85);
    \draw[thick] (4,0) arc (0:30:1);
    \coordinate (angle_label) at ($ (3,0) + (15:1.2) $);
    \node at (angle_label) {$\theta$};

If the height of the rib at this edge is :math:`h_r`, then the length of the position along the tip leading edge is:

..  math::

    h_r \sin(\theta)

And the height of the tip covering at this point is:

..  math::

    h_r * \cos(\theta)

Now, finally we have all the pieces to write the covering module!




