# relativity-visualized

Programmatic visual explanations of special relativity, built with **ManimGL**.

The project begins with one concrete question:

> Why is $E_0 = mc^2$ a geometric consequence of Lorentz invariance rather than an isolated formula to memorize?

The first sequence develops the idea through spacetime geometry and four-vectors:

```text
Lorentz transformation
    ↓
Minkowski spacetime
    ↓
proper time
    ↓
four-velocity
    ↓
four-momentum
    ↓
E² = p²c² + m²c⁴
    ↓
rest frame
    ↓
E₀ = mc²
```

## Repository principle

> **README explains the system. Issues explain the journey. Code proves the current state.**

- `README.md` and `docs/` contain durable concepts, architecture, notation, rationale, and usage.
- GitHub Issues contain experiments, evolving decisions, limitations, and implementation progress.
- `scenes/` is the executable evidence of what has actually been implemented.

Initial work is tracked in [Issue #1](https://github.com/cctsao1008/relativity-visualized/issues/1). Math-rendering normalization is tracked in [Issue #2](https://github.com/cctsao1008/relativity-visualized/issues/2).

## Why visualization?

Special relativity is often taught as a sequence of equations. That is mathematically valid, but it can hide the structural idea: Lorentz transformations preserve a spacetime interval, and the same geometry reappears in energy-momentum space.

This project therefore follows a consistent teaching order:

1. show the geometry,
2. identify the invariant,
3. introduce the corresponding four-vector,
4. derive the algebra,
5. only then specialize to the familiar formula.

The central analogy is:

| Spacetime | Energy-momentum space |
| --- | --- |
| $x^\mu = (ct,\mathbf{x})$ | $P^\mu = \left(E/c,\mathbf{p}\right)$ |
| $c^2 d\tau^2 = c^2 dt^2 - d\mathbf{x}^2$ | $m^2c^2 = E^2/c^2 - p^2$ |
| proper time $\tau$ is invariant | rest mass $m$ is invariant |
| Lorentz boost mixes $ct$ and $x$ | Lorentz boost mixes $E/c$ and $p$ |

## Current scope

The initial repository intentionally focuses on **1+1 dimensional motion** wherever possible. This keeps the geometry visible and the notation compact while preserving the essential relativistic structure.

The first five scenes are:

| Scene | Purpose |
| --- | --- |
| `01_lorentz_boost.py` | Show how Lorentz boosts mix time and space while preserving the interval. |
| `02_proper_time.py` | Connect the invariant interval to proper time. |
| `03_four_velocity.py` | Construct four-velocity and show its invariant Minkowski norm. |
| `04_four_momentum.py` | Construct four-momentum and identify its temporal component with energy. |
| `05_mass_energy_relation.py` | Visualize the energy-momentum hyperbola and recover $E_0 = mc^2$ in the rest frame. |

See [`docs/derivation.md`](docs/derivation.md) for the mathematical chain and [`docs/visual-storyboard.md`](docs/visual-storyboard.md) for the visual narrative.

## Toolchain

The first implementation targets **3Blue1Brown's ManimGL** (`3b1b/manim`) only.

Requirements:

- Python 3.10+
- ManimGL (`manimgl`)
- FFmpeg
- OpenGL
- LaTeX for equation rendering

Install the Python dependency:

```bash
python -m pip install -e .
```

Or install ManimGL directly:

```bash
python -m pip install manimgl
```

## Render a scene

From the repository root:

```bash
manimgl scenes/01_lorentz_boost.py LorentzBoost
```

Write the rendered animation to a file:

```bash
manimgl scenes/05_mass_energy_relation.py MassEnergyRelation -w
```

During development, rendering a single final frame is useful:

```bash
manimgl scenes/05_mass_energy_relation.py MassEnergyRelation -s
```

## Notation

We use metric signature $(+,-,-,-)$, so that

$$
x^\mu x_\mu = c^2t^2 - |\mathbf{x}|^2
$$

and

$$
P^\mu P_\mu = \frac{E^2}{c^2} - |\mathbf{p}|^2 = m^2c^2.
$$

Primary symbols:

| Symbol | Meaning |
| --- | --- |
| $c$ | speed of light |
| $v$ | ordinary three-velocity; in early scenes, one-dimensional velocity |
| $\beta = v/c$ | dimensionless velocity |
| $\gamma = 1/\sqrt{1-\beta^2}$ | Lorentz factor |
| $\tau$ | proper time |
| $U^\mu$ | four-velocity |
| $P^\mu$ | four-momentum |
| $p$ | ordinary relativistic momentum |
| $m$ | invariant/rest mass |
| $E$ | total relativistic energy |
| $E_0$ | rest energy |

## Derivation target

The project does **not** start by assuming $E = mc^2$.

It derives the invariant relation

$$
E^2 = p^2c^2 + m^2c^4
$$

and then evaluates it in the particle's rest frame:

$$
p = 0
\quad\Rightarrow\quad
E_0^2 = m^2c^4
\quad\Rightarrow\quad
E_0 = mc^2.
$$

The positive-energy branch is used for ordinary particles.

## Math-rendering convention

Repository Markdown follows GitHub's native mathematical-expression syntax:

- inline math uses `$...$`,
- display math uses `$$...$$`,
- fenced `math` blocks may be used when they improve readability or avoid Markdown conflicts,
- backticks are reserved for code, filenames, commands, and intentionally literal text.

## Boundaries

The first milestone does not attempt to cover:

- general relativity,
- curved spacetime,
- quantum field theory,
- full tensor calculus,
- relativistic electrodynamics,
- all historical derivations of mass-energy equivalence.

Those may be added later as separate research/visualization threads.

## Project status

Initial skeleton created from Issue #1. The five executable scenes are intentionally compact first-pass implementations. Their purpose is to establish a coherent, inspectable path from Lorentz geometry to the mass-energy relation before adding production-level polish.

## License

No license has been selected yet. Add one explicitly before treating the repository as reusable software outside personal/research use.
