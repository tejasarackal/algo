import csv, random

FILE = "data/kagerMinCut.txt"
ATTEMPTS = 300


def get_vertices(edges):
    vertices = set()
    for first, second in edges:
        vertices.add(first)
        vertices.add(second)
    return vertices


def create_graph(connections):
    E = []

    for neighbours in connections:
        first = neighbours[0]
        for second in neighbours[1:]:
            if (second, first) not in E:
                E.append((first, second))

    V = get_vertices(E)
    G = {'vertices':V, 'edges':E}
    return G


def merge(edges, a, b):
    for first, second in list(edges):
        if first == b:
            edges.remove((first, second))
            edges.append((a, second))
        if second == b:
            edges.remove((first, second))
            edges.append((first, a))


def remove_self_loops(edges):
    for first, second in list(edges):
        if first == second:
            edges.remove((first, second))


def remove_rand_edge(graph):
    E = graph['edges']

    # select random edge
    random_edge = random.choice(E)
    E.remove(random_edge)

    # merge the vertices connecting the deleted edge
    merge(E, random_edge[0], random_edge[1])

    # remove any self loops generated in the process
    remove_self_loops(E)

    # recompiling the graph
    V = get_vertices(E)
    graph = {'vertices':V, 'edges':E}
    return graph


def random_contraction(graph):
    while len(graph['vertices']) > 2:
        graph = remove_rand_edge(graph)

    return graph


def mincut(connections):
    G = create_graph(connections)
    F = random_contraction(G)
    return len(F['edges'])


if __name__ == '__main__':
    lines = []
    with open(file=FILE) as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            lines.append(line)

    r = (mincut(lines) for i in range(0, ATTEMPTS))
    print('last min', min(r))

