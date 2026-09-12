from manimlib import *
import numpy as np


class MassEnergyRelation(Scene):
    """Visualize the invariant mass shell and recover E0 = mc^2 at p = 0."""

    def construct(self):
        title = Text("Mass-energy equivalence is a rest-frame statement")
        title.to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=(-4, 4, 1),
            y_range=(0, 5, 1),
            width=9,
            height=5.5,
        )
        p_label = Tex("p").next_to(axes.x_axis.get_right(), DOWN)
        e_label = Tex("E/c").next_to(axes.y_axis.get_top(), LEFT)
        self.play(ShowCreation(axes), Write(p_label), Write(e_label))

        # Naturalized plotting units: c = 1 and mc = 1.
        # The rendered equation keeps explicit factors of c.
        mc = 1.0

        mass_shell = ParametricCurve(
            lambda u: axes.c2p(u, np.sqrt(u * u + mc * mc)),
            t_range=(-3.6, 3.6, 0.02),
        )
        self.play(ShowCreation(mass_shell))

        invariant = Tex(
            "\\left(\\frac{E}{c}\\right)^2-p^2=m^2c^2"
        )
        invariant.to_corner(UR).shift(DOWN * 0.8)
        self.play(Write(invariant))

        p0 = 2.4
        moving_dot = Dot(axes.c2p(p0, np.sqrt(p0 * p0 + mc * mc)))
        moving_label = Tex("(p,E/c)").next_to(moving_dot, RIGHT)
        self.play(FadeIn(moving_dot), Write(moving_label))

        relation = Tex("E^2=p^2c^2+m^2c^4")
        relation.to_edge(DOWN)
        self.play(Write(relation))

        rest_point = axes.c2p(0, mc)
        rest_label = Tex("p=0")
        rest_label.next_to(rest_point, LEFT)

        self.play(
            moving_dot.animate.move_to(rest_point),
            FadeOut(moving_label),
        )
        self.play(Write(rest_label))

        rest_relation = Tex("E_0^2=m^2c^4")
        rest_relation.next_to(invariant, DOWN, buff=0.5)
        self.play(Write(rest_relation))

        result = Tex("E_0=mc^2")
        result.scale(1.6)
        result.next_to(rest_relation, DOWN, buff=0.6)
        box = SurroundingRectangle(result)
        self.play(Write(result), ShowCreation(box))

        note = Text("same mass shell, different observer")
        note.scale(0.6)
        note.next_to(axes, LEFT)
        self.play(Write(note))
        self.wait(2)
