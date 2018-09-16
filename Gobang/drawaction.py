# -*- coding: utf-8 -*-
# @Time     : 2018/9/8 16:16
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : drawaction.py
from Gobang.setting import *
from Gobang.loadimage import LoadImage
import pygame

def draw_main(screen,game_state):
    draw_win_bg_img(screen)
    draw_title_img(screen)
    draw_checkerboard_img(screen)
    draw_checkerboard(screen)
    draw_pieces(screen)
    if game_state.state == GAME_OVER:
        draw_gameover_img(screen, game_state)
    else:
        draw_situation(screen,game_state)
    if game_state.stop == STOP:
        draw_how_to_play(screen)
    draw_buttons_img(screen,game_state)



def draw_checkerboard(screen):
    """绘制棋盘"""
    for r in range(ROW_COUNT):
        row_start_x_y = [CHECKERBOARD_ROW_LINE_START_X,CHECKERBOARD_ROW_LINE_START_Y + r * CHECKERBOARD_GRID_WIDTH]
        row_end_x_y = [CHECKERBOARD_ROW_LINE_END_X,CHECKERBOARD_ROW_LINE_END_Y + r * CHECKERBOARD_GRID_HEIGHT]
        pygame.draw.line(screen,CHECKERBOARD_LINE_COLOR,row_start_x_y,row_end_x_y,CHECKERBOARD_LINE_WIDTH)
        # r_font = pygame.font.SysFont('Arial',20)
        # r_font_surface = r_font.render(str(r),False,(0,0,0))
        # screen.blit(r_font_surface,(row_start_x_y[0]-20,row_start_x_y[1]-13))

    for c in range(COLUMN_COUNT):
        column_start_x_y = [CHECKERBOARD_COLUMN_LINE_START_X + c * CHECKERBOARD_GRID_WIDTH,CHECKERBOARD_COLUMN_LINE_START_Y]
        column_end_x_y = [CHECKERBOARD_COLUMN_LINE_END_X + c * CHECKERBOARD_GRID_HEIGHT,CHECKERBOARD_COLUMN_LINE_END_Y]
        pygame.draw.line(screen,CHECKERBOARD_LINE_COLOR,column_start_x_y,column_end_x_y,CHECKERBOARD_LINE_WIDTH)
        # s_font = pygame.font.SysFont('Arial',20)
        # s_font_surface = s_font.render(str(c),False,(0,0,0))
        # screen.blit(s_font_surface,(column_start_x_y[0]-5,column_start_x_y[1]-22))

def draw_pieces(screen):
    """绘制棋子，即绘制‘黑色棋子列表offensive_list’，‘白色棋子列表defensive_list’为白色"""
    for a in offensive_list:
        x = a[0] * CHECKERBOARD_GRID_WIDTH + CHECKERBOARD_COLUMN_LINE_END_X + 1
        y = a[1] * CHECKERBOARD_GRID_HEIGHT + CHECKERBOARD_COLUMN_LINE_START_Y
        pygame.draw.circle(screen, BLACK_PIECE, [x, y], 13)
        # print("黑棋")

    # 绘制自己的白色棋子
    for m in defensive_list:
        x = m[0] * CHECKERBOARD_GRID_WIDTH + CHECKERBOARD_ROW_LINE_START_X + 1
        y = m[1] * CHECKERBOARD_GRID_HEIGHT + CHECKERBOARD_ROW_LINE_START_Y
        pygame.draw.circle(screen, WHITE_PIECE, [x, y], 13)

def draw_title_img(screen):
    """绘制标题图片"""
    title_img_position = (CHECKERBOARD_WIDTH+110,25)
    screen.blit(LoadImage.load_img("images/title.png", 200, 80),title_img_position)

def draw_checkerboard_img(screen):
    """绘制棋盘背景图片"""
    checkerboard_img_position = (CHECKERBOARD_ROW_LINE_START_X-20, CHECKERBOARD_ROW_LINE_START_Y-20)
    screen.blit(LoadImage.load_img("images/checkerboard_bg.jpg",CHECKERBOARD_WIDTH+40,CHECKERBOARD_HEIGHT+40), checkerboard_img_position)

def draw_win_bg_img(screen):
    """绘制主窗口背景图片"""
    win_bg_img_position = (0,0)
    screen.blit(LoadImage.load_img("images/win_bg.jpg", WINDOW_WIDTH,WINDOW_HEIGHT),win_bg_img_position)

def draw_buttons_img(screen,game_state):
    """绘制按钮"""
    button1_position = (BUTTON_X, BUTTON_Y)
    button2_position = (BUTTON_X, BUTTON_Y + BUTTON_HEIGHT + 15)
    button3_position = (BUTTON_X, BUTTON_Y + BUTTON_HEIGHT * 2 + 30)
    if game_state.state == CHOOSE_VS:
        button1_img_path = "images/双人对弈按钮.png" # 双人对弈按钮
        button2_img_path = "images/人机对弈按钮.png" # 人机对弈按钮
        button3_img_path = "images/说明按钮.png" # 游戏说明按钮
    elif game_state.state == CHOOSE_RULE:
        button1_img_path = "images/普通模式按钮.png" # 普通规则按钮
        button2_img_path = "images/禁手模式按钮.png" # 禁手规则按钮
        button3_img_path = "images/返回按钮.png" # 返回按钮
    elif game_state.state == CHOOSE_SIDE:
        button1_img_path = "images/先手按钮.png" # 先手按钮
        button2_img_path = "images/后手按钮.png" # 后手按钮
        button3_img_path = "images/返回按钮.png" # 返回按钮
    elif game_state.state == PLAYING:
        button1_img_path = "images/认输按钮.png" # 认输按钮
        if game_state.rule == BREAKER_RULE:
            button2_img_path = "images/禁手按钮.png" # 禁手按钮
        elif game_state.rule == COMMON_RULE:
            button2_img_path = "images/禁手按钮.png" # 禁止点击禁手按钮
        button3_img_path = "images/悔棋按钮.png" # 重新开始按钮
    elif game_state.state == GAME_OVER:
        button1_img_path = "images/重新开始按钮.png"  # 再来一局按钮
        button2_img_path = "images/结束游戏按钮.png"  # 退出游戏
        button3_img_path = "images/说明按钮.png"  # 重新开始按钮

    screen.blit(LoadImage.load_img(button1_img_path, BUTTON_WIDTH, BUTTON_HEIGHT), button1_position)
    screen.blit(LoadImage.load_img(button2_img_path, BUTTON_WIDTH, BUTTON_HEIGHT), button2_position)
    screen.blit(LoadImage.load_img(button3_img_path, BUTTON_WIDTH, BUTTON_HEIGHT), button3_position)

def draw_gameover_img(screen, game_state):
    if game_state.vs == HUMAN_VS_HUMAN:
        if game_state.rule == COMMON_RULE:
            if game_state.win == OFFENSIVE:
                img_path = "images/黑方五连获胜.png"
            else:
                img_path = "images/白方五连获胜.png"
        else:
            if game_state.win == OFFENSIVE:
                img_path = "images/黑方五连获胜.png"
            elif game_state.win == DEFENSIVE and game_state.is_break:
                img_path = "images/黑禁白赢.png"
            elif game_state.win == DEFENSIVE and game_state.is_break is None:
                img_path = "images/白方五连获胜.png"
    elif game_state.vs == HUMAN_VS_AI:
        if game_state.rule == COMMON_RULE:
            if game_state.win == OFFENSIVE:
                img_path = "images/黑方五连获胜.png"
            else:
                img_path = "images/白方五连获胜.png"
        else:
            if game_state.win == OFFENSIVE:
                img_path = "images/黑方五连获胜.png"
            elif game_state.win == DEFENSIVE and game_state.is_break:
                img_path = "images/黑禁白赢.png"
            elif game_state.win == DEFENSIVE and game_state.is_break is None:
                img_path = "images/白方五连获胜.png"

    over_box_xy = (INFO_BOX_X, INFO_BOX_Y)
    screen.blit(LoadImage.load_img(img_path, INFO_BOX_WIDTH, INFO_BOX_HEIGHT), over_box_xy)

def draw_situation(screen,game_state):
    img_path = "images/对局情况.png"
    if game_state.vs == HUMAN_VS_HUMAN:
        if game_state.rule == COMMON_RULE:
            img_path = "images/双人无禁手.png"
        elif game_state.rule == BREAKER_RULE:
            img_path = "images/双人有禁手.png"
    elif game_state.vs == HUMAN_VS_AI:
        if game_state.rule == COMMON_RULE:
            img_path = "images/人机无禁手.png"
        elif game_state.rule == BREAKER_RULE:
            img_path = "images/人机有禁手.png"
    situation_pos = (INFO_BOX_X,INFO_BOX_Y)
    screen.blit(LoadImage.load_img(img_path, INFO_BOX_WIDTH, INFO_BOX_HEIGHT), situation_pos)

    situ_font_white_pos = (INFO_BOX_X + 75, INFO_BOX_Y + 89)
    situ_font_black_pos = (INFO_BOX_X + 75, INFO_BOX_Y + 55)
    situ_font_white = pygame.font.SysFont('BAUHS93.TTF', 22)
    situ_font_black = pygame.font.SysFont('BAUHS93.TTF', 22)
    situ_font_white_surface = situ_font_white.render(str(len(defensive_list)), False, (255, 62, 64))
    situ_font_black_surface = situ_font_black.render(str(len(offensive_list)), False, (255, 62, 64))
    screen.blit(situ_font_white_surface,situ_font_white_pos)
    screen.blit(situ_font_black_surface,situ_font_black_pos)

    if game_state.state == PLAYING:
        if game_state.step % 2:
            next_hint = '黑方下棋'
        else:
            next_hint = '白方下棋'
        situ_font_next_hint_pos = (INFO_BOX_X + 60, INFO_BOX_Y + 115)
        situ_font_next = pygame.font.SysFont('microsoftyaheimicrosoftyaheiuibold', 25, True)
        situ_font_pattern_surface = situ_font_next.render(next_hint, False, (110, 110, 110))
        screen.blit(situ_font_pattern_surface, situ_font_next_hint_pos)

def draw_how_to_play(screen):
    how_postion = (DESCRIPTION_X, DESCRIPTION_Y)
    screen.blit(LoadImage.load_img("images/游戏说明.png", DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT), how_postion)

