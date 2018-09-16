# -*- coding: utf-8 -*-
# @Time     : 2018/9/8 16:26
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : droppiece.py
import random

from Gobang.AI import *


def drop_piece(click_pos,game_state):
    """玩家下棋子（即在‘玩家棋子列表me_list’、‘总棋子列表ai_me_list’中添加棋子坐标）"""
    # 这里最后面加15的作用：均分每个格子，当玩家点击时某个点，则取最靠近点击坐标的点
    click_x = click_pos[0] - CHECKERBOARD_ROW_LINE_START_X + 15
    click_y = click_pos[1] - CHECKERBOARD_ROW_LINE_START_Y + 15
    x = click_x // CHECKERBOARD_GRID_HEIGHT
    y = click_y // CHECKERBOARD_GRID_WIDTH
    if (x,y) not in off_def_list:
        if game_state.vs == HUMAN_VS_HUMAN and game_state.state == PLAYING:
            if game_state.rule == COMMON_RULE:
                if game_state.step % 2:
                    offensive_list.append((x, y))
                    off_def_list.append((x, y))
                    print("黑棋子(offensive_list)列表：",offensive_list)
                    print("白棋子(defensive_list)列表：",defensive_list)
                    print("全部棋子(off_def_list)列表：",off_def_list)
                    print()
                    if game_state.is_five_with(offensive_list):
                        game_state.state = GAME_OVER
                        game_state.win = OFFENSIVE
                else:
                    defensive_list.append((x,y))
                    off_def_list.append((x, y))
                    print("黑棋子(offensive_list)列表：",offensive_list)
                    print("白棋子(defensive_list)列表：",defensive_list)
                    print("全部棋子(off_def_list)列表：",off_def_list)
                    print()
                    if game_state.is_five_with(defensive_list):
                        game_state.state = GAME_OVER
                        game_state.win = DEFENSIVE
            elif game_state.rule == BREAKER_RULE:
                if game_state.step % 2:
                    offensive_list.append((x, y))
                    off_def_list.append((x, y))
                    if game_state.breaker_rule_is_win(offensive_list, defensive_list):
                        game_state.state = GAME_OVER
                        game_state.win = OFFENSIVE
                else:
                    defensive_list.append((x, y))
                    off_def_list.append((x, y))
                    print(x, y)
                    if game_state.is_five_with(defensive_list):
                        game_state.state = GAME_OVER
                        game_state.win = DEFENSIVE
            game_state.step += 1
        elif game_state.vs == HUMAN_VS_AI and game_state.state == PLAYING:
            if not game_state.step % 2:
                defensive_list.append((x, y))
                off_def_list.append((x, y))
                print(x, y)
                if game_state.is_five_with(defensive_list):
                    game_state.state = GAME_OVER
                    game_state.win = DEFENSIVE
                game_state.step += 1
                # 玩家下棋后AI下棋
                if game_state.vs == HUMAN_VS_AI and game_state.state == PLAYING:
                    if game_state.step % 2:
                        x, y = AI()
                        print(x, y)
                        if (x, y) in offensive_list:
                            x, y = random.choice(list(set(all_list).difference(set(off_def_list))))
                            game_state.state = GAME_OVER
                            game_state.win = DEFENSIVE
                        offensive_list.append((x, y))
                        off_def_list.append((x, y))
                        if game_state.rule == BREAKER_RULE:
                            if game_state.breaker_rule_is_win(offensive_list, defensive_list):
                                game_state.state = GAME_OVER
                                game_state.win = DEFENSIVE
                        if game_state.rule == COMMON_RULE:
                            if game_state.is_five_with(offensive_list):
                                game_state.state = GAME_OVER
                                game_state.win = OFFENSIVE
                        game_state.step += 1
    return game_state