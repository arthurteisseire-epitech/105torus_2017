import argparse

def parse_all():
    parser = argparse.ArgumentParser()
    parser.add_argument("opt", type=int, help="1: Bisection\n2: Newton\n3:Secant", choices={1, 2, 3})
    parser.add_argument("a0", type=float, help="coefficient of the equation")
    parser.add_argument("a1", type=float, help="coefficient of the equation")
    parser.add_argument("a2", type=float, help="coefficient of the equation")
    parser.add_argument("a3", type=float, help="coefficient of the equation")
    parser.add_argument("a4", type=float, help="coefficient of the equation")
    parser.add_argument("n", type=int, help="precision")
    args = parser.parse_args()
    return (args)
