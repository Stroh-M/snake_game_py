import curses
import time
import random

def main(stdcr):
    # clear the screen (terminal)
    stdcr.clear()
    # remove the cursor 
    curses.curs_set(0)
    # set that the while loop shouldn't have to wait for a user input to continue 
    stdcr.nodelay(True)
    
    # get maximum height and width of the terminal being used 
    height, width = stdcr.getmaxyx()
    
    # set the initial direction (right)
    direction = (0, 1)
    
    # get random number to put the food at 
    yrandom = random.randrange(0, height)
    xrandom = random.randrange(0, width)
    
    # set the y and x variables so the snake should start in the middle 
    y = height // 2
    x = width // 2
    
    # snake is a list of where the previous positions of the snake was and the height and width are stored in tuples in a list
    snake = [(y, x)]
    
    # make the snake move and get bigger as it eats (play game)
    while True:
        # check if head of snake hit a wall 
        if snake[0][0] >= height or snake[0][1] >= width or snake[0][0] < 0 or snake[0][1] < 0:
            print("Hit a wall. Game over")
            quit()
        
        # check if head of snake hit into itself 
        for i in range(len(snake)):
            if i != 0:
                if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                    print("Bumped into yourself. Game over")
                    quit()
        
        # clear screen and enter # in every coordinates 
        stdcr.clear()
        for i in range(len(snake)):
            stdcr.addstr(snake[i][0], snake[i][1], "#")

        # add food in random cell
        stdcr.addstr(yrandom, xrandom, "*")

        # refresh terminal to see changes
        stdcr.refresh()

        # set .10 sec pause so it should move slower 
        time.sleep(0.10)

        # check if food was eaten if and if yes reset the random numbers 
        # to put food in new cell and don't remove last # coordinates so snake grows
        if y == yrandom and x == xrandom:
            yrandom = random.randrange(0, height)
            xrandom = random.randrange(0, width)
        else: # if not pop out the last # coordinates so snake stays the same length
            snake.pop(-1)
        
        # add one or minus one to move snake and coordinates
        y += direction[0]
        x += direction[1]

        # insert new coordinates to the beginning of the list 
        snake.insert(0, (y, x))
        
        # listen if key press and switch direction based on input of user 
        key = stdcr.getch()
        if key == curses.KEY_DOWN and direction != (-1, 0):
            direction = (1, 0)
        elif key == curses.KEY_UP and direction != (1, 0):
            direction = (-1 ,0 )
        elif key == curses.KEY_RIGHT and direction != (0, -1):
            direction = (0, 1)
        elif key == curses.KEY_LEFT and direction != (0, 1):
            direction = (0, -1)
        elif key == curses.KEY_END: # if button end is pressed program finishes
            quit()

# run program 
curses.wrapper(main)
