def print_format(x_n, n):
    if (float(str(x_n).rstrip('0')[:int(n) + 2]) == x_n):
        print('x = {x_n:.{n}g}'.format(x_n = x_n, n = n))
    else:
        print('x = {x_n:.{n}f}'.format(x_n = x_n, n = n))
