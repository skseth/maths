# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
# ---

# %% [markdown]
# **Digression from Elementary Differential Geometry - Andrew Pressley**
#
# Also see video: [Physics for Students - Differential Geometry Fundamental Concepts](https://www.youtube.com/watch?v=JU1t_46RIPc&t=345s)
#
#

# %% [markdown]
# **Curves in $R^2$ and $R^3$**
#
# **Level Curves** : expressed as f(x,y) = c or f(x,y,z) = c
#
# But another way is to see this as a parameterized curve:
#
# **Defn (Parameterized Curve)**
#
# A parameterized curve is a map $\gamma:(a,b) \to R^n$, for some interval (a,b) in R.
#
# A parameterized curve whose image is contained in (a part of) a level curve C, is called a "parameterization of C". A parameterization is not unique.
#
# Parabola: $\gamma(t) : (-\infty, +\infty) \to R^2: \gamma(t) = (t, t^2)$
#
# We can also use $(t^3, t^6)$ for example.
#
# Circle: $\gamma(t) : (0, 2\pi): \gamma(t) = (\cos(t), \sin(t))$
#
# Astroid: $\gamma(t) = \cos^3(t) + \sin^3(t)$ - the corresponding level curve is $x^{2/3} + y^{2/3} = 1$ 

# %% [markdown]
# **Smooth functions and Parameterized Curves**
#
# **Defn** $f:(a,b) \to R$ is said to be a smooth function if the derivative $\frac{d^nf}{dt^n}$ exists for all $n \ge 1$ and for all $t \in (a,b)$.
#
# Implication: If f and g are smooth functions, so are : sum. product, quotient and composite.
#
# **Note** Differentiation of vector valued function
#
# Given a function $\gamma(t) = (\gamma_1(t), \gamma_2(t), \dots, \gamma_n(t))$, then :
#
# $\dfrac{d\gamma(t)}{dt} = \left( \dfrac{d\gamma_1(t)}{dt}, \dfrac{d\gamma_2(t)}{dt}, \dots, \dfrac{d\gamma_n(t)}{dt}\right)$, amd so on for higher derivatives.
#
# We refer to the derivatives as $\dot\gamma, \ddot\gamma$ etc to save space.

# %% [markdown]
# **Tangent Vector**
#
# If $\gamma$ is a parameterized curve, its the first derivative $\dot\gamma(t)$ is called the tangent vector of $\gamma$ at the point $\gamma(t)$

# %% [markdown]
# **Proposition: If the tangent vector of a parameterized curve is constant, the image of the curve is (part of) a straight line**
#
# $\gamma(t) = \int \dfrac{d\gamma}{dt}{dt} = \int \mathbf{a} dt = t\mathbf{a} + \mathbf{b}$, where $\mathbf{b}$ is another constant vector.
#
#
# **Warning** A parameterized curve can intersect itself - i.e. the same point may be reached by 2 different values of the parameter t. So it is more accurate to say the "tangent vector of $\gamma$ at the parameter value t".

# %% [markdown]
# # Exercise

# %% [markdown]
# 1.1.1 Is g(t) = (t^2, t^4) a parameterization of the parabola $y = x^2$? Only half the parabola is covered since in g(t), $t^2$ can only take positive values. 
#
# 1.1.2. a) find parameterizations for $y^2 - x^2 = 1$ : $\gamma(t) = (\tan(t), \sec(t))$, $-\pi/2 \le t \le \pi/2$
#
# b) for $\frac{x^2}{4} + \frac{y^2}{9} = 1$: $\gamma(t) = (2\cos(t), 3\sin(t))$, $-\pi/2 \le t \le \pi/2$
#
# 1.1.3. (i) $\gamma(t) = (\cos^2(t), \sin^2(t))$ x + y = 1$
#
# (ii) $\gamma(t) = (e^t, t^2)$  $log(x) = \sqrt{y}$
#
# 1.1.4 Tangent vectors of 1.1.3: (i) : $(2\cos(t), -2\sin(t))$ (ii) $(e^t, 2t)$
#
# 1.1.5 Sketch Astroid - TBD
#
# 1.1.6 Consider ellipse: $\frac{x^2}{p^2} + \frac{y^2}{q^2} = 1$, where p > q > 0 . Eccentricity of ellipse $\epsilon = \sqrt{1 - q^2/p^2}$. Foci are at $(-\epsilon p, 0), (\epsilon p, 0)$. Verify $\gamma(t) = (p\cos(t), q\sin(t))$
#
# (a) Given a point (x,y) on the ellipse, with parameter $t_1$, then $\cos^2(t_1) + \sin^2(t_1) = 1$. The other way, given any $t$, the x,y coordinates are $(p\cos(t), q\sin(t))$. We can see it meets the equation of the ellipse.
#
# Total distance from 2 foci:
#
# Let $c^2 = p^2 - q^2 = \epsilon^2p^2, \epsilon = c/p$
#
# $$
# \begin{aligned}
# d_1^2 &= p^2\cos^2(t) + \epsilon^2p^2 + 2p^2\cos(t)\epsilon + q^2\sin^2(t) \\
#     &= p^2\cos^2(t) + c^2 + 2pc\cos(t) + (p^2 - c^2)\sin^2(t) \\
#     &= p^2 + 2pc\cos(t) + c^2\cos^2(t) = (p + c\cos(t))^2 \\
# d_1 &= p + c\cos(t) \\
# \text{ similarly } \\
# d_2 &= p - c\cos(t) \\
# d_1 + d_2 = 2p
# \end{aligned}
# $$
#
# (iii) Angle with tangent vector is same for both foci:
#
# tangent vector = $\dot{\gamma} = (-p\sin(t), q\cos(t))$. $\mathbf{f_1} = (p\cos(t) + p\epsilon, q\sin(t)), \mathbf{f_2} = (p\cos(t) - p\epsilon, q\sin(t))$.
#

# %% [markdown]
# $f_1.t = -p^2cos(t)sin(t) - p^2\epsilon\sin(t) + q^2\cos(t)\sin(t) = -p^2cos(t)sin(t) - pc\sin(t) + (p^2 - c^2)\cos(t)\sin(t) = -c\sin(t)(p + c\cos(t))$
#
# $f_2.t = -p^2cos(t)sin(t) + p^2\epsilon\sin(t) + q^2\cos(t)\sin(t) = -p^2cos(t)sin(t) + pc\sin(t) + (p^2 - c^2)\cos(t)\sin(t) = c\sin(t)(p - c\cos(t))$

# %% [markdown]
# $|y|^2 = p^2sin^2(t) + q^2cos^2(t) = p^2sin^2(t) + (p^2 - c^2)\cos^2(t) = p^2 - c^2\cos(t)$
#
#
# $|f1|^2 = p^2cos^2(t) + p^2e^2 + 2p^2ecos(t) + q^2sin^2(t) = p^2 + 2pccos(t) + c^2\cos^2(t) = (p + c\cos(t))^2$
#
# $|f2|^2 = p^2cos^2(t) + p^2e^2 - 2p^2ecos(t) + q^2sin^2(t) = p^2 - 2pccos(t) + c^2\cos^2(t) = (p - c\cos(t))^2$
#
#
# Based on this we see that the angles made by each foci have the relation $cos(\theta_1) = -\cos(\theta_2)$. This means the "supplementary angle" for 2nd foci is the same, since $\cos(\pi - )$

# %% [markdown]
# **1.1.7 Parameterized Equation of Cycloid**
#
# If we take the center as origin, and take a point at the bottom of the wheel, then when it does an angle t, the point is at $(-a\sin(t), -a\cos(t))$. The center itself has a equation of (at, a). So the final equation of each point is $(at -a\sin(t), a - a\cos(t)) = a(t - \sin(t), 1 - \cos(t))$

# %% [markdown]
# **1.1.8 - Intersection of cylinder and sphere - Viviani's Curve**
#
#

# %% [markdown]
# Given parameterization: (cos^2(t) - 1/2, sin(t)cos(t), sin(t))
#
# Is it on the circle? $(x + 1/2)^2 + y^2 + z^2 = 1 \implies \cos^4(t) + sin^2(t)cos^2(t) + sin^2(t) = \cos^2(t)(\cos^2(t) + \sin^2(t)) + \sin^2(t) = \cos^2(t) + \sin^2(t) = 1$ . So the parameterization satisfies the equation of the sphere.
#
# Is it on the cylinder? For the cylinder: x^2 + y^2 = 1/4. So $\cos^4(t) + 1/4 - \cos^2(t) + \sin^2(t)\cos^2(t) = 1/4$
#
# So definitely every point on the parameterized curve is on the intersection of the sphere and the cylinder.
#

# %% [markdown]
# **1.1.9 Normal line**
#
# tangent and normal for $(2\cos(t) - \cos(2t), 2\sin(t) - \sin(2t))$ at $t = \pi/4$
#
# tangent : $(-2\sin(t) + 2\sin(2t), 2\cos(t) - 2\cos(2t)) \equiv (-\sin(t) + \sin(2t), \cos(t) - \cos(2t)) = (\sqrt{2}/2 - 1, \sqrt{2}/2 )$
#
# perp : $(-\cos(t) + \cos(2t), -\sin(t) + \sin(2t)) = ( -\sqrt{2}/2, \sqrt{2}/2 - 1, )$
#
#

# %% [markdown]
# ## 1.2 Arc-Length
#
#

# %% [markdown]
# **Definition (Arc-Length)**
#
# The arc-length of a curve $\gamma$, starting at point $\gamma(t_0)$ is the function $s(t)$ given by :
#
# $$s(t) = \int_{t_0}^{t} \Vert \dot\gamma(u) \Vert du$$
#
# Note that length is positive in direction of increasing t. Suppose we start at a different starting point $\bar{t_0}$, then 
#
# $$\int_{t_0}^{t} \Vert \dot\gamma(u) \Vert du = \int_{\bar{t_0}}^{t} \Vert \dot\gamma(u) \Vert du + \int_{t_0}^{\bar{t_0}} \Vert \dot\gamma(u) \Vert du$$
#
# The equation should be read with both integrals being positive when $t_0 \lt \bar{t_0} \lt t$, other one or the other is negative.

# %% [markdown]
#

# %% [markdown]
#
