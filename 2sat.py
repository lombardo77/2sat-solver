# verify that formula is 2SAT instance 
# construct 2SAT graph
# run SCC algorithm
import sys


def sat_solver(f):
    lst = verify(f)
    g = get_graph(lst)
    gr = reverse_graph(g, lst)
    kosaraju(g, gr)


def negate(x):
    if x[0] == "~":
        return x[1]
    else:
        return "~" + x[0]


def reverse_graph(g, lst):
    gr = get_graph(lst, inhabit = False)
    for v in g.keys():
        for n in g[v]:
            gr[n].append(v)
    return gr


def kosaraju(g, gr):
    stack = []
    visited = set()
    scc = []

    def dfs(g, n):
        visited.add(n)
        scc.append(n)
        for i in g[n]:
            if i not in visited:
                dfs(g, i)
        stack.append(n)

    for v in g.keys():
        if v not in visited:
            dfs(g, v)
    print("__________")
    visited = set()
    for v in stack[::-1]:
        if v not in visited:
            dfs(gr, v)
            print(scc)
            scc = []


def get_graph(lst, inhabit=True):
    g = {}
    for k in lst:
        for i in k:
            g[i] = []
            if i[0] == '~':
                g[i[1]] = []
            else:
                g["~" + i] = []
    if not inhabit:
        return g

    for i in lst:
        g[negate(i[0])].append(i[1])
        g[negate(i[1])].append(i[0])
    return g


def verify(f):
    f = f.replace(" ", "")
    return list(map(lambda x: x
                    .replace("(", "")
                    .replace(")", "")
                    .split("|"), f.split("&")))


if __name__ == "__main__":
    sat_solver(sys.argv[1])
