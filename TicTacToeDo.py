from TicTacToe.TicTacToeEnv import TicTacToeEnv
from TicTacToe.TicTacToeQLearningAgent import TicTacToeQLearningAgent


# 创建环境
env = TicTacToeEnv()
print("[Success]--Creating TicTacToeEnv")

# 创建智能体
agent = TicTacToeQLearningAgent()
print("[Success]--Creating TicTacToeQLearningAgent")

# 训练智能体
for i in range(1000):
    # 在环境中重置状态
    state = env.reset()
    print("[Success]--env.reset")
    print(state)

    # 默认游戏未结束
    done = False
    print(done)

    round = 1
    # 未结束时执行下方循环
    while not done:
        # 选择动作
        action = agent.choose_action(state)
        print('Round',round)
        print('Action',action)
        print(state)
        # 执行动作，获取执行完的棋盘状态、奖励和结束标志
        result_state, reward, done, _ = env.step(action)
        print('result_state',result_state)
        print('reward',reward)
        print(done)

        # 更新Q值
        agent.update_q_value(state, action, reward, result_state)
        # 更新状态
        state = result_state
        round += 1

# 输出 Q 表
print("Final Q Table:")
for key, value in agent.q_table.items():
    print(key, "->", value)