from collections import defaultdict

class graph:
    def __init__(self) -> None:
        self.v = defaultdict(list)
    def append(self, v_):
        self.v[v_] = []
    def connect(self, v1_, v2_, w):
        self.v[v1_].append((v2_, w))
    
    # UNION FIND DATA STRUTURE
    def prepareUnion(self):
        self.parent_ = {}
        for i in range(len(self.v)):
            self.parent_[i] = -1
            self.parent_[i + 1000] = -1
    def parent(self, v_):
        if self.parent_[v_] == -1:
            return v_
        else:
            return self.parent(self.parent_[v_])
    def setParent(self, v1_, v2_):
        if self.parent_[v1_] == -1:
            self.parent_[v1_] = v2_
        else:
            self.setParent(self.parent_[v1_], v2_)
    ## end of union find data structure

    def kruskal(self):
        # preprocess
        self.prepareUnion()

        # preparing edges (sorting in asc order)
        vertices_asc = [(a,e[0],e[1]) for a in self.v for e in self.v[a]]
        tmp = []
        while len(vertices_asc):
            a = vertices_asc.pop()
            tmp.append(a) if not (a in vertices_asc) else None
        vertices_asc = tmp
        vertices_asc.sort(key=lambda e: e[2],reverse=True)

        # adding edges in asc order
        path = []
        for edge in vertices_asc:
            p1 = self.parent(edge[0])
            p2 = self.parent(edge[1])
            if p1 != p2:
                self.setParent(edge[0], edge[1])
                path.append(edge)

        return sum(list(map(lambda e:(e[2] if not (e in path) else 0),vertices_asc)))
    
    # specific functions
    def checksumProblem(self, rows, costs):
        N = len(rows[0])
        for i in range(N):
            self.append(i)
            self.append(1000 + i)
        for i in range(N):
            for j in range(N):
                if rows[i][j] == -1:
                    self.connect(i, j + 1000, costs[i][j])
        
    	
t = int(input())
t0 = t

while t > 0:
    out_ = 0

    N = int(input())
    n = 0
    Rows = []
    while n < N:
        Rows.append([int(i) for i in input().split(' ')])
        n += 1
    n = 0
    Costs = []
    while n < N:
        Costs.append([int(i) for i in input().split(' ')])
        n += 1
    
    chk_rows = ([int(i) for i in input().split(' ')])
    chk_cols = ([int(i) for i in input().split(' ')])

    g = graph()
    g.checksumProblem(rows=Rows, costs=Costs)
    out_ = g.kruskal()

    print("Case #", t0 - t + 1, ": ", out_, sep='')
    t -= 1