from window import Window, Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(0, 0), Point(100, 100))
    win.draw_line(line, "black")
    win.wait_for_close()

main()