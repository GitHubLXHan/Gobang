# -*- coding: utf-8 -*-
# @Time     : 2018/9/10 11:14
# @Author   : hany
# @Email    : 1026310040@qq.com
# @File     : loadimage.py

import pygame
from Gobang.setting import *

class LoadImage:
    # img_path = "images/"
    # checkerboard_img = None
    # title_img = None
    # win_bg_img = None
    # h_vs_h_btn_img = None
    # h_vs_c_btn_img = None
    # how_to_play_img = None
    # common_rule_img = None
    # breaker_rule_img = None
    # offensive_img = None
    # defensive_img = None
    # capitulate_img = None
    # restart_img = None

    def __init__(self):
        pass

    @staticmethod
    def load_img(path,width,height):
        """加载图片资源"""
        img_resource = pygame.image.load(path).convert_alpha()
        img_resource = pygame.transform.scale(img_resource,(width,height))
        return img_resource

    # @staticmethod
    # def load_title_img():
    #     """加载标题图片"""
    #     if not LoadImage.title_img:
    #         LoadImage.title_img = pygame.image.load(LoadImage.img_path + "title.png").convert_alpha()
    #         LoadImage.title_img = pygame.transform.scale(LoadImage.title_img,(180,100))
    #     return LoadImage.title_img

    # @staticmethod
    # def load_checkerboard_img():
    #     """加载棋盘背景图片"""
    #     if not LoadImage.checkerboard_img:
    #         LoadImage.checkerboard_img = pygame.image.load(LoadImage.img_path + "checkerboard_bg.jpg").convert_alpha()
    #         LoadImage.checkerboard_img = pygame.transform.scale(LoadImage.checkerboard_img,(CHECKERBOARD_WIDTH+40,CHECKERBOARD_HEIGHT+40))
    #     return LoadImage.checkerboard_img

    # @staticmethod
    # def load_win_bg_img():
    #     """加载主窗口背景图片"""
    #     if not LoadImage.win_bg_img:
    #         LoadImage.win_bg_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.win_bg_img = pygame.transform.scale(LoadImage.win_bg_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.win_bg_img

    # @staticmethod
    # def load_h_vs_h_btn_img():
    #     """加载双人对弈按钮图片"""
    #     if not LoadImage.h_vs_h_btn_img:
    #         LoadImage.h_vs_h_btn_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.h_vs_h_btn_img = pygame.transform.scale(LoadImage.h_vs_h_btn_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.h_vs_h_btn_img

    # @staticmethod
    # def load_h_vs_c_btn_img():
    #     """加载人机对弈按钮图片"""
    #     if not LoadImage.h_vs_c_btn_img:
    #         LoadImage.h_vs_c_btn_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.h_vs_c_btn_img = pygame.transform.scale(LoadImage.h_vs_c_btn_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.h_vs_c_btn_img
    #
    # @staticmethod
    # def load_how_to_play_img():
    #     """加载说明按钮图片"""
    #     if not LoadImage.how_to_play_img:
    #         LoadImage.how_to_play_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.how_to_play_img = pygame.transform.scale(LoadImage.how_to_play_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.how_to_play_img
    #
    # @staticmethod
    # def load_common_rule_img():
    #     """加载普通规则按钮图片"""
    #     if not LoadImage.common_rule_img:
    #         LoadImage.common_rule_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.common_rule_img = pygame.transform.scale(LoadImage.common_rule_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.common_rule_img
    #
    # @staticmethod
    # def load_breaker_rule_img():
    #     """加载禁手规则按钮图片"""
    #     if not LoadImage.breaker_rule_img:
    #         LoadImage.breaker_rule_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.breaker_rule_img = pygame.transform.scale(LoadImage.breaker_rule_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.breaker_rule_img
    #
    # @staticmethod
    # def load_offensive_img():
    #     """加载主窗口背景图片"""
    #     if not LoadImage.offensive_img:
    #         LoadImage.offensive_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.offensive_img = pygame.transform.scale(LoadImage.offensive_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.offensive_img
    #
    # @staticmethod
    # def load_win_bg_img():
    #     """加载主窗口背景图片"""
    #     if not LoadImage.win_bg_img:
    #         LoadImage.win_bg_img = pygame.image.load(LoadImage.img_path + "win_bg.jpg").convert_alpha()
    #         LoadImage.win_bg_img = pygame.transform.scale(LoadImage.win_bg_img,(WINDOW_WIDTH,WINDOW_HEIGHT))
    #     return LoadImage.win_bg_img