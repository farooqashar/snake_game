import random
import curses
from datetime import datetime

def game():        
    customization = input("Would You Like To Customize Game Settings? (Y or n) ")
    score = 0
    if str(customization) == "Y":
        speed = input("Enter game speed: (default: 125) ")
        initial_direction = input("Enter Initial Direction of Snake: (N or S or E or W) ")
        target_type = int(input("Enter Your Choice of Target: (1 for PI and 2 for Diamond) "))
    else:
        target_type = 2

    stdscr = curses.initscr()
    curses.curs_set(1)
    height, width = stdscr.getmaxyx()

    new_game_window = curses.newwin(height, width, 0, 0)
    new_game_window.keypad(1)

    try:
        new_game_window.timeout(int(speed))
    except:
        new_game_window.timeout(125)

    new_game_window.timeout(125)
    snake_x = width/2
    snake_y = height/8
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x-1],
        [snake_y, snake_x-2],
        [snake_y, snake_x-3],
        [snake_y, snake_x-4]
    ]

    target = [height/2, width/2]
    if target_type == 1:
        new_game_window.addch(int(target[0]), int(target[1]), curses.ACS_PI)
    else:
        new_game_window.addch(int(target[0]), int(target[1]), curses.ACS_DIAMOND)


    try: 

        if initial_direction == "N":
            key = curses.KEY_DOWN
        if initial_direction == "E":
            key = curses.KEY_RIGHT
        if initial_direction == "S":
            key = curses.KEY_DOWN
        if initial_direction == "W":
            key = curses.KEY_LEFT  
    except:
        key = curses.KEY_DOWN  


    while True:
        next_key = new_game_window.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, height] or snake[0][1]  in [0, width] or snake[0] in snake[1:]:
            curses.endwin()
            print("You lost :(")
            print("Your Score: ",score)
            quit()

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == target:
            score += 10
            target = None
            while target is None:
                new_target = [
                    random.randint(1, height-1),
                    random.randint(1, width-1)
                ]

                target = new_target if new_target not in snake else None
            
            if target_type == 1:
                new_game_window.addch(target[0], target[1], curses.ACS_PI)
            else:
                new_game_window.addch(target[0], target[1], curses.ACS_DIAMOND)
        else:
            snake_end = snake.pop()
            new_game_window.addch(int(snake_end[0]), int(snake_end[1]), ' ')
        try:
            new_game_window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
        except:
            print("You lost :(")
            print("Your Score: ",score)
            quit()

if __name__ == "__main__":

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print("It is currently " + current_time)
    print("Starting Snake Game...")

    try:
        game()
    except:
        print("Ending Snake Game...")
