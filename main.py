from manim import *


class Expo1(Scene):
    def construct(self):
        self: Scene

        text = Text("Welcome to expos")

        self.play(Write(text))
        self.wait(0.2)
        self.play(FadeOut(text))
