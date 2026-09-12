# Derivation: Lorentz Invariance to Rest Energy

This note develops the first mathematical spine of the project.

The target is not to begin with $E = mc^2$. The target is to derive

$$
E^2 = p^2 c^2 + m^2 c^4
$$

from Lorentz-invariant geometry, and then recover

$$
E_0 = mc^2
$$

as the rest-frame case.

---

## 1. Lorentz transformation

For two inertial frames with relative speed $v$ along the x-axis,

$$
ct' = \gamma(ct-\beta x)
$$

$$
x' = \gamma(x-\beta ct)
$$

with

$$
\beta = \frac{v}{c},\qquad
\gamma = \frac{1}{\sqrt{1-\beta^2}}.
$$

The transformation preserves the Minkowski interval:

$$
c^2t'^2-x'^2 = c^2t^2-x^2.
$$

In differential form,

$$
c^2dt^2-dx^2 = c^2d\tau^2,
$$

where $\tau$ is proper time.

For one-dimensional motion, $dx = v\,dt$, so

$$
d\tau = dt\sqrt{1-\frac{v^2}{c^2}} = \frac{dt}{\gamma}.
$$

Therefore,

$$
\frac{dt}{d\tau}=\gamma.
$$

---

## 2. Four-position and four-velocity

Define the four-position

$$
x^\mu=(ct,\mathbf{x}).
$$

The four-velocity is

$$
U^\mu = \frac{dx^\mu}{d\tau}.
$$

Using $dt/d\tau = \gamma$,

$$
U^\mu=(\gamma c,\gamma\mathbf{v}).
$$

With metric signature $(+,-,-,-)$, its Minkowski norm is

$$
U^\mu U_\mu
=\gamma^2(c^2-v^2).
$$

Since

$$
\gamma^2=\frac{1}{1-v^2/c^2},
$$

we obtain

$$
\boxed{U^\mu U_\mu=c^2}.
$$

This norm is Lorentz invariant.

---

## 3. Four-momentum

For a particle with invariant mass $m$, define

$$
P^\mu=mU^\mu.
$$

Therefore,

$$
P^\mu=(\gamma mc,\gamma m\mathbf{v}).
$$

The spatial part is the relativistic momentum

$$
\mathbf{p}=\gamma m\mathbf{v}.
$$

So the four-momentum can be written

$$
P^\mu=\left(P^0,\mathbf{p}\right).
$$

The temporal component is conventionally identified as

$$
P^0=\frac{E}{c},
$$

which gives

$$
\boxed{E=\gamma mc^2}.
$$

Thus

$$
\boxed{P^\mu=\left(\frac{E}{c},\mathbf{p}\right)}.
$$

---

## 4. Why energy and momentum belong together

Under a Lorentz boost along x,

$$
\begin{pmatrix}
E'/c\\
p_x'
\end{pmatrix}
=
\begin{pmatrix}
\gamma & -\beta\gamma\\
-\beta\gamma & \gamma
\end{pmatrix}
\begin{pmatrix}
E/c\\
p_x
\end{pmatrix}.
$$

Therefore,

$$
E' = \gamma(E-vp_x),
$$

$$
p_x' = \gamma\left(p_x-\frac{vE}{c^2}\right).
$$

This is structurally parallel to the transformation of $ct$ and $x$.

Energy and momentum are therefore not independent relativistic quantities. They are components of one Lorentz four-vector.

---

## 5. Four-momentum invariant

Because

$$
P^\mu=mU^\mu,
$$

and

$$
U^\mu U_\mu=c^2,
$$

we have

$$
P^\mu P_\mu = m^2c^2.
$$

Using

$$
P^\mu=\left(\frac{E}{c},\mathbf{p}\right),
$$

its norm is

$$
P^\mu P_\mu
=\frac{E^2}{c^2}-p^2.
$$

Therefore,

$$
\frac{E^2}{c^2}-p^2=m^2c^2.
$$

Multiplying by $c^2$,

$$
\boxed{E^2=p^2c^2+m^2c^4}.
$$

This is the central energy-momentum relation.

---

## 6. Rest frame

In the particle's rest frame,

$$
\mathbf{p}=0.
$$

Then

$$
E_0^2=m^2c^4.
$$

Choosing the positive-energy branch for an ordinary particle,

$$
\boxed{E_0=mc^2}.
$$

The familiar equation is therefore the zero-momentum specialization of the deeper invariant relation.

---

## 7. Geometric interpretation

For fixed $m$, the invariant equation

$$
\frac{E^2}{c^2}-p^2=m^2c^2
$$

defines a hyperbola in energy-momentum space.

Different inertial observers generally assign different values of $E$ and $p$, but all such measurements lie on the same mass shell.

The invariant is $m$, not $E$ and not $p$ individually.

This directly parallels spacetime:

$$
c^2t^2-x^2 = \text{invariant}
$$

versus

$$
\frac{E^2}{c^2}-p^2 = m^2c^2.
$$

---

## 8. Massless limit

For $m=0$,

$$
E^2=p^2c^2,
$$

so for positive energy,

$$
\boxed{E=pc}.
$$

This shows why zero rest mass does not imply zero energy.

---

## 9. Scope note

This derivation intentionally uses special relativity and classical relativistic particle mechanics only. It does not require general relativity or quantum field theory.

The animation sequence should preserve this dependency chain and avoid presenting later identities before their geometric basis has been introduced.
