import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def read_txt(filename):
	res = []
	with open(filename, "r") as f:
		for line in f:
			res.append(float(line))
	return res

if __name__ == '__main__':
	res = read_txt('./market_data/risk_free.txt')
	annual = np.mean(res) / 100
	daily = (annual + 1)**(1/250) - 1
	print("Annual risk free: {}".format(annual))
	print("Daily risk free: {}".format(daily))
	# plt.plot(res, label='risk free rate')
	# plt.title('1-year T-bill rate (%)')
	# plt.legend(loc='lower right')
	# plt.show()
