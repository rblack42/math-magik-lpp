Composite 3D Transformations
############################

In calculating the center of gravity for our model, we need to track how the center of mass for a given part moves as we align it into an assembly, them aligh an assembly into the final model. Qw uaw simple translation and rotation transformations to get our parts aligned as we wish in our design.

Translation Transformations
***************************

Mathematically, we can describe any transformation by setting up a
*transformation matcix* and using that matrix to calculate the effect of a
translation transformation.

Suppose we want to translate a shape using these distances in each coordinate
direction: $D_x$, $D_y$, and $D_z$. If we define a point, $P_0$ using three
positions: $P_x$, $O_y$, and $P_z$, then the translated point can be defined using
matrix multiplication:


..	math::

	T_1 = \left[\begin{matrix}1&0&0&0\\
		0&1&0&0 \\
		0&0&1&0 \\
		D_x&D_y&D_z&1\end{matrix}\right]

The position is given using a vector:

..	math::

	P_0 = \left[\begin{matrix}P_x&P_y&P_z&1\end{matrix}\right]

Let's try this multiplication using SymPy_:

..  mathcode::

    import sympy

    px, py, pz, dx, dy, dz = sympy.symbols('px py pz dx dy dz')
    T1 = sympy.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[dx,dy,dz,1]])
    p0 = sympy.Matrix([px,py,pz,1])
    p1 = p0 * T1
    p1

