import random
import curses

stdscr = curses.initscr()
curses.curs_set(0)
height, width = stdscr.getmaxyx()

new_game_window = curses.newwin(height, width, 0, 0)
new_game_window.keypad(1)
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
new_game_window.addch(int(target[0]), int(target[1]), curses.ACS_DIAMOND)

key = curses.KEY_DOWN

while True:
    next_key = new_game_window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, height] or snake[0][1]  in [0, width] or snake[0] in snake[1:]:
        curses.endwin()
        print("You lost :(")
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
        target = None
        while target is None:
            new_target = [
                random.randint(1, height-1),
                random.randint(1, width-1)
            ]
            target = new_target if new_target not in snake else None
        new_game_window.addch(target[0], target[1], curses.ACS_DIAMOND)
    else:
        snake_end = snake.pop()
        new_game_window.addch(int(snake_end[0]), int(snake_end[1]), ' ')

    new_game_window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)


if __name__ == "__main__":
    pass