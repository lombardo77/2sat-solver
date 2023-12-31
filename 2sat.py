# verify that formula is 2SAT instance 
# construct 2SAT graph
# run SCC algorithm
import sys


def sat_solver(f):
    lst = verify(f)
    g = get_graph(lst)
    gr = reverse_graph(g, lst)
    scc = kosaraju(g, gr)
    vals = set()
    for s in scc[::-1]:
        for v in s:
            if negate(v) in s:
                print("Not sat!")
                break
            if v not in vals and negate(v) not in vals:
                vals.add(v)
                if v[0] == '~':
                    print(f"{negate(v)} = 0")
                else:
                    print(f"{v} = 1")


def negate(x):
    if x[0] == "~":
        return x[1]
    else:
        return "~" + x[0]


def reverse_graph(g, lst):
    gr = get_graph(lst, inhabit=False)
    for v in g.keys():
        for n in g[v]:
            gr[n].append(v)
    return gr


def kosaraju(g, gr):
    stack = []
    visited = set()
    scc, all = set(), []

    def dfs(g, n, log=False):
        visited.add(n)
        for i in g[n]:
            if i not in visited:
                if log:
                    scc.add(i)
                dfs(g, i, log)
        if not log:
            stack.append(n)

    for v in g.keys():  # first traversal
        if v not in visited:
            dfs(g, v)

    visited = set()
    for v in stack[::-1]:  # second traversal (on G^t)
        if v not in visited:
            scc.add(v)
            dfs(gr, v, log=True)
            all.append(scc)
            scc = set()

    return all  # returns scc in topological order


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
