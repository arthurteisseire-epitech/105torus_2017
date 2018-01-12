def bisection(a0, a1, a2, a3, a4, n):
	x_d = 0
	x_f = 1
	for i in range(0, 15):
		x_n = (x_d + x_f) / 2
		print('%.*g' %(n, x_n))
		y_d = f4(x_d, a0, a1, a2, a3, a4)
		y_f = f4(x_f, a0, a1, a2, a3, a4)
		if ((y_d >= 0 and y_f <= 0) or (y_d <= 0 and y_f >= 0)):
			x_f = x_n
		else:
			x_d = x_n

def f4(x, a0, a1, a2, a3, a4):
	return (a4 * pow(x, 4) + a3 * pow(x, 3) + a2 * pow(x, 2) + a1 * x + a0)
