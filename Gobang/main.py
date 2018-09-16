# -*- coding: utf-8 -*-
# @Time     : 2018/9/6 9:30
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : main.py

from Gobang.drawaction import draw_main
from Gobang.checkaction import *
from Gobang.gamestate import *
from Gobang.setting import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Gobang")
    game_state = GameState()
    while game_state.is_playing:
        game_state = check_event(game_state)
        draw_main(screen,game_state)
        pygame.display.update()


if __name__ == '__main__':
    main()