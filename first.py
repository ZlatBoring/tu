import random
import matplotlib.pyplot as plt
import numpy as np

def tossCoin(prs):
	state = 0
	randomNumber = random.random()
	pr = 0
	while pr != 1:
		pr += prs[state]
		if randomNumber < pr:
			return state
		state += 1

if __name__== "__main__":
	N = 10000
	T = 100
	prs = [[0.75, 0.25], [0.45, 0.55]]
	
	countPs0 = [0] * T
	countPs1 = [0] * T
	startPos = 0
	
	theorP0 = []
	a = np.array([1, 0])
	for i in range(T):
		theorP0.append(a[startPos])
		b = np.array(prs, float)
		a = np.dot(a, b)
	
	for i in range(N):
		ts = []
		for j in range(T):
			if(j > 0):
				startPos = tossCoin(prs[startPos])
				if(startPos == 0):
					countPs0[j] += 1
				if(startPos == 1): 
					countPs1[j] += 1
				ts.append(j)
			else :
				countPs0[j] += 1

	countPs0[:] = [float(x) / N for x in countPs0]
	countPs1[:] = [float(x) / N for x in countPs1]

	plt.plot(countPs0)
	plt.plot(theorP0)
	plt.show() 