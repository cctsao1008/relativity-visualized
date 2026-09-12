from manimlib import *


class FourVelocity(Scene):
    """Construct four-velocity from proper time and expose its invariant norm."""

    def construct(self):
        title = Text("Four-velocity turns motion into a Lorentz four-vector")
        title.to_edge(UP)
        self.play(Write(title))

        x_mu = Tex("x^\\mu=(ct,\\mathbf{x})")
        x_mu.scale(1.2)
        self.play(Write(x_mu))

        definition = Tex(
            "U^\\mu=\\frac{dx^\\mu}{d\\tau}"
        )
        definition.next_to(x_mu, DOWN, buff=0.7)
        self.play(Write(definition))

        expanded = Tex(
            "U^\\mu=\\left(c\\frac{dt}{d\\tau},"
            "\\frac{d\\mathbf{x}}{d\\tau}\\right)"
        )
        expanded.next_to(definition, DOWN, buff=0.7)
        self.play(Write(expanded))

        gamma_form = Tex(
            "U^\\mu=(\\gamma c,\\gamma\\mathbf{v})"
        )
        gamma_form.next_to(expanded, DOWN, buff=0.7)
        self.play(Write(gamma_form))

        norm = Tex(
            "U^\\mu U_\\mu="
            "\\gamma^2(c^2-v^2)"
        )
        norm.to_edge(LEFT).shift(DOWN * 2.6)
        self.play(Write(norm))

        result = Tex("U^\\mu U_\\mu=c^2")
        result.scale(1.3)
        result.to_edge(RIGHT).shift(DOWN * 2.6)
        box = SurroundingRectangle(result)
        self.play(Write(result), ShowCreation(box))
        self.wait(2)
