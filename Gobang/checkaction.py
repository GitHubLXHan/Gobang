# -*- coding: utf-8 -*-
# @Time     : 2018/9/8 16:24
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : checkaction.py
import pygame
import sys

from Gobang.droppiece import *
from Gobang.gamestate import *

def check_event(game_state):
    """点击事件总函数，在此函数中调用其他函数"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.is_playing = False
        if event .type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            if is_click_checkerboard(click_pos) and game_state.state == PLAYING:
                game_state = drop_piece(click_pos,game_state)
            if is_click_btn_board(click_pos) and game_state.stop is None:
                # 判断点击到哪个按钮，改变被点击按钮的状态值
                game_state = change_btn_state(click_pos,game_state)
            if game_state.stop == STOP:
                if DESCRIPTION_X + 219 < click_pos[0] < DESCRIPTION_X + 250\
                    and DESCRIPTION_Y + 43 < click_pos[1] < DESCRIPTION_Y + 63:
                    print("关闭说明框")
                    game_state.stop = None
    return game_state

def is_click_checkerboard(click_pos):
    """判断点击的坐标是否在棋盘之内"""
    # 这里减去13、加上13的作用：使玩家最大限度可点击棋盘外13个像素单位
    if click_pos[0] < CHECKERBOARD_ROW_LINE_START_X - 13 or click_pos[0] > CHECKERBOARD_ROW_LINE_START_X + 13 + CHECKERBOARD_WIDTH\
        or click_pos[1] < CHECKERBOARD_ROW_LINE_START_X - 13 or click_pos[1] > CHECKERBOARD_ROW_LINE_START_X + 13 + CHECKERBOARD_HEIGHT:
        return False
    return True

def is_click_btn_board(click_pos):
    """判断点击的坐标是否在按钮区域"""
    if click_pos[0] < BUTTON_X or click_pos[0] > BUTTON_X + BUTTON_WIDTH\
        or click_pos[1] < BUTTON_Y or click_pos[1] > BUTTON_Y + BUTTON_HEIGHT*3 + 40:
        return False
    return True

def change_btn_state(click_pos,game_state):
    print("成功进入")
    # “选择对弈双方”状态
    if game_state.state == CHOOSE_VS:
        if BUTTON_Y < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT:
            game_state.vs = HUMAN_VS_HUMAN
            game_state.state = CHOOSE_RULE
            print("选择双人")
        elif BUTTON_Y + BUTTON_HEIGHT + 20 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT* 2 + 20:
            game_state.vs = HUMAN_VS_AI
            game_state.state = CHOOSE_RULE
            print("选择人机")
        elif BUTTON_Y + BUTTON_HEIGHT* 2 + 40 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT* 3 + 40:
            game_state.stop = STOP
            print("DESCRIPTION_Y",DESCRIPTION_Y,"DESCRIPTION_X",DESCRIPTION_X,"DESCRIPTION_HEIGHT",DESCRIPTION_HEIGHT,"DESCRIPTION_WIDTH",DESCRIPTION_WIDTH)
    # “选择对弈规则”状态
    elif game_state.state == CHOOSE_RULE:
        if BUTTON_Y < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT:
            game_state.rule = COMMON_RULE
            game_state.state = CHOOSE_SIDE
            if game_state.vs == HUMAN_VS_AI:
                game_state.state = PLAYING
                game_state.set_side(OFFENSIVE)
                offensive_list.append((7,7))
                off_def_list.append((7,7))
                game_state.step += 1
                print("电脑先下")
            print("选择普通规则")
        elif BUTTON_Y + BUTTON_HEIGHT + 20 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT* 2 + 20:
            game_state.rule = BREAKER_RULE
            game_state.state = CHOOSE_SIDE
            if game_state.vs == HUMAN_VS_AI:
                game_state.state = PLAYING
                game_state.set_side(OFFENSIVE)
                offensive_list.append((7, 7))
                off_def_list.append((7, 7))
                game_state.step += 1
                print("电脑先下")
            print("选择禁手规则")
        elif BUTTON_Y + BUTTON_HEIGHT* 2 + 40 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT* 3 + 40:
            game_state.state = CHOOSE_VS
            game_state.vs = None
            print("返回上一步")
    # “选择先后手”状态
    elif game_state.state == CHOOSE_SIDE:
        if BUTTON_Y < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT:
            game_state.set_side(OFFENSIVE)
            game_state.state = PLAYING
            print("选择先手")
        elif BUTTON_Y + BUTTON_HEIGHT + 20 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT * 2 + 20:
            game_state.set_side(DEFENSIVE)
            game_state.state = PLAYING
            print("选择后手")
        elif BUTTON_Y + BUTTON_HEIGHT * 2 + 40 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT * 3 + 40:
            game_state.state = CHOOSE_RULE
            game_state.rule = None
            print("返回上一步")
    # “游戏中”状态
    elif game_state.state == PLAYING:
        if BUTTON_Y < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT:
            if game_state.vs == HUMAN_VS_HUMAN:
                if game_state.step % 2:
                    game_state.state = GAME_OVER
                    game_state.win = DEFENSIVE
                    print("黑方认输")
                else:
                    game_state.state = GAME_OVER
                    game_state.win = OFFENSIVE
                    print("白方认输")
            elif game_state.vs == HUMAN_VS_AI:
                if not game_state.step % 2:
                    game_state.state = GAME_OVER
                    game_state.win = OFFENSIVE
                    print("白方认输")
        elif BUTTON_Y + BUTTON_HEIGHT + 20 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT * 2 + 20:
            if game_state.rule == BREAKER_RULE and game_state.vs == HUMAN_VS_HUMAN:
                if game_state.step % 2:
                    if game_state.is_breaker(defensive_list, offensive_list) or game_state.is_long_with(defensive_list):
                        game_state.state = GAME_OVER
                        game_state.win = OFFENSIVE
                else:
                    if game_state.is_breaker(offensive_list, defensive_list) or game_state.is_long_with(offensive_list):
                        game_state.state = GAME_OVER
                        game_state.win = DEFENSIVE
                        game_state.is_break = True
                    print("查看黑棋是否禁手")
            elif game_state.rule == BREAKER_RULE and game_state.vs == HUMAN_VS_AI:
                if not game_state.step % 2:
                    if game_state.is_breaker(offensive_list, defensive_list) or game_state.is_long_with(offensive_list):
                        game_state.state = GAME_OVER
                        game_state.win = DEFENSIVE
                        game_state.is_break = True
        elif BUTTON_Y + BUTTON_HEIGHT * 2 + 40 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT * 3 + 40:
            if len(offensive_list) >= 1 and len(defensive_list) >= 1:
                if game_state.vs == HUMAN_VS_HUMAN :
                    if game_state.step % 2:
                        del defensive_list[-1]
                        print("白方悔棋")
                    else:
                        del offensive_list[-1]
                        print("黑方悔棋")
                    del off_def_list[-1]
                    game_state.step -= 1
                elif game_state.vs == HUMAN_VS_AI:
                    if not game_state.step % 2:
                        if len(offensive_list) >= 1 and len(defensive_list) >= 1:
                            del defensive_list[-1]
                            del offensive_list[-1]
                            del off_def_list[-2:]
                print("悔棋")
    # 棋局结束状态
    elif game_state.state == GAME_OVER:
        if BUTTON_Y < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT:
            game_state = GameState()
        elif BUTTON_Y + BUTTON_HEIGHT + 20 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT * 2 + 20:
            sys.exit(0)
        elif BUTTON_Y + BUTTON_HEIGHT * 2 + 40 < click_pos[1] < BUTTON_Y + BUTTON_HEIGHT * 3 + 40:
            game_state.stop = STOP

    return game_state