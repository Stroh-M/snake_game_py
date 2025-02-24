import curses
import time
import random

def main(stdcr):
    stdcr.clear()
    curses.curs_set(0)
    stdcr.nodelay(True)
    stdcr.border()
    
    height, width = stdcr.getmaxyx()
    direction = (0, 1)
        
    yrandom = random.randrange(0, height)
    xrandom = random.randrange(0, width)
    
    y = height // 2
    x = width // 2
    
    snakePositions = [(y, x)]
    
    while True:
        
        stdcr.clear()
        for i in range(len(snakePositions)):
            stdcr.addstr(snakePositions[i][0], snakePositions[i][1], "#")
        stdcr.addstr(yrandom, xrandom, "*")
        stdcr.refresh()
        
        time.sleep(0.10)
        
        if y == yrandom and x == xrandom:
            yrandom = random.randrange(0, height)
            xrandom = random.randrange(0, width)
        else:
            snakePositions.pop(-1)
        
        y += direction[0]
        x += direction[1]
        snakePositions.insert(0, (y, x))
        
        key = stdcr.getch()
        if key == curses.KEY_DOWN and direction != (-1, 0):
            direction = (1, 0)
        elif key == curses.KEY_UP and direction != (1, 0):
            direction = (-1 ,0 )
        elif key == curses.KEY_RIGHT and direction != (0, -1):
            direction = (0, 1)
        elif key == curses.KEY_LEFT and direction != (0, 1):
            direction = (0, -1)
            
        
    
    
curses.wrapper(main)
