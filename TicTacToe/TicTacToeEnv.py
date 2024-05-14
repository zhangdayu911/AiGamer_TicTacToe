#!/usr/bin/env python3
import numpy as np


class TicTacToeEnv:
    #-------------初始化-------------
    def __init__(self):
        self.board = np.zeros((3, 3))  # 初始化3x3的棋盘
        self.current_player = 1  # 初始化当前玩家为1

    # -------------重置整个棋盘-------------
    def reset(self):
        self.board = np.zeros((3, 3))  # 重置棋盘为全零
        self.current_player = 1  # 重置当前玩家为1
        return self.board

    # -------------下棋-------------
    def step(self, action):
        row, col = action
        if self.board[row, col] != 0:  # 如果该位置已经有棋子了
            return self.board, -10, True, []  # 返回当前状态、负奖励、游戏结束、空动作列表

        self.board[row, col] = self.current_player  # 在棋盘上放置当前玩家的棋子
        done, winner = self.check_winner()  # 检查游戏是否结束以及是否有获胜者

        if done:  # 如果游戏结束
            if winner == 0:  # 平局
                reward = 0
            elif winner == self.current_player:  # 当前玩家获胜
                reward = 10
            else:  # 对手获胜
                reward = -10
            # print('Done',self.board)
        else:  # 游戏未结束
            reward = 0

        self.current_player = -self.current_player  # 切换当前玩家
        return self.board, reward, done, self.get_legal_actions()

    # -------------玩家操作-------------
    def human_move(self):
        valid_move = False
        while not valid_move:
            try:
                row = int(input("请输入行数（0-2）："))
                col = int(input("请输入列数（0-2）："))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("无效的位置，请输入0-2之间的行列数。")
                elif self.board[row, col] != 0:
                    print("该位置已被占据，请选择其他位置。")
                else:
                    valid_move = True
            except ValueError:
                print("请输入整数值。")

        self.board[row, col] = self.current_player
        done, winner = self.check_winner()
        if done:
            if winner == 0:
                print("平局！")
            elif winner == self.current_player:
                print("你赢了！")
            else:
                print("你输了！")
        else:
            self.current_player = -self.current_player

    # -------------判断胜利-------------
    def check_winner(self):
        for player in [1, -1]:
            # 检查行
            for i in range(3):
                if np.all(self.board[i, :] == player):
                    return True, player
            # 检查列
            for i in range(3):
                if np.all(self.board[:, i] == player):
                    return True, player
            # 检查对角线
            if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
                return True, player
        # 检查是否有空位置
        if not np.any(self.board == 0):
            return True, 0  # 平局
        # 游戏未结束
        return False, None

    # -------------判断剩余位置-------------
    def get_legal_actions(self):
        # 返回当前可用位置，返回的是list
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    # -------------判断剩余位置-------------
    def render(self):
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 1:
                    print('X', end=' ')
                elif self.board[i, j] == -1:
                    print('O', end=' ')
                else:
                    print('-', end=' ')
            print()



