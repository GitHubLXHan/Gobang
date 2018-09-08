# -*- coding: utf-8 -*-
# @Time     : 2018/9/6 13:27
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : ai.py

from Gobang.setting import *

def negativeMax(is_ai, depth, alpha, beta):
    """
    负极大值搜索
    alpha_beta剪枝法
    """
    # 判断胜负或搜索层数并返回评估值
    if is_over(ai_list) or is_over(me_list) or depth == 0:
        return evaluation(is_ai)

    # 获取为落子的位子
    blank_list = list(set(all_list).difference(set(ai_me_list)))
    # 重新排序最后一次落子的四周的点
    blank_list = rearrange(blank_list)

    for next_step in blank_list:
        global search_count
        search_count += 1

        # 去掉那些四周无子的点
        if not has_neighbor(next_step):
            continue

        # 试着走一步
        if is_ai:
            ai_list.append(next_step)
        else:
            me_list.append(next_step)
        ai_me_list.append(next_step)
        value = -negativeMax(not is_ai, depth-1, -beta, -alpha)

        # 把试走一步退掉
        if is_ai:
            ai_list.remove(next_step)
        else:
            me_list.remove(next_step)
        ai_me_list.remove(next_step)
        # 评判是否需要剪枝
        if value > alpha:
            if depth == 3:
                AI_next_point[0],AI_next_point[1] = next_step[0],next_step[1]
                return value
            if value >= beta:
                global cut_count
                cut_count += 1
                return beta
            alpha = value
    return alpha


def has_neighbor(next_step):
    """"
    假设下一步的周围有子可能是最优点
    在negativeMax()中调用此函数
    跳过那些四周无子的点
    """
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if (next_step[0]+i,next_step[1]+j) in ai_me_list:
                return True
    return False

def rearrange(blank_list):
    """
    假设最后一次落子四周的位置可能是最优点
    将最后一次落子四周的位置置于blank_list前端
    """
    last_step = ai_me_list[-1]
    for b in blank_list:
        for i in range(-1,2):
            for j in range(-1,2):
                if i ==0 and j == 0:
                    continue
                next_step = (last_step[0]+i,last_step[1]+j)
                if next_step in blank_list:
                    blank_list.remove(next_step)
                    blank_list.insert(0, next_step)
    return blank_list


def is_over(list_now):
    """"判断胜负"""
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if r < ROW_COUNT - 4 and (r, c) in list_now and (r+1, c) in list_now and (r+2, c) in list_now and (r+3, c) in list_now and (r+4, c) in list_now:
                return True
            elif c < COLUMN_COUNT - 4 and (r, c) in list_now and (r, c+1) in list_now and (r, c+2) in list_now and (r, c+3) in list_now and (r, c+4) in list_now:
                return True
            elif r < ROW_COUNT and c < COLUMN_COUNT and (r, c) in list_now and (r+1, c+1) in list_now and (r+2, c+2) in list_now and (r+3, c+3) in list_now and (r+4, c+4) in list_now:
                return True
            elif r > 3 and c < COLUMN_COUNT and (r, c) in list_now and (r-1, c+1) in list_now and (r-2, c+2) in list_now and (r-3, c+3) in list_now and (r-4, c+4) in list_now:
                return True
    return False

# 评估函数
def evaluation(is_ai):
    # 初始分数值
    total_score = 0
    # 当评估方是下子方 list1为下子方
    if is_ai:
        list1 = ai_list
        list2 = me_list
    else:
        list1 = me_list
        list2 = ai_list
    # 评估主动方(下子方)
    Active_scores_all = []
    Active_score = 0 # 下子方最后的分数，在下面的for循环中逐次累加
    for l1 in list1:
        r, c = l1[0], l1[1]
        # calc_score返回一个元组(temp_score,Active_scores_all)，
        # 分别赋值给整数temp_score、列表Active_scores_all。
        # 纵向找最高分棋型，返回一个最高分整数还有一个存有元组形式的
        # 各个方向的最高分棋型的坐标点的列表（也就是说存储着各个最高分棋型的坐标）。
        temp_score, Active_scores_all = calc_score(r, c, 0, 1, list1, list2, Active_scores_all)
        Active_score += temp_score
        # 横向找最高分棋型
        temp_score, Active_scores_all = calc_score(r, c, 1, 0, list1, list2, Active_scores_all)
        Active_score += temp_score
        # 左下斜向找最高分棋型
        temp_score, Active_scores_all = calc_score(r, c, 1, 1, list1, list2, Active_scores_all)
        Active_score += temp_score
        # 右上斜向找最高分棋型
        temp_score, Active_scores_all = calc_score(r, c, -1, 1, list1, list2, Active_scores_all)
        Active_score += temp_score
    # 评估被动方(非下子方)
    # 此处同下子方
    Passive_scores_all = []
    Passive_score = 0
    for l2 in list2:
        r, c = l2[0], l2[1]
        temp_score, Passive_scores_all = calc_score(r, c, 0, 1, list2, list1, Passive_scores_all)
        Passive_score += temp_score
        temp_score, Passive_scores_all = calc_score(r, c, 1, 0, list2, list1, Passive_scores_all)
        Passive_score += temp_score
        temp_score, Passive_scores_all = calc_score(r, c, 1, 1, list2, list1, Passive_scores_all)
        Passive_score += temp_score
        temp_score, Passive_scores_all = calc_score(r, c, -1, 1, list2, list1, Passive_scores_all)
        Passive_score += temp_score
    # 总评
    total_score = Active_score - Passive_score * 0.1
    return total_score


# 计算每个方向上的分值
# list1是下子方
# scores_all用于避免重复计算和奖励棋型相交
def calc_score(r, c, x_direction, y_direction, list1, list2, scores_all):
    add_score = 0
    max_score = (0, None)
    # 避免重复计算
    for score_all in scores_all:
        for ps in score_all[1]:
            if r == ps[0] and c == ps[1] and x_direction == score_all[2][0] and y_direction == score_all[2][1]:
                return 0, scores_all
    # 获得棋型
    # 获得各个方向的气棋型
    # x, y = r + (poffset + noffset) * x_direction, c + (poffset + noffset) * y_direction
    # 此公式可理解为：
    # 当x_direction、y_direction分别为0、1则为纵向的棋型
    # 当x_direction、y_direction分别为1、0则为横向的棋型
    # 当x_direction、y_direction分别为1、1则为左下向的棋型
    # 当x_direction、y_direction分别为-1、1则为右上向的棋型
    # noffset、poffset相当于不断改变的棋盘上的x、y坐标
    # 根据评分表，有活三活四等情况，所以获取长度为6的棋型
    for noffset in range(-5, 1):
        position = []
        for poffset in range(0, 6):
            x, y = r + (poffset + noffset) * x_direction, c + (poffset + noffset) * y_direction
            # 计算出x、y坐标后，判断是否存在list1或者list2中，做标记存储在position列表中
            # 规则如下：
            #     若存在下子方的列表中，则标记为1，
            #     若存在对方的列表中，则标记为2，
            #     若为空格，则标记为0
            # 因为评分表是以0,1两个数字做棋型判断数，所以有上述标记规则
            if (x, y) in list2:
                position.append(2)
            elif (x, y) in list1:
                position.append(1)
            else:
                position.append(0)
        # 将长度为6的棋型切分为长度为5和长度为6的棋型并转换为元组，用于接下来获取最高分的操作
        temp_shape5 = tuple([i for i in position[0: -1]])
        temp_shape6 = tuple(position)
        # 获取最高分的棋型，并存储此棋型的坐标值，用于防止重复计算的情况发生
        for score, shape in scoreModel:
            if temp_shape5 == shape or temp_shape6 == shape:
                if score > max_score[0]:
                    max_score = (score, ((r + (0 + noffset) * x_direction, c + (0 + noffset) * y_direction),
                                         (r + (1 + noffset) * x_direction, c + (1 + noffset) * y_direction),
                                         (r + (2 + noffset) * x_direction, c + (2 + noffset) * y_direction),
                                         (r + (3 + noffset) * x_direction, c + (3 + noffset) * y_direction),
                                         (r + (4 + noffset) * x_direction, c + (4 + noffset) * y_direction)), (x_direction, y_direction))
    # 如果棋型与不同方向上的棋型相交，则得分翻三倍
    if max_score[1] is not None:
        for score_all in scores_all:
            for ps1 in score_all[1]:
                for ps2 in max_score[1]:
                    if ps1 == ps2 and max_score[0] > 10 and score_all[0] > 10:
                        add_score += max_score[0] + score_all[0]
        scores_all.append(max_score)
    return add_score + max_score[0], scores_all

def AI():
    """AI下棋"""
    global search_count
    global cut_count
    # 搜索的次数
    search_count = 0
    # 剪枝的次数
    cut_count = 0
    # 负极大值搜索
    negativeMax(True,3,-99999999,+9999999)
    print("搜索次数：",search_count,"剪枝次数：",cut_count)
    return AI_next_point[0],AI_next_point[1]




