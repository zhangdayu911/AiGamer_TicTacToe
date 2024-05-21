#!/user/bin/env python3

import numpy as np
from TicTacToe.TicTacToeEnv import TicTacToeEnv
from TicTacToe.TicTacToeQLearningAgent import TicTacToeQLearningAgent
# 创建环境
env = TicTacToeEnv()
print("[Success]--Creating TicTacToeEnv")
# 创建智能体
agent = TicTacToeQLearningAgent()
print("[Success]--Creating TicTacToeQLearningAgent")
# 在环境中重置状态
state = env.reset()
# print("[Success]--env.reset")
# print(state)

# 默认游戏未结束
done = False
# print(done)


# 测试uniform方法，生成在指定范围内均匀分布的随机数
# i = 0
# while i <5 :
#     test_uniform = np.random.uniform(0, 1)
#     print(test_uniform)
#     i += 1



# # map方法的作用查看，将一个指定的函数应用于一个或多个迭代对象（如列表、元组等）中的每一个元素
# state = np.zeros((3, 3))
# print(state,'  --------  type:',type(state))
# map = map(tuple, state)
# print(map,'  --------  type:',type(map))
# state_tuple = tuple(map)
# print(state_tuple,'  --------  type:',type(state_tuple))



# 测试get方法
state_tuple = tuple(map(tuple, state))
# print('state_tuple',state_tuple)
print(q_table.get((state_tuple, action), 0.0))




#  井字棋策略

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
#               e.g.胜速决定了采用哪种已知策略，参考5子棋，对方2连3你必输，所以你选择冲4争子，放弃'阻拦对手高分策略'选择'我方最高分策略'；
#                   这里也可以采用双方得分对比来判断，下一步对方的分高意味着对方会比我们更快胜利？

#  策略表：(状态，玩家，行动，得分)
#       状态：状态+探索率
#           探索率：执行期需要根据当前状态下'探索率'和对应'状态得分'来判断是采用'探索策略'还是'执行策略'

#  得分（趋近胜利+趋近阻拦对手胜利？）



#  探索

#  复盘


