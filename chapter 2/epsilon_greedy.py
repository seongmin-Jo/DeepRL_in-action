import numpy as np
import get_best_action as get_best_action


class epsilon_greedy:
    def __init__(self):
        self.epsilon = 0.01
        
    def get_action(self):
        if np.random.rand() < self.epsilon:
            # 무작위 행동 반환
            action = env.action_space.sample()
        else:
            # 최고의 행동 선택 
            action = get_best_action(actions, rewards)
        return action
