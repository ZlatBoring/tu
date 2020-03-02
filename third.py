from util import *

if __name__== "__main__":
	N = 10000
	T = 100
	prs = [[0.7, 0.2, 0.1], [0.1, 0.6, 0.3], [0, 0, 1]]
	init_state = [1, 0, 0]
	count = simulate_with_absorb(N, T, prs, init_state)
	
	print(count)
	print(calculate_theor_absorb(prs, init_state))
	'''plot(simulate(N, T, prs, init_state)[init_state.index(1)], 
		calculate_theor_matrix(prs, init_state, T))
	'''
	