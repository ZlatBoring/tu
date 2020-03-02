from util import *

if __name__== "__main__":
	N = 10000
	T = 100
	prs = [[0.7, 0.3], [0.4, 0.6]]
	init_state = [0, 1]
	count_array = simulate(N, T, prs, init_state)
	plot(count_array[init_state.index(1)], 
		calculate_theor_matrix(prs, init_state, T))
	