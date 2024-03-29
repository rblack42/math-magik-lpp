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

Rotations
*********

First, we rotate arount the **x** axis by an angle $\theta$:

..  math::

	R_x = \left[\begin{matrix}1&0&0&0\\
		0&\cos{\theta}&\sin{\theta}&0 \\
		0&-\sin{\theta}&\cos{\theta}&0 \\
		0&0&0&1\end{matrix}\right]

	R_y = \left[\begin{matrix} \cos{\beta}&0&-\sin{\beta}&0\\
		0&1&0&0 \\
		\sin{\beta}&0&\cos{\beta}&0 \\
		0&0&0&1\end{matrix}\right]

	R_z = \left[\begin{matrix}\cos{\zeta}&-\sin{\zeta}&0&0\\
		\sin{\zeta}&\cos{\zeta}&0&0 \\
		0&0&1&0 \\
		0&0&0&1\end{matrix}\right]



