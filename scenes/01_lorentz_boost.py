from manimlib import *
import numpy as np


class LorentzBoost(Scene):
    """Visualize a 1+1D Lorentz boost and the invariant spacetime interval."""

    def construct(self):
        title = Text("Lorentz transformation preserves the spacetime interval")
        title.to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=(-5, 5, 1),
            y_range=(-1, 6, 1),
            width=10,
            height=6,
        )
        x_label = Tex("x").next_to(axes.x_axis.get_right(), DOWN)
        ct_label = Tex("ct").next_to(axes.y_axis.get_top(), LEFT)
        self.play(ShowCreation(axes), Write(x_label), Write(ct_label))

        # Use c = 1 in the diagram so time and space share the same axis scale.
        event = np.array([2.0, 4.0])
        event_dot = Dot(axes.c2p(*event))
        event_vector = Arrow(axes.c2p(0, 0), axes.c2p(*event), buff=0)
        event_label = Tex("(x,ct)").next_to(event_dot, RIGHT)
        self.play(GrowArrow(event_vector), FadeIn(event_dot), Write(event_label))

        invariant = Tex("(ct)^2-x^2=\text{invariant}")
        invariant.to_corner(UR).shift(DOWN * 0.8)
        self.play(Write(invariant))

        # Positive-time branch of t^2 - x^2 = s^2, with s^2 = 12 for the event above.
        s2 = event[1] ** 2 - event[0] ** 2

        def hyperbola_point(x):
            return axes.c2p(x, np.sqrt(x * x + s2))

        hyperbola = ParametricCurve(
            lambda u: hyperbola_point(u),
            t_range=(-3.5, 3.5, 0.02),
        )
        self.play(ShowCreation(hyperbola))

        beta = 0.55
        gamma = 1.0 / np.sqrt(1.0 - beta**2)

        # Axes of S' expressed in S coordinates: x'=0 => x=beta ct,
        # and ct'=0 => ct=beta x.
        ct_prime = Line(
            axes.c2p(0, 0),
            axes.c2p(beta * 5.0, 5.0),
        )
        x_prime = Line(
            axes.c2p(-4.5, beta * -4.5),
            axes.c2p(4.5, beta * 4.5),
        )
        ct_prime_label = Tex("ct'").next_to(ct_prime.get_end(), RIGHT)
        x_prime_label = Tex("x'").next_to(x_prime.get_end(), DOWN)

        boost_eq = Tex(
            "ct'=\\gamma(ct-\\beta x),\\qquad "
            "x'=\\gamma(x-\\beta ct)"
        )
        boost_eq.to_edge(DOWN)

        self.play(
            ShowCreation(ct_prime),
            ShowCreation(x_prime),
            Write(ct_prime_label),
            Write(x_prime_label),
        )
        self.play(Write(boost_eq))

        xp = gamma * (event[0] - beta * event[1])
        ctp = gamma * (event[1] - beta * event[0])
        transformed = Tex(
            f"(x',ct')=({xp:.2f},{ctp:.2f})"
        )
        transformed.next_to(boost_eq, UP)
        self.play(Write(transformed))

        conclusion = Tex("(ct')^2-(x')^2=(ct)^2-x^2")
        conclusion.next_to(invariant, DOWN)
        self.play(Write(conclusion))
        self.wait(2)
