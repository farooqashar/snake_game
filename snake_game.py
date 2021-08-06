import random 
import curses


stdscr = curses.initscr()
curses.curs_set(2)
screen_dimensions = stdscr.getmaxyx()
screen_width = screen_dimensions[0]
screen_height = screen_dimensions[1]

new_game_window = curses.newwin(screen_height,screen_width,0,0)

new_game_window.keypad(1)
new_game_window.timeout(110)

snake_x = screen_width/8
snake_y = screen_height/4
