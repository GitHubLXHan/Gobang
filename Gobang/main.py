# -*- coding: utf-8 -*-
# @Time     : 2018/9/6 9:30
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : main.py

import pygame
from Gobang.ai import *

def init_para():
    """初始化棋盘的棋子"""
    for r in range(ROW_COUNT+1):
        for c in range(COLUMN_COUNT):
            all_list.append((r,c))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Gobang")
    is_game = True
    init_para()# 初始化棋盘
    while is_game:
        is_game = check_event(is_game)
        screen.fill((216,130,24))
        draw_checkerboard(screen)
        draw_pieces(screen)
        pygame.display.update()

def draw_checkerboard(screen):
    """绘制棋盘"""
    for r in range(ROW_COUNT+1):
        row_start_x_y = [CHECKERBOARD_ROW_LINE_START_X,CHECKERBOARD_ROW_LINE_START_Y + r * CHECKERBOARD_GRID_WIDTH]
        row_end_x_y = [CHECKERBOARD_ROW_LINE_END_X,CHECKERBOARD_ROW_LINE_END_Y + r * CHECKERBOARD_GRID_HEIGHT]
        pygame.draw.line(screen,CHECKERBOARD_LINE_COLOR,row_start_x_y,row_end_x_y,CHECKERBOARD_LINE_WIDTH)

    for c in range(COLUMN_COUNT+1):
        column_start_x_y = [CHECKERBOARD_COLUMN_LINE_START_X + c * CHECKERBOARD_GRID_WIDTH,CHECKERBOARD_COLUMN_LINE_START_Y]
        column_end_x_y = [CHECKERBOARD_COLUMN_LINE_END_X + c * CHECKERBOARD_GRID_HEIGHT,CHECKERBOARD_COLUMN_LINE_END_Y]
        pygame.draw.line(screen,CHECKERBOARD_LINE_COLOR,column_start_x_y,column_end_x_y,CHECKERBOARD_LINE_WIDTH)

def draw_pieces(screen):
    """绘制棋子，即绘制‘AI棋子列表ai_list’为黑色，‘ME棋子列表me_list’为白色"""
    for a in ai_list:
        x = (a[0]+1) * CHECKERBOARD_GRID_WIDTH - 5
        y = (a[1]+1) * CHECKERBOARD_GRID_HEIGHT - 5
        pygame.draw.circle(screen,AI_BLACK_PIECE,[x,y],13)
        # print("黑棋")

    # 绘制自己的白色棋子
    for m in me_list:
        x = (m[0]+1) * CHECKERBOARD_GRID_WIDTH - 5
        y = (m[1]+1) * CHECKERBOARD_GRID_HEIGHT - 5
        pygame.draw.circle(screen,ME_WHITE_PIECE,[x,y],13)



def check_event(is_game):
    """点击事件总函数，在此函数中调用其他函数"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False
        if event .type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            if is_click_blank(click_pos):
                drop_piece(click_pos)
                if is_over(me_list):
                    print("游戏结束,你赢了")
                else:
                    print("AI第一次下棋")
                    # AI下棋
                    ai_piece = AI()
                    ai_list.append(ai_piece)
                    ai_me_list.append(ai_piece)
                    if is_over(ai_list):
                        print("游戏结束，AI赢了")


    return is_game

def is_click_blank(click_pos):
    """判断点击的坐标是否在棋盘之内"""
    # 这里减去13、加上13的作用：使玩家最大限度可点击棋盘外13个像素单位
    if click_pos[0] < CHECKERBOARD_ROW_LINE_START_X - 13 or click_pos[0] > CHECKERBOARD_ROW_LINE_START_X + 13 + CHECKERBOARD_WIDTH\
        or click_pos[1] < CHECKERBOARD_ROW_LINE_START_X - 13 or click_pos[1] > CHECKERBOARD_ROW_LINE_START_X + 13 + CHECKERBOARD_HEIGHT:
        return False
    return True

def drop_piece(click_pos):
    """玩家下棋子（即在‘玩家棋子列表me_list’、‘总棋子列表ai_me_list’中添加棋子坐标）"""
    # 这里最后面加15的作用：均分每个格子，当玩家点击时某个点，则取最靠近点击坐标的点
    click_x = click_pos[0] - CHECKERBOARD_ROW_LINE_START_X + 15
    click_y = click_pos[1] - CHECKERBOARD_ROW_LINE_START_Y + 15
    x = click_x // CHECKERBOARD_GRID_HEIGHT
    y = click_y // CHECKERBOARD_GRID_WIDTH
    if (x,y) not in ai_me_list:
        me_list.append((x,y))
        ai_me_list.append((x,y))
        print(x, y)


if __name__ == '__main__':
    main()