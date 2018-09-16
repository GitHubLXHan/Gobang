# -*- coding: utf-8 -*-
# @Time     : 2018/9/8 16:32
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : gamestate.py

from Gobang.setting import *

class GameState:
    def __init__(self):
        self.init_para()
        self.state = CHOOSE_VS
        self.vs = None
        self.rule = None
        self.side = None
        self.step = None
        self.is_playing = True
        self.win = None
        self.stop = None
        self.is_break = None
    def set_side(self,side):
        if side == OFFENSIVE:
            self.side = OFFENSIVE
            self.step = 1
        else:
            self.side = DEFENSIVE
            self.step = 0


    def init_para(self):
        """初始化棋盘的棋子"""
        global offensive_list
        global defensive_list
        global off_def_list
        global all_list
        offensive_list.clear()
        defensive_list.clear()
        off_def_list.clear()
        all_list.clear()
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT):
                all_list.append((r, c))
        print("all_list的长度", len(all_list))


    @staticmethod
    def is_five_with(list_now):
        """"判断胜是否五连"""
        if len(off_def_list) > 1:
            last_step = off_def_list[-1]
        else:
            return False
        for r,c in zip(range(last_step[0] - 5, last_step[0] + 2),range(last_step[1] - 5, last_step[1] + 2)):
            # 横向
            if (r, last_step[1]) not in list_now \
                    and (r + 1, last_step[1]) in list_now \
                    and (r + 2, last_step[1]) in list_now \
                    and (r + 3, last_step[1]) in list_now \
                    and (r + 4, last_step[1]) in list_now \
                    and (r + 5, last_step[1]) in list_now \
                    and (r + 6, last_step[1]) not in list_now:
                return True
            # 纵向
            elif (last_step[0], c) not in list_now \
                    and (last_step[0], c + 1) in list_now \
                    and (last_step[0], c + 2) in list_now \
                    and (last_step[0], c + 3) in list_now \
                    and (last_step[0], c + 4) in list_now \
                    and (last_step[0], c + 5) in list_now \
                    and (last_step[0], c + 6) not in list_now:
                return True
            # 右斜下向
            elif (r, c) not in list_now \
                    and (r + 1, c + 1) in list_now \
                    and (r + 2, c + 2) in list_now \
                    and (r + 3, c + 3) in list_now \
                    and (r + 4, c + 4) in list_now\
                    and (r + 5, c + 5) in list_now\
                    and (r + 6, c + 6) not in list_now:
                return True
            # 左斜上向
            elif (r, 2 * last_step[1] - c) not in list_now \
                    and (r + 1, 2 * last_step[1] - c - 1) in list_now \
                    and (r + 2, 2 * last_step[1] - c - 2) in list_now \
                    and (r + 3, 2 * last_step[1] - c - 3) in list_now \
                    and (r + 4, 2 * last_step[1] - c - 4) in list_now \
                    and (r + 5, 2 * last_step[1] - c - 5) in list_now \
                    and (r + 6, 2 * last_step[1] - c - 6) not in list_now:
                return True
        return False

    @staticmethod
    def breaker_rule_is_win(list1, list2):
        """人机对弈且有禁手的模式下黑方判断胜负"""
        if GameState.is_five_with(list1) and GameState.is_breaker(list1, list2):
            return True


    @staticmethod
    def is_long_with(list_now):
        """判断是否长连"""
        if len(list_now) > 1:
            last_step = list_now[-1]
        else:
            return False
        for r,c in zip(range(last_step[0] - 5, last_step[0] + 2), range(last_step[1] - 5, last_step[1] + 2)):
            # 判断是否长连
            # 横向
            if (r, last_step[1]) in list_now \
                    and (r + 1, last_step[1]) in list_now \
                    and (r + 2, last_step[1]) in list_now \
                    and (r + 3, last_step[1]) in list_now \
                    and (r + 4, last_step[1]) in list_now \
                    and (r + 5, last_step[1]) in list_now:
                return True
            # 纵向
            elif (last_step[0], c) in list_now \
                    and (last_step[0], c + 1) in list_now \
                    and (last_step[0], c + 2) in list_now \
                    and (last_step[0], c + 3) in list_now \
                    and (last_step[0], c + 4) in list_now \
                    and (last_step[0], c + 5) in list_now:
                return True
            # 右斜下向
            elif (r, c) in list_now \
                    and (r + 1, c + 1) in list_now \
                    and (r + 2, c + 2) in list_now \
                    and (r + 3, c + 3) in list_now \
                    and (r + 4, c + 4) in list_now \
                    and (r + 5, c + 5) in list_now:
                return True
            # 左斜上向
            elif (r, 2 * last_step[1] - c) in list_now \
                    and (r + 1, 2 * last_step[1] - c - 1) in list_now \
                    and (r + 2, 2 * last_step[1] - c - 2) in list_now \
                    and (r + 3, 2 * last_step[1] - c - 3) in list_now \
                    and (r + 4, 2 * last_step[1] - c - 4) in list_now \
                    and (r + 4, 2 * last_step[1] - c - 4) in list_now:
                return True
    @staticmethod
    def is_breaker(list1, list2):
        """判断是否三三禁手或者四四禁手"""
        if len(list1) > 1 and len(list2) > 1:
            last_step = list1[-1]
        else:
            return False
        for r,c in zip(range(last_step[0] - 3, last_step[0] + 1), range(last_step[1] - 3, last_step[1] + 1)):
            # 判断是否三三禁手(方式一)
            # 横向
            if ((r, last_step[1]) in list1
            and (r + 1, last_step[1]) in list1
            and (r + 2, last_step[1]) not in off_def_list
            and (r + 3, last_step[1]) in list1)\
            or \
            ((r, last_step[1]) in list1
            and (r + 1, last_step[1]) not in off_def_list
            and (r + 2, last_step[1]) in list1
            and (r + 3, last_step[1]) in list1)\
            or \
            ((r, last_step[1]) not in off_def_list
            and (r + 1, last_step[1]) in list1
            and (r + 2, last_step[1]) in list1
            and (r + 3, last_step[1]) in list1)\
            or \
            ((r, last_step[1]) in list1
            and (r + 1, last_step[1]) in list1
            and (r + 2, last_step[1]) in list1
            and (r + 3, last_step[1]) not in off_def_list):
                print("横向有")
                if GameState.row_have(r, last_step[1], list1, list2):
                    return True
            # 纵向
            elif ((last_step[0], c) in list1
            and (last_step[0], c + 1) in list1
            and (last_step[0], c + 2) not in off_def_list
            and (last_step[0], c + 3) in list1)\
            or \
            ((last_step[0], c) in list1
            and (last_step[0], c + 1) not in off_def_list
            and (last_step[0], c + 2) in list1
            and (last_step[0], c + 3) in list1)\
            or \
            ((last_step[0], c) not in off_def_list
            and (last_step[0], c + 1) in list1
            and (last_step[0], c + 2) in list1
            and (last_step[0], c + 3) in list1)\
            or \
            ((last_step[0], c) in list1
            and (last_step[0], c + 1) in list1
            and (last_step[0], c + 2) in list1
            and (last_step[0], c + 3) not in off_def_list):
                print("纵向有")
                if GameState.column_have(last_step[0], c, list1, list2):
                    return True
            # 右斜下向
            elif ((r, c) in list1
            and (r + 1, c + 1) in list1
            and (r + 2, c + 2) not in off_def_list
            and (r + 3, c + 3) in list1)\
            or \
            ((r, c) in list1
            and (r + 1, c + 1) not in off_def_list
            and (r + 2, c + 2) in list1
            and (r + 3, c + 3) in list1)\
            or \
            ((r, c) not in off_def_list
            and (r + 1, c + 1) in list1
            and (r + 2, c + 2) in list1
            and (r + 3, c + 3) in list1)\
            or \
            ((r, c) in list1
            and (r + 1, c + 1) in list1
            and (r + 2, c + 2) in list1
            and (r + 3, c + 3) not in off_def_list):
                print("右斜下向有")
                if GameState.rht_have(r, c, list1, list2):
                    return True
            # 左斜上向
            elif ((r, 2 * last_step[1] - c) in list1
            and (r + 1, 2 * last_step[1] - c - 1) in list1
            and (r + 2, 2 * last_step[1] - c - 2) not in off_def_list
            and (r + 3, 2 * last_step[1] - c - 3) in list1)\
            or \
            ((r, 2 * last_step[1] - c) in list1
            and (r + 1, 2 * last_step[1] - c - 1) not in off_def_list
            and (r + 2, 2 * last_step[1] - c - 2) in list1
            and (r + 3, 2 * last_step[1] - c - 3) in list1)\
            or\
            ((r, 2 * last_step[1] - c) in list1
            and (r + 1, 2 * last_step[1] - c - 1) in list1
            and (r + 2, 2 * last_step[1] - c - 2) in list1
            and (r + 3, 2 * last_step[1] - c - 3) not in off_def_list)\
            or \
            ((r, 2 * last_step[1] - c) not in off_def_list
            and (r + 1, 2 * last_step[1] - c - 1) in list1
            and (r + 2, 2 * last_step[1] - c - 2) in list1
            and (r + 3, 2 * last_step[1] - c - 3) in list1):
                print("左斜上向有")
                if GameState.lht_have(r, 2 * last_step[1] - c, list1, list2):
                    return True
        return False

    @staticmethod
    # 当横向出现活三或活四
    def row_have(x, y, list1, list2):
        """
        当横向出现活三或活四的情况下，
        此方法用于判断另外其他三个方向上是否也出现活三或活四的情况
        在is_breaker()函数中调用本函数
        """
        # 纵向
        for row in range(x, x + 4):
            for column in range(y - 3, y + 1):
                pieces = 0
                for c in range(column, column+4):
                    if (row, c) in list1 and (row, c) not in list2:
                        pieces +=1
                if pieces >= 3:
                    return True

        for row in range(x,x+4):
            # 右斜下
            for r, c in zip(range(row - 3, row + 1), range(y - 3, y + 1)):
                pieces = 0
                for i in range(4):
                    if (r + i, c + i) in list1 and (r + i, c + i) in list2:
                        pieces += 1
                if pieces >= 3:
                    return True
            # 左斜上
            for r, c in zip(range(row - 3, row + 1), range(y - 3, y + 1)):
                pieces = 0
                for i in range(4):
                    if (r + i , 2 * y - c - i) in list1 and (r + i , 2 * y - c - i) not in list2:
                        pieces += 1
                if pieces >= 3:
                    return True
        return False

    # 当纵向出现活三或活四
    @staticmethod
    def column_have(x, y, list1, list2):
        """
         当纵向出现活三或活四的情况下，
         此方法用于判断另外其他三个方向上是否也出现活三或活四的情况
         在is_breaker()函数中调用本函数
         """
        for column in range(y, y + 4):
            # 横向
            for row in range(x-3, x + 1):
                pieces = 0
                for r in range(row, row+4):
                    if (r, column) in list1 and (r, column) not in list2:
                        pieces +=1
                if pieces >= 3:
                    return True
        for column in range(y, y + 4):
            # 右斜下
            for r, c in zip(range(x - 3, x + 1), range(column - 3, column + 1)):
                pieces = 0
                for i in range(4):
                    if (r + i, c + i) in list1 and (r + i, c + i) in list2:
                        pieces += 1
                if pieces >= 3:
                    return True
            # 左斜上
            for r, c in zip(range(x - 3, x + 1), range(column + 3, column - 1, -1)):
                pieces = 0
                for i in range(4):
                    if (r + i , c - i) in list1 and (r + i , c - i) not in list2:
                        pieces += 1
                if pieces >= 3:
                    return True
        return False

    # 当右斜下出现活三或活四
    @staticmethod
    def rht_have(x, y, list1, list2):
        """
         当右斜下方向出现活三或活四的情况下，
         此方法用于判断另外其他三个方向上是否也出现活三或活四的情况
         在is_breaker()函数中调用本函数
         """
        for row, column in zip(range(x, x + 4), range(y,  y + 4)):
            # 纵向
            for c in range(column - 3, column):
                pieces = 0
                for i in range(4):
                    if (row, c + i) in list1 and (row, c + i) not in list2:
                        pieces +=1
                if pieces >= 3:
                    return True
            # 横向
            for r in range(row - 3, row):
                pieces = 0
                for i in range(4):
                    if (r + i, column) in list1 and (r + i, column) not in list2:
                        pieces += 1
                if pieces >= 3:
                    return True
            # 左斜上
            for r, c in zip(range(row - 3, row + 1), range(column + 3, column - 1, -1)):
                pieces = 0
                for i in range(4):
                    if (r + i, c - i) in list1 and (r + i, c - i) not in list2:
                        pieces += 1
                if pieces <= 3:
                    return True

    # 当左斜上出现活三或活四
    @staticmethod
    def lht_have(x, y, list1, list2):
        """
         当左斜上出现活三或活四的情况下，
         此方法用于判断另外其他三个方向上是否也出现活三或活四的情况
         在is_breaker()函数中调用本函数
         """
        for row, column in zip(range(x, x + 4), range(y, y - 4, -1)):
            # 横向
            for r in range(row - 3, row + 1):
                pieces = 0
                for i in range(4):
                    if (r + i, column) in list1 and (r + i, column) not in list2:
                        pieces += 1
                if pieces >= 3:
                    return True
            # 纵向
            for c in range(column - 3, column + 1):
                pieces = 0
                for i in range(4):
                    if (row, c + i) in list1 and (row, c + i) not in list2:
                        pieces += 1
                if pieces >= 3:
                    return True

            # 右斜下
            for r, c in zip(range(row - 3, row + 1), range(column - 3, column +1)):
                pieces = 0
                for i in range(4):
                    if (r + i, c + i) in list1 and (r + i, c + i) not in list2:
                        pieces += 1
                if pieces >= 3:
                    return  True
