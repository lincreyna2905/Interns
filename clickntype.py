from graphics import*

def main():
    win = GraphWin("CLick and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)
        
main()