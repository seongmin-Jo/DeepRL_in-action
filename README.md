# DeepRL_in-action

Rebuild code for Deep Reinforcement Learning in Action to make library and more fancy



def get_best_action(actions):
	best_action = 0
	max_action_value = 0
	for i in range(len(actions)): #A 
		cur_action_value = get_action_value(actions[i]) #B
		if cur_action_value > max_action_value:
			best_action = i
			max_action_value = cur_action_value
	return best_action







## Chapter 2

 - 2.1 get_best_actions
 - 2.2 Epsilon Greedy Starategy
 - 2.3 Reward Function
