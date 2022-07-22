from manim_slide import *
import math

config.background_color = "#161c20"

temp = TexTemplate()
temp.add_to_preamble(r"\usepackage{stmaryrd,mathtools}")
temp.add_to_preamble(r"\newcommand{\comm}[2]{\left\llbracket#1,#2\right\rrbracket}")
temp.add_to_document(r"\fontfamily{lmss}\selectfont")
# temp.add_to_document(r"\fontfamily{phv}\selectfont")

def MyTex(*x,tex_environment="center",tex_template="",color=WHITE,scale=1.0):
    return Tex(*x,
        tex_template=temp,
        tex_environment=tex_environment,
        color=color,
        scale=scale
    )

toc=Group(
    MyTex(r"\bfseries Lecture 1").scale(1.2),
    MyTex(r"Basics of decoding"),
    MyTex(r"Surface code"),
    MyTex(r"Stat mech mapping"),
    MyTex(r"Examples"),
    MyTex(r"\bfseries Lecture 2").scale(1.2),
    MyTex(r"Stat mech decoding"),
    MyTex(r"Tensor network decoding"),
    MyTex(r"Extensions"),
).scale(0.9).arrange(DOWN,aligned_edge=LEFT,buff=0.25).move_to(ORIGIN)
toc[0:5].shift(0.75*UP)
toc[0].set_x(0).shift(0.25*UP)
toc[5].set_x(0).shift(0.25*UP)

# footer=VGroup(
#     MyTex(r"$\texttt{christopherchubb.com/IBM2022}$"),
#     MyTex(r"$\texttt{github.com/chubbc/IBM2022}$"),
#     MyTex(r"$\texttt{\@QuantumChubb}$"),
# ).arrange(DOWN).scale(1/2).to_corner(DOWN).set_opacity(.5).shift(0.375*DOWN)

footer=VGroup(
    MyTex(r"$\texttt{github.com/chubbc/IBM2022}$"),
    MyTex(r"$\texttt{christopherchubb.com/IBM2022}$"),
    MyTex(r"$\texttt{@QuantumChubb}$"),
).arrange(RIGHT,buff=2).scale(1/2).to_corner(DOWN).set_opacity(.5).shift(0.375*DOWN)


if True:
    big=True; width_thin=2.5; width_medium=5; width_thick=5
    radius_int=0.025; radius_crosshair=0.1
    time_shift=0; time_colour=0; time_indicate=0; time_wait=1/30; ints=[]
    def findIntersection(A,B):
        (x1,y1,x2,y2)=A
        (x3,y3,x4,y4)=B
        if (x1,y1)==(x3,y3):# or (x2,y2)==(x4,y4):
            return None
        px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        if px<=x1 or px>=x2 or px<=x3 or px>=x4:
            return None
        return (px, py, 0.0)
    def checkIntersection(scene,i,M,R,m,r,Q,int_num):
        if m[i-1][:2]==m[i][:2]:
            return
        int = findIntersection(m[i-1],m[i])
        if not big:
            scene.play(
                M[i-1].animate.set_color(YELLOW).set_stroke(width=width_thick),
                M[i].animate.set_color(YELLOW).set_stroke(width=width_thick),
                # Transform(int_text[1],Text(str(int_num)).move_to(int_text[1]).scale(0.5)),
                run_time=time_indicate
            )
        if int==None:
            if not big:
                scene.play(
                    M[i-1].animate.set_color(GREEN).set_stroke(width=width_medium),
                    M[i].animate.set_color(GREEN).set_stroke(width=width_medium),
                    run_time=time_indicate
                )
        if int!=None:
            C=Circle(radius_int,color=YELLOW).set_fill(YELLOW,opacity=1).move_to(int)
            ints.append(C)
            Q.append((int[0],int[1],'r'))
            Q.append((int[0],int[1],'r'))
            Q.append((int[0],int[1],'l'))
            Q.append((int[0],int[1],'l'))
            r.append((int[0],int[1],m[i][2],m[i][3]))
            R.append(Line([r[-1][0],r[-1][1],0],[r[-1][2],r[-1][3],0],stroke_width=width_thick,color=YELLOW))
            r.append((int[0],int[1],m[i-1][2],m[i-1][3]))
            R.append(Line([r[-1][0],r[-1][1],0],[r[-1][2],r[-1][3],0],stroke_width=width_thick,color=YELLOW))
            Q.sort(key=lambda x:x[0])

            scene.remove(M[i-1],M[i])
            m[i-1]=(m[i-1][0],m[i-1][1],int[0],int[1])
            m[i]=(m[i][0],m[i][1],int[0],int[1])
            M[i-1]=Line([m[i-1][0],m[i-1][1],0],[m[i-1][2],m[i-1][3],0],stroke_width=width_thick,color=YELLOW)
            M[i]=Line([m[i][0],m[i][1],0],[m[i][2],m[i][3],0],stroke_width=width_thick,color=YELLOW)
            if not big:
                scene.add(M[i-1],M[i],R[-2],R[-1])

            if not big:
                scene.play(
                    FadeIn(C),
                    Flash(C,flash_radius=.5),
                    run_time=time_indicate
                )
            else:
                scene.add(C)
            scene.add_foreground_mobjects(C)
            if not big:
                scene.play(
                    M[i-1].animate.set_color(GREEN).set_stroke(width=width_medium),
                    M[i].animate.set_color(GREEN).set_stroke(width=width_medium),
                    R[-2].animate.set_color(RED).set_stroke(width=width_thin),
                    R[-1].animate.set_color(RED).set_stroke(width=width_thin),
                    run_time=time_indicate
                )
            else:
                scene.add(
                    M[i-1].set_color(GREEN).set_stroke(width=width_medium),
                    M[i].set_color(GREEN).set_stroke(width=width_medium),
                    R[-2].set_color(RED).set_stroke(width=width_thin),
                    R[-1].set_color(RED).set_stroke(width=width_thin))



class Title(SlideScene):
    def construct(self):
        title = MyTex(r"\bfseries\textsc{QEC Decoding}").scale(1.25).shift(2.5*UP)
        arxiv = MyTex(r"\bfseries{Decoding and statistical mechanics}}").scale(.75).shift(1.5*UP)
        name = MyTex("Christopher T.\ Chubb")
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
            toc[4].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[5].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[4].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[5].width*LEFT/1.2),
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
            toc[8].animate.scale(1.2).set_color(YELLOW).shift(0.1*toc[8].width*RIGHT)
        )
        self.slide_break()

        self.play(
            toc[8].animate.scale(1/1.2).set_color(WHITE).shift(0.1*toc[8].width*LEFT/1.2),
        )

class Basics(SlideScene):
    def construct(self):
        tocindex=1
        heading = toc[tocindex].copy()
        self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
        self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
        self.slide_break()


        p0=MyTex("Passive").move_to(3*LEFT+2*UP)
        p1=ImageMobject("./bike.jpg",height=2).move_to(3*LEFT+DOWN/2)
        p2=ImageMobject("./magnetic.jpg",height=2).move_to(3*LEFT+DOWN/2)
        p1.height=3
        p2.height=3

        a0=MyTex("Active").move_to(3*RIGHT+2*UP)
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

        heading_maxprob = MyTex("Which is the most likely ", "error","?")
        heading_maxprob[1].set_color(YELLOW)

        self.play(FadeIn(heading_maxprob))
        self.slide_break()

        self.play(heading_maxprob.animate.shift(2*UP))
        paulitoprob=MyTex("Error",r"$\to$","Probability")
        paulitoprob[0].set_color(YELLOW)
        paulitoprob[2].set_color(RED)
        self.play(FadeIn(paulitoprob[0]))
        self.slide_break()
        self.play(TransformFromCopy(paulitoprob[0],paulitoprob[2]),FadeIn(paulitoprob[1]))
        self.slide_break()

        pauli=MyTex(r"{\bigotimes}_{i}P_i",tex_environment="align*").next_to(paulitoprob[1],LEFT).set_color(YELLOW)
        iid=MyTex(r"{\prod}_{i}p_i(",r"P_i",r")",tex_environment="align*").next_to(paulitoprob[1],RIGHT)
        iid[0].set_color(RED)
        iid[1].set_color(YELLOW)
        iid[2].set_color(RED)
        self.play(
            Transform(paulitoprob[0],pauli),
            Transform(paulitoprob[2],iid)
        )
        self.slide_break()

        corr=MyTex(r"{\prod}_{j}\phi_j(",r"P_{R_j}",r")",tex_environment="align*").next_to(paulitoprob[1],RIGHT)
        corr[0].set_color(RED)
        corr[1].set_color(YELLOW)
        corr[2].set_color(RED)
        self.play(
            Transform(paulitoprob[2],corr)
        )
        self.slide_break()

        self.play(
            Transform(paulitoprob[0],MyTex("Error").set_color(YELLOW).next_to(paulitoprob[1],LEFT)),
            Transform(paulitoprob[2],MyTex("Probability").set_color(RED).next_to(paulitoprob[1],RIGHT)),
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

        maxprob=MyTex(r"\mathop{\mathrm{arg\,max}}",r"_E",r" \mathrm{Pr}(", r"E", r")",tex_environment="align*").shift(2.5*DOWN)
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

        heading_maxlike = MyTex("Which is the most likely ", "error class","?").shift(2*UP)
        heading_maxlike[1].set_color(BLUE)
        self.play(Transform(heading_maxprob,heading_maxlike))
        self.slide_break()

        classtoprob=MyTex("Error class").next_to(paulitoprob[1],LEFT).set_color(BLUE).shift(RIGHT/2)
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

        maxlike=MyTex(
            r"\mathop{\mathrm{arg\,max}}",
            r"_{\overline{E}}",
            r" \mathrm{Pr}(",
            r"\overline{E}",
            r")",tex_environment="align*").shift(2.5*DOWN)
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

        mld=MyTex("Maximum likelihood condition").shift(1.75*UP)
        sr=SurroundingRectangle(maxlike,color=WHITE,buff=0.25)
        self.play(FadeIn(mld),FadeIn(sr))
        self.slide_break()

        self.play(Circumscribe(maxlike[2:5],color=WHITE))
        self.slide_break()

        coset1=MyTex(
            r"\mathrm{Pr}(",
            r"\overline E",
            r")",
            tex_environment="align*"
        )#.scale(1)
        coset1[0].set_color(RED)
        coset1[1].set_color(BLUE)
        coset1[2].set_color(RED)
        coset2=MyTex(
            r":=\sum_{",
            r"E",
            r"\in",
            r"\overline E}",
            r"\mathrm{Pr}(",
            r"E",
            r")",
            tex_environment="align*"
        ).next_to(coset1,RIGHT)#.scale(1).next_to([-.5,-1.75,0],RIGHT)
        coset2[0].set_color(WHITE)
        coset2[1].set_color(YELLOW)
        coset2[2].set_color(WHITE)
        coset2[3].set_color(BLUE)
        coset2[4].set_color(RED)
        coset2[5].set_color(YELLOW)
        coset2[6].set_color(RED)
        coset3=MyTex(
            r"=",
            r"\sum_{S\in\text{Stab}}",
            r"\mathrm{Pr}(",
            r"E",
            r"S",
            r")",
            tex_environment="align*"
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
                    MyTex("Edges = Qubits"),
                    MyTex("Vertices = X stab"),
                    MyTex("Faces = Z stab"),
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
                Xstab+=MyTex("X").move_to(LEFT-0.6*UP).scale(1.5)
                Xstab+=MyTex("X").move_to(RIGHT+0.6*UP).scale(1.5)
                Xstab+=MyTex("X").move_to(UP-0.6*RIGHT).scale(1.5)
                Xstab+=MyTex("X").move_to(DOWN+0.6*RIGHT).scale(1.5)
                Xstab.set_color(BLUE).move_to(3*RIGHT+4*UP)

                Zstab=VGroup()
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(LEFT)
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(RIGHT)
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(DOWN)
                Zstab+=Circle(radius=0.15,fill_opacity=1).move_to(UP)
                Zstab+=Square(side_length=2,stroke_width=8).move_to(ORIGIN)
                Zstab+=MyTex("Z").move_to(1.6*LEFT).scale(1.5)
                Zstab+=MyTex("Z").move_to(1.6*RIGHT).scale(1.5)
                Zstab+=MyTex("Z").move_to(1.6*UP).scale(1.5)
                Zstab+=MyTex("Z").move_to(1.6*DOWN).scale(1.5)
                Zstab.set_color(RED).move_to(6*RIGHT+7*UP)

                righttext=VGroup(
                    MyTex("\\bfseries Z errors"),
                    MyTex("Logical = loops"),
                    MyTex("Errors = paths"),
                    MyTex("Syn. = end-points"),
                    MyTex("\\bfseries X errors"),
                    MyTex("Logical = co-loops"),
                    MyTex("Errors = co-paths"),
                    MyTex("Syn. = co-end-points"),
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
                odds=MyTex(r"\text{In:Out} ","= {",r"{\Pr(\text{In})}",r"\over",r"{\Pr(\text{Out})}",r"}",tex_environment="align*")
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

            subsec1=False
            subsec2=False
            subsec3=False
            subsec4=False
            subsec5=False
            subsec6=False
            subsec7=False

            subsec1=True
            subsec2=True
            subsec3=True
            subsec4=True
            subsec5=True

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
                toric_code+=MyTex("Z",color=RED).move_to([-0.5,-0.25,0]).scale(.5)
                toric_code+=MyTex("Z",color=RED).move_to([-0.5,-1+0.25,0]).scale(.5)
                toric_code+=MyTex("Z",color=RED).move_to([-1+0.2,-0.5,0]).scale(.5)
                toric_code+=MyTex("Z",color=RED).move_to([-0.2,-0.5,0]).scale(.5)
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.0,0.5,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.0,1.5,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([0.5,1.0,0.0])
                toric_code+=Circle(radius=0.075,fill_opacity=1,color=BLUE).move_to([1.5,1.0,0.0])
                toric_code+=Line(UP+RIGHT/2,UP+3*RIGHT/2,stroke_width=8,color=BLUE)
                toric_code+=Line(RIGHT+UP/2,RIGHT+3*UP/2,stroke_width=8,color=BLUE)
                toric_code+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[+0.5,+0.25,0]).scale(.5)
                toric_code+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[-0.5,-0.25,0]).scale(.5)
                toric_code+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[-0.2,+0.5,0]).scale(.5)
                toric_code+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[+0.2,-0.5,0]).scale(.5)
                toric_code+=MyTex("Toric code").move_to(2.25*DOWN).scale(0.75)

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
                ev_model+=MyTex("$J_Z$",color=BLUE).scale(.5).move_to([-0.5,1.2,0.0])
                #
                ev_model+=Line([-0.5,-0.5,0.0],[-0.5,-1.5,0.0],stroke_width=8,color=RED)
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([-0.5,-0.5,0.0])
                ev_model+=Circle(radius=0.075,stroke_opacity=1,color="#161c20",fill_opacity=1,fill_color="#161c20").move_to([-0.5,-1.5,0.0])
                ev_model+=Circle(radius=0.075,color=RED,stroke_width=8).move_to([-0.5,-0.5,0.0])
                ev_model+=Circle(radius=0.075,color=RED,stroke_width=8).move_to([-0.5,-1.5,0.0])
                ev_model+=MyTex("$J_X$",color=RED).scale(.5).move_to([-0.25,-.8,0.0])
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
                ev_model+=MyTex("$J_Y$",color=PINK).scale(.5).move_to([0.7,0.2,0.0])
                #
                ev_model+=MyTex("Eight-vertex model").move_to(2.25*DOWN).scale(0.75)

                toric_code.scale(1.25).move_to(ORIGIN)
                ev_model.scale(1.25).move_to(3.5*RIGHT)
                arrow=MyTex("$\\rightarrow$")

                self.play(FadeIn(toric_code))
                self.slide_break()

                self.play(toric_code.animate.shift(3.5*LEFT))
                self.slide_break()

                self.play(TransformFromCopy(toric_code[0:6],ev_model[0:6]),FadeIn(arrow))
                self.play(TransformFromCopy(toric_code[6:34],ev_model[6:40]))
                self.play(FadeIn(ev_model[40:]))
                self.slide_break()

                eq=VGroup(Tex(r"$\Pr(\overline{E}):=\sum_{S\in\mathcal S}\Pr(ES)$").set_color(RED),Tex(r"$Z_E=\sum_{\vec s}e^{-\beta H_E(\vec s)}$").set_color(BLUE))
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
                gloss_l+=MyTex("Pauli code + Pauli noise")
                gloss_l+=MyTex("Threshold")
                gloss_l+=MyTex("Error class probabilties")
                gloss_l+=MyTex("Decoding")
                gloss_l+=MyTex("Stabilisers")
                gloss_l+=MyTex("Pauli errors")
                gloss_l.set_color(RED)

                gloss_r=VGroup()
                gloss_r+=MyTex("Disordered stat mech model")
                gloss_r+=MyTex("Phase transition")
                gloss_r+=MyTex("Partition functions")
                gloss_r+=MyTex("Approx.\\ part.\\ functions")
                gloss_r+=MyTex("Classical spins")
                gloss_r+=MyTex("Disordered couplings")
                gloss_r.set_color(BLUE)

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
                comm=MyTex(r"\comm{A}{B}:=\begin{dcases} +1 &:A,B\text{ commute},\\-1&:\text{otherwise}.\end{dcases}",tex_environment="align*")
                comm2=MyTex(r"AB=\comm{A}{B}BA",tex_environment="align*")
                self.play(FadeIn(comm))
                self.slide_break()
                self.play(Transform(comm,comm2))
                self.slide_break()
                self.play(FadeOut(comm))
                self.slide_break()

            if subsec4:
                ham = MyTex(
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
                    tex_environment="align*"
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

                m=ham[0:5]; d=UP; c=RED; t=r"\fontfamily{lmss}\selectfont {\text{Disordered}}\atop{\text{Hamiltonian}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                # self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.play(m.animate.scale(1/1.2))
                self.slide_break()


                m=ham[6]; d=DOWN; c=ORANGE; t=r"\fontfamily{lmss}\selectfont {\text{Sum over}}\atop{\text{1 qubit Paulis}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                # self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.play(m.animate.scale(1/1.2))
                self.slide_break()

                m=ham[7]; d=UP; c=GREEN; t=r"\fontfamily{lmss}\selectfont {\text{Coupling}}\atop{\text{strength}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                # self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.play(m.animate.scale(1/1.2))
                self.slide_break()

                m=ham[8]; d=DOWN; c=BLUE; t=r"\fontfamily{lmss}\selectfont \text{Disorder}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                # self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.play(m.animate.scale(1/1.2))
                self.slide_break()

                m=ham[9:]; d=UP; c=PURPLE; t=r"\fontfamily{lmss}\selectfont {\text{Degrees of}}\atop{\text{freedom}}"
                braces+=Brace(mobject=m,direction=d)
                braces+=braces[-1].get_tex(t).scale(0.75).set_color(c)
                braces[-2:-1].set_color(c)
                self.play(m.animate.set_color(c).scale(1.2),GrowFromCenter(braces[-2]),FadeIn(braces[-1]))
                self.slide_break()
                # self.play(m.animate.set_color(WHITE).scale(1/1.2),braces[-2].animate.set_color(WHITE),braces[-1].animate.set_color(WHITE))
                self.play(m.animate.scale(1/1.2))
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
                self.play(ham.animate.set_color(WHITE),FadeOut(braces))
                self.slide_break()

                self.play(ham.animate.shift(1.5*UP))
                self.slide_break()

                points=VGroup(
                    MyTex(r"\textbullet",r" Ising-type (sum of product of spins)"),
                    MyTex(r"\textbullet",r" Disorder flips terms (ferro v.\ anti-ferro)"),
                    MyTex(r"\textbullet",r" Local code $\Rightarrow$ local stat mech model"),
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
                # hams+=MyTex(
                #     r"H_{E",r"S_l",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)",r"\comm{\sigma}{E}",r"\comm{\sigma}{S_l}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                #     tex_environment="align*")
                #
                # hams+=MyTex(
                #     r"H_{E",r"S_l",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)",r"\comm{\sigma}{E}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k ",r"\comm{\sigma}{S_l}",
                #     tex_environment="align*")
                #
                # hams+=MyTex(
                #     r"H_{E",r"S_l",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)",r"\comm{\sigma}{E}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k ",r"(-1)^{\delta_{k,l}}",
                #     tex_environment="align*")


                gauge=MyTex(r"How do stabilisers act on this?").move_to(1.5*UP)
                self.play(FadeIn(gauge))
                self.slide_break()

                oldham=MyTex(
                    r"H_{E",r"}(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"\rrbracket\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*")
                oldham.move_to(ham)
                self.remove(*ham)
                self.add(oldham)
                ham=MyTex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"S_l",r"\rrbracket\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*")
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

                oldham=MyTex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"S_l",r"\rrbracket",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*")
                oldham[1].set_color(YELLOW)
                oldham[3].set_color(YELLOW)
                oldham.move_to(ham)
                self.remove(*ham)
                self.add(oldham)
                ham=MyTex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E",r"\rrbracket",r"\comm{\sigma}{S_l}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*")
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

                oldham=MyTex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E\rrbracket",r"\comm{\sigma}{S_l}",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*")
                oldham[1].set_color(YELLOW)
                oldham[3].set_color(YELLOW)
                oldham.move_to(oldham)
                self.remove(*ham)
                self.add(oldham)
                ham=MyTex(
                    r"H_{E",r"S_l}",r"(\vec s):=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E\rrbracket",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",r"(-1)^{\delta_{k,l}}",
                    tex_environment="align*")
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

                oldham=MyTex(
                    r"H_{E",r"S_l}",r"(\vec s)",r":=-\sum_{i}\sum_{\sigma\in\mathcal P_i}J_i(\sigma)\,\llbracket \sigma,E\rrbracket",r"\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",r"(-1)^{\delta_{k,l}}",
                    tex_environment="align*")
                oldham[1].set_color(YELLOW)
                oldham[5].set_color(YELLOW)
                oldham.move_to(oldham)
                self.remove(*ham)
                self.add(oldham)
                ham=MyTex(
                    r"H_{E",r"S_l}",r"(\vec s)",r"=H_{E}(\vec{s}\oplus",r"\vec{e_l}",r")",
                    tex_environment="align*")
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



                gauge2=MyTex(r"Applying stabiliser = Flipping spin").move_to(1.5*DOWN)
                self.play(FadeIn(gauge2))
                self.slide_break()

                gauge3=MyTex(r"Z_E=Z_{E {{S}} }",tex_environment="align*").move_to(1.5*DOWN)
                gauge3[1].set_color(YELLOW)
                self.play(FadeOut(gauge2))
                self.play(FadeIn(gauge3))
                self.slide_break()

                self.play(Circumscribe(gauge3))
                self.slide_break()

                self.play(FadeOut(gauge),FadeOut(gauge3),FadeOut(ham))
                self.slide_break()

            if subsec5:
                sc=0.9

                eq1=MyTex(r"Z_E",r"\stackrel{!}{=}",r"\Pr(\overline{E})",tex_environment="align*",scale=sc)
                eq1[0].set_color(BLUE)
                eq1[2].set_color(RED)
                eq1.scale(sc)
                self.play(FadeIn(eq1))
                self.slide_break()

                self.play(eq1.animate.shift(1.5*UP))
                eq2=MyTex(r"\sum_",r"{\vec s}",r"e^{-\beta H_{ {{E}} }({{\vec s}})}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc)
                eq2[:-2].set_color(BLUE)
                eq2[-1].set_color(RED)
                eq2.scale(sc)
                # self.play(FadeIn(eq2))
                self.play(TransformFromCopy(eq1[0],eq2[:-2]),TransformFromCopy(eq1[1],eq2[-2]),TransformFromCopy(eq1[-1],eq2[-1]))
                self.slide_break()

                x=MyTex(r"\sum_",r"{S}",r"e^{-\beta H_{ {{E}}{{S}} }({{\vec 1}})}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc)
                x[:-2].set_color(BLUE)
                x[-1].set_color(RED)
                x.scale(sc)
                self.play(
                    Transform(eq2[0],x[0]),
                    Transform(eq2[1],x[1]),
                    Transform(eq2[2],x[2]),
                    Transform(eq2[3],x[3]),
                    Transform(eq2[5],x[4]),
                    Transform(eq2[4],x[5]),
                    FadeIn(x[6]),
                    Transform(eq2[6],x[7]),
                    eq2[7].animate.move_to(x[8]),
                    eq2[8].animate.move_to(x[9]),
                )
                self.slide_break()

                self.remove(x[6],*eq2)
                eq2=MyTex(r"\sum_",r"{S}",r"e^{-\beta H_{ {{ES}} }(\vec 1)}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc).move_to(eq2)
                eq2[:-2].set_color(BLUE)
                eq2[-1].set_color(RED)
                eq2.scale(sc)
                self.add(eq2)
                x=MyTex(r"\sum_",r"{F\in\overline{E}}",r"e^{-\beta H_{ {{F}} }(\vec 1)}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc).move_to(eq2)
                x[:-2].set_color(BLUE)
                x[-1].set_color(RED)
                x.scale(sc)
                self.play(Transform(eq2,x))
                self.slide_break()

                self.remove(*eq2)
                eq2=MyTex(r"\sum_{F\in\overline{E}}e^{",r"-\beta H_{F}(\vec 1)",r" }",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc).move_to(eq2)
                eq2[:-2].set_color(BLUE)
                eq2[-1].set_color(RED)
                eq2.scale(sc)
                self.add(eq2)
                x=MyTex(r"\sum_{F\in\overline{E}}e^{",r"\sum_{i,\sigma_i}\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}",r" }",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc).move_to(eq2)
                x[:-2].set_color(BLUE)
                x[-1].set_color(RED)
                x.scale(sc)
                self.play(Transform(eq2,x))
                self.slide_break()

                self.remove(*eq2)
                eq2=MyTex(r"\sum_{F\in\overline{E}}",r"e^{",r"\sum_{i,\sigma_i}",r"\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc).move_to(eq2)
                eq2[:-2].set_color(BLUE)
                eq2[-1].set_color(RED)
                eq2.scale(sc)
                self.add(eq2)
                x=MyTex(r"\sum_{F\in\overline{E}}",r"\prod_{i}",r"e^{",r"\sum_{\sigma_i}",r"\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\Pr(F)",tex_environment="align*",scale=sc).move_to(eq2)
                x[:-2].set_color(BLUE)
                x[-1].set_color(RED)
                x.scale(sc)
                self.play(
                    Transform(eq2[0],x[0]),
                    Transform(eq2[1],x[2]),
                    Transform(eq2[2],x[1]),
                    FadeIn(x[3]),
                    Transform(eq2[3],x[4]),
                    Transform(eq2[4],x[5]),
                    Transform(eq2[5],x[6]),
                )
                self.slide_break()

                self.remove(*eq2,x[3])
                eq2=MyTex(r"\sum_{F\in\overline{E}}\prod_{i}e^{\sum_{\sigma_i}\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}",r"\Pr(F)",tex_environment="align*",scale=sc).move_to(eq2)
                eq2[:-3].set_color(BLUE)
                eq2[-2:].set_color(RED)
                eq2.scale(sc)
                self.add(eq2)
                x=MyTex(r"\sum_{F\in\overline{E}}\prod_{i}e^{\sum_{\sigma_i}\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}",r"\prod_ip_i(F_i)",tex_environment="align*",scale=sc).move_to(eq2)
                x[:-3].set_color(BLUE)
                x[-2:].set_color(RED)
                x.scale(sc)
                self.play(
                    Transform(eq2,x)
                )
                self.slide_break()

                self.remove(*eq2)
                eq2=MyTex(r"\sum_{F\in\overline{E}}\prod_{i}e^{\sum_{\sigma_i}\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\prod_i",r"p_i(F_i)",tex_environment="align*",scale=sc).move_to(eq2)
                eq2[:-3].set_color(BLUE)
                eq2[-2:].set_color(RED)
                eq2.scale(sc)
                self.add(eq2)
                x=MyTex(r"\sum_{F\in\overline{E}}\prod_{i}e^{\sum_{\sigma_i}\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\prod_i",r"e^{\log p_i(F_i)}",tex_environment="align*",scale=sc).move_to(eq2)
                x[:-3].set_color(BLUE)
                x[-2:].set_color(RED)
                x.scale(sc)
                self.play(Transform(eq2,x))
                self.slide_break()

                self.remove(*eq2)
                eq2=MyTex(r"\sum_{F\in\overline{E}}\prod_{i}e^{\sum_{\sigma_i}\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}}",r"\stackrel{!}{=}",r"\sum_{F\in\overline{E}}\prod_ie^{\log p_i(F_i)}",tex_environment="align*",scale=sc).move_to(eq2)
                eq2[0].set_color(BLUE)
                eq2[2].set_color(RED)
                eq2.scale(sc)
                self.add(eq2)

                # self.play(eq1.animate.shift(1*UP),eq2.animate.shift(1*UP))
                eq3=MyTex(r"\sum_{\sigma_i}\beta J_i(\sigma_i)\comm{\sigma_i}{F_i}",r"\stackrel{!}{=}",r"\log p_i(F_i)",tex_environment="align*",scale=sc).move_to(eq2)
                eq3[0].set_color(BLUE)
                eq3[2].set_color(RED)
                eq3.move_to(1.5*DOWN)
                eq3.scale(sc)
                self.play(
                    TransformFromCopy(eq2[0],eq3[0]),
                    TransformFromCopy(eq2[1],eq3[1]),
                    TransformFromCopy(eq2[2],eq3[2]),
                )
                self.slide_break()

                self.play(FadeOut(eq2),eq3.animate.shift(1.5*UP))
                self.slide_break()

                eq4=MyTex(r"\beta J_i(\sigma_i)",r"=",r"\frac{1}{4}\sum_{\tau_i}\log p(\tau_i)\comm{\sigma_i}{\tau^{-1}_i}",tex_environment="align*",scale=sc).move_to(eq2)
                eq4[0].set_color(BLUE)
                eq4[2].set_color(YELLOW)
                eq4.move_to(2*DOWN)
                eq4.scale(sc)
                # self.play(eq1.animate.shift(UP/2),eq2.animate.shift(UP/2),eq3.animate.shift(UP/2))
                # self.slide_break()
                self.play(FadeIn(eq4))
                self.slide_break()

                sr=SurroundingRectangle(eq4,WHITE,buff=0.2)
                self.play(Write(sr))
                self.slide_break()

                self.remove(*eq3)
                eq3=MyTex(r"\sum_{\sigma_i}",r"\beta J_i(\sigma_i)",r"\comm{\sigma_i}{F_i}",r"\stackrel{!}{=}",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3).scale(sc)
                eq3[:3].set_color(BLUE)
                eq3[-1].set_color(RED)
                self.add(eq3)
                eq3_new=MyTex(r"\sum_{\sigma_i}",r"\frac 14 \sum_{\tau_i}\log p_i(\tau_i)\comm{\sigma_i}{\tau_i^{-1}}",r"\comm{\sigma_i}{F_i}",r"=",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3).scale(sc)
                eq3_new[0].set_color(BLUE)
                eq3_new[1].set_color(YELLOW)
                eq3_new[2].set_color(BLUE)
                eq3_new[4].set_color(RED)
                self.play(
                    Transform(eq3[0],eq3_new[0]),
                    TransformFromCopy(eq4[2],eq3_new[1]),
                    Transform(eq3[2],eq3_new[2]),
                    Transform(eq3[3],eq3_new[3]),
                    Transform(eq3[4],eq3_new[4]),
                    FadeOut(eq3[1]),
                )
                self.slide_break()

                self.remove(*eq3,*eq3_new)
                eq3=MyTex(r"\sum_{\sigma_i}",r"\frac 14",r"\sum_{\tau_i}\log p_i(\tau_i)",r"\,\bigl\llbracket\sigma_i,\tau_i^{-1}",r"\bigr\rrbracket",r"\,\llbracket\sigma_i,",r"F_i",r"\rrbracket",r"=",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3_new).scale(sc)
                eq3[0].set_color(BLUE)
                eq3[1:5].set_color(YELLOW)
                eq3[5:8].set_color(BLUE)
                eq3[9].set_color(RED)
                self.add(eq3)
                eq3_new=MyTex(r"\sum_{\tau_i}\log p(\tau_i)",r"\frac 14",r"\sum_{\sigma_i}",r"\,\bigl\llbracket\sigma_i,\tau^{-1}_i",r"F_i",r"\bigr\rrbracket",r"=",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3).scale(sc)
                eq3_new[0:6].set_color(YELLOW)
                eq3_new[7].set_color(RED)
                self.play(
                    Transform(eq3[0],eq3_new[2]),
                    Transform(eq3[1],eq3_new[1]),
                    Transform(eq3[2],eq3_new[0]),
                    Transform(eq3[3],eq3_new[3]),
                    Transform(eq3[4],eq3_new[5]),
                    Transform(eq3[6],eq3_new[4]),
                    Transform(eq3[8],eq3_new[6]),
                    Transform(eq3[9],eq3_new[7]),
                    FadeOut(eq3[5]),
                    FadeOut(eq3[7]),
                )
                self.slide_break()

                self.remove(*eq3,*eq3_new)
                eq3=MyTex(r"\sum_{\tau_i}\log p(\tau_i)",r"\frac 14 \sum_{\sigma_i} \comm{\sigma_i}{\tau^{-1}_iF_i}",r"=",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3).scale(sc)
                eq3[0:2].set_color(YELLOW)
                eq3[3].set_color(RED)
                self.add(eq3)
                eq3_new=MyTex(r"\sum_{\tau_i}\log p(\tau_i)",r"\delta_{\tau_i,F_i}",r"=",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3).scale(sc)
                eq3_new[0:2].set_color(YELLOW)
                eq3_new[3].set_color(RED)
                self.play(
                    Transform(eq3,eq3_new),
                )
                self.slide_break()

                self.remove(*eq3)
                eq3=MyTex(r"\sum_{\tau_i}",r"\log p(",r"\tau_i",r")",r"\delta_{\tau_i,F_i}",r"=",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3).scale(sc)
                eq3[0:5].set_color(YELLOW)
                eq3[6].set_color(RED)
                self.add(eq3)
                eq3_new=MyTex(r"\log p(",r"F_i",r")",r"=",r"\log p_i(F_i)",tex_environment="align*").move_to(eq3).scale(sc)
                eq3_new[0:3].set_color(YELLOW)
                eq3_new[4].set_color(RED)
                self.play(
                    Transform(eq3[0],eq3_new[1]),
                    Transform(eq3[2],eq3_new[1]),
                    Transform(eq3[4],eq3_new[1]),
                    Transform(eq3[1],eq3_new[0]),
                    Transform(eq3[3],eq3_new[2]),
                    Transform(eq3[5],eq3_new[3]),
                    Transform(eq3[6],eq3_new[4]),
                )
                self.slide_break()

                self.play(FadeOut(eq3))
                self.slide_break()

                eq1_new=MyTex(r"Z_E",r"=",r"\Pr(\overline{E})",tex_environment="align*").move_to(eq1).shift(3*DOWN/4 ).scale(sc)
                eq1_new[0].set_color(BLUE)
                eq1_new[2].set_color(RED)
                self.play(eq4.animate.shift(3*UP/4),sr.animate.shift(3*UP/4),Transform(eq1,eq1_new))
                self.slide_break()

                nish=MyTex("Nishimori condition").shift(1.5*UP)
                self.play(FadeOut(eq1))
                self.play(eq4.animate.move_to(ORIGIN),sr.animate.move_to(ORIGIN))
                self.slide_break()

                self.play(FadeIn(nish))
                self.slide_break()

                self.play(FadeOut(eq4),FadeOut(sr),FadeOut(nish))
                self.slide_break()
                # self.play(eq4.animate.shift(3*UP/4),sr.animate.shift(3*UP/4),Transform(eq1,eq1_new))

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class Examples(SlideScene):
        def construct(self):
            tocindex=4
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            subsec1=False
            subsec2=False
            subsec3=False

            subsec1=True
            subsec2=True
            subsec3=True

            if subsec1:
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
                tc_stab+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[+0.5,+0.25,0]).scale(.5)
                tc_stab+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[-0.5,-0.25,0]).scale(.5)
                tc_stab+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[-0.2,+0.5,0]).scale(.5)
                tc_stab+=MyTex("X",color=BLUE).move_to(UP+RIGHT+[+0.2,-0.5,0]).scale(.5)

                tc_1qb=VGroup()
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([-0.5,1.0,0.0])
                tc_1qb+=MyTex("I",color=YELLOW).move_to([-0.5,1.2,0]).scale(.5)
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([0.5,1,0.0])
                tc_1qb+=MyTex("X",color=YELLOW).move_to([0.5,1.2,0]).scale(.5)
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([-0.5,0,0.0])
                tc_1qb+=MyTex("Y",color=YELLOW).move_to([-0.5,0.2,0]).scale(.5)
                tc_1qb+=Circle(radius=0.075,fill_opacity=1,color=YELLOW).move_to([1.0,-0.5,0.0])
                tc_1qb+=MyTex("Z",color=YELLOW).move_to([0.8,-0.5,0]).scale(.5)


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
                    MyTex("0: Code + noise"),
                    MyTex("1: DoF on each stabiliser"),
                    MyTex("2: Interactions from 1-qubit Paulis"),
                    MyTex(r"$H_{I}=-\sum_{v\sim v'}J\,s_{v}s_{v'}$"),
                    MyTex("3: Disorder"),
                    MyTex(r"$H_{E}=-\sum_{v\sim v'}Je_{vv'}\,s_{v}s_{v'}$"),
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

            if subsec2:
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
                tc[1]+=MyTex(r"Z",color=YELLOW).move_to([-0.5,1.2,0]).scale(0.5)

                for x in range(-1,3):
                    for y in range(-1,3):
                        tc[2]+=Circle(radius=0.05,stroke_opacity=0.75,stroke_color=RED,fill_color="#161c20",fill_opacity=1).move_to([x-0.5,y-0.5,0])

                tc[2]+=Line(LEFT/2+DOWN/2,LEFT/2+3*DOWN/2,stroke_width=8, color=RED)
                tc[2]+=Circle(radius=0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT/2+DOWN/2)
                tc[2]+=Circle(radius=0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT/2+3*DOWN/2)
                tc[2]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(LEFT/2+DOWN)
                tc[2]+=MyTex(r"X",color=YELLOW).move_to([-0.3,-.8,0]).scale(0.5)

                tc[3]+=Line(ORIGIN,RIGHT,stroke_color=PINK,stroke_width=8)
                tc[3]+=Line(RIGHT/2+UP/2,RIGHT/2+DOWN/2,stroke_color=PINK,stroke_width=8)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(ORIGIN)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT/2+UP/2)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT/2+DOWN/2)
                tc[3]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(RIGHT/2)
                tc[3]+=MyTex(r"Y",color=YELLOW).move_to([0.7,0.2,0]).scale(0.5)

                tc.scale(1.125).shift(DOWN)

                tc_labs=VGroup(
                    MyTex(r"\bfseries Toric code"),
                    MyTex(r"\text{Bit-flip}",r"&=",r"\text{RBIM}\\",r"\text{Indep.\ X\&Z}",r"&=",r"\text{RBIM}","+",r"\text{RBIM}\\",r"\text{Depolarising}",r"&=",r"\text{Rand.\ 8-vertex}",tex_environment="align*")
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
                cc[1]+=MyTex(r"Z",color=YELLOW).move_to(p+0.4*UP+0.2*RIGHT).scale(.8)

                p=DIAG+RIGHT
                cc[2]+=Line(p,p-DIAG2+ss*DOWN,stroke_color=RED,stroke_width=8)
                cc[2]+=Line(p,p+RIGHT+ss*DOWN,stroke_color=RED,stroke_width=8)
                cc[2]+=Line(p,p-DIAG+ss*DOWN,stroke_color=RED,stroke_width=8)
                cc[2]+=Circle(radius=2*0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG2+ss*DOWN)
                cc[2]+=Circle(radius=2*0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p-DIAG+ss*DOWN)
                cc[2]+=Circle(radius=2*0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(p+RIGHT+ss*DOWN)
                cc[2]+=Circle(radius=0.1,fill_opacity=1,color=YELLOW).move_to(p)
                cc[2]+=MyTex(r"X",color=YELLOW).move_to(p+0.4*UP+0.2*RIGHT).scale(.8)

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
                cc[3]+=MyTex(r"Y",color=YELLOW).move_to(p+0.4*UP+0.2*RIGHT).scale(.8)

                cc.move_to(3*RIGHT+DOWN).scale(.5).scale(1.25)

                cc_labs=VGroup(
                    MyTex(r"\bfseries Colour code"),
                    MyTex(r"\text{Bit-flip}",r"&=",r"\text{3-spin RBIM}\\",r"\text{Indep.\ X\&Z}",r"&=",r"\text{3-spin RBIM}","+",r"\text{3-spin RBIM}\\",r"\text{Depolarising}",r"&=",r"\text{Rand.\ interacting 8-vertex}",tex_environment="align*")
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
                self.slide_break()

            if subsec3:
                nish=MyTex(r"\beta J(\sigma)=\frac 14 \sum_\tau \log p(\tau)\comm{\sigma}{\tau^{-1}}",tex_environment="align*")
                self.play(FadeIn(nish))
                self.slide_break()

                nish2=VGroup(
                    MyTex(r"\beta J(I)=\frac 14\log p(I)p(X)p(Y)p(Z)",tex_environment="align*"),
                    MyTex(r"\beta J(X)=\frac 14\log \frac{p(I)p(X)}{p(Y)p(Z)}",tex_environment="align*").set_color(RED),
                    MyTex(r"\beta J(Y)=\frac 14\log \frac{p(I)p(Y)}{p(X)p(Z)}",tex_environment="align*").set_color(PURPLE),
                    MyTex(r"\beta J(Z)=\frac 14\log \frac{p(I)p(Z)}{p(X)p(Y)}",tex_environment="align*").set_color(BLUE ),
                ).arrange(DOWN,buff=0.5).scale(0.75)
                self.play(
                    ReplacementTransform(nish,nish2[0]),
                    TransformFromCopy(nish,nish2[1]),
                    TransformFromCopy(nish,nish2[2]),
                    TransformFromCopy(nish,nish2[3]),
                )
                self.slide_break()

                self.play(FadeOut(nish2[0]))
                self.slide_break()
                nish2=nish2[1:]

                self.play(nish2.animate.shift(1.5*RIGHT))
                self.slide_break()

                tc=VGroup(VGroup(),VGroup(),VGroup(),VGroup())
                for x in range(-1,2):
                    tc[0]+=Line(RIGHT*x+1.75*DOWN,RIGHT*x+1.75*UP).set_color(WHITE).set_opacity(0.25)
                    tc[0]+=Line(UP*x+1.75*LEFT,UP*x+1.75*RIGHT).set_color(WHITE).set_opacity(0.25)

                # for x in range(-1,2):
                #     for y in range(-1,2):
                #         tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x-0.5,y,0])
                #         tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x+0.5,y,0])
                #         tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y-0.5,0])
                #         tc[0]+=Circle(radius=0.05,fill_opacity=1,color=WHITE).move_to([x,y+0.5,0])

                for x in range(-1,2):
                    for y in range(-1,2):
                        tc[1]+=Circle(radius=0.05,stroke_opacity=0.75,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1).move_to([x,y,0])

                tc[1]+=Line(LEFT+UP,UP,stroke_width=8, color=BLUE)
                tc[1]+=Circle(radius=0.075,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT+UP)
                tc[1]+=Circle(radius=0.075,stroke_color=BLUE,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(UP)
                # tc[1]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(LEFT/2+UP)
                tc[1]+=MyTex(r"$J_Z$",color=BLUE).move_to([-0.5,1.2,0]).scale(0.5)

                for x in range(-1,3):
                    for y in range(-1,3):
                        tc[2]+=Circle(radius=0.05,stroke_opacity=0.75,stroke_color=RED,fill_color="#161c20",fill_opacity=1).move_to([x-0.5,y-0.5,0])

                tc[2]+=Line(LEFT/2+DOWN/2,LEFT/2+3*DOWN/2,stroke_width=8, color=RED)
                tc[2]+=Circle(radius=0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT/2+DOWN/2)
                tc[2]+=Circle(radius=0.075,stroke_color=RED,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(LEFT/2+3*DOWN/2)
                # tc[2]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(LEFT/2+DOWN)
                tc[2]+=MyTex(r"$J_X$",color=RED).move_to([-0.3,-.8,0]).scale(0.5)

                tc[3]+=Line(RIGHT/2+UP/2,RIGHT/2+DOWN/2,stroke_color=PINK,stroke_width=8)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT/2+UP/2)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT/2+DOWN/2)
                tc[3]+=MyTex(r"$J_Y$",color=PINK).move_to([0.7,0.2,0]).scale(0.5)
                tc[3]+=Line(ORIGIN,RIGHT,stroke_color=PINK,stroke_width=8)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(ORIGIN)
                tc[3]+=Circle(radius=0.075,stroke_color=PINK,fill_color="#161c20",fill_opacity=1,stroke_width=8).move_to(RIGHT)
                # tc[3]+=Circle(radius=0.05,fill_opacity=1,color=YELLOW).move_to(RIGHT/2)

                tc.scale(1.25).shift(4*LEFT+0.25*DOWN)

                self.play(FadeIn(tc))
                self.slide_break()

                dep=VGroup(
                    MyTex("Depolarising"),
                    MyTex(r"$(1-p,\,p/3,\,p/3,\,p/3)$"),
                    MyTex(r"=\frac 14\log \frac{3(1-p)}{p}",tex_environment="align*").set_color(RED),
                    MyTex(r"=\frac 14\log \frac{3(1-p)}{p}",tex_environment="align*").set_color(PINK),
                    MyTex(r"=\frac 14\log \frac{3(1-p)}{p}",tex_environment="align*").set_color(BLUE),
                ).arrange(DOWN,buff=0.5).scale(0.75)
                dep[1].shift(0.25*UP).scale(0.75)
                dep[0:2].set_x(3)
                self.play(FadeIn(dep[0:2]))
                self.slide_break()
                for i in range(3):
                    dep[i+2].next_to(nish2[i])
                self.play(Write(dep[2]),Write(dep[3]),Write(dep[4]))
                self.slide_break()

                self.play(FadeOut(dep))
                self.slide_break()

                xz=VGroup(
                    MyTex(r"Indep.\ X\&Z"),
                    MyTex(r"$\bigl((1-x)(1-z),\,x(1-z),\,xz,\,(1-x)z\bigr)$"),
                    MyTex(r"=\frac 12\log \frac{1-z}{z}",tex_environment="align*").set_color(RED),
                    MyTex(r"=0",tex_environment="align*").set_color(PINK),
                    MyTex(r"=\frac 12\log \frac{1-x}{x}",tex_environment="align*").set_color(BLUE),
                ).arrange(DOWN,buff=0.5).scale(0.75)
                xz[0].move_to(dep[0])
                xz[1].move_to(dep[1]).scale(.75)
                self.play(FadeIn(xz[0:2]))
                self.slide_break()
                for i in range(3):
                    xz[i+2].next_to(nish2[i])
                self.play(Write(xz[2]),Write(xz[4]))
                self.slide_break()
                self.play(Write(xz[3]))
                self.slide_break()
                self.play(FadeOut(xz))
                self.slide_break()

                bit=VGroup(
                    MyTex(r"Bit-flip"),
                    MyTex(r"$\bigl((1-p),p,0,0\bigr)$"),
                    MyTex(r"=+\infty",tex_environment="align*").set_color(RED),
                    MyTex(r"=~???",tex_environment="align*").set_color(PINK),
                    MyTex(r"=~???",tex_environment="align*").set_color(BLUE),
                ).arrange(DOWN,buff=0.5).scale(0.75)
                bit[0].move_to(dep[0])
                bit[1].move_to(dep[1]).scale(.75)
                self.play(FadeIn(bit[0:2]))
                self.slide_break()
                for i in range(3):
                    bit[i+2].next_to(nish2[i])

                self.play(Write(bit[2]))
                self.slide_break()

                self.play(Write(bit[3]),Write(bit[4]))
                self.slide_break()

                self.play(FadeOut(tc[2]),FadeOut(tc[3][0:3]),tc[3][3].animate.shift(0.2*LEFT))
                self.play(FadeOut(bit[2]),FadeOut(nish2[0]))
                self.slide_break()


                bit2=MyTex(r"\beta J(Y)",r"+",r"\beta J(Z)",r"=\frac 12\log\frac{p(I)}{p(X)}",r"=\frac 12\log\frac{1-p}{p}",tex_environment="align*").scale(0.75).move_to(nish2[1]).shift(RIGHT)
                bit2[0].set_color(PINK)
                bit2[2].set_color(BLUE)

                self.play(
                    Transform(bit[3],bit2[0]),
                    Transform(nish2[1],bit2[0]),
                    Transform(bit[4],bit2[2]),
                    Transform(nish2[2],bit2[2]),
                    FadeIn(bit2[1]),
                    FadeIn(bit2[3]),
                )
                self.slide_break()

                self.play(
                    Write(bit2[-1]),
                )
                self.slide_break()

                self.play(FadeOut(bit[3:]),FadeOut(nish2[1:3]),FadeOut(bit2),FadeOut(tc[0]),FadeOut(tc[1]),FadeOut(tc[3][3:]),FadeOut(bit[0:2]))
                self.slide_break()

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class SMD(SlideScene):
        def construct(self):
            tocindex=6
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            subsec1=False
            subsec2=False
            subsec3=False
            subsec4=False

            subsec1=True
            subsec2=True
            subsec3=True
            subsec4=True

            if subsec1:
                # Reduction

                maxlike=MyTex(
                    r"\mathop{\mathrm{arg\,max}}",
                    r"_{\overline{E}}",
                    r" \mathrm{Pr}(",
                    r"\overline{E}",
                    r")",tex_environment="align*")
                maxlike[1].set_color(BLUE)
                maxlike[2].set_color(RED)
                maxlike[3].set_color(BLUE)
                maxlike[4].set_color(RED)
                self.play(FadeIn(maxlike))
                self.slide_break()

                oldmaxlike=maxlike
                maxlike=MyTex(
                    r"\mathop{\mathrm{arg\,max}}",
                    r"_{\overline{E}}",
                    r"Z_{",
                    r"E",
                    r"}(T_N)",tex_environment="align*")
                maxlike[1].set_color(BLUE)
                maxlike[2].set_color(RED)
                maxlike[3].set_color(BLUE)
                maxlike[4].set_color(RED)
                self.play(
                    ReplacementTransform(oldmaxlike[0],maxlike[0]),
                    ReplacementTransform(oldmaxlike[1],maxlike[1]),
                    ReplacementTransform(oldmaxlike[2],maxlike[2]),
                    ReplacementTransform(oldmaxlike[3],maxlike[3]),
                    ReplacementTransform(oldmaxlike[4],maxlike[4]),
                )
                self.slide_break()

                self.play(maxlike.animate.shift(2*UP))
                self.slide_break()

                steps=VGroup(
                    MyTex("Step 1: Measure the syndrome, $s$"),
                    MyTex("Step 2: Construct an arbitrary error $A_s$ with syndrome $s$"),
                    MyTex("Step 3: Approximate $\Pr(\overline{A_sL_l})=Z_{A_sL_l}$ for each logical class"),
                    MyTex("Step 4: Pick the $l$ for which $\Pr(\overline{A_sL_l})$ is maximised"),
                    MyTex("Step 5: Apply $(A_sL_l)^{-1}$"),
                ).arrange(DOWN,aligned_edge=LEFT).move_to(DOWN)
                for i in range(5):
                    self.play(Write(steps[i]))
                    self.slide_break()

                self.play(FadeOut(steps),FadeOut(maxlike))
                self.slide_break()

            if subsec2:

                ax=Axes(
                    x_range=[0,10,10],
                    y_range=[0,1,1],
                    x_length=10,
                    y_length=4,
                    axis_config={
                        "include_tip": True,
                        "include_numbers": False,
                        "numbers_to_exclude": [r for r in range(3,25) if np.mod(r,5)!=0]
                    },
                )
                axis_labels=MyTex("Physical error rate", "Logical error rate").scale(0.5)
                axis_labels[0].next_to(ax,DOWN)
                axis_labels[1].rotate(90*DEGREES).next_to(ax,LEFT)

                x=np.arange(-5,5,0.1)
                l1 = ax.get_line_graph(
                    x_values = x+5,
                    y_values = 1/(1+np.exp(-x/4)),
                    vertex_dot_radius=0,
                    line_color=RED,
                    stroke_width = 3,
                )
                l2 = ax.get_line_graph(
                    x_values = x+5,
                    y_values = 1/(1+np.exp(-x/2)),
                    vertex_dot_radius=0,
                    line_color=ORANGE,
                    stroke_width = 3,
                )
                l3 = ax.get_line_graph(
                    x_values = x+5,
                    y_values = 1/(1+np.exp(-x*2)),
                    vertex_dot_radius=0,
                    line_color=YELLOW,
                    stroke_width = 3,
                )
                l4 = ax.get_line_graph(
                    x_values = x+5,
                    y_values = 1/(1+np.exp(-x*4)),
                    vertex_dot_radius=0,
                    line_color=GREEN,
                    stroke_width = 3,
                )
                l5 = ax.get_line_graph(
                    x_values = x+5,
                    y_values = 1/(1+np.exp(-x*8)),
                    vertex_dot_radius=0,
                    line_color=BLUE,
                    stroke_width = 3,
                )
                th=(ax.get_line_graph(
                    x_values = [5,5],
                    y_values = [0,1],
                    vertex_dot_radius=0,
                    line_color=WHITE,
                    stroke_width = 3,
                ))
                self.play(FadeIn(ax),FadeIn(axis_labels))
                self.slide_break()

                self.play(Write(l1,run_time=1))
                self.slide_break()
                self.play(Write(l2,run_time=2))
                self.slide_break()
                self.play(Write(l3,run_time=3))
                self.slide_break()
                self.play(Write(l4,run_time=4))
                self.slide_break()
                self.play(Write(l5,run_time=5))
                self.slide_break()
                self.play(Write(th))
                self.slide_break()

                x=0.5
                c=RED
                low_hist=VGroup()
                r=np.random.rand(4)
                r[0]=r[0]+x
                r=2*r/sum(r)
                for i in range(4):
                    low_hist+=Rectangle(width=0.5,height=r[i],fill_opacity=0.5).shift((1+i)*RIGHT/2+r[i]*UP/2)
                low_hist.set_color(c).next_to(3*LEFT,UP)
                self.play(FadeIn(low_hist))
                self.slide_break()
                high_hist=VGroup()
                r=np.random.rand(4)+x
                r=2*r/sum(r)
                for i in range(4):
                    high_hist+=Rectangle(width=0.5,height=r[i],fill_opacity=0.5).shift((1+i)*RIGHT/2+r[i]*UP/2)
                high_hist.set_color(c).next_to(3*RIGHT+1.5*DOWN,UP)
                self.play(FadeIn(high_hist))
                self.slide_break()

                x=[2,4,8,16]
                c=[ORANGE,YELLOW,GREEN,BLUE]
                for j in range(4):
                    old_low_hist=low_hist
                    low_hist=VGroup()
                    r=np.random.rand(4)
                    r[0]=r[0]+x[j]
                    r=2*r/sum(r)
                    for i in range(4):
                        low_hist+=Rectangle(width=0.5,height=r[i],fill_opacity=0.5).shift((1+i)*RIGHT/2+r[i]*UP/2)
                    low_hist.set_color(c[j]).next_to(3*LEFT,UP)

                    old_high_hist=high_hist
                    high_hist=VGroup()
                    r=np.random.rand(4)+x[j]
                    r=2*r/sum(r)
                    for i in range(4):
                        high_hist+=Rectangle(width=0.5,height=r[i],fill_opacity=0.5).shift((1+i)*RIGHT/2+r[i]*UP/2)
                    high_hist.set_color(c[j]).next_to(3*RIGHT+1.5*DOWN,UP)
                    self.play(
                        ReplacementTransform(old_low_hist,low_hist),
                        ReplacementTransform(old_high_hist,high_hist)
                    )
                    self.slide_break()

                self.play(
                    FadeOut(ax),
                    FadeOut(l1),
                    FadeOut(l2),
                    FadeOut(l3),
                    FadeOut(l4),
                    FadeOut(l5),
                    FadeOut(low_hist),
                    FadeOut(high_hist),
                    FadeOut(axis_labels),
                    FadeOut(th),
                )

                self.slide_break()

            if subsec3:
                # Phase transition proof

                prob=MyTex("\Pr(s,l):=\Pr(\overline{D_sL_l})",tex_environment="align*").move_to(UP/2)
                self.play(FadeIn(prob))
                self.slide_break()

                mld=MyTex(r"MLD: $\Pr(s,1)\geq \Pr(s,l)~\forall s,l$").move_to(DOWN/2)
                self.play(FadeIn(mld))
                self.slide_break()

                self.play(prob.animate.shift(2*UP),mld.animate.shift(2*UP))
                self.slide_break()

                fed=MyTex(
                    r"\Delta_m(E):=&F_{EL_m}(\beta_N)-F_{E}(\beta_n)\\",
                    r"\Delta_m(s,l)=&\frac{1}{\beta_N}\log \frac{\Pr(s,l)}{\Pr(s,l\oplus m)}\\",
                    r"\Delta_m:=&\left\langle\Delta_m(s,l)\right\rangle_{s,l}\\",
                    r"=&\frac{1}{\beta_N}\sum_{s,l}\Pr(s,l)\log \frac{\Pr(s,l)}{\Pr(s,l\oplus m)}",
                    tex_environment="align*").move_to(2*DOWN)
                self.play(Write(fed[0]))
                self.slide_break()

                self.play(Write(fed[1]))
                self.slide_break()

                self.play(FadeOut(prob),FadeOut(mld),FadeOut(fed[0]),fed[1].animate.shift(2*UP))
                self.slide_break()

                fed[2:4].shift(1.5*UP)
                self.play(Write(fed[2]))
                self.slide_break()
                self.play(Write(fed[3]))
                self.slide_break()

                self.play(FadeOut(fed[1]),FadeOut(fed[2]),FadeOut(fed[3]))
                self.slide_break()

                below=VGroup(
                    MyTex("Below threshold").scale(1.25),
                    MyTex(r"$\Pr(\text{dec.\ success})\to 1$"),
                    # MyTex(r"$\Delta_m\to +\infty$"),
                    MyTex(r"$\Delta_m(E)\stackrel{a.s.}{\to}+\infty$"),
                ).arrange(DOWN).set_color(BLUE).shift(3.5*LEFT)
                above=VGroup(
                    MyTex("Above threshold").scale(1.25),
                    MyTex(r"$\Pr(\text{dec.\ success})\to 1/K$"),
                    # MyTex(r"$\Delta_m\to +\infty$"),
                    MyTex(r"$\Delta_m(E)\stackrel{a.s.}{\to}0$"),
                ).arrange(DOWN).set_color(RED).shift(3.5*RIGHT)
                below[0].shift(0.5*UP)
                above[0].shift(0.5*UP)

                self.play(FadeIn(below[0]),FadeIn(above[0]))
                self.slide_break()

                self.play(Write(below[1:]))
                self.slide_break()

                self.play(Write(above[1:]))
                self.slide_break()

                self.play(FadeOut(below),FadeOut(above))
                self.slide_break()

            if subsec4:
                # Phase diagram + other decoders (beta-MFE, MP=MWPM, TND, Wootton, BSV matchgate)
                ax=Axes(
                    x_range=[0,2,2],
                    y_range=[0,5,5],
                    x_length=6,
                    y_length=4,
                    axis_config={
                        "include_tip": False,
                        "include_numbers": False,
                        "numbers_to_exclude": [r for r in range(3,25) if np.mod(r,5)!=0]
                    },
                )
                axis_labels=MyTex("Noise parameter", "Temperature").scale(0.75)
                axis_labels[0].next_to(ax,DOWN)
                axis_labels[1].rotate(90*DEGREES).next_to(ax,LEFT)

                y=np.arange(0,4.01,0.01)
                pt = ax.get_line_graph(
                    x_values = np.sqrt(1-(y-2)**2/(y-6)**2),
                    y_values = y,
                    vertex_dot_radius=0,
                    line_color=WHITE,
                    stroke_width = 3,
                )
                phase=Polygon(*[ax.coords_to_point(np.sqrt(1-(yy-2)**2/(yy-6)**2),yy) for yy in y],ax.coords_to_point(0,0),fill_opacity=0.25,fill_color=YELLOW,stroke_opacity=0)

                nish=VGroup()
                for x in np.arange(0,2,0.1):
                    nish+=Line(
                        ax.coords_to_point(x,np.sqrt(8*x+1)-1),
                        ax.coords_to_point(x+0.05,np.sqrt(8*x+1+8*0.05)-1)
                    )

                # self.add(DashedVMobject(nish))
                self.play(Write(ax))
                self.slide_break()

                self.play(Write(axis_labels))
                self.slide_break()

                self.play(Write(pt))
                self.slide_break()

                self.play(Write(nish))
                self.slide_break()

                self.play(Write(phase))
                self.slide_break()

                phase_text=VGroup(
                    VGroup(
                        MyTex("Ordered").scale(1.2),
                        MyTex("EC possible"),
                        MyTex(r"$\Delta_m(E)\to +\infty$"),
                    ).arrange(DOWN).move_to(2.75*LEFT+0.5*DOWN),
                    VGroup(
                        MyTex("Disrdered").scale(1.2),
                        MyTex("EC impossible"),
                        MyTex(r"$\Delta_m(E)\to 0$"),
                    ).arrange(DOWN).move_to(2*RIGHT+2*UP),
                ).scale(0.5)

                self.play(FadeIn(phase_text[0]))
                self.slide_break()

                self.play(FadeIn(phase_text[1]))
                self.slide_break()

                ML=VGroup(
                    Circle(radius=0.1,fill_opacity=1).move_to(ax.coords_to_point(1,2)),
                    Arrow(ax.coords_to_point(1.5,1.5),ax.coords_to_point(1,2)),
                    MyTex("ML").next_to(ax.coords_to_point(1.5,1.5),RIGHT,buff=0).scale(0.75)
                ).set_color(BLUE)

                MP=VGroup(
                    Circle(radius=0.1,fill_opacity=1).move_to(ax.coords_to_point(np.sqrt(8)/3,0)),
                    Arrow(ax.coords_to_point(1.5,0.5),ax.coords_to_point(np.sqrt(8)/3,0)),
                    MyTex("MP").next_to(ax.coords_to_point(1.5,0.5),RIGHT,buff=0).scale(0.75)
                ).set_color(RED)

                MFE=VGroup(
                    Circle(radius=0.1,fill_opacity=1).move_to(ax.coords_to_point(np.sqrt(24)/5,1)),
                    Arrow(ax.coords_to_point(1.5,1),ax.coords_to_point(np.sqrt(24)/5,1)),
                    MyTex("$T$-MFE").next_to(ax.coords_to_point(1.5,1),RIGHT,buff=0).scale(0.75)
                ).set_color(GREEN)


                self.play(Write(ML))
                self.slide_break()

                self.play(Write(MP))
                self.slide_break()

                self.play(Write(MFE))
                self.slide_break()

                self.play(
                    FadeOut(ax),
                    FadeOut(pt),
                    FadeOut(nish),
                    FadeOut(phase_text),
                    FadeOut(phase),
                    FadeOut(axis_labels),
                    FadeOut(ML),
                    FadeOut(MP),
                    FadeOut(MFE),
                )

                # self.add(phase,ax,axis_labels,pt)
                # self.add(nish)


                self.slide_break()

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class TND(SlideScene):
        def construct(self):
            tocindex=7
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            subsec1=False
            subsec2=False
            subsec3=False
            subsec4=False

            subsec1=True
            subsec2=True
            subsec3=True
            subsec4=True

            if subsec1:

                handwaving=ImageMobject("handwaving.png").scale(1)
                self.play(FadeIn(handwaving))
                self.slide_break()

                self.play(FadeOut(handwaving))
                self.slide_break()

                tc=VGroup()
                tc+=Line([-1.25,-1,0],[+1.25,-1,0],stroke_opacity=0.5)
                tc+=Line([-1.25,+1,0],[+1.25,+1,0],stroke_opacity=0.5)
                tc+=Line([-1.25,0,0],[+1.25,0,0],stroke_opacity=0.5)
                tc+=Line([-0.5,1,0],[-0.5,-1,0],stroke_opacity=0.5)
                tc+=Line([0.5,1,0],[0.5,-1,0],stroke_opacity=0.5)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(ORIGIN)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(LEFT)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(RIGHT)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(UP)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(UP+LEFT)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(UP+RIGHT)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(DOWN+LEFT)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(DOWN+RIGHT)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(DOWN)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(DOWN/2+LEFT/2)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(DOWN/2+RIGHT/2)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(UP/2+LEFT/2)
                tc+=Circle(radius=0.05,color=WHITE,fill_opacity=1).move_to(UP/2+RIGHT/2)
                tc+=Circle(radius=0.1,color=RED).move_to([-1,+0.5,0])
                tc+=Circle(radius=0.1,color=RED).move_to([+1,+0.5,0])
                tc+=Circle(radius=0.1,color=RED).move_to([-1,-0.5,0])
                tc+=Circle(radius=0.1,color=RED).move_to([+1,-0.5,0])
                tc+=Circle(radius=0.1,color=RED).move_to([0,-0.5,0])
                tc+=Circle(radius=0.1,color=RED).move_to([0,+0.5,0])
                tc+=Circle(radius=0.1,color=BLUE,fill_color=config.background_color,fill_opacity=1).move_to([-0.5,-1,0])
                tc+=Circle(radius=0.1,color=BLUE,fill_color=config.background_color,fill_opacity=1).move_to([-0.5,+1,0])
                tc+=Circle(radius=0.1,color=BLUE,fill_color=config.background_color,fill_opacity=1).move_to([-0.5, 0,0])
                tc+=Circle(radius=0.1,color=BLUE,fill_color=config.background_color,fill_opacity=1).move_to([+0.5,-1,0])
                tc+=Circle(radius=0.1,color=BLUE,fill_color=config.background_color,fill_opacity=1).move_to([+0.5,+1,0])
                tc+=Circle(radius=0.1,color=BLUE,fill_color=config.background_color,fill_opacity=1).move_to([+0.5, 0,0])

                tn=VGroup()
                for x in range(3):
                    tn+=Line([x,0,0],[x,2,0],color=RED)
                    tn+=Line([0,x,0],[2,x,0],color=BLUE)
                for x in range(2):
                    tn+=Line([x+.5,0,0],[x+.5,2,0],color=BLUE)
                    tn+=Line([0,x+.5,0],[2,x+.5,0],color=RED)
                for x in range(2):
                    for y in range(3):
                        tn+=Circle(radius=0.05,color=BLUE,fill_opacity=1).move_to([x+0.5,y,0])
                for x in range(3):
                    for y in range(2):
                        tn+=Circle(radius=0.05,color=RED,fill_opacity=1).move_to([x,y+.5,0])
                for x in range(3):
                    for y in range(3):
                        tn+=Rectangle(width=0.2,height=0.2,fill_color=GRAY,fill_opacity=1).move_to([x,y,0])
                for x in range(2):
                    for y in range(2):
                        tn+=Rectangle(width=0.2,height=0.2,fill_color=GRAY,fill_opacity=1).move_to([x+.5,y+.5,0])

                tn+=VGroup(Line([2.5,1,0],[3.5,1,0],color=RED).shift(0.5*RIGHT),
                    Line([3,0.5,0],[3,1.5,0],color=BLUE).shift(0.5*RIGHT),
                    Rectangle(width=0.2,height=0.2,fill_color=GRAY,fill_opacity=1).move_to([3.5,1,0]),
                    MyTex("$x_1$",color=BLUE).move_to([3,1.7,0]).shift(0.5*RIGHT).scale(0.75),
                    MyTex("$x_2$",color=BLUE).move_to([3,.3,0]).shift(0.5*RIGHT).scale(0.75),
                    MyTex("$z_1$",color=RED).move_to([2.3,1,0]).shift(0.5*RIGHT).scale(0.75),
                    MyTex("$z_2$",color=RED).move_to([3.7,1,0]).shift(0.5*RIGHT).scale(0.75),
                    MyTex("=p(E",r"X^{x_1+x_2}",r"Z^{z_1+z_2}",r")",tex_environment="align*").move_to([3.5,-0.2,0]).shift(0.5*RIGHT).scale(0.75)
                    ).scale(0.75)
                tn[-1][-1][1].set_color(BLUE)
                tn[-1][-1][2].set_color(RED)


                tc.scale(1.25).next_to(3.5*LEFT+1.5*UP,DOWN)
                tn.scale(1.25).next_to(3*RIGHT+1.5*UP,DOWN)

                self.play(Write(tc))
                self.slide_break()

                self.play(TransformFromCopy(tc,tn[:-1]))
                self.slide_break()

                self.play(Write(tn[-1]))
                self.slide_break()

                self.play(FadeOut(tn),FadeOut(tc))

            if subsec2:
                a=1.5     # lattice spacing
                r=.75   # MPS square radius
                w=5   # thinner line thickness
                ww=20  # thicker line thickness

                MPS1=Group(
                    Line(2*a*LEFT,2*a*RIGHT),
                    Line(-2*a*RIGHT,-2*a*RIGHT+UP,stroke_width=w),
                    Line(-1*a*RIGHT,-1*a*RIGHT+UP,stroke_width=w),
                    Line( 0*a*RIGHT, 0*a*RIGHT+UP,stroke_width=w),
                    Line(+1*a*RIGHT,+1*a*RIGHT+UP,stroke_width=w),
                    Line(+2*a*RIGHT,+2*a*RIGHT+UP,stroke_width=w),
                    Square(r).set_fill("#9999ff",opacity=1).move_to(-2*a*RIGHT),
                    Square(r).set_fill("#9999ff",opacity=1).move_to(-1*a*RIGHT),
                    Square(r).set_fill("#9999ff",opacity=1).move_to( 0*a*RIGHT),
                    Square(r).set_fill("#9999ff",opacity=1).move_to(+1*a*RIGHT),
                    Square(r).set_fill("#9999ff",opacity=1).move_to(+2*a*RIGHT),
                    MyTex("Matrix Product State").move_to(DOWN)
                ).move_to(DOWN)

                self.play(FadeIn(MPS1[6:-1]))
                self.add_foreground_mobjects(MPS1[6:-1])
                self.play(FadeIn(MPS1[:6]))
                self.slide_break()

                self.play(FadeIn(MPS1[-1]))
                self.slide_break()

                bonds=Group(
                    MyTex("Bonds").move_to(UP).set_color(YELLOW),
                    Triangle(color=YELLOW).scale(0.2).set_fill(YELLOW,opacity=1).rotate(60*DEGREES).move_to(-1.5*a*RIGHT-0.5*UP),
                    Triangle(color=YELLOW).scale(0.2).set_fill(YELLOW,opacity=1).rotate(60*DEGREES).move_to(-0.5*a*RIGHT-0.5*UP),
                    Triangle(color=YELLOW).scale(0.2).set_fill(YELLOW,opacity=1).rotate(60*DEGREES).move_to(+0.5*a*RIGHT-0.5*UP),
                    Triangle(color=YELLOW).scale(0.2).set_fill(YELLOW,opacity=1).rotate(60*DEGREES).move_to(+1.5*a*RIGHT-0.5*UP),
                )
                self.play(FadeIn(bonds[0]),FadeIn(bonds[1:],shift=DOWN))
                self.slide_break()


                self.remove_foreground_mobjects(MPS1[6:-1])

                self.play(FadeOut(MPS1),FadeOut(bonds))
                self.slide_break()

            if subsec3:
                a=1.25     # lattice spacing
                r=.5   # MPS square radius
                g=0.1   # gap between multi-edges

                # Square(r).set_fill("#9999ff",opacity=1).move_to(+2*a*RIGHT),

                TN_ten=Group(*[
                    Group(*[
                        Square(r).set_fill("#ff9999",opacity=1).move_to([i*a,j*a,0])
                    for j in range(4)])
                for i in range(4)])
                TN_ver=Group(*[Line([0,i*a,0],[3*a,i*a,0]) for i in range(4)])
                TN_hor=Group(*[Line([j*a,0,0],[j*a,3*a,0]) for j in range(4)])

                self.add_foreground_mobjects(TN_ten)

                TN=Group(TN_ten,TN_hor,TN_ver).move_to(DOWN/2)

                self.play(FadeIn(TN[0]))
                self.play(FadeIn(TN[1]),FadeIn(TN[2]))
                self.slide_break()

                self.play(Indicate(TN_ten[0],scale=1.1))
                self.slide_break()

                MPS=Group(*[
                    Square(r).set_fill("#9999ff",opacity=1).move_to([0,j*a,0])
                for j in range(4)]).move_to(TN_ten[0])
                self.play(ReplacementTransform(TN_ten[0],MPS))
                self.slide_break()

                # self.play(Circumscribe(MPS))
                # self.slide_break()
                #
                # self.play(Circumscribe(TN_ten[1:]))
                # self.slide_break()

                self.play( *[Circumscribe(Group(MPS[j],TN_ten[1][j]),run_time=2) for j in range(4)] )
                # for j in range(4):
                #     self.play(Circumscribe(Group(
                #         MPS[3-j],
                #         TN_ten[1][3-j]
                #     )))
                self.slide_break()

                self.play(
                    MPS[0].animate.set_fill("#ff66ff"),
                    MPS[1].animate.set_fill("#ff66ff"),
                    MPS[2].animate.set_fill("#ff66ff"),
                    MPS[3].animate.set_fill("#ff66ff"),
                    FadeOut(TN_ten[1],target_position=MPS),
                    TN_hor[1].animate.shift((a-g)*LEFT),
                    TN_hor[0].animate.shift(g*LEFT),
                )
                self.slide_break()

                bondarrows=Group(*[
                    Triangle(color=YELLOW).scale(0.2).set_fill(YELLOW,opacity=1).rotate(-30*DEGREES).move_to(i*a*UP)
                for i in range(3)]).move_to(MPS).shift(0.5*RIGHT)

                self.play(FadeIn(bondarrows,shift=LEFT))
                self.slide_break()

                self.play(FadeOut(bondarrows))
                self.slide_break()

                self.play(
                    MPS[0].animate.set_fill("#9999ff"),
                    MPS[1].animate.set_fill("#9999ff"),
                    MPS[2].animate.set_fill("#9999ff"),
                    MPS[3].animate.set_fill("#9999ff"),
                    TN_hor[1].animate.shift(g*LEFT),
                    TN_hor[0].animate.shift(g*RIGHT),
                )
                self.remove(TN_hor[1])
                self.slide_break()


                self.play(
                    MPS[0].animate.set_fill("#ff66ff"),
                    MPS[1].animate.set_fill("#ff66ff"),
                    MPS[2].animate.set_fill("#ff66ff"),
                    MPS[3].animate.set_fill("#ff66ff"),
                    FadeOut(TN_ten[2],target_position=MPS),
                    TN_hor[2].animate.shift((2*a-g)*LEFT),
                    TN_hor[0].animate.shift(g*LEFT),
                )
                self.slide_break()
                self.play(
                    MPS[0].animate.set_fill("#9999ff"),
                    MPS[1].animate.set_fill("#9999ff"),
                    MPS[2].animate.set_fill("#9999ff"),
                    MPS[3].animate.set_fill("#9999ff"),
                    TN_hor[2].animate.shift(g*LEFT),
                    TN_hor[0].animate.shift(g*RIGHT),
                )
                self.remove(TN_hor[2])
                self.slide_break()

                self.play(
                    MPS[0].animate.set_fill("#ff66ff"),
                    MPS[1].animate.set_fill("#ff66ff"),
                    MPS[2].animate.set_fill("#ff66ff"),
                    MPS[3].animate.set_fill("#ff66ff"),
                    FadeOut(TN_ten[3],target_position=MPS),
                    TN_hor[3].animate.shift((3*a-g)*LEFT),
                    TN_hor[0].animate.shift(g*LEFT),
                    Uncreate(TN_ver[0]),
                    Uncreate(TN_ver[1]),
                    Uncreate(TN_ver[2]),
                    Uncreate(TN_ver[3]),
                )
                self.slide_break()
                self.play(
                    MPS[0].animate.set_fill("#9999ff"),
                    MPS[1].animate.set_fill("#9999ff"),
                    MPS[2].animate.set_fill("#9999ff"),
                    MPS[3].animate.set_fill("#9999ff"),
                    TN_hor[3].animate.shift(g*LEFT),
                    TN_hor[0].animate.shift(g*RIGHT),
                )
                self.remove(TN_hor[3])
                self.slide_break()


                self.play(
                    FadeOut(MPS[3],target_position=MPS[2]),
                    FadeOut(MPS[0],target_position=MPS[1]),
                    TN_hor[0].animate.scale(0.5)
                )
                self.slide_break()

                res_ten=Square(r).set_fill("#9999ff",opacity=1).move_to(MPS[1]).shift(a*UP/2)

                self.play(
                    FadeOut(MPS[1],target_position=res_ten),
                    FadeOut(MPS[2],target_position=res_ten),
                    FadeIn(res_ten),
                    TN_hor[0].animate.scale(0)
                )
                self.remove(TN_hor[0])
                self.slide_break()

                self.play(res_ten.animate.shift(1.5*a*RIGHT))
                self.slide_break()

                self.play(FadeOut(res_ten))

            if subsec4:

                x=[3,1,5,2,0,6,4]
                y=[0,1,2,3,4,5,6]
                e=[(0,1),(0,2),(1,3),(1,4),(2,3),(2,5),(3,4),(3,5),(3,6),(4,6),(5,6)]
                sweep_l=DashedLine([-7*.75,-3.5*.75-.5,0],[-7*.75,3.5*.75-.5,0], dash_length=0.25*.75)
                sweep_t=Group(*[
                    Circle(0.25,color=WHITE).set_fill("#ff9999",opacity=1).move_to([.75*1.5*(y[i]-3),.75*.9*(x[i]-3)-.5,0])
                for i in range(7)])
                sweep_e=Group(*[
                    Line([.75*1.5*(y[ee[0]]-3),.75*(x[ee[0]]-3)-.5,0],[.75*1.5*(y[ee[1]]-3),.75*.9*(x[ee[1]]-3)-.5,0])
                for ee in e])


                self.play(FadeIn(sweep_t))
                self.add_foreground_mobjects(sweep_t)
                self.play(FadeIn(sweep_e))
                self.slide_break()

                self.play(FadeIn(sweep_l.shift(RIGHT/2),shift=RIGHT/2))
                self.slide_break()

                self.play(sweep_l.animate.shift(1.375*RIGHT))
                self.slide_break()

                new_ten=Circle(0.25,color=WHITE).set_fill("#ff66ff",opacity=1).move_to([-4.5,-0.5,0])

                self.play(
                    ReplacementTransform(sweep_t[0],new_ten),
                    Transform(sweep_e[0],Line(new_ten.get_center(),sweep_e[0].end)),
                    Transform(sweep_e[1],Line(new_ten.get_center(),sweep_e[1].end)),
                )
                self.slide_break()
                mps=VGroup(
                    Line([-4.5,-0.5-.25,0],[-4.5,-0.5+.25,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+.5,0]),
                )
                self.play(
                    ReplacementTransform(new_ten,mps),
                    Transform(sweep_e[0],Line(mps[1].get_right(),sweep_e[0].end)),
                    Transform(sweep_e[1],Line(mps[2].get_right(),sweep_e[1].end)),
                )
                self.slide_break()


                self.play(sweep_l.animate.shift(1.125*RIGHT))
                self.slide_break()
                self.play(
                    Uncreate(sweep_e[0]),
                    Transform(mps[1],Circle(0.25,color=WHITE).set_fill("#ff66ff",opacity=1).move_to(mps[1])),
                    FadeOut(sweep_t[1],target_position=mps[1]),
                    Transform(sweep_e[2],Line([-4.5,-0.5-.5,0],sweep_e[2].end)),
                    Transform(sweep_e[3],Line([-4.5,-0.5-.5,0],sweep_e[3].end)),
                )
                self.slide_break()
                oldmps=mps
                mps=VGroup(
                    Line([-4.5,-0.5-1,0],[-4.5,-0.5+1,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-1,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5  ,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+1,0]),
                )
                self.play(
                    ReplacementTransform(oldmps[0],mps[0]),
                    ReplacementTransform(oldmps[1],mps[1:3]),
                    ReplacementTransform(oldmps[2],mps[3]),
                    Transform(sweep_e[1],Line(mps[3].get_right(),sweep_e[1].end)),
                    Transform(sweep_e[2],Line(mps[2].get_right(),sweep_e[2].end)),
                    Transform(sweep_e[3],Line(mps[1].get_right(),sweep_e[3].end)),
                )
                self.slide_break()


                self.play(sweep_l.animate.shift(1.125*RIGHT))
                self.slide_break()
                self.play(
                    Uncreate(sweep_e[1]),
                    Transform(mps[3],Circle(0.25,color=WHITE).set_fill("#ff66ff",opacity=1).move_to(mps[3])),
                    FadeOut(sweep_t[2],target_position=mps[3]),
                    Transform(sweep_e[4],Line(mps[3].get_center(),sweep_e[4].end)),
                    Transform(sweep_e[5],Line(mps[3].get_center(),sweep_e[5].end)),
                )
                self.slide_break()
                oldmps=mps
                mps=VGroup(
                    Line([-4.5,-0.5-1.5,0],[-4.5,-0.5+1.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-1.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-0.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+0.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+1.5,0]),
                )
                self.play(
                    ReplacementTransform(oldmps[0],mps[0]),
                    ReplacementTransform(oldmps[1],mps[1]),
                    ReplacementTransform(oldmps[2],mps[2]),
                    ReplacementTransform(oldmps[3],mps[3:5]),
                    Transform(sweep_e[5],Line(mps[4].get_right(),sweep_e[5].end)),
                    Transform(sweep_e[4],Line(mps[3].get_right(),sweep_e[4].end)),
                    Transform(sweep_e[2],Line(mps[2].get_right(),sweep_e[2].end)),
                    Transform(sweep_e[3],Line(mps[1].get_right(),sweep_e[3].end)),
                )
                self.slide_break()

                self.play(sweep_l.animate.shift(1.125*RIGHT))
                self.slide_break()
                self.play(
                    Uncreate(sweep_e[4]),
                    Uncreate(sweep_e[2]),
                    Transform(mps[2:4],Circle(0.25,color=WHITE).set_fill("#ff66ff",opacity=1).move_to(mps[3]).shift(0.5*DOWN)),
                    FadeOut(sweep_t[3],target_position=mps[3]),
                    Transform(sweep_e[6],Line(mps[3].get_center()+0.5*DOWN,sweep_e[6].end)),
                    Transform(sweep_e[7],Line(mps[3].get_center()+0.5*DOWN,sweep_e[7].end)),
                    Transform(sweep_e[8],Line(mps[3].get_center()+0.5*DOWN,sweep_e[8].end)),
                )
                self.slide_break()
                oldmps=mps
                mps=VGroup(
                    Line([-4.5,-0.5-2,0],[-4.5,-0.5+2,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-2,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-1,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5  ,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+1,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+2,0]),
                )
                self.play(
                    ReplacementTransform(oldmps[0],mps[0]),
                    ReplacementTransform(oldmps[1],mps[1]),
                    ReplacementTransform(oldmps[2],mps[2:5]),
                    ReplacementTransform(oldmps[4],mps[5]),
                    Transform(sweep_e[5],Line(mps[5].get_right(),sweep_e[5].end)),
                    Transform(sweep_e[7],Line(mps[4].get_right(),sweep_e[7].end)),
                    Transform(sweep_e[8],Line(mps[3].get_right(),sweep_e[8].end)),
                    Transform(sweep_e[6],Line(mps[2].get_right(),sweep_e[6].end)),
                    Transform(sweep_e[3],Line(mps[1].get_right(),sweep_e[3].end)),
                )
                self.slide_break()

                self.play(sweep_l.animate.shift(1.125*RIGHT))
                self.slide_break()
                self.play(
                    Uncreate(sweep_e[3]),
                    Uncreate(sweep_e[6]),
                    Transform(mps[1:3],Circle(0.25,color=WHITE).set_fill("#ff66ff",opacity=1).move_to(mps[1])),
                    FadeOut(sweep_t[4],target_position=mps[1]),
                    Transform(sweep_e[9],Line(mps[1].get_center(),sweep_e[9].end)),
                )
                self.slide_break()
                oldmps=mps
                mps=VGroup(
                    Line([-4.5,-0.5-1.5,0],[-4.5,-0.5+1.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-1.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-0.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+0.5,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+1.5,0]),
                )
                self.play(
                    ReplacementTransform(oldmps,mps),
                    Transform(sweep_e[5],Line(mps[4].get_right(),sweep_e[5].end)),
                    Transform(sweep_e[7],Line(mps[3].get_right(),sweep_e[7].end)),
                    Transform(sweep_e[8],Line(mps[2].get_right(),sweep_e[8].end)),
                    Transform(sweep_e[9],Line(mps[1].get_right(),sweep_e[9].end)),
                )
                self.slide_break()


                self.play(sweep_l.animate.shift(1.125*RIGHT))
                self.slide_break()
                self.play(
                    Uncreate(sweep_e[5]),
                    Uncreate(sweep_e[7]),
                    Transform(mps[3:5],Circle(0.25,color=WHITE).set_fill("#ff66ff",opacity=1).move_to(mps[4])),
                    FadeOut(sweep_t[5],target_position=mps[4]),
                    Transform(sweep_e[10],Line(mps[4].get_center(),sweep_e[10].end)),
                )
                self.slide_break()
                oldmps=mps
                mps=VGroup(
                    Line([-4.5,-0.5-1,0],[-4.5,-0.5+1,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5-1,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5  ,0]),
                    Square(0.75*.75,color=WHITE).set_fill("#9999ff",opacity=1).move_to([-4.5,-0.5+1,0]),
                )
                self.play(
                    ReplacementTransform(oldmps[0],mps[0]),
                    ReplacementTransform(oldmps[1],mps[1]),
                    ReplacementTransform(oldmps[2],mps[2]),
                    ReplacementTransform(oldmps[3],mps[3]),
                    Transform(sweep_e[10],Line(mps[3].get_right(),sweep_e[10].end)),
                    Transform(sweep_e[8],Line(mps[2].get_right(),sweep_e[8].end)),
                    Transform(sweep_e[9],Line(mps[1].get_right(),sweep_e[9].end)),
                )
                self.slide_break()


                self.play(sweep_l.animate.shift(1.125*RIGHT))
                self.slide_break()
                self.play(
                    Uncreate(sweep_e[10]),
                    Uncreate(sweep_e[8]),
                    Uncreate(sweep_e[9]),
                    Transform(mps,Circle(0.25,color=WHITE).set_fill("#ff66ff",opacity=1).move_to(mps[2])),
                    FadeOut(sweep_t[6],target_position=mps[1]),
                )
                self.slide_break()

                self.play(FadeOut(sweep_l,shift=0.5*RIGHT),mps.animate.move_to(DOWN/2))
                self.slide_break()
                self.remove(sweep_l)

                self.play(FadeOut(mps))
                self.slide_break()

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

class Extensions(SlideScene):
        def construct(self):
            tocindex=8
            heading = toc[tocindex].copy()
            self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
            self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
            self.slide_break()

            subsec1=False
            subsec2=False
            subsec3=False
            subsec4=False

            subsec1=True
            subsec2=True
            subsec3=True
            subsec4=True

            if subsec1:
                # Phen.

                rep_lines=VGroup()
                rep_qubits=VGroup()
                anc_qubits=VGroup()
                anc_lines=VGroup()

                d=8
                t=5
                for tt in range(t):
                    rep_lines+=Line([0,tt,0],[d-1,tt,0]).set_opacity(0.5)
                    rep_qubits+=VGroup()
                    for x in range(d):
                        rep_qubits[-1]+=Circle(radius=0.1,color=WHITE,fill_opacity=1).move_to([x,tt,0])
                for tt in range(t-1):
                    for x in range(d-1):
                        # anc_qubits+=Circle(radius=0.1,color="#161c20",fill_opacity=1).move_to([x+0.5,tt+0.5,0])
                        anc_lines+=Line([x+1,tt+1,0],[x,tt,0],stroke_opacity=0.5)
                        anc_lines+=Line([x,tt+1,0],[x+1,tt,0],stroke_opacity=0.5)
                        anc_qubits+=Circle(radius=0.1,color=WHITE,fill_color="#161c20",fill_opacity=1).move_to([x+0.5,tt+0.5,0])

                check=VGroup(
                    Line([3,2,0],[4,2,0],stroke_width=10),
                    Circle(radius=0.15,fill_opacity=1).move_to([3,2,0]),
                    Circle(radius=0.15,fill_opacity=1).move_to([4,2,0]),
                    MyTex("X").move_to([3,2.5,0]),
                    MyTex("X").move_to([4,2.5,0])
                ).set_color(RED).shift(2*LEFT)

                check2=VGroup(
                    Line([3,2,0],[3.5,2.5,0],stroke_width=10,color=RED),
                    Line([3.5,2.5,0],[4,2,0],stroke_width=10,color=RED),
                    Line([3,2,0],[3.5,1.5,0],stroke_width=10,color=RED),
                    Line([3.5,1.5,0],[4,2,0],stroke_width=10,color=RED),
                    Circle(radius=0.15,fill_opacity=1,color=RED).move_to([3,2,0]),
                    Circle(radius=0.15,fill_opacity=1,color=RED).move_to([4,2,0]),
                    Circle(radius=0.15,stroke_color=RED,stroke_width=8,fill_color="#161c20",fill_opacity=1).move_to([3.5,2.5,0]),
                    Circle(radius=0.15,stroke_color=RED,stroke_width=8,fill_color="#161c20",fill_opacity=1).move_to([3.5,1.5,0]),
                    MyTex("X",color=RED).move_to([3,2.5,0]),
                    MyTex("X",color=RED).move_to([4,2.5,0]),
                    MyTex("X",color=RED).move_to([3.5,3,0]),
                    MyTex("X",color=RED).move_to([3.5,2,0]),
                ).shift(2*LEFT)

                gauge=VGroup(
                    Line([3,2,0],[3.5,2.5,0],stroke_width=10,color=BLUE),
                    Line([3.5,2.5,0],[4,2,0],stroke_width=10,color=BLUE),
                    Line([3,2,0],[3.5,1.5,0],stroke_width=10,color=BLUE),
                    Line([3.5,1.5,0],[4,2,0],stroke_width=10,color=BLUE),
                    Circle(radius=0.15,stroke_color=BLUE,stroke_width=8,fill_color="#161c20",fill_opacity=1).move_to([3,2,0]),
                    Circle(radius=0.15,stroke_color=BLUE,stroke_width=8,fill_color="#161c20",fill_opacity=1).move_to([4,2,0]),
                    Circle(radius=0.15,fill_opacity=1,color=BLUE).move_to([3.5,2.5,0]),
                    Circle(radius=0.15,fill_opacity=1,color=BLUE).move_to([3.5,1.5,0]),
                    MyTex("Z",color=BLUE).move_to([3,2.5,0]),
                    MyTex("Z",color=BLUE).move_to([4,2.5,0]),
                    MyTex("Z",color=BLUE).move_to([3.5,3,0]),
                    MyTex("Z",color=BLUE).move_to([3.5,2,0]),
                ).shift(0.5*RIGHT+0.5*UP)

                VGroup(rep_lines,rep_qubits,anc_lines,anc_qubits,check,check2,gauge).move_to(ORIGIN)

                self.play(Write(rep_lines[2]))
                self.play(Write(rep_qubits[2]))
                self.slide_break()

                self.play(Write(check))
                self.slide_break()

                # self.play(FadeOut(check[3:]))
                # self.slide_break()
                # check=check[0:3]

                self.play(
                    FadeIn(VGroup(rep_lines[1],rep_qubits[1]),shift=UP),
                    FadeIn(VGroup(rep_lines[3],rep_qubits[3]),shift=DOWN),
                )
                self.play(
                    FadeIn(VGroup(rep_lines[0],rep_qubits[0]),shift=UP),
                    FadeIn(VGroup(rep_lines[4],rep_qubits[4]),shift=DOWN),
                )
                self.slide_break()

                self.play(Write(anc_qubits))
                self.add_foreground_mobjects(anc_qubits)
                self.slide_break()

                self.play(FadeOut(rep_lines),FadeIn(anc_lines),FadeOut(check))
                self.remove_foreground_mobjects(anc_qubits)
                self.slide_break()
                self.play(Write(check2))
                self.slide_break()

                self.play(Write(gauge))
                self.slide_break()

                self.play(
                    FadeOut(anc_lines),
                    FadeOut(check2),
                    FadeOut(gauge),
                    FadeOut(rep_qubits),
                    FadeOut(anc_qubits),
                )
                self.slide_break()

            if subsec2:
                #
                sc_lines=VGroup()
                sc_qubits=VGroup()
                anc_qubits=VGroup()
                anc_lines=VGroup()

                d=3
                t=5
                for tt in range(t):
                    sc_lines+=VGroup()
                    for i in range(d+1):
                        sc_lines[-1]+=Line([i,0,tt],[i,d,tt],stroke_opacity=0.5)
                        sc_lines[-1]+=Line([0,i,tt],[d,i,tt],stroke_opacity=0.5)

                for x in range(d+1):
                    for y in range(d+1):
                        anc_lines+=Line([x,y,0],[x,y,t-1],stroke_opacity=0.25)

                check2=VGroup(
                    Line(LEFT,RIGHT,stroke_width=10,color=RED),
                    Line(DOWN,UP,stroke_width=10,color=RED),
                    Line(IN,OUT,stroke_width=10,color=RED),
                ).shift(UP+RIGHT+2*OUT)

                gauge=VGroup(
                    Line(ORIGIN,RIGHT,stroke_width=10,color=RED),
                    Line(RIGHT+IN,IN,stroke_width=10,color=RED),
                    Line(RIGHT,RIGHT+IN,stroke_width=10,color=RED),
                    Line(ORIGIN,IN,stroke_width=10,color=RED),
                ).set_color(BLUE).shift(2*UP+2*RIGHT+3*OUT)

                gauge2=VGroup(
                    Line(ORIGIN,RIGHT,stroke_width=10,color=RED),
                    Line(RIGHT,RIGHT+UP,stroke_width=10,color=RED),
                    Line(RIGHT+UP,UP,stroke_width=10,color=RED),
                    Line(ORIGIN,UP,stroke_width=10,color=RED),
                ).set_color(BLUE).shift(2*UP+2*RIGHT+1*OUT)


                VGroup(check2,sc_lines,anc_lines,gauge,gauge2).move_to(ORIGIN)
                self.play(Write(sc_lines[2]),Write(check2[0:2]))
                self.slide_break()

                self.play(VGroup(sc_lines[2],sc_qubits,check2[0:2]).animate.rotate(0.3,axis=IN).rotate(1.35,axis=LEFT))

                VGroup(sc_lines[0:2],sc_lines[3:],anc_qubits,anc_lines,check2[2],gauge,gauge2).rotate(0.3,axis=IN).rotate(1.35,axis=LEFT)
                self.slide_break()

                self.play(
                    FadeIn(sc_lines[1],shift=UP),
                    FadeIn(sc_lines[3],shift=DOWN)
                )
                self.play(
                    FadeIn(sc_lines[0],shift=UP),
                    FadeIn(sc_lines[4],shift=DOWN)
                )
                self.slide_break()

                self.play(FadeIn(anc_lines))
                self.slide_break()
                self.play(FadeOut(anc_lines))
                self.slide_break()

                self.play(Write(check2[2]))
                self.slide_break()

                self.play(Write(gauge2))
                self.slide_break()

                self.play(Write(gauge[0:2]))
                self.slide_break()

                self.play(Write(gauge[2:]))
                self.slide_break()

                self.play(FadeOut(Group(gauge,gauge2,check2,sc_lines)))
                self.slide_break()

            if subsec3:
                # Correlated noise

                corr_text=MyTex("What about correlated noise models?")
                self.play(Write(corr_text))
                self.slide_break()

                self.play(corr_text.animate.shift(1.5*UP))
                self.slide_break()

                # err=MyTex(r"$\Pr\left(\bigo\right)$What about correlated noise models?")

                paulitoprob=MathTex("\\text{Error}","\\to","\\text{Probability}").move_to(0.5*DOWN)
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

                # self.remove(iid,corr,pauli)
                # self.play(corr_text.animate.shift(UP),paulitoprob.animate.shift(2*UP))
                self.play(FadeOut(corr_text),FadeOut(paulitoprob))
                self.slide_break()

                corr_example=VGroup(VGroup(),VGroup(),VGroup())
                for i in range(5):
                    corr_example[0]+=Circle(radius=0.1,color=WHITE,fill_opacity=1).move_to(i*RIGHT)
                for i in range(5):
                    corr_example[0]+=MyTex(str(i+1)).move_to(i*RIGHT+0.75*UP)
                corr_example[1]+=Circle(radius=0.375,color=RED)
                corr_example[1]+=MyTex("$p_1$").move_to(0.75*DOWN).set_color(RED)

                corr_example[2]+=Ellipse(width=1.5,height=.75,color=RED).move_to(2.5*RIGHT)
                corr_example[2]+=MyTex("$\phi_{34}$").move_to(2.5*RIGHT+0.75*DOWN).set_color(RED)

                corr_example.move_to(ORIGIN)

                self.play(FadeIn(corr_example[0]))
                self.slide_break()

                self.play(Write(corr_example[1]))
                self.slide_break()

                corr_example2=VGroup(
                    MyTex(r"\text{iid: }","p_1(","E_1",r")\,p_2(","E_2",r")\,p_3(","E_3",r")\,p_4(","E_4",r")\,p_5(","E_5",")",tex_environment="align*"),
                    MyTex(r"\text{corr: }",r"\phi_{1,2}(","E_1,E_2",r")\,\phi_{2,3}(","E_2,E_3",r")\,\phi_{3,4}(","E_3,E_4",r")\,\phi_{4,5}(","E_4,E_5",")",tex_environment="align*")
                ).arrange(DOWN,aligned_edge=LEFT).move_to(1.5*DOWN)
                corr_example2[0][1].set_color(RED)
                corr_example2[0][3].set_color(RED)
                corr_example2[0][5].set_color(RED)
                corr_example2[0][7].set_color(RED)
                corr_example2[0][9].set_color(RED)
                corr_example2[0][11].set_color(RED)
                corr_example2[0][2].set_color(YELLOW)
                corr_example2[0][4].set_color(YELLOW)
                corr_example2[0][6].set_color(YELLOW)
                corr_example2[0][8].set_color(YELLOW)
                corr_example2[0][10].set_color(YELLOW)

                corr_example2[1][1].set_color(RED)
                corr_example2[1][3].set_color(RED)
                corr_example2[1][5].set_color(RED)
                corr_example2[1][7].set_color(RED)
                corr_example2[1][9].set_color(RED)
                corr_example2[1][2].set_color(YELLOW)
                corr_example2[1][4].set_color(YELLOW)
                corr_example2[1][6].set_color(YELLOW)
                corr_example2[1][8].set_color(YELLOW)

                self.play(corr_example[0:2].animate.shift(UP))
                corr_example[2].shift(UP)
                self.play(Write(corr_example2[0]))
                self.slide_break()

                self.play(Write(corr_example[2]))
                self.slide_break()

                self.play(Write(corr_example2[1]))
                self.slide_break()

                self.play(FadeOut(corr_example),FadeOut(corr_example2))
                self.slide_break()

                ham = MyTex(
                    r"H_E(\vec s):=-",r"\sum_{i}",r"\sum_{\sigma\in\mathcal P_{i\vphantom{R}}}",r"J_i",r"(\sigma)\comm{\sigma}{E}\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*"
                )

                self.play(Write(ham))
                self.slide_break()

                self.play(
                    ham[1:4].animate.set_color(YELLOW),
                )
                self.slide_break()

                oldham=ham
                ham = MyTex(
                    r"H_E(\vec s):=-",r"\sum_{j}",r"\sum_{\sigma\in\mathcal P_{R_j}}",r"J_j",r"(\sigma)\comm{\sigma}{E}\prod_{ k:\comm{\sigma}{S_k}=-1 } s_k",
                    tex_environment="align*"
                ).move_to(oldham)
                ham[1:4].set_color(YELLOW),
                self.play(
                    ReplacementTransform(oldham[0],ham[0]),
                    ReplacementTransform(oldham[1],ham[1]),
                    ReplacementTransform(oldham[2],ham[2]),
                    ReplacementTransform(oldham[3],ham[3]),
                    ReplacementTransform(oldham[4],ham[4]),
                )
                self.slide_break()

                nish=MyTex(
                    r"\beta ",
                    r"J_j",
                    r"(\sigma)",
                    r"=",
                    r"\frac{1}{\left|\mathcal P_{R_j}\right|}",
                    r"\sum_{\tau\in\mathcal P_{R_j}}",
                    r"\log \phi_j",
                    r"(\tau)",
                    r"\comm{\sigma}{\tau^{-1}}",tex_environment="align*")
                nish.move_to(1*DOWN)

                self.play(ham.animate.shift(1*UP).set_color(WHITE))
                self.play(Write(nish))
                self.slide_break()

                newnish=MyTex(
                    r"\beta ",
                    r"J",
                    r"(\sigma)",
                    r"=",
                    r"\frac{1}{\left|\mathcal P\right|}",
                    r"\sum_{\tau\in\mathcal P}",
                    r"\log \Pr",
                    r"(\tau)",
                    r"\comm{\sigma}{\tau^{-1}}",tex_environment="align*").move_to(nish)
                self.play(Transform(nish,newnish))
                self.slide_break()

                self.play(FadeOut(nish),FadeOut(ham))
                self.slide_break()

            if subsec4:
                lines=VGroup()
                qubits=VGroup()
                spins=VGroup()
                X=7
                Y=4
                for x in range(X):
                    lines+=Line([x,-0.75,0],[x,Y-.25,0],stroke_opacity=0.25)
                for y in range(Y):
                    lines+=Line([-.75,y,0],[X-.25,y,0],stroke_opacity=0.25)

                for x in range(X):
                    for y in range(Y):
                        spins+=Circle(radius=0.1,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to([x,y,0])
                        qubits+=Circle(radius=0.05,fill_opacity=1).move_to([x-0.5,y,0])
                        qubits+=Circle(radius=0.05,fill_opacity=1).move_to([x+0.5,y,0])
                        qubits+=Circle(radius=0.05,fill_opacity=1).move_to([x,y-0.5,0])
                        qubits+=Circle(radius=0.05,fill_opacity=1).move_to([x,y+0.5,0])

                iid=VGroup()
                iid+=Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2)
                iid+=Line(ORIGIN,RIGHT,color=BLUE,stroke_width=10)
                iid+=Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(ORIGIN)
                iid+=Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(RIGHT)
                iid+=Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2)
                iid.shift(2*UP)

                corr1=VGroup(
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT+UP/2),
                    Line(ORIGIN,RIGHT,color=BLUE,stroke_width=10),
                    Line(RIGHT+UP,RIGHT,color=BLUE,stroke_width=10),
                    Line(RIGHT+UP,ORIGIN,color=BLUE,stroke_width=10),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(ORIGIN),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(RIGHT),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(RIGHT+UP),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT+UP/2),
                ).shift(RIGHT)

                corr2=VGroup(
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(DOWN/2),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(UP/2),
                    Line(UP,DOWN,color=BLUE,stroke_width=10),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(ORIGIN),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(UP),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(DOWN),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(DOWN/2),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(UP/2),
                ).shift(3*RIGHT+2*UP)

                corr3=VGroup(
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2+UP),
                    Line(ORIGIN,RIGHT,color=BLUE,stroke_width=10),
                    Line(ORIGIN,UP,color=BLUE,stroke_width=10),
                    Line(UP+RIGHT,RIGHT,color=BLUE,stroke_width=10),
                    Line(UP+RIGHT,UP,color=BLUE,stroke_width=10),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(ORIGIN),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(UP),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(RIGHT),
                    Circle(radius=0.15,stroke_width=10,stroke_color=BLUE,fill_opacity=1,fill_color=config.background_color).move_to(UP+RIGHT),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2),
                    Circle(radius=0.1,color=YELLOW,fill_opacity=1).move_to(RIGHT/2+UP),
                ).shift(5*RIGHT+UP)

                qubits.set_color(WHITE)
                cover=Rectangle(width=5,height=5,color=config.background_color,fill_opacity=1).shift(1.25*LEFT)#.next_to(LEFT,3*RIGHT+3*UP)
                VGroup(lines,qubits,spins,iid,corr1,corr2,corr3).move_to(ORIGIN)
                self.play(Write(VGroup(lines,qubits,spins)))
                self.slide_break()

                self.play(FadeIn(iid[0]))
                self.slide_break()
                self.play(FadeIn(iid[1:]))
                self.slide_break()

                self.play(FadeIn(corr1[0:2]))
                self.slide_break()
                self.play(FadeIn(corr1[2:]))
                self.slide_break()

                self.play(FadeIn(corr2[0:2]))
                self.slide_break()
                self.play(FadeIn(corr2[2:]))
                self.slide_break()

                self.play(FadeIn(corr3[0:2]))
                self.slide_break()
                self.play(FadeIn(corr3[2:]))
                self.slide_break()

                self.play(FadeIn(cover))
                self.remove(*corr1,*corr2,*iid)
                self.play(VGroup(lines,qubits,spins,cover,corr3).animate.shift(2*RIGHT))
                self.slide_break()


                corr_form=MyTex(r"\eta:=\frac{\Pr(X_e|X_{e'})}{\Pr(X_e|I_{e'})}",tex_environment="align*").move_to(UP+RIGHT).scale(.8)
                corr_mc=ImageMobject("corr_mc.png").scale(1).move_to(4*LEFT)
                corr_th=MyTex(r"\eta=1:&~~~10.917(3)\%\\",r"\eta=2:&~~~10.04(6)\%",tex_environment="align*").move_to(RIGHT+DOWN).scale(.8)
                self.play(FadeIn(corr_mc,shift=RIGHT))
                self.play(Write(VGroup(corr_form,corr_th)))
                self.slide_break()

                cover2=Rectangle(fill_color=config.background_color,fill_opacity=1,stroke_color=config.background_color,width=20,height=6)
                self.play(FadeIn(cover2))
                self.remove(
                    lines,qubits,spins,corr3,corr_mc,corr_form,corr_th,cover2,cover
                )

            self.play(FadeIn(toc[0:tocindex]),FadeIn(toc[tocindex+1:]), ReplacementTransform(heading,toc[tocindex]))

# class Conclusion(SlideScene):
#     def construct(self):
#         tocindex=-1
#         heading = toc[tocindex].copy()
#         self.add(toc[0:tocindex],heading,toc[tocindex+1:],footer)
#         self.play(FadeOut(toc[0:tocindex]),FadeOut(toc[tocindex+1:]), heading.animate.move_to(ORIGIN).scale(1.5).to_corner(UP))
#         self.slide_break()
#
#         temp = MyTexTemplate()
#         temp.add_to_preamble(r"\usepackage{marvosym} \usepackage{fontawesome}")
#
#         summary=MyTex("Summary of ","what ","is ","going on").scale(.75).move_to([0,2,0])
#         summary[1].set_color(YELLOW)
#         summary[3].set_color(RED)
#
#         arxiv=MyTex(r"\texttt{\bfseries arXiv:~????.?????}").next_to(summary,DOWN,buff=1).scale(.8)
#         package=MyTex(r"\texttt{\bfseries github:~chubbc/manim\_slides}").next_to(arxiv,DOWN,buff=.25).scale(.8)
#
#         email=MyTex(r"\faEnvelope~~\texttt{me@christopherchubb.com}", tex_template=temp)
#         website=MyTex(r"\faLink~~\texttt{christopherchubb.com}", tex_template=temp)
#         twitter=MyTex(r"\faTwitter~~\texttt{@QuantumChubb}", tex_template=temp)
#         github=MyTex(r"\faGithub~~\texttt{chubbc}", tex_template=temp)
#         socials=VGroup(github,twitter,website,email).arrange(DOWN).scale(0.75).shift(2*DOWN)
#
#         self.play(Write(summary))
#         self.slide_break()
#         self.play(Write(arxiv),Write(package))
#         self.slide_break()
#         self.play(Write(socials))
#         self.slide_break()
