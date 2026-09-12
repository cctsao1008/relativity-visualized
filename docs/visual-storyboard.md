# Visual Storyboard

This storyboard defines the teaching intent of the first animation sequence. It is not a production log. Temporary experiments and implementation history belong in GitHub Issues.

## Narrative objective

The viewer should leave with one structural idea:

> `E₀ = mc²` is the rest-frame consequence of the Lorentz-invariant geometry of four-momentum.

The animation should therefore avoid opening with `E = mc²` as a magical identity. The sequence must establish invariance first.

---

## Scene 1 — Lorentz boost

**File:** `scenes/01_lorentz_boost.py`

### Teaching objective

Show that Lorentz transformations mix time and space while preserving a hyperbolic interval.

### Visual sequence

1. Draw axes labelled `x` and `ct`.
2. Draw an event vector from the origin.
3. Display
   
   `c²t² - x² = invariant`.
4. Introduce a boosted frame with tilted spacetime axes.
5. Keep the event invariant while changing its coordinates.
6. Draw one representative invariant hyperbola.

### Viewer takeaway

The coordinates change; the Minkowski norm does not.

---

## Scene 2 — Proper time

**File:** `scenes/02_proper_time.py`

### Teaching objective

Connect the invariant interval to a physically meaningful scalar measured along a worldline.

### Visual sequence

1. Reuse the `ct`–`x` geometry.
2. Draw a timelike worldline segment.
3. Mark coordinate intervals `dt` and `dx`.
4. Morph

   `c²dt² - dx²`

   into

   `c²dτ²`.
5. Substitute `dx = v dt`.
6. Resolve to

   `dτ = dt / γ`.

### Viewer takeaway

Proper time is the Lorentz-invariant clock interval associated with the moving object.

---

## Scene 3 — Four-velocity

**File:** `scenes/03_four_velocity.py`

### Teaching objective

Show that differentiating four-position with respect to proper time naturally produces a four-vector with invariant magnitude `c`.

### Visual sequence

1. Start from

   `x^μ = (ct, x)`.
2. Apply `d/dτ` visually to both components.
3. Obtain

   `U^μ = (γc, γv)`.
4. Evaluate the Minkowski norm.
5. Collapse the algebra to

   `U^μ U_μ = c²`.

### Viewer takeaway

Ordinary velocity changes across observers, but the four-velocity has a fixed Minkowski norm.

---

## Scene 4 — Four-momentum

**File:** `scenes/04_four_momentum.py`

### Teaching objective

Introduce four-momentum as mass times four-velocity and make the energy-momentum pairing visually explicit.

### Visual sequence

1. Start with

   `P^μ = mU^μ`.
2. Expand to

   `P^μ = (γmc, γmv)`.
3. Label spatial component

   `p = γmv`.
4. Replace the temporal component with

   `E/c`.
5. Arrive at

   `P^μ = (E/c, p)`.
6. Place beside

   `x^μ = (ct, x)`

   to emphasize the structural analogy.

### Viewer takeaway

Energy and momentum are not separate relativistic bookkeeping devices; they are components of one four-vector.

---

## Scene 5 — Mass-energy relation

**File:** `scenes/05_mass_energy_relation.py`

### Teaching objective

Make the invariant energy-momentum relation geometrically visible, then recover rest energy.

### Visual sequence

1. Draw axes `p` and `E/c`.
2. Draw the positive-energy mass shell

   `(E/c)² - p² = (mc)²`.
3. Place a point on the hyperbola and label it `(p, E/c)`.
4. Move the point along the same hyperbola to represent different inertial observers.
5. Keep the invariant label `m` fixed.
6. Display

   `E² = p²c² + m²c⁴`.
7. Move to the rest-frame point where `p = 0`.
8. Reduce the equation to

   `E₀ = mc²`.
9. Optionally show the `m = 0` asymptote as a future extension:

   `E = pc`.

### Viewer takeaway

`E₀ = mc²` is not the whole relation. It is the rest-frame intercept of the invariant mass shell.

---

## Visual consistency rules

- Use `(+,-,-,-)` metric signature throughout.
- Keep `ct` and `E/c` as vertical coordinates in diagrams.
- Keep equations adjacent to the geometry they explain.
- Prefer transformations/morphs over replacing one unrelated equation card with another.
- Avoid decorative animation that does not carry conceptual information.
- Use the same symbol definitions in all scenes and docs.
- Do not imply that mass literally disappears when energy is released; distinguish invariant mass, total energy, and binding energy carefully when later topics are added.

## First milestone acceptance criteria

The five scenes should render independently, but also form one continuous conceptual chain when played in order. The viewer should be able to reconstruct the following argument without outside text:

```text
Lorentz invariance
→ proper time
→ four-velocity invariant
→ four-momentum invariant
→ energy-momentum relation
→ rest-frame energy
```
