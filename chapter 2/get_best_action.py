import numpy as np
import gym

class get_beset_action():
    
    def __init__(self,  episodes):
        self.episodes = episodes
        
    def get_action_and_reward(self):
        actions = np.zeros(self.episodes)
        rewards = 0
        
        for episode in range(1, self.episodes):
            env = gym.make('CartPole-v0')
            state = env.reset()
            done = False
            
            while not done:
                action = env.action_space.sample()
                n_state, reward, done, info = env.step(action)
                actions[episode] = action
                rewards += reward
            actions.tolist()
    
        return actions, rewards
        
    def get_best_action(self, actions, rewards):
        best_action = 0
        max_action_value = 0
        for action in actions:
            cur_action_value = rewards
            if cur_action_value > max_action_value:
                best_action = action
                max_action_value = cur_action_value
        return best_action
