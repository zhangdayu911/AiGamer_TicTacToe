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
        # 将state转化为一纬
        state_tuple = tuple(map(tuple, state))
        # print('state_tuple',state_tuple)
        # print('get方法',self.q_table.get((state_tuple, action), 0.0))
        return self.q_table.get((state_tuple, action), 0.0)

    def get_opponent_best_q_value(self,next_state):
        next_state_tuple = tuple(map(tuple, next_state))
        opponent_best_q_value = max([self.get_q_value(next_state_tuple, a) for a in self.get_legal_actions(next_state)],
                                    default=0.0)
        return opponent_best_q_value


    def update_q_value(self, state, action, reward, next_state):
        # 将state转化为元祖
        state_tuple = tuple(map(tuple, state))

        # print('state_tuple',state_tuple)
        # 获取当前Q值
        current_q_value = self.get_q_value(state_tuple, action)
        # print('current_q_value',current_q_value)
        # 判断self.get_legal_actions(next_state)不为空时执行，即下一步有剩余可选位置
        if  self.get_legal_actions(next_state) and reward !=5:
            # next_q_value_list=[]
            # 计算下一个状态的最大Q值
            # for a in self.get_legal_actions(next_state):
            #     # print('a为',a)
            #     a_value = self.get_q_value(next_state, a)
            #     # print('a_value为',a_value)
            #     next_q_value_list.append(a_value)
            #     # print('next_q_value_list为',next_q_value_list)
            # max_next_q_value = max(next_q_value_list)
            # print('max_next_q_value',max_next_q_value)
            # 根据Q-learning公式计算新的Q值
            new_q_value = current_q_value + self.alpha * (reward + self.gamma * (-self.get_opponent_best_q_value(next_state)) - current_q_value)
        else:
            new_q_value = reward
        # print('new_q_value', new_q_value)

        # 更新Q表
        self.q_table[(state_tuple, action)] = new_q_value
        # print('q_table',self.q_table)



    def get_legal_actions(self, state):
        #返回了当前剩余可选位置的list
        return [(i, j) for i in range(3) for j in range(3) if state[i, j] == 0]



    def choose_action(self, state,env):
        # 遍历所有可选动作的q_value
        q_values = {a: self.get_q_value(state, a) for a in self.get_legal_actions(state)}
        # 获取最大q值的行动
        max_q_value = max(q_values.values())
        best_actions = [a for a, q in q_values.items() if q == max_q_value]
        # 在q_vlaue中随机选择一个动作
        best_actions_index = random.randint(0, len(best_actions) - 1)
        best_action = best_actions[best_actions_index]

        # 获取当前已探索率
        state_tuple = tuple(map(tuple, state))
        legal_actions = self.get_legal_actions(state)
        known_actions = [action for action in legal_actions if (state_tuple, action) in self.q_table]
        if not legal_actions:
            known_epsilon = 0
        else:
            known_epsilon = len(known_actions) / len(legal_actions)

        # 计算 q_values 的平均值
        average_q_value = np.mean(list(q_values.values()))

        # 随机探索，如果小于探索值则随机探索；
        if np.random.uniform(0, 1) < self.epsilon or known_epsilon * average_q_value <= 5:  # 探索
            # 在当前剩余可选位置的list中随机选择一个
            location = self.get_legal_actions(state)
            return location[random.randint(0, len(location) - 1)]
        else:
            opponent_state, opponent_reward, opponent_done, _ = env.step(best_action)
            opponent_q_values = {o: self.get_q_value(opponent_state, o) for o in self.get_legal_actions(opponent_state)}
            if opponent_q_values.values():
                max_opponent_q_value = max(opponent_q_values.values())
                best_opponent_actions = [a for a, q in opponent_q_values.items() if q == max_opponent_q_value]
                # 在q_vlaue中随机选择一个动作
                best_opponent_actions_index = random.randint(0, len(best_opponent_actions) - 1)
                best_opponent_action = best_opponent_actions[best_opponent_actions_index]

                if max_q_value >= max_opponent_q_value :  # 利用Q表选择最优动作
                    # 返回最优动作
                    return best_action
                else:
                    best_action = best_opponent_action
                    return best_action



#  动作：
#  根据探索率和胜率选择对应探索还是执行；
#       探索策略（已探索率*胜率<=50%则执行探索率）：
#           选择未探索的路径
#       已知策略（已探索率*胜率>50%则执行已知策略）：
#           随机数<设定探索率：
#               选择未探索的路径
#           随机数>=设定探索率：
#               我方最高分策略（胜速）
#               阻拦对手最高分策略（胜速）



