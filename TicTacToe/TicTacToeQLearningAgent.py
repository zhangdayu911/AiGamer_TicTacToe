#!/usr/bin/env python3

import numpy as np
import random


class TicTacToeQLearningAgent:
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=1.0):
        self.epsilon = epsilon  # 探索率
        self.alpha = alpha  # 学习率
        self.gamma = gamma  # 折扣因子
        self.q_table = {}  # 初始化Q表为空字典

    def get_q_value(self, state, action):
        state_tuple = tuple(map(tuple, state))
        # print('state_tuple',state_tuple)
        return self.q_table.get((state_tuple, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        # 获取当前Q值
        current_q_value = self.get_q_value(state, action)
        # print('current_q_value',current_q_value)
        # self.get_legal_actions(next_state)不为空时执行，即下一步有剩余可选位置
        if  self.get_legal_actions(next_state):
            # 计算下一个状态的最大Q值
            max_next_q_value = max([self.get_q_value(next_state, a) for a in self.get_legal_actions(next_state)])
            # print('max_next_q_value',max_next_q_value)
            # 根据Q-learning公式计算新的Q值
            new_q_value = current_q_value + self.alpha * (reward + self.gamma * max_next_q_value - current_q_value)
            # print('new_q_value',new_q_value)
            # 将state转化为元祖
            state_tuple = tuple(map(tuple, state))
            # print('state_tuple',state_tuple)
            # 更新Q表
            self.q_table[(state_tuple, action)] = new_q_value
            # print('q_table',self.q_table)



    def get_legal_actions(self, state):
        #返回了当前剩余可选位置的list
        return [(i, j) for i in range(3) for j in range(3) if state[i, j] == 0]

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:  # 探索
            # 在当前剩余可选位置的list中随机选择一个
            location = self.get_legal_actions(state)
            return location[random.randint(0, len(location) - 1)]
        else:  # 利用Q表选择最优动作
            q_values = {a: self.get_q_value(state, a) for a in self.get_legal_actions(state)}
            max_q_value = max(q_values.values())
            best_actions = [a for a, q in q_values.items() if q == max_q_value]
            best_actions_index = random.randint(0, len(best_actions) - 1)
            return best_actions[best_actions_index]




