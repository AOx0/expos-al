from manim import *


class Expo1(Scene):
    def construct(self):
        self: Scene

        text = MathTex(r"""
            \left(
            \begin{array}{ccccc|c}
             1 & 2 & 4 & 1 & -1 & 1 \\
             2 & 4 & 8 & 3 & -4 & 2 \\
             1 & 3 & 7 & 0 & 3 & -2 \\
            \end{array}
            \right)
        """)

        self.play(Write(text))
        self.wait(0.2)
        self.play(FadeOut(text))
