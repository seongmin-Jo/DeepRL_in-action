# DeepRL_in-action

Rebuild code for Deep Reinforcement Learning in Action to make library and more fancy

See get_best_actions function of chapter 2

```
def get_best_action(actions):
	best_action = 0
	max_action_value = 0
	for i in range(len(actions)): 
		cur_action_value = get_action_value(actions[i]) 
		if cur_action_value > max_action_value:
			best_action = i
			max_action_value = cur_action_value
	return best_action
```

They didn't define not only action, but also get_action_valuse and there are more than one such function
Of course, there is no information about what is environment

In this repistory, l will fill up Undefined function and make a library for basic RL


## Chapter 2

 - 2.1 get_best_actions 
 - 2.2 Epsilon Greedy Starategy
 - 2.3 Reward Function
