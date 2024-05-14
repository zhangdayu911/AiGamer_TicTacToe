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
        # print('Round',round)
        # print('Action',action)
        # print(state)
        # 执行动作，获取执行完的棋盘状态、奖励和结束标志
        result_state, reward, done, _ = env.step(action)
        # print('result_state',result_state)
        # print('reward',reward)
        # print(done)

        # 更新Q值
        agent.update_q_value(state, action, reward, result_state)
        # 更新状态
        state = result_state
        round += 1


# 输出 Q 表
print("Final Q Table:")
for key, value in agent.q_table.items():
    print(key, "->", value)


# 游戏循环
play_again = True
while play_again:
    # 在环境中重置状态
    state = env.reset()
    done = False

    # 游戏循环
    while not done:
        # 玩家动作
        env.render()
        env.human_move()
        done, _ = env.check_winner()
        if done:
            break

        # AI动作
        state, _, done, _ = env.step(agent.choose_action(state))
        env.render()

    # 询问是否再玩一局
    play_again_input = input("是否再玩一局？(yes/no): ")
    play_again = play_again_input.lower() == "yes"


