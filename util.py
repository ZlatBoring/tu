import random
import matplotlib.pyplot as plt
import numpy as np

def toss_coin(prs):
	state = 0
	pr = 0
	randomNumber = random.random()
	while pr != 1:
		pr += prs[state]
		if randomNumber < pr:
			return state
		state += 1

def simulate(N, T, prs, init_state):
	pos = init_state.index(1)
	count_array = [[0] * T for _ in range(len(init_state))]
	for _ in range(N):
		count_array[pos][0] += 1
		for j in range(1, T):
			pos = toss_coin(prs[pos])
			count_array[pos][j] += 1
		pos = init_state.index(1)

	for array in count_array:
		array[:] = [float(x) / N for x in array]
	
	return count_array

def simulate_with_absorb(N, T, prs, init_state):
	pos = init_state.index(1)
	steps_to_absorb = 0
	for _ in range(N):
		for j in range(1, T):
			if(prs[pos].count(1) == 1):
				steps_to_absorb += j - 1
				break
			pos = toss_coin(prs[pos])
		pos = init_state.index(1)

	return steps_to_absorb / N

def calculate_theor_matrix(prs, init_state, T):
	theor_array = []
	a = np.array(init_state)	
	for _ in range(T):
		theor_array.append(a[init_state.index(1)])
		b = np.array(prs, float)
		a = np.dot(a, b)
	return theor_array

def calculate_theor_linear(prs):
	prs = np.array(prs, float)
	prs = prs.transpose()
	for i in range(len(prs)): 
		prs[i][i] -= 1
		prs[len(prs) - 1][i] = 1
	
	b = np.array([0] * len(prs))
	b[len(prs) - 1] = 1
	theor_array = np.linalg.solve(prs,b)
	return theor_array

def calculate_theor_absorb(prs, init_state):
	if(prs[init_state.index(1)].count(1) == 1):
		return 0

	prs = np.array([[1 - prs[0][0], -prs[0][1]], 
					[-prs[1][0], 1 - prs[1][1]]], float)
	b = np.array([1] * 2)
	theor_array = np.linalg.solve(prs, b)
	return theor_array[init_state.index(1)]
	

def plot(pr_array, theor_array):
	plt.plot(pr_array)
	plt.plot(theor_array)
	plt.show() 
