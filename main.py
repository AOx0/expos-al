from manim import *


def animate_change(self, text, text0, text3, text3_pos, offset, n1, n2):
    text_b = MathTex(r"-2 {(" + str(n1) + "})} + {(" + str(n2) + ")}").next_to(text, DOWN).shift(DOWN)

    if offset == 5:
        text3[0][9 + offset:9 + offset + 2].set_color(YELLOW)
        text3[0][1 + offset:1 + offset + 2].set_color(YELLOW)
        text_b[0][3:5].set_color(YELLOW)
        text_b[0][8:10].set_color(YELLOW)
    else:
        text3[0][10 + offset].set_color(YELLOW)
        text3[0][2 + offset].set_color(YELLOW)
        text_b[0][3].set_color(YELLOW)
        text_b[0][7].set_color(YELLOW)

    self.play(AnimationGroup(Transform(text0, text3), FadeIn(text_b)))
    self.wait(0.5)
    self.play(AnimationGroup(Transform(text0, text3_pos), FadeOut(text_b)))
    self.wait(0.1)

    if offset == 5:
        text3[0][9 + offset:9 + offset + 2].set_color(WHITE)
        text3[0][1 + offset:1 + offset + 2].set_color(WHITE)
    else:
        text3[0][10 + offset].set_color(WHITE)
        text3[0][2 + offset].set_color(WHITE)

    self.play(Transform(text0, text3_pos))


class Expo1(Scene):
    def construct(self):
        self: Scene

        corona = ImageMobject("./Intro.jpg")
        corona.scale(0.4)

        self.play(FadeIn(corona))

        self.wait(3)

        self.play(*[FadeOut(obj) for obj in self.mobjects])

        text1 = MathTex(r"\text{Ejercicio}").shift(UP)
        text2 = MathTex(r"\text{Archivo 1 - Problema 1D}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Mayo 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        text0 = Text(
            "Resolver los siguientes sistemas de ecuaciones por medio\n"
            "de Gauss y de interpretacion geometrica del conjunto solucion", font_size=23.0
        )

        self.play(Write(text0))

        self.wait(2)

        text0.shift(UP * 2)

        text1 = MathTex(
            r"""
            x_1 + 2x_2 + 4x_3 + x_4  -x_5 = 1\\
            2x_1 + 4x_2 + 8x_3 + 3x_4 -4x_5 = 2 \\
            x_1 + 3x_2 + 7x_3 + 0x_4 + 3x_5 = -2 \\
            """
        )

        self.play(Write(text1))

        self.wait(1)

        self.play(FadeOut(text0), FadeOut(text1))

        text0 = MathTex(r"""
        \left(
            \begin{array}{ccccc|c}
             1 & 2 & 4 & 1 & -1 & 1 \\
             2 & 4 & 8 & 3 & -4 & 2 \\
             1 & 3 & 7 & 0 & 3 & -2 \\
            \end{array}
        \right)
        """)

        text = MathTex(r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     2 & 4 & 8 & 3 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """)

        text_a = MathTex(r"""-2 R_1 + R_2""").next_to(text, UP).shift(UP)
        text_b = MathTex(r"""-2 {(1)} + {(2)}""").next_to(text, DOWN).shift(DOWN)

        # self.add(index_labels(text[0]))

        text_b[0][3].set_color(YELLOW)
        text_b[0][7].set_color(YELLOW)

        text2 = MathTex(
            r"""
            \left(
                \begin{array}{ccccc|c}
                 1 & 2 & 4 & 1 & -1 & 1 \\
                 0 & 4 & 8 & 3 & -4 & 2 \\
                 1 & 3 & 7 & 0 & 3 & -2 \\
                \end{array}
            \right)
            """,
        )

        text[0][10].set_color(YELLOW)
        text[0][2].set_color(YELLOW)

        text2[0][10].set_color(YELLOW)
        text2[0][2].set_color(YELLOW)

        self.play(Write(text0))
        self.wait(1)
        self.play(Write(text_a))
        self.wait(1)
        self.play(AnimationGroup(Write(text_b), Transform(text0, text)))
        self.wait(1)
        self.play(AnimationGroup(Transform(text0, text2), FadeOut(text_b)))
        self.wait(0.1)
        text2[0][10].set_color(WHITE)
        text2[0][2].set_color(WHITE)
        self.play(Transform(text0, text2))

        animate_change(
            self, text, text0,
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 4 & 8 & 3 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 8 & 3 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            1, 2, 4
        )

        animate_change(
            self, text, text0,
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 8 & 3 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 0 & 3 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            2, 4, 8
        )

        animate_change(
            self, text, text0,
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 0 & 3 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 0 & 1 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            3, 1, 3
        )

        animate_change(
            self, text, text0,
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 0 & 1 & -4 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 0 & 1 & -2 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            5, -1, -4
        )

        animate_change(
            self, text, text0,
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 0 & 1 & -2 & 2 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            MathTex(
                r"""
                \left(
                    \begin{array}{ccccc|c}
                     1 & 2 & 4 & 1 & -1 & 1 \\
                     0 & 0 & 0 & 1 & -2 & 0 \\
                     1 & 3 & 7 & 0 & 3 & -2 \\
                    \end{array}
                \right)
                """,
            ),
            7, 1, 2
        )

        self.play(FadeOut(text_a))

        self.wait(0.5)

        text_a = MathTex(r"""- R_1 + R_3""").next_to(text, UP).shift(UP)

        self.play(Write(text_a))

        text4 = MathTex(
            r"""
            \left(
                \begin{array}{ccccc|c}
                 1 & 2 & 4 & 1 & -1 & 1 \\
                 0 & 0 & 0 & 1 & -2 & 0 \\
                 1 & 3 & 7 & 0 & 3 & -2 \\
                \end{array}
            \right)
            """
        )

        text4[0][2:8].set_color(YELLOW)
        text4[0][9:10].set_color(YELLOW)

        text4[0][18:18 + 5].set_color(YELLOW)
        text4[0][19+5:18+8].set_color(YELLOW)

        self.wait(0.5)

        self.play(Transform(text0, text4))

        self.wait(1)

        text5 = MathTex(
            r"""
            \left(
                \begin{array}{ccccc|c}
                 1 & 2 & 4 & 1 & -1 & 1 \\
                 0 & 0 & 0 & 1 & -2 & 0 \\
                 0 & 1 & 3 & -1 & 4 & -3 \\
                \end{array}
            \right)
            """
        )

        self.play(FadeTransform(text0, text5), FadeOut(text_a))

        text_a = MathTex(r"""R_2 \leftrightarrow R_3""").next_to(text, UP).shift(UP)
        self.play(Write(text_a))

        self.wait(0.5)

        text6 = MathTex(
            r"""
            \left(
                \begin{array}{ccccc|c}
                 1 & 2 & 4 & 1 & -1 & 1 \\
                 0 & 1 & 3 & -1 & 4 & -3 \\
                 0 & 0 & 0 & 1 & -2 & 0 \\
                \end{array}
            \right)
            """
        )

        self.play(FadeTransform(text5, text6), FadeOut(text_a))

        self.wait(0.5)

        self.play(text6.animate.shift(UP*2))

        text6 = MathTex(
            r"""
            x_4 - 2x_5 = 0 
            """
        )

        text7 = MathTex(
            r"""
            x_4 = 2x_5\\
            """
        ).next_to(text6, DOWN)

        self.wait(0.5)

        self.play(Write(text6))
        self.wait(0.2)

        self.play(Write(text7))
        self.wait(0.2)

        self.play(AnimationGroup(
            FadeOut(text6),
            text7.animate.shift(LEFT * 4),
        ))

        self.wait(0.2)

        text9 = MathTex(
            r"""
            x_2 + 3x_3 -x_4 + 4x_5 = -3
            """
        ).shift(RIGHT)

        text10 = MathTex(
            r"""
            x_2 + 3x_3 -2x_5 + 4x_5 = -3
            """
        ).next_to(text9, DOWN)

        text11 = MathTex(
            r"""
            x_2 + 3x_3 + 2x_5 = -3
            """
        ).next_to(text10, DOWN)

        text12 = MathTex(
            r"""
            x_2 = -3 - 3x_3 - 2x_5
            """
        ).next_to(text11, DOWN)

        self.play(Write(text9))
        self.wait(0.2)

        self.play(Write(text10))
        self.wait(0.2)

        self.play(Write(text11))
        self.wait(0.2)

        self.play(Write(text12))
        self.wait(0.2)

        self.play(AnimationGroup(
            FadeOut(text9),
            FadeOut(text10),
            FadeOut(text11),
            text7.animate.shift(UP),
            text12.animate.next_to(text7, RIGHT * 1.5)
        ))

        self.play(AnimationGroup(
            text12.animate.shift(UP),
        ))

        self.wait(0.2)

        text13 = MathTex(
            r"""
            x_1 + 2x_2 + 4x_3 + x_4 -1x_5 = 1
            """
        ).shift(0.5 * DOWN)

        text14 = MathTex(
            r"""
            x_1 + 2(-3 - 3x_3 - 2x_5) + 4x_3 + (2x_5) -1x_5 = 1
            """
        ).next_to(text13, DOWN)

        text15 = MathTex(
            r"""
            x_1 -6 - 6x_3 - 4x_5 + 4x_3 + 2x_5 -1x_5 = 1
            """
        ).next_to(text14, DOWN)

        text16 = MathTex(
            r"""
            x_1 - 2x_3 - 3x_5 = 7
            """
        ).next_to(text15, DOWN)

        text17 = MathTex(
            r"""
            x_1 = 2x_3 + 3x_5 + 7
            """
        ).next_to(text16, DOWN)

        self.play(Write(text13))
        self.wait(0.2)

        self.play(Write(text14))
        self.wait(0.2)

        self.play(Write(text15))
        self.wait(0.2)

        self.play(Write(text16))
        self.wait(0.2)

        self.play(Write(text17))
        self.wait(0.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        text100 = MathTex("x_4 = 2x_5")
        text101 = MathTex("x_2 = - 3x_3 - 2x_5 -3").next_to(text100, UP)
        text102 = MathTex("x_1 = 2x_3 + 3x_5 + 7").next_to(text100, DOWN)

        self.play(*[FadeIn(mob) for mob in [text100, text101, text102]])

        self.wait(0.2)

        self.play(*[mob.animate.shift(UP * 2) for mob in [text100, text101, text102]])

        result = MathTex(r"""
        \left( \begin{array}{r}
             x_1 \\
             x_2 \\
             x_4
        \end{array} \right)
        =
        x_3 \left( \begin{array}{r}
             2\\
             - 3\\
             0
        \end{array} \right)
        +
        x_5 \left( \begin{array}{r}
             3\\
             -2\\
             2
        \end{array} \right)
        +
        \left( \begin{array}{r}
             7\\
             -3\\
             0
        \end{array} \right)
        """).shift(DOWN)

        self.play(Write(result))

        self.wait(5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        self.wait(1)


def parametric(u: float, v:float ):
    return np.array([
        -3.0 * u - 2.0 * v - 3.0,
        2.0 * u,
        2.0 * u + 3.0 * v + 7.0,
    ])


class Expo1Pos(ThreeDScene):
    def construct(self):
        curve1 = Surface(
            lambda u, v: np.array([
                -3.0 * u - 2.0 * v - 3.0,
                2.0 * u,
                2.0 * u + 3.0 * v + 7.0,
            ])
            , color=RED, u_range=[-PI, PI], v_range=[-PI, PI]
        ).set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)

        self.begin_ambient_camera_rotation(rate=1)

        self.play(Create(axes), Create(curve1))

        self.wait()


class Expo2(Scene):
    def construct(self):
        corona = ImageMobject("./Intro.jpg")
        corona.scale(0.4)

        self.play(FadeIn(corona))

        self.wait(3)

        self.play(*[FadeOut(obj) for obj in self.mobjects])

        text1 = MathTex(r"\text{Ejercicio}").shift(UP)
        text2 = MathTex(r"\text{Archivo 2 - Problema C25}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Mayo 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        text1 = MathTex(r"\text{1. Determine si } S \text{ genera } M_{2,2}").shift(UP * 2)
        text2 = MathTex(r"\text{2. Determine si } S \text{ es linealmente independiente}").next_to(text1, DOWN)

        self.play(Write(text1))
        self.play(Write(text2))

        texto = MathTex(r"""
        S = \left\{
            \left(
            \begin{array}{cc}
                 1 & 2 \\
                 2 & 1\\
            \end{array}
            \right),
            \left(
            \begin{array}{cc}
                 2 & 1 \\
                 -1 & 2\\
            \end{array}
            \right),
            \left(
            \begin{array}{cc}
                 0 & 1 \\
                 1 & 2\\
            \end{array}
            \right)
        \right\}""")

        self.play(Write(texto))
        self.wait(1)

        self.play(*[FadeOut(obj) for obj in (text1, text2)])

        gen1 = MathTex(r"""
            \text{gen}(S) = 
            x_1 \left(
            \begin{array}{cc}
                 1 & 2 \\
                 2 & 1\\
            \end{array}
            \right) + 
            x_2 \left(
            \begin{array}{cc}
                 2 & 1 \\
                 -1 & 2\\
            \end{array}
            \right) +
            x_3 \left(
            \begin{array}{cc}
                 0 & 1 \\
                 1 & 2\\
            \end{array}
            \right)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen1))
        self.wait(1)

        gen2 = MathTex(r"""
            \text{gen}(S) = 
             \left(
            \begin{array}{cc}
                 x_1 & 2x_1 \\
                 2x_1 & x_1\\
            \end{array}
            \right) + 
            \left(
            \begin{array}{cc}
                 2x_2 & x_2 \\
                 -x_2 & 2x_2\\
            \end{array}
            \right) +
            \left(
            \begin{array}{cc}
                 0 & x_3 \\
                 x_3 & 2x_3\\
            \end{array}
            \right)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen2))
        self.wait(1)

        gen3 = MathTex(r"""
            \text{gen}(S) = 
             \left(
                \begin{array}{cc}
                     x_1 + 2x_2 & 2x_1 + x_2 + x_3\\
                     2x_1-x_2+x_3 & x_1+2x_2+2x_3\\
                \end{array}
            \right)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen3))
        self.wait(1)

        gen4 = MathTex(r"""
           \left(
               \begin{array}{cc}
                    a & b\\
                    c & d\\
               \end{array}
           \right) = 
            \left(
               \begin{array}{cc}
                    x_1 + 2x_2 & 2x_1 + x_2 + x_3\\
                    2x_1-x_2+x_3 & x_1+2x_2+2x_3\\
               \end{array}
           \right)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen4))
        self.wait(1)

        gen5 = MathTex(r"""
           x_1 + 2x_2 = a\\
           2x_1 + x_2 + x_3 = b\\
           2x_1-x_2+x_3 = c\\
           x_1+2x_2+2x_3 = d
       """)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen5))
        self.wait(1)

        gen6 = MathTex(r"""
            \left(
               \begin{array}{ccc|c}
                    1 & 2 & 0 & a \\
                    2 & 1 & 1 & b \\
                    2 & -1 & 1 & c\\
                    1 & 2 & 2 & d\\
               \end{array}
           \right)
        """)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen6))
        self.wait(1)

        gen7 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & -3 & 1 & b-2 a \\
 2 & -1 & 1 & c \\
 1 & 2 & 2 & d \\
\end{array}
\right)
        """)
        gen7m = MathTex(r"\xrightarrow{-2 R_1 + R_2}").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen8 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & -3 & 1 & b-2 a \\
 0 & -5 & 1 & c-2 a \\
 1 & 2 & 2 & d \\
\end{array}
\right)
                """)
        gen8m = MathTex(r"\xrightarrow{-2 R_1 + R_3}").next_to(gen8, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen8), Write(gen8m))
        self.wait(1)

        gen9 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & -3 & 1 & b-2 a \\
 0 & -5 & 1 & c-2 a \\
 0 & 0 & 2 & d-a \\
\end{array}
\right)
                        """)
        gen9m = MathTex(r"\xrightarrow{- R_1 + R_4}").next_to(gen9, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen9), Write(gen9m))
        self.wait(1)

        gen10 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & 1 & -\frac{1}{3} & \frac{1}{3} (2 a-b) \\
 0 & -5 & 1 & c-2 a \\
 0 & 0 & 2 & d-a \\
\end{array}
\right)
                                """)
        gen10m = MathTex(r"\xrightarrow{- \frac{1}{3}R_2 }").next_to(gen10, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen10), Write(gen10m))
        self.wait(1)

        gen10 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & 1 & -\frac{1}{3} & \frac{1}{3} (2 a-b) \\
 0 & 0 & -\frac{2}{3} & \frac{4 a}{3}-\frac{5 b}{3}+c \\
 0 & 0 & 2 & d-a \\
\end{array}
\right)
                                        """)
        gen10m = MathTex(r"\xrightarrow{5 R_2 + R_3}").next_to(gen10, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen10), Write(gen10m))
        self.wait(1)

        gen10 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & 1 & -\frac{1}{3} & \frac{1}{3} (2 a-b) \\
 0 & 0 & 1 & \frac{1}{2} (-4 a+5 b-3 c) \\
 0 & 0 & 2 & d-a \\
\end{array}
\right)
                                                """)
        gen10m = MathTex(r"\xrightarrow{-\frac{3}{2} R_3}").next_to(gen10, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen10), Write(gen10m))
        self.wait(1)

        gen10 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & 1 & -\frac{1}{3} & \frac{1}{3} (2 a-b) \\
 0 & 0 & 1 & \frac{1}{2} (-4 a+5 b-3 c) \\
 0 & 0 & 0 & 3 a-5 b+3 c+d \\
\end{array}
\right)
                                                        """)
        gen10m = MathTex(r"\xrightarrow{-2 R_3 + R_4}").next_to(gen10, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen10), Write(gen10m))
        self.wait(1)

        gen10 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 2 & 0 & a \\
 0 & 1 & 0 & \frac{b-c}{2} \\
 0 & 0 & 1 & \frac{1}{2} (-4 a+5 b-3 c) \\
 0 & 0 & 0 & 3 a-5 b+3 c+d \\
\end{array}
\right)
                                                                """)
        gen10m = MathTex(r"\xrightarrow{\frac{1}{3} R_3 + R_2}").next_to(gen10, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen10), Write(gen10m))
        self.wait(1)

        gen10 = MathTex(r"""
\left(
\begin{array}{ccc|c}
 1 & 0 & 0 & a-b+c \\
 0 & 1 & 0 & \frac{b-c}{2} \\
 0 & 0 & 1 & \frac{1}{2} (-4 a+5 b-3 c) \\
 0 & 0 & 0 & 3 a-5 b+3 c+d \\
\end{array}
\right)
                                                                        """)
        gen10m = MathTex(r"\xrightarrow{-2 R_2 + R_1}").next_to(gen10, LEFT)

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen10), Write(gen10m))
        self.wait(1)

        gen10 = MathTex(r"""
                    \text{La matriz reducida tiene la diagonal (1,1,1)}\\ 
                    \therefore \text{Hay 3 unos principales}\\
                    \therefore S \text{ es linearmente independiente}\\
                    0 \neq 3 a-5 b+3 c+d\\
                    \therefore \text{No hay } x_1, x_2, x_3 \text{ que generen } M_{2,2}\\
                    \therefore S \text{ no genera } M_{2,2}
                """)

        self.play(*[obj.animate.shift(UP * 4) for obj in self.mobjects])
        self.play(Write(gen10))

        self.wait(10)

        self.play(*[FadeOut(obj) for obj in self.mobjects])
