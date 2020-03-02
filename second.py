from util import *

if __name__== "__main__":
	N = 10000
	T = 100
	prs = [[0.2, 0.3, 0.5], [0.1, 0.7, 0.2], [0.1, 0.3, 0.6]]
	init_state = [1, 0, 0]
	count_array = simulate(N, T, prs, init_state)
	for i in range(len(prs)):
		print(count_array[i][T - 1])
	
	print("linear theory = ", calculate_theor_linear(prs))
	"""
	plot(count_array[init_state.index(1)], 
		calculate_theor_matrix(prs, init_state, T))
	"""