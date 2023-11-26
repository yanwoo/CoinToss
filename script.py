import random

def play_game(max_rounds):
    total_reward = 0
    rounds = 0

    while True:
        # max_roundsを超えたらゲーム終了
        rounds += 1
        if rounds > max_rounds:
            break

        # 50%の確率でゲーム終了
        if random.random() < 0.5:
            break

        reward = 2 ** rounds  # 当たった場合の報酬
        total_reward += reward

    return total_reward, rounds - 1

def calculate_expected_value(num_simulations, max_rounds):
    total_expected_value = 0
    max_implemented_round = 0
    max_reward = 0

    for _ in range(num_simulations):
        reward, rounds = play_game(max_rounds)
        total_expected_value += reward
        if max_implemented_round < rounds:
            max_implemented_round = rounds
        if max_reward < reward:
            max_reward = reward 

    expected_value = total_expected_value / num_simulations
    return expected_value, max_implemented_round, max_reward 

if __name__ == "__main__":
    num_simulations = 100000  # シミュレーション回数
    max_rounds = 100  # 最大ラウンド数

    expected_value, max_round, max_reward = calculate_expected_value(num_simulations, max_rounds)

    print(f"シミュレーション回数: {num_simulations}")
    print(f"最大ラウンド数: {max_rounds}")
    print(f"期待値: {expected_value}")
    print(f"最大試行ラウンド数: {max_round}")
    print(f"最大報酬: {max_reward}")
