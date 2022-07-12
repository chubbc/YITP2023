from manim_slide import *
import math

config.background_color = "#161c20"

toc=Group(
    Tex(r"\bfseries Lecture 1").scale(1.2),
    Tex("Basics of decoding"),
    Tex("Surface code"),
    Tex("Decoding as stat mech"),
    Tex(r"\bfseries Lecture 2").scale(1.2),
    Tex("Other models"),
    Tex("Stat mech decoders"),
    Tex("Tensor network decoding"),
).scale(0.9).arrange(DOWN,aligned_edge=LEFT,buff=0.25).move_to(ORIGIN)
toc[0:4].shift(UP)
toc[0].set_x(0).shift(0.25*UP)
toc[4].set_x(0).shift(0.25*UP)

footer=MathTex("\\texttt{christopherchubb.com/IBM2022}").scale(1/2).to_corner(DOWN).set_opacity(.5)

class Title(SlideScene):
    def construct(self):
        title = Tex(r"\bfseries\textsc{QEC Decoding}").scale(1.25).shift(2.5*UP)
        arxiv = Tex(r"\bfseries{Decoding and statistical mechanics}}").scale(.75).shift(1.5*UP)
        name = Tex("Christopher T.\ Chubb")
        ethz=SVGMobject("ethz_logo_white.svg").scale(1/3).move_to(1.5*DOWN)
        self.add(name,title,arxiv,ethz,footer)
        self.slide_break()

        self.play(Unwrite(title),Unwrite(arxiv),Unwrite(name),Unwrite(ethz))
        self.wait()
        self.play(FadeIn(toc))
        self.slide_break()

        self.play(
            toc[1].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[1].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[1].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[1].width*LEFT/1.2),
            toc[2].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[2].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[2].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[2].width*LEFT/1.2),
            toc[3].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[3].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[3].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[3].width*LEFT/1.2),
            toc[5].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[5].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[5].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[5].width*LEFT/1.2),
            toc[6].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[6].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[6].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[6].width*LEFT/1.2),
            toc[7].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[7].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[7].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[7].width*LEFT/1.2),
        )

class Basics(SlideScene):
    def construct(self):
        tocindex=1
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        self.slide_break()


        p0=Tex("Passive").move_to(3*LEFT+2*UP)
        p1=ImageMobject("./bike.jpg",height=2).move_to(3*LEFT+DOWN/2)
        p2=ImageMobject("./magnetic.jpg",height=2).move_to(3*LEFT+DOWN/2)
        p1.height=3
        p2.height=3

        a0=Tex("Active").move_to(3*RIGHT+2*UP)
        a1=ImageMobject("./segway.jpg",height=2).move_to(3*RIGHT+DOWN/2)
        a2=ImageMobject("./qec.png",height=2).move_to(3*RIGHT+DOWN/2)
        a1.height=3
        a2.height=3
        a2.width=6

        self.play(FadeIn(p0),FadeIn(a0))
        self.slide_break()

        self.play(FadeIn(p1))
        self.slide_break()

        self.play(FadeIn(a1))
        self.slide_break()

        self.play(FadeOut(p1))
        self.play(FadeIn(p2))
        self.slide_break()

        self.play(FadeOut(a1))
        self.play(FadeIn(a2))
        self.slide_break()

        self.play(FadeOut(p0),FadeOut(p2),FadeOut(a0),FadeOut(a2))


        # ax=Axes(
        #     x_range=[0,10,10],
        #     y_range=[0,1,1],
        #     x_length=10,
        #     y_length=4,
        #     axis_config={
        #         "include_tip": True,
        #         "include_numbers": False,
        #         "numbers_to_exclude": [r for r in range(3,25) if np.mod(r,5)!=0]
        #     },
        # )
        # axis_labels=Tex("Physical error rate", "Logical error rate").scale(0.5)
        # axis_labels[0].next_to(ax,DOWN)
        # axis_labels[1].rotate(90*DEGREES).next_to(ax,LEFT)
        #
        # x=np.arange(-5,5,0.1)
        # l1 = ax.get_line_graph(
        #     x_values = x+5,
        #     y_values = 1/(1+np.exp(-x/4)),
        #     vertex_dot_radius=0,
        #     line_color="#FF0000",
        #     stroke_width = 3,
        # )
        # l2 = ax.get_line_graph(
        #     x_values = x+5,
        #     y_values = 1/(1+np.exp(-x/2)),
        #     vertex_dot_radius=0,
        #     line_color="#777700",
        #     stroke_width = 3,
        # )
        # l3 = ax.get_line_graph(
        #     x_values = x+5,
        #     y_values = 1/(1+np.exp(-x*2)),
        #     vertex_dot_radius=0,
        #     line_color="#00FF00",
        #     stroke_width = 3,
        # )
        # l4 = ax.get_line_graph(
        #     x_values = x+5,
        #     y_values = 1/(1+np.exp(-x*4)),
        #     vertex_dot_radius=0,
        #     line_color="#007777",
        #     stroke_width = 3,
        # )
        # l5 = ax.get_line_graph(
        #     x_values = x+5,
        #     y_values = 1/(1+np.exp(-x*8)),
        #     vertex_dot_radius=0,
        #     line_color="#0000FF",
        #     stroke_width = 3,
        # )
        # th=(ax.get_line_graph(
        #     x_values = [5,5],
        #     y_values = [0,1],
        #     vertex_dot_radius=0,
        #     line_color=WHITE,
        #     stroke_width = 3,
        # ))
        # self.play(FadeIn(ax),FadeIn(axis_labels))
        # self.slide_break()
        #
        # self.play(Write(l1,run_time=1))
        # self.slide_break()
        # self.play(Write(l2,run_time=2))
        # self.slide_break()
        # self.play(Write(l3,run_time=3))
        # self.slide_break()
        # self.play(Write(l4,run_time=4))
        # self.slide_break()
        # self.play(Write(l5,run_time=5))
        # self.slide_break()
        # self.play(Write(th))
        # self.slide_break()
        #
        # self.play(FadeOut(ax),FadeOut(axis_labels),FadeOut(l1),FadeOut(l2),FadeOut(l3),FadeOut(l4),FadeOut(l5),FadeOut(th))
        # self.slide_break()
        # self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))





        heading_maxprob = Tex("Which is the most likely ", "error","?")
        heading_maxprob[1].set_color(YELLOW)

        self.play(FadeIn(heading_maxprob))
        self.slide_break()

        self.play(heading_maxprob.animate.shift(2*UP))
        paulitoprob=MathTex("\\text{Error}","\\to","\\text{Probability}")
        paulitoprob[0].set_color(YELLOW)
        paulitoprob[2].set_color(RED)
        self.play(FadeIn(paulitoprob[0]))
        self.slide_break()
        self.play(TransformFromCopy(paulitoprob[0],paulitoprob[2]),FadeIn(paulitoprob[1]))
        self.slide_break()

        pauli=MathTex("{\\bigotimes}_{i}P_i").next_to(paulitoprob[1],LEFT).set_color(YELLOW)
        iid=MathTex("{\\prod}_{i}p_i(","P_i",")").next_to(paulitoprob[1],RIGHT)
        iid[0].set_color(RED)
        iid[1].set_color(YELLOW)
        iid[2].set_color(RED)
        self.play(
            Transform(paulitoprob[0],pauli),
            Transform(paulitoprob[2],iid)
        )
        self.slide_break()

        corr=MathTex("{\\prod}_{j}\phi_j(","P_{R_j}",")").next_to(paulitoprob[1],RIGHT)
        corr[0].set_color(RED)
        corr[1].set_color(YELLOW)
        corr[2].set_color(RED)
        self.play(
            Transform(paulitoprob[2],corr)
        )
        self.slide_break()

        self.play(
            Transform(paulitoprob[0],Tex("Error").set_color(YELLOW).next_to(paulitoprob[1],LEFT)),
            Transform(paulitoprob[2],Tex("Probability").set_color(RED).next_to(paulitoprob[1],RIGHT)),
        )
        self.slide_break()


        h=[0.680,0.305,0.734,0.218,0.260,0.673,0.634,0.926,0.513,0.267,0.451,
        0.571,0.347,0.721,0.241,0.352,0.387,0.213,0.950,0.704,0.494,0.582,0.860,
        0.853,0.442,0.796,0.937,0.912,0.211,0.221,0.056,0.201,0.425,0.159,0.264,
        0.961,0.270,0.398,0.438,0.840]
        H=[sum(h[0:10]),sum(h[10:20]),sum(h[20:30]),sum(h[30:40])]
        maxh=35;
        maxH=2;
        l=40;

        bar=VGroup()
        for i in range(l):
            bar+=Rectangle(width=0.25,height=2*h[i],color=YELLOW).set_fill(YELLOW,opacity=0.25).next_to([i/4-(l-1)/8,-2,0],UP).set_stroke(width=2)
        self.play(paulitoprob.animate.shift(UP),TransformFromCopy(paulitoprob[0],bar))
        self.slide_break()

        self.play(
            bar[maxh].animate.set_stroke(color=YELLOW),
            bar[maxh].animate.set_fill(YELLOW,opacity=.75)
        )
        self.slide_break()

        maxprob=MathTex("\mathop{\mathrm{arg\,max}}","_E"," \mathrm{Pr}(", "E", ")").shift(2.5*DOWN)
        maxprob[1].set_color(YELLOW)
        maxprob[2].set_color(RED)
        maxprob[3].set_color(YELLOW)
        maxprob[4].set_color(RED)

        self.play(TransformFromCopy(bar[maxh],maxprob))
        self.slide_break()

        anims=[]
        for i in range(0,10):
            anims.append(bar[i].animate.shift(0.75*LEFT))
        for i in range(10,20):
            anims.append(bar[i].animate.shift(0.25*LEFT))
        for i in range(20,30):
            anims.append(bar[i].animate.shift(0.25*RIGHT))
        for i in range(30,40):
            anims.append(bar[i].animate.shift(0.75*RIGHT))
        self.play(*anims)
        self.slide_break()

        self.play(Circumscribe(bar[0:10]))
        self.play(Circumscribe(bar[10:20]))
        self.play(Circumscribe(bar[20:30]))
        self.play(Circumscribe(bar[30:40]))
        self.slide_break()

        heading_maxlike = Tex("Which is the most likely ", "error class","?").shift(2*UP)
        heading_maxlike[1].set_color(BLUE)
        self.play(Transform(heading_maxprob,heading_maxlike))
        self.slide_break()

        classtoprob=Tex("Error class").next_to(paulitoprob[1],LEFT).set_color(BLUE).shift(RIGHT/2)
        self.play(
            Transform(paulitoprob[0],classtoprob),
            paulitoprob[1].animate.shift(RIGHT/2),
            paulitoprob[2].animate.shift(RIGHT/2)
        )
        self.slide_break()

        bar2=VGroup()
        for i in range(4):
            bar2+=Rectangle(width=2.5,height=H[i]/5,color=BLUE).set_fill(BLUE,opacity=0.25).next_to([1.25*(2*i-3),-2,0],UP).set_stroke(width=2)
        self.play(
            Transform(bar[0:10],bar2[0]),
            Transform(bar[10:20],bar2[1]),
            Transform(bar[20:30],bar2[2]),
            Transform(bar[30:40],bar2[3])
        )
        self.slide_break()

        maxlike=MathTex(
            "\mathop{\mathrm{arg\,max}}",
            "_{\overline{E}}",
            " \mathrm{Pr}(",
            "\overline{E}",
            ")").shift(2.5*DOWN)
        maxlike[1].set_color(BLUE)
        maxlike[2].set_color(RED)
        maxlike[3].set_color(BLUE)
        maxlike[4].set_color(RED)
        self.play(
            bar2[maxH].animate.set_fill(BLUE,opacity=.75),
            Transform(maxprob,maxlike)
        )
        self.slide_break()

        self.play(
            FadeOut(paulitoprob),
            FadeOut(bar),
            FadeOut(heading_maxprob),
            FadeOut(bar2),
            FadeOut(maxprob),
            maxlike.animate.shift(3.0*UP)
        )
        self.slide_break()

        mld=Tex("Maximum likelihood condition").shift(1.75*UP)
        sr=SurroundingRectangle(maxlike,color=WHITE,buff=0.25)
        self.play(FadeIn(mld),FadeIn(sr))
        self.slide_break()

        self.play(Circumscribe(maxlike[2:5],color=WHITE))
        self.slide_break()

        coset1=MathTex(
            r"\mathrm{Pr}(",
            r"\overline E",
            r")"
        )#.scale(1)
        coset1[0].set_color(RED)
        coset1[1].set_color(BLUE)
        coset1[2].set_color(RED)
        coset2=MathTex(
            r":=\sum_{",
            r"E",
            r"\in",
            r"\overline E}",
            r"\mathrm{Pr}(",
            r"E",
            r")"
        ).next_to(coset1,RIGHT)#.scale(1).next_to([-.5,-1.75,0],RIGHT)
        coset2[0].set_color(WHITE)
        coset2[1].set_color(YELLOW)
        coset2[2].set_color(WHITE)
        coset2[3].set_color(BLUE)
        coset2[4].set_color(RED)
        coset2[5].set_color(YELLOW)
        coset2[6].set_color(RED)
        coset3=MathTex(
            r"=",
            r"\sum_{S\in\mathrm{Stab}}",
            r"\mathrm{Pr}(",
            r"E",
            r"S",
            r")"
        ).next_to(coset2,RIGHT)#.scale(1).next_to([-.5,-3,0],RIGHT)
        coset3[0].set_color(WHITE)
        coset3[1].set_color(WHITE)
        coset3[2].set_color(RED)
        coset3[3].set_color(YELLOW)
        coset3[4].set_color(WHITE)
        coset3[5].set_color(RED)

        coset1.shift(0.25*UP)
        coset=VGroup(coset1,coset2,coset3).move_to(2*DOWN)

        self.play(TransformFromCopy(maxlike[2:5],coset1))
        self.slide_break()

        self.play(Write(coset2))
        self.slide_break()

        self.play(Write(coset3))
        self.slide_break()

        self.play(Circumscribe(coset3[1],color=WHITE))
        self.slide_break()

        self.play(
            FadeOut(coset),
            FadeOut(mld),
            FadeOut(sr),
            FadeOut(maxlike)
        )




        self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class SurfaceCode(SlideScene):
        def construct(self):
            tocindex=2
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            subsec1=False
            subsec2=False

            subsec1=True
            subsec2=True

            if subsec1:
                d=6
                lattice=VGroup()
                for y in range(0,2*d-1,2):
                    lattice+=Line(y*UP,(2*d-2)*RIGHT+y*UP,stroke_opacity=0.25)
                for x in range(1,2*d-2,2):
                    lattice+=Line(x*RIGHT,(2*d-2)*UP+x*RIGHT,stroke_opacity=0.25)
                lattice.set_color(WHITE)

                lefttext=VGroup(
                    Tex("Edges = Qubits"),
                    Tex("Vertices = X stab"),
                    Tex("Faces = Z stab"),
                ).scale(0.9).arrange(DOWN,buff=0.5)
                # lefttext[0].shift(0.5*UP)
                lefttext[1].set_color(BLUE)
                lefttext[2].set_color(RED)
                lefttext.move_to(5*LEFT)

                qubits=VGroup()
                for x in range(0,2*d-1):
                    for y in range(0,2*d-1):
                        if (x%2)==(y%2):
                            qubits+=Circle(radius=0.1,fill_opacity=1).move_to([x,y,0])
                qubits.set_fill(WHITE).set_color(WHITE)

                Xstab=VGroup()
                Xstab+=Circle(radius=0.15,fill_opacity=1).move_to(LEFT)
                Xstab+=Circle(radius=0.15,fill_opacity=1).move_to(RIGHT)
                Xstab+=Circle(radius=0.15,fill_opacity=1).move_to(DOWN)
                Xstab+=Circle(radius=0.15,fill_opacity=1).move_to(UP)
                Xstab+=Line(LEFT,RIGHT,stroke_width=8)
                Xstab+=Line(DOWN,UP,stroke_width=8)
                Xstab+=Tex("X").move_to(LEFT-0.6*UP).scale(1.5)
                Xstab+=Tex("X").move_to(RIGHT+0.6*UP).scale(1.5)
                Xstab+=Tex("X").move_to(UP-0.6*RIGHT).scale(1.5)
                Xstab+=Tex("X").move_to(DOWN+0.6*RIGHT).scale(1.5)
                Xstab.set_color(BLUE).move_to(3*RIGHT+4*UP)

                Zstab=VGroup()
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(LEFT)
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(RIGHT)
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(DOWN)
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(UP)
                Zstab+=Square(side_length=2,stroke_width=8).move_to(ORIGIN)
                Zstab+=Tex("Z").move_to(1.6*LEFT).scale(1.5)
                Zstab+=Tex("Z").move_to(1.6*RIGHT).scale(1.5)
                Zstab+=Tex("Z").move_to(1.6*UP).scale(1.5)
                Zstab+=Tex("Z").move_to(1.6*DOWN).scale(1.5)
                Zstab.set_color(RED).move_to(6*RIGHT+7*UP)

                righttext=VGroup(
                    Tex("\\bfseries Z errors"),
                    Tex("Logical = loops"),
                    Tex("Errors = paths"),
                    Tex("Syn. = end-points"),
                    Tex("\\bfseries X errors"),
                    Tex("Logical = co-loops"),
                    Tex("Errors = co-paths"),
                    Tex("Syn. = co-end-points"),
                ).scale(0.75).arrange(DOWN,buff=0.25)
                righttext[0:4].set_color(RED).shift(UP)
                righttext[4:8].set_color(BLUE)
                righttext.move_to(5*RIGHT)

                Zlog=VGroup()
                Zlog+=Line(2*UP,2*UP+(2*d-2)*RIGHT,stroke_width=8)
                for x in range(0,2*d-1,2):
                    Zlog+=Circle(radius=0.15,fill_opacity=1).move_to(x*RIGHT+2*UP)
                Zlog.set_color(RED)

                Xlog=VGroup()
                Xlog+=Line(2*RIGHT,2*RIGHT+(2*d-2)*UP,stroke_width=8)
                for x in range(0,2*d-1,2):
                    Xlog+=Circle(radius=0.15,fill_opacity=1).move_to(x*UP+2*RIGHT)
                Xlog.set_color(BLUE)

                Zerr=VGroup()
                Zerr+=Line([5,6,0],[5,10,0],stroke_width=8)
                Zerr+=Line([5,10,0],[7,10,0],stroke_width=8)
                Zerr+=Circle(radius=0.15,fill_opacity=1).move_to([5,7,0])
                Zerr+=Circle(radius=0.15,fill_opacity=1).move_to([5,9,0])
                Zerr+=Circle(radius=0.15,fill_opacity=1).move_to([6,10,0])
                Zerr.set_color(RED)
                Zerr+=Circle(radius=0.25,color=YELLOW).move_to([5,6,0])
                Zerr+=Circle(radius=0.25,color=YELLOW).move_to([7,10,0])


                Xerr=VGroup()
                Xerr+=Line([4,3,0],[6,3,0],stroke_width=8)
                Xerr+=Line([6,3,0],[6,7,0],stroke_width=8)
                Xerr+=Line([6,7,0],[8,7,0],stroke_width=8)
                Xerr+=Circle(radius=0.15,fill_opacity=1).move_to([5,3,0])
                Xerr+=Circle(radius=0.15,fill_opacity=1).move_to([6,4,0])
                Xerr+=Circle(radius=0.15,fill_opacity=1).move_to([6,6,0])
                Xerr+=Circle(radius=0.15,fill_opacity=1).move_to([7,7,0])
                Xerr.set_color(BLUE)
                Xerr+=Circle(radius=0.25,color=YELLOW).move_to([4,3,0])
                Xerr+=Circle(radius=0.25,color=YELLOW).move_to([8,7,0])

                VGroup(lattice,qubits,Xstab,Zstab,Zlog,Xlog,Zerr,Xerr).scale(0.5).move_to(ORIGIN)



                self.play(*[Write(l) for l in lattice])
                self.slide_break()

                self.play(Write(lefttext[0]))
                self.play(*[Write(t) for t in qubits])
                self.slide_break()

                self.play(Write(lefttext[1]))
                self.play(*[Write(t) for t in Xstab])
                self.slide_break()

                self.play(Write(lefttext[2]))
                self.play(*[Write(t) for t in Zstab])
                self.slide_break()

                self.play(FadeOut(Xstab),FadeOut(Zstab))
                self.slide_break()

                self.play(Write(righttext[0]))
                self.slide_break()
                self.play(Write(righttext[1]))
                self.play(Write(Zlog))
                self.slide_break()
                self.play(Write(righttext[2]))
                self.play(Write(Zerr[0:-2]))
                self.slide_break()
                self.play(Write(righttext[3]))
                self.play(Flash(Zerr[-2]),Flash(Zerr[-1]))
                self.play(FadeIn(Zerr[-2]),FadeIn(Zerr[-1]),run_time=0.25)
                self.slide_break()

                # self.play(Write(righttext[4]))
                # self.slide_break()
                # self.play(Write(righttext[5]))
                # self.play(Write(Xlog))
                # self.slide_break()
                # self.play(Write(righttext[6]))
                # self.play(Write(Xerr[0:-2]))
                # self.slide_break()
                # self.play(Write(righttext[7]))
                # self.play(Flash(Xerr[-2],color=RED),Flash(Xerr[-1],color=RED))
                # self.play(FadeIn(Xerr[-2]),FadeIn(Xerr[-1]),run_time=0.25)
                # self.slide_break()

                self.play(Write(righttext[4]))
                self.play(Write(righttext[5]),Write(Xlog))
                self.play(Write(righttext[6:]),Write(Xerr))
                self.slide_break()

                self.play(FadeOut(lefttext),FadeOut(righttext))
                self.play(FadeOut(Zlog),FadeOut(Xlog),FadeOut(Zerr),FadeOut(Xerr))
                self.play(FadeOut(qubits),FadeOut(lattice))
                self.slide_break()

            if subsec2:
                X=16
                Y=11
                lattice=VGroup()
                for y in range(0,Y+1):
                    lattice+=Line([-0.5,y,0],[X+0.5,y,0])
                for x in range(0,X+1):
                    lattice+=Line([x,0,0],[x,Y,0])
                lattice.set_color(WHITE).set_opacity(0.25)

                E=VGroup()
                # E+=Line([3,5,0],[4,5,0])
                # E+=Line([4,5,0],[5,5,0])
                # E+=Line([5,5,0],[5,4,0])
                # E+=Line([5,4,0],[4,4,0])
                #
                # E+=Line([7,6,0],[8,6,0])
                # E+=Line([8,6,0],[8,7,0])
                # E+=Line([8,7,0],[8,8,0])
                #
                # E+=Line([9,3,0],[10,3,0])
                # E+=Line([10,3,0],[10,2,0])
                E+=Line([3,5,0],[4,5,0])
                E+=Line([4,5,0],[5,5,0])
                E+=Line([5,4,0],[4,4,0])
                E+=Line([8,6,0],[8,7,0])
                E+=Line([8,7,0],[8,8,0])
                E+=Line([10,3,0],[10,2,0])
                E+=Line([7,6,0],[8,6,0])
                E+=Line([9,3,0],[10,3,0])
                E+=Line([5,5,0],[5,4,0])
                E.set_stroke(width=8).set_color(RED)

                S=VGroup()
                S+=Circle(radius=0.2).move_to([3,5,0])
                S+=Circle(radius=0.2).move_to([4,4,0])
                S+=Circle(radius=0.2).move_to([7,6,0])
                S+=Circle(radius=0.2).move_to([8,8,0])
                S+=Circle(radius=0.2).move_to([9,3,0])
                S+=Circle(radius=0.2).move_to([10,2,0])
                S.set_color(YELLOW)

                C=VGroup()
                C+=Line([3,5,0],[3,4,0])
                C+=Line([3,4,0],[4,4,0])
                C+=Line([7,6,0],[7,8,0])
                C+=Line([7,8,0],[8,8,0])
                C+=Line([9,3,0],[9,2,0])
                C+=Line([9,2,0],[10,2,0])
                C.set_color(BLUE).set_stroke(width=8)

                cl=5*RIGHT+2*UP
                cr=11*RIGHT+9*UP
                S2=VGroup()
                S2+=Circle(radius=0.2).move_to(cl)
                S2+=Circle(radius=0.2).move_to(cr)
                S2.set_color(YELLOW)
                Eout=VGroup(Line(cl,UP*cl[1]+0.5*LEFT),Line(cr,UP*cr[1]+(X+0.5)*RIGHT))
                Eout.set_color(BLUE).set_stroke(width=8)

                Ein=VGroup()
                Ein+=VGroup(
                    Line([5,2,0],[11,2,0]),
                    Line([11,2,0],[11,9,0]))
                Ein+=VGroup(
                    Line([5,2,0],[5,9,0]),
                    Line([5,9,0],[11,9,0]))
                Ein+=VGroup(
                    Line([5,2,0],[5,4,0]),
                    Line([5,4,0],[11,4,0]),
                    Line([11,4,0],[11,9,0]))
                Ein+=VGroup(
                    Line([5,2,0],[6,2,0]),
                    Line([6,2,0],[6,6,0]),
                    Line([6,6,0],[10,6,0]),
                    Line([10,6,0],[10,9,0]),
                    Line([10,9,0],[11,9,0]),)
                Ein.set_color(RED).set_stroke(width=8)

                flow=VGroup()
                for t in range(0,13):
                    flow+=VGroup()
                for x in range(5,12):
                    for y in range(2,10):
                        if x<cr[0]:
                            flow[x+y-7]+=Line([x,y,0],[x+1,y,0])
                        if y<cr[1]:
                            flow[x+y-7]+=Line([x,y,0],[x,y+1,0])
                flow.set_color(RED).set_stroke(width=8)


                VGroup(lattice,E,S,C,S2,Eout,Ein,flow).scale(0.5).move_to(ORIGIN)
                # self.add(lattice2)




                self.play(FadeIn(lattice))
                for e in E:
                    self.play(FadeIn(e))
                self.slide_break()
                self.play(Write(S))
                self.slide_break()
                self.play(FadeOut(E))
                self.slide_break()

                self.play(Write(C[0:2]))
                self.play(Write(C[2:4]))
                self.play(Write(C[4:6]))
                self.slide_break()

                self.play(FadeIn(E))
                self.slide_break()

                self.play(FadeOut(E),FadeOut(S),FadeOut(C))
                self.slide_break()

                self.play(Write(S2))
                self.slide_break()

                self.play(Write(Eout))
                self.slide_break()

                self.play(Write(Ein[0]))
                self.slide_break()
                self.play(FadeOut(Ein[0]))
                self.play(Write(Ein[1]))
                self.slide_break()
                self.play(FadeOut(Ein[1]))
                self.play(Write(Ein[2]))
                self.slide_break()
                self.play(FadeOut(Ein[2]))
                self.play(Write(Ein[3]))
                self.slide_break()
                self.play(FadeOut(Ein[3]))
                self.slide_break()

                # for f in flow:
                #     self.play(Write(f),run_time=0.25)
                # self.slide_break()
                # self.play(FadeOut(flow))

                for f in flow:
                    self.play(*[Write(ff) for ff in f],run_time=0.25)
                    self.wait(0.25)
                self.slide_break()

                in_n_out=VGroup(lattice,S2,Eout,flow)
                self.play(in_n_out.animate.shift(3.5*LEFT).scale(.75))

                # odds=MathTex("\\textrm{In:Out} = \\frac{","\\Pr(\\overline{\textrm{In}})","}{","\\Pr(\\overline{\\textrm{Out}})","}")
                odds=MathTex(r"\textrm{In:Out} ","= {",r"{\Pr(\textrm{In})}",r"\over",r"{\Pr(\textrm{Out})}",r"}")
                # odds=MathTex("\\textrm{In:Out} = \\frac{","\\Pr(\\textrm{In})","}{","\\Pr(\\textrm{Out})","}")
                odds.move_to(3.5*RIGHT+2*UP)
                odds[0].set_color(YELLOW)
                odds[2].set_color(RED)
                odds[4].set_color(BLUE)
                self.play(Write(odds[0]))
                self.slide_break()
                self.play(Write(odds[1]),Write(odds[3]))
                self.slide_break()
                self.play(Write(odds[2]),Indicate(flow,scale_factor=1.05))
                self.slide_break()
                self.play(Write(odds[4]),Indicate(Eout,scale_factor=1))
                self.slide_break()

                # diagonal=SVGMobject("diagonal.svg").scale(2).move_to(4*RIGHT+DOWN)
                diagonal=ImageMobject("diagonal.png").scale(1.2).move_to(3.5*RIGHT+DOWN)

                self.play(FadeIn(diagonal,shift=UP))
                self.slide_break()

                self.play(
                    FadeOut(diagonal),
                    FadeOut(lattice),
                    FadeOut(Eout),
                    FadeOut(flow),
                    FadeOut(odds),
                    FadeOut(S2))
                self.slide_break()

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class StatMech(SlideScene):
        def construct(self):
            tocindex=3
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            comm_temp = TexTemplate()
            comm_temp.add_to_preamble(r"\usepackage{stmaryrd,mathtools}")
            comm_temp.add_to_preamble(r"\newcommand{\comm}[2]{\left\llbracket#1,#2\right\rrbracket}")


            subsec1=False
            subsec2=False
            subsec3=False
            subsec4=False
            subsec5=False
            subsec6=False

            subsec1=True
            subsec2=True
            subsec3=True
            subsec4=True
            subsec5=True
            subsec6=True

            if subsec1:
                toric_code=VGroup()
                for x in range(-1,2):
                    toric_code+=Line(RIGHT*x+1.75*DOWN,RIGHT*x+1.75*UP).set_color(WHITE).set_opacity(0.25)
                    toric_code+=Line(UP*x+1.75*LEFT,UP*x+1.75*RIGHT).set_color(WHITE).set_opacity(0.25)
                for x in range(-1,2):
                    for y in range(-1,2):
                        toric_code+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x-0.5,y,0])
                        toric_code+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x+0.5,y,0])
                        toric_code+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y-0.5,0])
                        toric_code+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y+0.5,0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=RED).move_to([-0.5,0.0,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=RED).move_to([-0.5,-1.0,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=RED).move_to([-1.0,-0.5,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=RED).move_to([0.0,-0.5,0.0])
                toric_code+=Line(ORIGIN,LEFT,stroke_width=8,color=RED)
                toric_code+=Line(ORIGIN,DOWN,stroke_width=8,color=RED)
                toric_code+=Line(DOWN+LEFT,LEFT,stroke_width=8,color=RED)
                toric_code+=Line(DOWN+LEFT,DOWN,stroke_width=8,color=RED)
                toric_code+=Tex("$Z$",color=RED).move_to([-0.5,-0.25,0]).scale(.5)
                toric_code+=Tex("$Z$",color=RED).move_to([-0.5,-1+0.25,0]).scale(.5)
                toric_code+=Tex("$Z$",color=RED).move_to([-1+0.2,-0.5,0]).scale(.5)
                toric_code+=Tex("$Z$",color=RED).move_to([-0.2,-0.5,0]).scale(.5)
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.0,0.5,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.0,1.5,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([0.5,1.0,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.5,1.0,0.0])
                toric_code+=Line(UP+RIGHT/2,UP+3*RIGHT/2,stroke_width=8,color=BLUE)
                toric_code+=Line(RIGHT+UP/2,RIGHT+3*UP/2,stroke_width=8,color=BLUE)
                toric_code+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[+0.5,+0.25,0]).scale(.5)
                toric_code+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[-0.5,-0.25,0]).scale(.5)
                toric_code+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[-0.2,+0.5,0]).scale(.5)
                toric_code+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[+0.2,-0.5,0]).scale(.5)
                toric_code+=Tex("Toric code").move_to(2.5*DOWN).scale(0.75)

                ev_model=VGroup()
                for x in range(-1,2):
                    ev_model+=Line(RIGHT*x+1.75*DOWN,RIGHT*x+1.75*UP).set_color(WHITE).set_opacity(0.25)
                    ev_model+=Line(UP*x+1.75*LEFT,UP*x+1.75*RIGHT).set_color(WHITE).set_opacity(0.25)
                for x in range(-1,2):
                    for y in range(-1,2):
                        ev_model+=Circle(radius=0.05,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([x,y,0])
                        ev_model+=Circle(radius=0.05,stroke_opacity=0.75,color=BLUE).move_to([x,y,0])
                for x in range(-1,3):
                    for y in range(-1,3):
                        ev_model+=Circle(radius=0.05,stroke_opacity=0.5,color=RED).move_to([x-0.5,y-0.5,0])
                ev_model+=Line(UP,UP+LEFT,stroke_width=8,color=BLUE)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(UP)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(UP+LEFT)
                ev_model+=Circle(radius=0.075,color=BLUE,stroke_width=8).move_to(UP)
                ev_model+=Circle(radius=0.075,color=BLUE,stroke_width=8).move_to(LEFT+UP)
                ev_model+=Tex("$J_Z$",color=BLUE).scale(.5).move_to([-0.5,1.2,0.0])
                #
                ev_model+=Line([-0.5,-0.5,0.0],[-0.5,-1.5,0.0],stroke_width=8,color=RED)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([-0.5,-0.5,0.0])
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([-0.5,-1.5,0.0])
                ev_model+=Circle(radius=0.075,color=RED,stroke_width=8).move_to([-0.5,-0.5,0.0])
                ev_model+=Circle(radius=0.075,color=RED,stroke_width=8).move_to([-0.5,-1.5,0.0])
                ev_model+=Tex("$J_X$",color=RED).scale(.5).move_to([-0.25,-.8,0.0])
                #
                ev_model+=Line(ORIGIN,RIGHT,stroke_width=8,color=PINK)
                ev_model+=Line(RIGHT/2+DOWN/2,RIGHT/2+UP/2,stroke_width=8,color=PINK)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(ORIGIN)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(RIGHT)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(RIGHT/2+UP/2)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(RIGHT/2+DOWN/2)
                ev_model+=Circle(radius=0.075,color=PINK,stroke_width=8).move_to(ORIGIN)
                ev_model+=Circle(radius=0.075,color=PINK,stroke_width=8).move_to(RIGHT)
                ev_model+=Circle(radius=0.075,color=PINK,stroke_width=8).move_to(RIGHT/2+UP/2)
                ev_model+=Circle(radius=0.075,color=PINK,stroke_width=8).move_to(RIGHT/2+DOWN/2)
                ev_model+=Tex("$J_Y$",color=PINK).scale(.5).move_to([0.7,0.2,0.0])
                #
                ev_model+=Tex("Eight-vertex model").move_to(2.5*DOWN).scale(0.75)

                toric_code.scale(1.25).move_to(ORIGIN)
                ev_model.scale(1.25).move_to(3.5*RIGHT)
                arrow=Tex("$\\rightarrow$")

                self.play(FadeIn(toric_code))
                self.slide_break()

                self.play(toric_code.animate.shift(3.5*LEFT))
                self.slide_break()

                self.play(TransformFromCopy(toric_code[0:6],ev_model[0:6]),FadeIn(arrow))
                self.play(TransformFromCopy(toric_code[6:34],ev_model[6:40]))
                self.play(FadeIn(ev_model[40:]))
                self.slide_break()

                eq=VGroup(Tex(r"$\Pr(\overline{E}):=\sum_{S\in\mathcal S}\Pr(ES)$"),Tex(r"$Z_E=\sum_{\vec s}e^{-\beta H_E(\vec s)}$"))
                eq[0].move_to(toric_code)
                eq[1].move_to(ev_model)

                self.play(FadeOut(toric_code,shift=5*LEFT))
                self.play(FadeIn(eq[0],shift=5*RIGHT))
                self.slide_break()
                self.play(FadeOut(ev_model,shift=5*RIGHT))
                self.play(FadeIn(eq[1],shift=5*LEFT))
                self.slide_break()

                self.play(FadeOut(eq),FadeOut(arrow))
                self.slide_break()

            if subsec2:
                gloss_l=VGroup()
                gloss_l+=Tex("Pauli code + Pauli noise")
                gloss_l+=Tex("Threshold")
                gloss_l+=Tex("Error class probabilties")
                gloss_l+=Tex("Decoding")
                gloss_l+=Tex("Stabilisers")
                gloss_l+=Tex("Pauli errors")

                gloss_r=VGroup()
                gloss_r+=Tex("Disordered stat mech model")
                gloss_r+=Tex("Phase transition")
                gloss_r+=Tex("Partition functions")
                gloss_r+=Tex("Approx.\\ part.\\ functions")
                gloss_r+=Tex("Classic spins")
                gloss_r+=Tex("Disordered couplings")

                gloss_m=VGroup(Tex("$\\rightarrow$"),Tex("$\\rightarrow$"),Tex("$\\rightarrow$"),Tex("$\\rightarrow$"),Tex("$\\rightarrow$"),Tex("$\\rightarrow$"),Tex("$\\rightarrow$"))

                gloss_l[0].move_to(ORIGIN)
                self.play(FadeIn(gloss_l[0]))
                self.slide_break()

                self.play(gloss_l[0].animate.shift(3.75*LEFT))
                gloss_l[1:].move_to(3.75*LEFT)
                gloss_m.move_to(0.25*LEFT)
                gloss_r.move_to(3.5*RIGHT)
                self.play(TransformFromCopy(gloss_l[0],gloss_r[0]),FadeIn(gloss_m[0]))
                self.slide_break()

                self.play(VGroup(gloss_l[0],gloss_m[0],gloss_r[0]).animate.shift(1.5*UP))
                self.slide_break()

                for i in range(1,4):
                    VGroup(gloss_l[i],gloss_m[i],gloss_r[i]).shift((1.-i)*UP)
                    self.play(FadeIn(gloss_l[i]))
                    self.slide_break()
                    self.play(TransformFromCopy(gloss_l[i],gloss_r[i]),FadeIn(gloss_m[i]))
                    self.slide_break()

                self.play(FadeOut(gloss_l[1:4]),FadeOut(gloss_m[1:4]),FadeOut(gloss_r[1:4]))
                self.slide_break()

                VGroup(gloss_l[4],gloss_m[4],gloss_r[4]).shift(0.5*DOWN)
                VGroup(gloss_l[5],gloss_m[5],gloss_r[5]).shift(1.5*DOWN)

                for i in range(4,6):
                    self.play(FadeIn(gloss_l[i]))
                    self.slide_break()
                    self.play(TransformFromCopy(gloss_l[i],gloss_r[i]),FadeIn(gloss_m[i]))
                    self.slide_break()

                self.play(
                    FadeOut(gloss_l[0]),
                    FadeOut(gloss_m[0]),
                    FadeOut(gloss_r[0]),
                    FadeOut(gloss_l[4:6]),
                    FadeOut(gloss_m[4:6]),
                    FadeOut(gloss_r[4:6])
                )
                self.slide_break()

            if subsec3:
                comm_temp = TexTemplate()
                comm_temp.add_to_preamble(r"\usepackage{stmaryrd,mathtools}")
                comm_temp.add_to_preamble(r"\newcommand{\comm}[2]{\left\llbracket#1,#2\right\rrbracket}")
                # comm_temp.add_to_preamble(r"\usepackage{mathbbol}")

                comm=Tex(r"\comm{A}{B}:=\begin{dcases} +1 &:A,B\textrm{ commute},\\-1&:\textrm{otherwise}.\end{dcases}",tex_environment="align*",tex_template=comm_temp)
                comm2=Tex(r"AB=\comm{A}{B}BA",tex_environment="align*",tex_template=comm_temp)
                self.play(FadeIn(comm))
                self.slide_break()
                self.play(Transform(comm,comm2))
                self.slide_break()
                self.play(FadeOut(comm))
                self.slide_break()

            if subsec4:
                ham = Tex(
                    r"H_{", #0
                    r"E", #1
                    r"}(", #2
                    r"\vec s", #3
                    r")", #4
                    r":=-", #5
                    r"\sum_{i}\sum_{\sigma\in\mathcal P_i}", #6
                    r"J_i(\sigma)", #7
                    r"\comm{\sigma}{E}", #8
                    r"\prod_{ {{k:\comm{\sigma}{S_k}=-1}} } s_k", #9,10,11
                    tex_environment="align*",tex_template=comm_temp
                )
                self.play(Write(ham))
                self.slide_break()

                braces=VGroup()

                x=.625
                self.play(
                    ham[0:5].animate.shift(x*LEFT),
                    ham[5].animate.shift(x*3*LEFT/5),
                    ham[6].animate.shift(x*1*LEFT/5),
                    ham[7].animate.shift(x*1*RIGHT/5),
                    ham[8].animate.shift(x*3*RIGHT/5),
                    ham[9:].animate.shift(x*RIGHT),
                )
                self.slide_break()

                # m=ham[0:5]; d=UP; c=RED; t=r"{\textrm{Disordered}}\atop{\textrm{Hamiltonian}}"
                # braces+=Brace(mobject=m,direction=d)
                # braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                # braces[-2:-1].set_color(c)
                # self.play(m.animate.set_color(c),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                # self.slide_break()
                #
                # m=ham[6]; d=DOWN; c=YELLOW; t=r"{\textrm{Sum over}}\atop{\textrm{1 qubit Paulis}}"
                # braces+=Brace(mobject=m,direction=d)
                # braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                # braces[-2:-1].set_color(c)
                # self.play(m.animate.set_color(c),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                # self.slide_break()
                #
                # m=ham[7]; d=UP; c=GREEN; t=r"{\textrm{Coupling}}\atop{\textrm{strength}}"
                # braces+=Brace(mobject=m,direction=d)
                # braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                # braces[-2:-1].set_color(c)
                # self.play(m.animate.set_color(c),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                # self.slide_break()
                #
                # m=ham[8]; d=DOWN; c=BLUE; t=r"\textrm{Disorder}"
                # braces+=Brace(mobject=m,direction=d)
                # braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                # braces[-2:-1].set_color(c)
                # self.play(m.animate.set_color(c),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                # self.slide_break()
                #
                # m=ham[9]; d=UP; c=PURPLE; t=r"{\textrm{Degrees of}}\atop{\textrm{freedom}}"
                # braces+=Brace(mobject=m,direction=d)
                # braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                # braces[-2:-1].set_color(c)
                # self.play(m.animate.set_color(c),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                # self.slide_break()

                m=ham[0:5]; d=UP; c=YELLOW; t=r"{\textrm{Disordered}}\atop{\textrm{Hamiltonian}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.slide_break()


                m=ham[6]; d=DOWN; c=YELLOW; t=r"{\textrm{Sum over}}\atop{\textrm{1 qubit Paulis}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.slide_break()

                m=ham[7]; d=UP; c=YELLOW; t=r"{\textrm{Coupling}}\atop{\textrm{strength}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.slide_break()

                m=ham[8]; d=DOWN; c=YELLOW; t=r"\textrm{Disorder}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.slide_break()

                m=ham[9:]; d=UP; c=YELLOW; t=r"{\textrm{Degrees of}}\atop{\textrm{freedom}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.slide_break()

                x=-.625
                self.play(
                    ham[0:5].animate.shift(x*LEFT),
                    ham[5].animate.shift(x*3*LEFT/5),
                    ham[6].animate.shift(x*1*LEFT/5),
                    ham[7].animate.shift(x*1*RIGHT/5),
                    ham[8].animate.shift(x*3*RIGHT/5),
                    ham[9:].animate.shift(x*RIGHT),
                    braces[0:2].animate.shift(x*LEFT),
                    braces[2:4].animate.shift(x*1*LEFT/5),
                    braces[4:6].animate.shift(x*1*RIGHT/5),
                    braces[6:8].animate.shift(x*3*RIGHT/5),
                    braces[8:10].animate.shift(x*RIGHT),
                )
                self.slide_break()

                self.play(FadeOut(braces))
                self.slide_break()

                self.play(ham.animate.shift(1.5*UP))
                self.slide_break()

                points=VGroup(
                    Tex(r"\textbullet",r" Ising-type (sum of product of spins)"),
                    Tex(r"\textbullet",r" Disorder flips terms (ferro v.\ anti-ferro)"),
                    Tex(r"\textbullet",r" Local code $\Rightarrow$ local stat mech model"),
                ).arrange(DOWN,aligned_edge=LEFT).move_to(DOWN)

                self.play(FadeIn(points[0][0]),FadeIn(points[1][0]),FadeIn(points[2][0]))
                self.slide_break()

                VGroup(points[0][1],points[1][1],points[2][1]).set_color(YELLOW)

                self.play(Write(points[0][1]),ham[6].animate.set_color(YELLOW).scale(1.2),ham[9:].animate.set_color(YELLOW).scale(1.2))
                self.slide_break()
                self.play(points[0][1].animate.set_color(WHITE),ham[6].animate.set_color(WHITE).scale(1/1.2),ham[9:].animate.set_color(WHITE).scale(1/1.2))
                self.slide_break()

                self.play(Write(points[1][1]),ham[8].animate.set_color(YELLOW).scale(1.2))
                self.slide_break()
                self.play(points[1][1].animate.set_color(WHITE),ham[8].animate.set_color(WHITE).scale(1/1.2))
                self.slide_break()

                self.play(Write(points[2][1]),ham[10].animate.set_color(YELLOW).scale(1.2))
                self.slide_break()
                self.play(points[2][1].animate.set_color(WHITE),ham[10].animate.set_color(WHITE).scale(1/1.2))
                self.slide_break()

                self.play(FadeOut(points))
                self.play(ham.animate.shift(DOWN*1.5))
                self.slide_break()



                # hams = VGroup()
                #     #1 4 new
                #
                #
                #
                # hams+=Tex(
                #     r"H_{E",r"S_l",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)",r"\comm{\sigma}{E}",r"\comm{\sigma}{S_l}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                #     tex_environment="align*",tex_template=comm_temp)
                #
                # hams+=Tex(
                #     r"H_{E",r"S_l",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)",r"\comm{\sigma}{E}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k ",r"\comm{\sigma}{S_l}",
                #     tex_environment="align*",tex_template=comm_temp)
                #
                # hams+=Tex(
                #     r"H_{E",r"S_l",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)",r"\comm{\sigma}{E}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k ",r"(-1)^{\delta_{k,l}}",
                #     tex_environment="align*",tex_template=comm_temp)


                gauge=Tex(r"How do stabilisers act on this?").move_to(1.5*UP)
                self.play(FadeIn(gauge))
                self.slide_break()

                oldham=Tex(
                    r"H_{E",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"\rrbracket\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*",tex_template=comm_temp)
                oldham.move_to(ham)
                self.remove(*ham)
                self.add(oldham)
                ham=Tex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"S_l",r"\rrbracket\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*",tex_template=comm_temp)
                ham[1].set_color(YELLOW)
                ham[3].set_color(YELLOW)
                ham.move_to(oldham)
                self.play(
                    ReplacementTransform(oldham[0],ham[0]),
                    ReplacementTransform(oldham[1],ham[2]),
                    ReplacementTransform(oldham[2],ham[4]),
                )
                self.play(
                    FadeIn(ham[1]),
                    FadeIn(ham[3]),
                )
                self.slide_break()

                oldham=Tex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"S_l",r"\rrbracket",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*",tex_template=comm_temp)
                oldham[1].set_color(YELLOW)
                oldham[3].set_color(YELLOW)
                oldham.move_to(ham)
                self.remove(*ham)
                self.add(oldham)
                ham=Tex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"\rrbracket",r"\comm{\sigma}{S_l}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*",tex_template=comm_temp)
                ham[1].set_color(YELLOW)
                ham[4].set_color(YELLOW)
                ham.move_to(oldham)
                self.play(
                    ReplacementTransform(oldham[0],ham[0]),
                    ReplacementTransform(oldham[1],ham[1]),
                    ReplacementTransform(oldham[2],ham[2]),
                    ReplacementTransform(oldham[3],ham[3]),
                    ReplacementTransform(oldham[4],ham[4]),
                    ReplacementTransform(oldham[5],ham[5]),
                )
                self.slide_break()

                oldham=Tex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E\rrbracket",r"\comm{\sigma}{S_l}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*",tex_template=comm_temp)
                oldham[1].set_color(YELLOW)
                oldham[3].set_color(YELLOW)
                oldham.move_to(oldham)
                self.remove(*ham)
                self.add(oldham)
                ham=Tex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E\rrbracket",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",r"(-1)^{\delta_{k,l}}",
                    tex_environment="align*",tex_template=comm_temp)
                ham[1].set_color(YELLOW)
                ham[4].set_color(YELLOW)
                ham.move_to(oldham)
                self.play(
                    ReplacementTransform(oldham[0],ham[0]),
                    ReplacementTransform(oldham[1],ham[1]),
                    ReplacementTransform(oldham[2],ham[2]),
                    ReplacementTransform(oldham[3],ham[4]),
                    ReplacementTransform(oldham[4],ham[3]),
                )
                self.slide_break()

                oldham=Tex(
                    r"H_{E",r"S_l}",r"(\vec s)",r":=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E\rrbracket",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",r"(-1)^{\delta_{k,l}}",
                    tex_environment="align*",tex_template=comm_temp)
                oldham[1].set_color(YELLOW)
                oldham[5].set_color(YELLOW)
                oldham.move_to(oldham)
                self.remove(*ham)
                self.add(oldham)
                ham=Tex(
                    r"H_{E",r"S_l}",r"(\vec s)",r"=H_{E}(\vec{s}\oplus",r"\vec{e_l}",r")",
                    tex_environment="align*",tex_template=comm_temp)
                ham[1].set_color(YELLOW)
                ham[4].set_color(YELLOW)
                ham.move_to(oldham)
                self.play(
                    ReplacementTransform(oldham[0],ham[0]),
                    ReplacementTransform(oldham[1],ham[1]),
                    ReplacementTransform(oldham[2],ham[2]),
                    FadeOut(oldham[3:])
                )
                self.play(
                    FadeIn(ham[3:])
                )
                self.slide_break()



                gauge2=Tex(r"Applying stabiler = Flipping spin").move_to(1.5*DOWN)
                self.play(FadeIn(gauge2))
                self.slide_break()

                gauge3=Tex(r"Z_E=Z_{E {{S}} }",tex_environment="align*").move_to(1.5*DOWN)
                gauge3[1].set_color(YELLOW)
                self.play(FadeOut(gauge2))
                self.play(FadeIn(gauge3))
                self.slide_break()

                self.play(Circumscribe(gauge3))
                self.slide_break()

                self.play(FadeOut(gauge),FadeOut(gauge3),FadeOut(ham))
                self.slide_break()

            if subsec5:
                tc_lattice=VGroup()
                for x in range(-1,2):
                    tc_lattice+=Line(RIGHT*x+1.75*DOWN,RIGHT*x+1.75*UP).set_color(WHITE).set_opacity(0.25)
                    tc_lattice+=Line(UP*x+1.75*LEFT,UP*x+1.75*RIGHT).set_color(WHITE).set_opacity(0.25)

                tc_qubits=VGroup()
                for x in range(-1,2):
                    for y in range(-1,2):
                        tc_qubits+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x-0.5,y,0])
                        tc_qubits+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x+0.5,y,0])
                        tc_qubits+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y-0.5,0])
                        tc_qubits+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y+0.5,0])

                tc_stab=VGroup()
                tc_stab+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.0,0.5,0.0])
                tc_stab+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.0,1.5,0.0])
                tc_stab+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([0.5,1.0,0.0])
                tc_stab+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.5,1.0,0.0])
                tc_stab+=Line(UP+RIGHT/2,UP+3*RIGHT/2,stroke_width=8,color=BLUE)
                tc_stab+=Line(RIGHT+UP/2,RIGHT+3*UP/2,stroke_width=8,color=BLUE)
                tc_stab+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[+0.5,+0.25,0]).scale(.5)
                tc_stab+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[-0.5,-0.25,0]).scale(.5)
                tc_stab+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[-0.2,+0.5,0]).scale(.5)
                tc_stab+=Tex("$X$",color=BLUE).move_to(UP+RIGHT+[+0.2,-0.5,0]).scale(.5)

                tc_1qb=VGroup()
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([-0.5,1.0,0.0])
                tc_1qb+=Tex("$I$",color=YELLOW).move_to([-0.5,1.2,0]).scale(.5)
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([0.5,1,0.0])
                tc_1qb+=Tex("$X$",color=YELLOW).move_to([0.5,1.2,0]).scale(.5)
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([-0.5,0,0.0])
                tc_1qb+=Tex("$Y$",color=YELLOW).move_to([-0.5,0.2,0]).scale(.5)
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([1.0,-0.5,0.0])
                tc_1qb+=Tex("$Z$",color=YELLOW).move_to([0.8,-0.5,0]).scale(.5)


                # Other things
                RBIM_spins=VGroup()
                for x in range(-1,2):
                    for y in range(-1,2):
                        RBIM_spins+=Circle(radius=0.05,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([x,y,0])
                        RBIM_spins+=Circle(radius=0.05,stroke_opacity=0.75,color=BLUE).move_to([x,y,0])



                RBIM_bonds=VGroup()
                RBIM_bonds+=Line(LEFT,ORIGIN,stroke_width=8,color=BLUE)
                RBIM_bonds+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([-1,0,0])
                RBIM_bonds+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([0,0,0])
                RBIM_bonds+=Circle(radius=0.075,color=BLUE,stroke_width=8).move_to([-1,0,0])
                RBIM_bonds+=Circle(radius=0.075,color=BLUE,stroke_width=8).move_to([0,0,0])
                RBIM_bonds+=Line(RIGHT,RIGHT+DOWN,stroke_width=8,color=BLUE)
                RBIM_bonds+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(RIGHT)
                RBIM_bonds+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to(RIGHT+DOWN)
                RBIM_bonds+=Circle(radius=0.075,color=BLUE,stroke_width=8).move_to(RIGHT)
                RBIM_bonds+=Circle(radius=0.075,color=BLUE,stroke_width=8).move_to(RIGHT+DOWN)

                toric_code=VGroup(tc_lattice,tc_qubits,tc_stab,tc_1qb)
                RBIM=VGroup(RBIM_spins,RBIM_bonds)
                VGroup(toric_code,RBIM).move_to(3*RIGHT).scale(1.25)

                steps=VGroup(
                    Tex("0: Code + noise"),
                    Tex("1: DoF on each stabiliser"),
                    Tex("2: Interactions from 1-qubit Paulis"),
                    Tex(r"$H_{I}=-\sum_{v\sim v'}J\,s_{v}s_{v'}$"),
                    Tex("3: Disorder"),
                    Tex(r"$H_{E}=-\sum_{v\sim v'}Je_{vv'}\,s_{v}s_{v'}$"),
                ).arrange(DOWN,aligned_edge=LEFT,buff=0.5).move_to(2.5*LEFT)
                steps[3].set_x(-2.5).set_color(BLUE)
                steps[5].set_x(-2.5).set_color(BLUE)
                steps.scale(.75)

                self.play(FadeIn(steps[0]))
                self.slide_break()

                self.play(FadeIn(tc_lattice))
                self.play(FadeIn(tc_qubits))
                self.slide_break()

                self.play(FadeIn(tc_stab))
                self.slide_break()

                self.play(FadeIn(steps[1]))
                self.slide_break()
                self.play(FadeOut(tc_stab),FadeIn(RBIM_spins))
                self.slide_break()


                self.play(FadeIn(steps[2]))
                self.slide_break()
                self.play(FadeIn(tc_1qb[0:2]))
                self.slide_break()
                self.play(FadeIn(tc_1qb[2:4]))
                self.slide_break()
                self.play(FadeIn(tc_1qb[4:6]))
                self.add_foreground_mobject(tc_1qb[4:6])
                self.slide_break()
                self.play(FadeIn(RBIM_bonds[0:5]))
                self.slide_break()
                self.play(FadeIn(tc_1qb[6:8]))
                self.add_foreground_mobject(tc_1qb[6:8])
                self.slide_break()
                self.play(FadeIn(RBIM_bonds[5:]))
                self.slide_break()
                self.remove_foreground_mobject(tc_1qb[4:6])
                self.remove_foreground_mobject(tc_1qb[6:8])
                self.play(FadeOut(tc_1qb))
                self.slide_break()
                self.play(FadeIn(steps[3]))
                self.slide_break()

                self.play(FadeIn(steps[4]))
                self.slide_break()
                self.play(FadeIn(steps[5]))
                self.slide_break()
                self.play(FadeOut(tc_qubits))
                self.slide_break()

                self.play(FadeOut(steps),FadeOut(tc_lattice),FadeOut(RBIM))

            if subsec6:
                tc=VGroup(VGroup(),VGroup(),VGroup(),VGroup())
                for x in range(-1,2):
                    tc[0]+=Line(RIGHT*x+1.75*DOWN,RIGHT*x+1.75*UP).set_color(WHITE).set_opacity(0.25)
                    tc[0]+=Line(UP*x+1.75*LEFT,UP*x+1.75*RIGHT).set_color(WHITE).set_opacity(0.25)

                for x in range(-1,2):
                    for y in range(-1,2):
                        tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x-0.5,y,0])
                        tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x+0.5,y,0])
                        tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y-0.5,0])
                        tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y+0.5,0])

                for x in range(-1,2):
                    for y in range(-1,2):
                        tc[1]+=Circle(radius=0.05,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to([x,y,0])

                tc[1]+=Line(LEFT+UP,UP,stroke_width=8, color=BLUE)
                tc[1]+=Circle(radius=0.075,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT+UP)
                tc[1]+=Circle(radius=0.075,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(UP)
                tc[1]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(LEFT/2+UP)
                tc[1]+=Tex(r"$Z$",color=YELLOW).move_to([-0.5,1.2,0]).scale(0.5)

                for x in range(-1,3):
                    for y in range(-1,3):
                        tc[2]+=Circle(radius=0.05,stroke_opacity=0.75,stroke_color=RED,fill_color="#161c20",fill_opacity=1).move_to([x-0.5,y-0.5,0])

                tc[2]+=Line(LEFT/2+DOWN/2,LEFT/2+3*DOWN/2,stroke_width=8, color=RED)
                tc[2]+=Circle(radius=0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT/2+DOWN/2)
                tc[2]+=Circle(radius=0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT/2+3*DOWN/2)
                tc[2]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(LEFT/2+DOWN)
                tc[2]+=Tex(r"$X$",color=YELLOW).move_to([-0.3,-.8,0]).scale(0.5)

                tc[3]+=Line(ORIGIN,RIGHT,stroke_color=PINK,stroke_width=8)
                tc[3]+=Line(RIGHT/2+UP/2,RIGHT/2+DOWN/2,stroke_color=PINK,stroke_width=8)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(ORIGIN)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT/2+UP/2)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT/2+DOWN/2)
                tc[3]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(RIGHT/2)
                tc[3]+=Tex(r"$Y$",color=YELLOW).move_to([0.7,0.2,0]).scale(0.5)

                tc.scale(1.125).shift(DOWN)

                tc_labs=VGroup(
                    Tex(r"\bfseries Toric code"),
                    Tex(r"\text{Bit-flip}",r"&=",r"\textrm{RBIM}\\",r"\text{Indep.\ X\&Z}",r"&=",r"\textrm{RBIM}","+",r"\textrm{RBIM}\\",r"\textrm{Depolarising}",r"&=",r"\textrm{Rand.\ 8-vertex}",tex_environment="align*")
                )
                tc_labs[1][2].set_color(BLUE)
                tc_labs[1][5].set_color(BLUE)
                tc_labs[1][7].set_color(RED)
                tc_labs[1][-1].set_color(PINK)
                tc_labs[0].scale(0.75)
                tc_labs[1].scale(0.5)
                tc_labs[0].move_to(2.5*UP)
                tc_labs[1].move_to(1.5*UP)
                self.play(FadeIn(tc_labs[0]))
                self.play(FadeIn(tc[0]))
                self.slide_break()
                self.play(FadeIn(tc_labs[1][0:3]))
                self.play(FadeIn(tc[1]))
                self.slide_break()
                self.play(FadeIn(tc_labs[1][3:8]))
                self.play(FadeIn(tc[2]))
                self.slide_break()
                self.play(FadeIn(tc_labs[1][8:]))
                self.play(FadeIn(tc[3]))
                self.slide_break()

                DIAG=np.array([1/2,math.sqrt(3)/2,0])
                DIAG2=np.array([1/2,-math.sqrt(3)/2,0])

                cc=VGroup(VGroup(),VGroup(),VGroup(),VGroup())
                cc[0]+=Line(ORIGIN,DIAG).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG,DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+RIGHT,DIAG+RIGHT+DIAG2).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+2*RIGHT+DIAG2,DIAG+RIGHT+DIAG2).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+RIGHT,DIAG+DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+DIAG+RIGHT-DIAG2,2*DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0][:6].shift(2*DIAG+RIGHT-DIAG2)
                #
                cc[0]+=Line(ORIGIN,DIAG).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG,DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+RIGHT,DIAG+RIGHT+DIAG2).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+2*RIGHT+DIAG2,DIAG+RIGHT+DIAG2).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+RIGHT,DIAG+DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+DIAG+RIGHT-DIAG2,2*DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0][6:].shift(2*RIGHT+DIAG+DIAG2)
                #
                cc[0]+=Line(ORIGIN,DIAG).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG,DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+RIGHT,DIAG+RIGHT+DIAG2).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+2*RIGHT+DIAG2,DIAG+RIGHT+DIAG2).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+RIGHT,DIAG+DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(DIAG+DIAG+RIGHT-DIAG2,2*DIAG+RIGHT).set_color(WHITE).set_opacity(0.25)
                #
                cc[0]+=Line(2*DIAG+2*RIGHT,2*DIAG+2*RIGHT+LEFT).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(2*DIAG+2*RIGHT,2*DIAG+2*RIGHT+DIAG).set_color(WHITE).set_opacity(0.25)
                cc[0]+=Line(2*DIAG+2*RIGHT,2*DIAG+2*RIGHT+DIAG2).set_color(WHITE).set_opacity(0.25)

                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(ORIGIN)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG-DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(2*RIGHT+DIAG+DIAG2)
                cc[0][-8:].shift(DIAG+RIGHT+DIAG-DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(ORIGIN)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG-DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(2*RIGHT+DIAG+DIAG2)
                cc[0][-8:].shift(2*RIGHT+DIAG+DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(ORIGIN)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(DIAG+RIGHT+DIAG-DIAG2)
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(2*RIGHT+DIAG+DIAG2)
                #
                cc[0]+=Circle(radius=0.1,fill_opacity=1,color=WHITE).move_to(RIGHT+RIGHT+DIAG+DIAG)

                ss=0.25
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT+DIAG+RIGHT)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT+DIAG-DIAG2)
                cc[1][0:3].shift(DIAG+RIGHT+DIAG-DIAG2)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT+DIAG+RIGHT)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT+DIAG-DIAG2)
                cc[1][3:6].shift(RIGHT+RIGHT+DIAG+DIAG2)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT+DIAG+RIGHT)
                cc[1]+=Circle(radius=0.1,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to(RIGHT+DIAG-DIAG2)
                for x in cc[1]:
                    cc[2]+=x.copy().set_stroke(color=RED)
                cc[1].shift(ss*UP)
                cc[2].shift(ss*DOWN)

                p=DIAG+RIGHT+DIAG+RIGHT+RIGHT-DIAG2-DIAG2
                cc[1]+=Line(p,p-DIAG2+ss*UP,stroke_color=BLUE,stroke_width=8)
                cc[1]+=Line(p,p+RIGHT+ss*UP,stroke_color=BLUE,stroke_width=8)
                cc[1]+=Line(p,p-DIAG+ss*UP,stroke_color=BLUE,stroke_width=8)
                cc[1]+=Circle(radius=2*0.075,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG2+ss*UP)
                cc[1]+=Circle(radius=2*0.075,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG+ss*UP)
                cc[1]+=Circle(radius=2*0.075,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p+RIGHT+ss*UP)
                cc[1]+=Circle(radius=0.1,fill_opacity=1,color=YELLOW).move_to(p)
                cc[1]+=Tex(r"$Z$",color=YELLOW).move_to(p+0.4*UP+0.2*RIGHT).scale(.8)

                p=DIAG+RIGHT
                cc[2]+=Line(p,p-DIAG2+ss*DOWN,stroke_color=RED,stroke_width=8)
                cc[2]+=Line(p,p+RIGHT+ss*DOWN,stroke_color=RED,stroke_width=8)
                cc[2]+=Line(p,p-DIAG+ss*DOWN,stroke_color=RED,stroke_width=8)
                cc[2]+=Circle(radius=2*0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG2+ss*DOWN)
                cc[2]+=Circle(radius=2*0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG+ss*DOWN)
                cc[2]+=Circle(radius=2*0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p+RIGHT+ss*DOWN)
                cc[2]+=Circle(radius=0.1,fill_opacity=1,color=YELLOW).move_to(p)
                cc[2]+=Tex(r"$X$",color=YELLOW).move_to(p+0.4*UP+0.2*RIGHT).scale(.8)

                p=RIGHT+DIAG2+RIGHT+DIAG+RIGHT+DIAG
                cc[3]+=Line(p,p-DIAG2+ss*DOWN,stroke_color=PINK,stroke_width=8)
                cc[3]+=Line(p,p+RIGHT+ss*DOWN,stroke_color=PINK,stroke_width=8)
                cc[3]+=Line(p,p-DIAG+ss*DOWN,stroke_color=PINK,stroke_width=8)
                cc[3]+=Line(p,p-DIAG2+ss*UP,stroke_color=PINK,stroke_width=8)
                cc[3]+=Line(p,p+RIGHT+ss*UP,stroke_color=PINK,stroke_width=8)
                cc[3]+=Line(p,p-DIAG+ss*UP,stroke_color=PINK,stroke_width=8)
                cc[3]+=Circle(radius=2*0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG2+ss*DOWN)
                cc[3]+=Circle(radius=2*0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG+ss*DOWN)
                cc[3]+=Circle(radius=2*0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p+RIGHT+ss*DOWN)
                cc[3]+=Circle(radius=2*0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG2+ss*UP)
                cc[3]+=Circle(radius=2*0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG+ss*UP)
                cc[3]+=Circle(radius=2*0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p+RIGHT+ss*UP)
                cc[3]+=Circle(radius=0.1,fill_opacity=1,color=YELLOW).move_to(p)
                cc[3]+=Tex(r"$Y$",color=YELLOW).move_to(p+0.4*UP+0.2*RIGHT).scale(.8)

                cc.move_to(3*RIGHT+DOWN).scale(.5).scale(1.25)

                cc_labs=VGroup(
                    Tex(r"\bfseries Colour code"),
                    Tex(r"\text{Bit-flip}",r"&=",r"\textrm{3-spin RBIM}\\",r"\text{Indep.\ X\&Z}",r"&=",r"\textrm{3-spin RBIM}","+",r"\textrm{3-spin RBIM}\\",r"\textrm{Depolarising}",r"&=",r"\textrm{Rand.\ interacting 8-vertex}",tex_environment="align*")
                )
                cc_labs[1][2].set_color(BLUE)
                cc_labs[1][5].set_color(BLUE)
                cc_labs[1][7].set_color(RED)
                cc_labs[1][-1].set_color(PINK)
                cc_labs[0].scale(0.75)
                cc_labs[1].scale(0.5)
                cc_labs[0].move_to(3*RIGHT+2.5*UP)
                cc_labs[1].move_to(3*RIGHT+1.5*UP)
                self.play(tc.animate.shift(3*LEFT),tc_labs.animate.shift(3*LEFT))
                self.slide_break()
                self.play(FadeIn(cc),FadeIn(cc_labs))
                self.slide_break()
                self.play(FadeOut(tc),FadeOut(tc_labs),FadeOut(cc),FadeOut(cc_labs))

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class OtherModels(SlideScene):
        def construct(self):
            tocindex=5
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            # contents

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class SMD(SlideScene):
        def construct(self):
            tocindex=6
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            # contents

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class TND(SlideScene):
        def construct(self):
            tocindex=7
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            # contents

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))



class Conclusion(SlideScene):
    def construct(self):
        tocindex=-1
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        self.slide_break()

        temp = TexTemplate()
        temp.add_to_preamble(r"\usepackage{marvosym} \usepackage{fontawesome}")

        summary=Tex("Summary of ","what ","is ","going on").scale(.75).move_to([0,2,0])
        summary[1].set_color(YELLOW)
        summary[3].set_color(RED)

        arxiv=Tex(r"\texttt{\bfseries arXiv:~????.?????}").next_to(summary,DOWN,buff=1).scale(.8)
        package=Tex(r"\texttt{\bfseries github:~chubbc/manim\_slides}").next_to(arxiv,DOWN,buff=.25).scale(.8)

        email=Tex(r"\faEnvelope~~\texttt{me@christopherchubb.com}", tex_template=temp)
        website=Tex(r"\faLink~~\texttt{christopherchubb.com}", tex_template=temp)
        twitter=Tex(r"\faTwitter~~\texttt{@QuantumChubb}", tex_template=temp)
        github=Tex(r"\faGithub~~\texttt{chubbc}", tex_template=temp)
        socials=VGroup(github,twitter,website,email).arrange(DOWN).scale(0.75).shift(2*DOWN)

        self.play(Write(summary))
        self.slide_break()
        self.play(Write(arxiv),Write(package))
        self.slide_break()
        self.play(Write(socials))
        self.slide_break()
