# pip install windows-curses
# https://docs.python.org/3/library/curses.html
import curses

screen = curses.initscr()
curses.resize_term(50, 120)
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
# screen.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
curses.noecho() 
curses.curs_set(0) 
screen.keypad(1) 
curses.mousemask(curses.ALL_MOUSE_EVENTS)

key=0
while key!=27: # Esc to close
    key = screen.getch() 
    if key == curses.KEY_MOUSE:
        _, mx, my, _, k = curses.getmouse()
        # y, x = screen.getyx()
        # if k == 2 or k == 4:
        if True:
            
            # screen.erase()
            try:
                screen.addstr(my, mx, '  ', curses.color_pair(2))
                screen.addstr(0, 0, 'mx, my = %i,%i'%(mx,my))
            except curses.error:
                pass
    screen.refresh()

curses.endwin()