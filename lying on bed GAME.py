from graphics import *

def main():

    win = GraphWin("Hospital room", 500 , 500)
    win.setBackground('black')
    bed = Rectangle(Point(490,160), Point(250,490))
    bed.setFill('White')
    bed.draw(win)

    bedsheet = Rectangle(Point(480,170), Point(260,480))
    bedsheet.setFill('blue')
    bedsheet.draw(win)

    pillow = Rectangle(Point(445,400), Point(300,465))
    pillow.setFill('dark blue')
    pillow.draw(win)

    desk = Rectangle(Point(265,15), Point(480,30))
    desk.setFill('White')
    desk.draw(win)

    deskright = Rectangle(Point(465,30), Point(480,100))
    deskright.setFill('White')
    deskright.draw(win)
    deskleft = Rectangle(Point(280,30), Point(265,100))
    deskleft.setFill('White')
    deskleft.draw(win)

    deskcolor = Rectangle(Point(280, 15), Point(265, 100))
    deskcolor.setFill('brown')
    deskcolor.draw(win)
    deskcolor = Rectangle(Point(260, 15), Point(480, 100))
    deskcolor.setFill('brown')
    deskcolor.draw(win)
    centre = Point(0, 0)
    circ = Circle(centre, 110)
    circ.setFill('gainsboro')
    circ.draw(win)
    door = Rectangle(Point(109,15), Point(0,0))
    door.setFill('grey')
    door.draw(win)
    drawer = Rectangle(Point(280, 100), Point(360, 110))
    drawer.setFill('White')
    drawer.draw(win)
    centre = Point(323,105)
    circ = Circle(centre, 3)
    circ.setFill('brown')
    circ.draw(win)


    win.getMouse()
    win.close()

main()










