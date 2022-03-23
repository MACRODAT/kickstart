t = int(input())
t0 = t

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        pos = 0
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            pos = midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    if not found:
        pos = first
                
    return (pos, found)

class SortedDictForRabbit(dict):
    def __init__(self) -> None:
        # super()
        self.hl = [] ## helper list

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()
    
    def __setitem__(self, pos, val):
        it = (pos, val[0])
        if it[0] in self.__dict__:
            self.__dict__[it[0]].append(it[1])
        else:
            self.__dict__[it[0]] = [it[1]]
            i = binarySearch(self.hl, it[0])[0]
            self.hl.insert(i, it[0])

    def __len__(self) -> int:
        return len(self.hl)
    
    def pop(self):
        i = self.hl[-1]
        el = (i, self.__dict__[i])
        del self.hl[-1]
        del self.__dict__[i]
        return el

while t>0:
    out = 0

    R, C = [int(i) for i in input().split(' ')]
    Rows = []
    j = 0
    while j < R:
        Rows.append([int(i) for i in input().split(' ')])
        j += 1
    i = 0
    j = 0

    # FIFO STACK
    fifo = []
    # SORTED HISTOGRAM
    hist = SortedDictForRabbit()

    while i < R:
        while j < C:
            if Rows[i][j] in hist:
                hist[Rows[i][j]].append((i,j))
            else:
                hist[Rows[i][j]] = [(i,j)]

            j += 1
        j = 0
        i += 1

    i = 0
    j = 0
    
    def checkCell(pi, pj):
        val = Rows[pi][pj]
        if pi > 0 and abs(Rows[pi - 1][pj] - val) > 1:
            fifo.append((val - 1, (pi - 1, pj)))
        if pj > 0 and abs(Rows[pi][pj - 1] - val) > 1:
            fifo.append((val - 1, (pi, pj - 1)))
        if pi < R - 1 and abs(Rows[pi + 1][pj] - val) > 1:
            fifo.append((val - 1, (pi + 1, pj)))
        if pj < C - 1 and abs(Rows[pi][pj + 1] - val) > 1:
            fifo.append((val - 1, (pi, pj + 1)))

    while (hist).__len__() > 0:
        cur = hist.pop() # index 0 : largest !
        val = cur[0]
        for item in cur[1]:
            checkCell(item[0], item[1])

            while len(fifo):
                el = fifo.pop(0)
                el_i = el[1]
                old_val = Rows[el_i[0]][el_i[1]]
                Rows[el_i[0]][el_i[1]] = val - 1
                out += val - 1 - old_val

                hist[old_val].remove(el_i)
                if (val - 1 in hist):
                    hist[val - 1].append(el_i)
                else:
                    hist[val - 1] =  [el_i]
    print("Case #", t0 - t + 1, ": ", out, sep='')
    t -= 1