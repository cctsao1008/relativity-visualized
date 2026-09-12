from manimlib import *


class ProperTime(Scene):
    """Connect the invariant spacetime interval to proper time."""

    def construct(self):
        title = Text("Proper time is the invariant interval measured by the traveler")
        title.to_edge(UP)
        self.play(Write(title))

        eq1 = Tex("c^2d\\tau^2=c^2dt^2-dx^2")
        eq1.scale(1.2)
        self.play(Write(eq1))
        self.wait()

        eq2 = Tex("dx=v\\,dt")
        eq2.next_to(eq1, DOWN, buff=0.6)
        self.play(Write(eq2))

        eq3 = Tex(
            "c^2d\\tau^2=c^2dt^2-v^2dt^2"
        )
        eq3.next_to(eq2, DOWN, buff=0.6)
        self.play(Write(eq3))

        eq4 = Tex(
            "d\\tau=dt\\sqrt{1-\\frac{v^2}{c^2}}"
        )
        eq4.next_to(eq3, DOWN, buff=0.6)
        self.play(Write(eq4))

        gamma = Tex(
            "\\gamma=\\frac{1}{\\sqrt{1-v^2/c^2}}"
        )
        gamma.to_edge(LEFT).shift(DOWN * 2.5)
        self.play(Write(gamma))

        result = Tex("d\\tau=\\frac{dt}{\\gamma}")
        result.scale(1.3)
        result.to_edge(RIGHT).shift(DOWN * 2.5)
        box = SurroundingRectangle(result)
        self.play(Write(result), ShowCreation(box))
        self.wait(2)
