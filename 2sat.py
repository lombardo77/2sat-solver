# verify that formula is 2SAT instance 
# construct 2SAT graph
# run SCC algorithm
import sys


def sat_solver(f):
    lst = verify(f)
    g = get_graph(lst)
    print(lst)
    for i in lst:
        g[negate(i[0])].append(i[1])
        g[negate(i[1])].append(i[0])
    print(g)


def negate(x):
    if x[0] == "~":
        return x[1]
    else:
        return "~" + x[0]


def get_graph(lst):
    g = {}
    for k in lst:
        for i in k:
            g[i] = []
            if i[0] == '~':
                g[i[1]] = []
            else:
                g["~" + i] = []
    return g


def verify(f):
    f = f.replace(" ", "")
    return list(map(lambda x: x
                    .replace("(", "")
                    .replace(")", "")
                    .split("|"), f.split("&")))


if __name__ == "__main__":
    sat_solver(sys.argv[1])
