# -*- coding: utf-8 -*-
# @Time     : 2018/9/6 13:27
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : AI.py

from Gobang.setting import *
from Gobang.gamestate import GameState

# 判断游戏是否结束
# 四种情况
def is_GameOver(list_now):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if r < ROW_COUNT - 4 and (r, c) in list_now and (r+1, c) in list_now and (r+2, c) in list_now and (r+3, c) in list_now and (r+4, c) in list_now:
				return True
			elif c < COLUMN_COUNT - 4 and (r, c) in list_now and (r, c+1) in list_now and (r, c+2) in list_now and (r, c+3) in list_now and (r, c+4) in list_now:
				return True
			elif r < ROW_COUNT - 4 and c < COLUMN_COUNT - 4 and (r, c) in list_now and (r+1, c+1) in list_now and (r+2, c+2) in list_now and (r+3, c+3) in list_now and (r+4, c+4) in list_now:
				return True
			elif r > 3 and c < COLUMN_COUNT - 4 and (r, c) in list_now and (r-1, c+1) in list_now and (r-2, c+2) in list_now and (r-3, c+3) in list_now and (r-4, c+4) in list_now:
				return True
	return False

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
	for noffset in range(-5, 1):
		position = []
		for poffset in range(0, 6):
			x, y = r + (poffset + noffset) * x_direction, c + (poffset + noffset) * y_direction
			if (x, y) in list2:
				position.append(2)
			elif (x, y) in list1:
				position.append(1)
			else:
				position.append(0)
		temp_shape5 = tuple([i for i in position[0: -1]])
		temp_shape6 = tuple(position)
		for score, shape in scoreModel:
			if temp_shape5 == shape or temp_shape6 == shape:
				if score > max_score[0]:
					max_score = (score, ((r + (0 + noffset) * x_direction, c + (0 + noffset) * y_direction),
										 (r + (1 + noffset) * x_direction, c + (1 + noffset) * y_direction),
										 (r + (2 + noffset) * x_direction, c + (2 + noffset) * y_direction),
										 (r + (3 + noffset) * x_direction, c + (3 + noffset) * y_direction),
										 (r + (4 + noffset) * x_direction, c + (4 + noffset) * y_direction)), (x_direction, y_direction))
	# 如果棋型相交，则得分增加
	if max_score[1] is not None:
		for score_all in scores_all:
			for ps1 in score_all[1]:
				for ps2 in max_score[1]:
					if ps1 == ps2 and max_score[0] > 10 and score_all[0] > 10:
						add_score += max_score[0] + score_all[0]
		scores_all.append(max_score)
	return add_score + max_score[0], scores_all


# 评估函数
def evaluation(is_ai):
	total_score = 0
	if is_ai:
		list1 = off_def_list
		list2 = defensive_list
	else:
		list1 = defensive_list
		list2 = off_def_list
	# 评估主动方(下子方)
	Active_scores_all = []
	Active_score = 0
	for l1 in list1:
		r, c = l1[0], l1[1]
		temp_score, Active_scores_all = calc_score(r, c, 0, 1, list1, list2, Active_scores_all)
		Active_score += temp_score
		temp_score, Active_scores_all = calc_score(r, c, 1, 0, list1, list2, Active_scores_all)
		Active_score += temp_score
		temp_score, Active_scores_all = calc_score(r, c, 1, 1, list1, list2, Active_scores_all)
		Active_score += temp_score
		temp_score, Active_scores_all = calc_score(r, c, -1, 1, list1, list2, Active_scores_all)
		Active_score += temp_score
	# 评估被动方(非下子方)
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


# 重新排列未落子的位置列表
# 假设离最后落子的邻居位置最有可能是最优点
def Rearrange(blank_list):
	last_step = off_def_list[-1]
	for bl in blank_list:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					continue
				next_step = (last_step[0]+i, last_step[1]+j)
				if next_step in blank_list:
					blank_list.remove(next_step)
					blank_list.insert(0, next_step)
	return blank_list



# 判断下一步位置是否存在相邻的子
def has_neighbor(next_step):
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue
			if (next_step[0]+i, next_step[1]+j) in off_def_list:
				return True
	return False

def negativeMax(is_ai, depth, alpha, beta):
    """
    负极大值搜索
    alpha_beta剪枝法
    """
    # 判断胜负或搜索层数并返回评估值
    if is_GameOver(offensive_list) or is_GameOver(defensive_list) or depth == 0:
        return evaluation(is_ai)

    # GameState.is_five_with(offensive_list) or GameState.is_five_with(defensive_list) or

    # 获取为落子的位子
    blank_list = list(set(all_list).difference(set(off_def_list)))
    # 重新排序最后一次落子的四周的点
    blank_list = Rearrange(blank_list)

    for next_step in blank_list:
        global search_count
        search_count += 1

        # 去掉那些四周无子的点
        if not has_neighbor(next_step):
            continue
        # 试着走一步
        if is_ai:
            offensive_list.append(next_step)
        else:
            defensive_list.append(next_step)

        off_def_list.append(next_step)
        value = -negativeMax(not is_ai, depth-1, -beta, -alpha)

        # 把试走一步退掉
        if is_ai:
            offensive_list.remove(next_step)
        else:
            defensive_list.remove(next_step)
        off_def_list.remove(next_step)
        # 评判是否需要剪枝
        if value > alpha:
            if depth == 3:
                AI_next_point[0],AI_next_point[1] = next_step[0],next_step[1]
            if value >= beta:
                global cut_count
                cut_count += 1
                return beta
            alpha = value
    return alpha


def AI():
    """AI下棋"""
    global search_count
    global cut_count
    # 搜索的次数
    search_count = 0
    # 剪枝的次数
    cut_count = 0
    # 负极大值搜索
    negativeMax(True,3,-99999999,99999999)
    print("搜索次数：",search_count,"剪枝次数：",cut_count)
    return AI_next_point[0],AI_next_point[1]




