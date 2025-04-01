from manim import *

class diskpend(Scene):
    def construct(self):
        circle = Circle(radius=0.2, color=GREEN)  # create a circle
        circle.move_to(LEFT * 2)
        seg = Line([-2.2,0,0], [-1.8,0,0], color=GREEN)

        l = Line([-2.2,-0.2,0], [2.2,-0.2,0])

        self.add(circle, seg, l)  # animate the creation of the square
        self.wait(1)

        circle.generate_target()
        circle.target.shift(4*RIGHT)
        seg.generate_target()
        seg.target.shift(4*RIGHT).rotate(3*PI)

        self.play(MoveToTarget(circle), MoveToTarget(seg), run_time=4, rate_func=linear)
        # self.play(MoveToTarget(seg), run_time=4, rate_func=linear)


        self.wait(2)
