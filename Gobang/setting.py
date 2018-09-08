# -*- coding: utf-8 -*-
# @Time     : 2018/9/6 15:36
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : setting.py


WINDOW_WIDTH = 650
WINDOW_HEIGHT = 500
#设置关于棋盘的参数
ROW_COUNT = 15
COLUMN_COUNT = 15
CHECKERBOARD_GRID_WIDTH = 30
CHECKERBOARD_GRID_HEIGHT = 30
CHECKERBOARD_WIDTH = 450
CHECKERBOARD_HEIGHT = 450
CHECKERBOARD_ROW_LINE_START_X = 25
CHECKERBOARD_ROW_LINE_START_Y = 25
CHECKERBOARD_ROW_LINE_END_X = 475
CHECKERBOARD_ROW_LINE_END_Y = 25
CHECKERBOARD_COLUMN_LINE_START_X = 25
CHECKERBOARD_COLUMN_LINE_START_Y = 25
CHECKERBOARD_COLUMN_LINE_END_X = 25
CHECKERBOARD_COLUMN_LINE_END_Y = 475
CHECKERBOARD_LINE_COLOR = (0,0,0)
CHECKERBOARD_LINE_WIDTH = 1
CHECKERBOARD_LINE_HEIGHT = 450
# 设置关于棋子的列表
ai_list = []
me_list = []
ai_me_list = []
all_list = []
# 设置棋子的颜色
AI_BLACK_PIECE = (0,0,0)
ME_WHITE_PIECE = (255,255,255)
# 搜索的次数
search_count = 0
# 剪枝的次数
cut_count = 0
# AI下一步需要走的位置
AI_next_point = [0, 0]
# 棋型评分表
scoreModel = [(50, (0, 1, 1, 0, 0)),
              (50, (0, 0, 1, 1, 0)),
              (200, (1, 1, 0, 1, 0)),
              (500, (0, 0, 1, 1, 1)),
              (500, (1, 1, 1, 0, 0)),
              (5000, (0, 1, 1, 1, 0)),
              (5000, (0, 1, 0, 1, 1, 0)),
              (5000, (0, 1, 1, 0, 1, 0)),
              (5000, (1, 1, 1, 0, 1)),
              (5000, (1, 1, 0, 1, 1)),
              (5000, (1, 0, 1, 1, 1)),
              (5000, (1, 1, 1, 1, 0)),
              (5000, (0, 1, 1, 1, 1)),
              (50000, (0, 1, 1, 1, 1, 0)),
              (99999999, (1, 1, 1, 1, 1))]