from manimlib import *


class FourMomentum(Scene):
    """Construct four-momentum and expose the energy-momentum pairing."""

    def construct(self):
        title = Text("Energy and momentum are components of one four-vector")
        title.to_edge(UP)
        self.play(Write(title))

        start = Tex("P^\\mu=mU^\\mu")
        start.scale(1.3)
        self.play(Write(start))

        expanded = Tex(
            "P^\\mu=(\\gamma mc,\\gamma m\\mathbf{v})"
        )
        expanded.next_to(start, DOWN, buff=0.7)
        self.play(Write(expanded))

        momentum = Tex("\\mathbf{p}=\\gamma m\\mathbf{v}")
        momentum.next_to(expanded, DOWN, buff=0.7)
        self.play(Write(momentum))

        energy = Tex("E=\\gamma mc^2")
        energy.next_to(momentum, DOWN, buff=0.7)
        self.play(Write(energy))

        final = Tex(
            "P^\\mu=\\left(\\frac{E}{c},\\mathbf{p}\\right)"
        )
        final.scale(1.3)
        final.next_to(energy, DOWN, buff=0.8)
        box = SurroundingRectangle(final)
        self.play(Write(final), ShowCreation(box))

        spacetime = Tex("x^\\mu=(ct,\\mathbf{x})")
        spacetime.to_corner(DL)
        energy_momentum = Tex(
            "P^\\mu=\\left(E/c,\\mathbf{p}\\right)"
        )
        energy_momentum.to_corner(DR)

        self.play(Write(spacetime), Write(energy_momentum))
        self.wait(2)
