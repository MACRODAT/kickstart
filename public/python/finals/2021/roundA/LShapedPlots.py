k = int(input())
k0 = k

while (k > 0):
    out = 0
    R, C = [int(i) for i in input().split(' ')]
    j = R
    Rows = []
    while j > 0:
        Rows.append([int(i) for i in input().split(' ')])
        j -= 1
    def maxGoodSegment(i0, j0, stepi = 1, stepj = 0):
        max_ = 0
        while (0 <= i0 + stepi < R) and  (0 <= j0 + stepj < C):
                i0 += stepi
                j0 += stepj
                if Rows[i0][j0] == 0:
                    return max_
                max_ += 1
        return max_

    class Bound:
        def __init__(self, R0, C0, default_ = 0) -> None:
            self.data = [[default_ for _ in range(C0)] for _ in range(R0)]
            self.R = R0
            self.C = C0
            self.defaultOutOfBounds = default_
        def d(self, i, j):
            if 0 <= i < self.R and 0 <= j < self.C:
                return self.data[i][j]
            else:
                return self.defaultOutOfBounds
        def __getitem__(self, k):
            return self.data[k[0]][k[1]]
    
    Top = Bound(R, C)
    Bottom = Bound(R, C)
    Left = Bound(R, C)
    Right = Bound(R, C)
 
    j = 0
    i = 0
    while (i < R):
        while (j < C):
            if Rows[i][j] != 0:
                Top.data[i][j] = 1 + Top.d(i - 1, j)
                Left.data[i][j] = 1 + Left.d(i, j - 1)
            j += 1
        j = 0
        i += 1
    i = R - 1
    j = C - 1
    while (i >= 0):
        while (j >= 0):
            if Rows[i][j] != 0:
                Bottom.data[i][j] = 1 + Bottom.d(i + 1, j)
                Right.data[i][j] = 1 + Right.d(i, j + 1)
            j -= 1
        j = C - 1
        i -= 1
    j = 0
    i = 0
    while (i < R):
        while (j < C):
            if Rows[i][j] != 0:
                #       mju
                #  mil (i,j)  mir
                #       mjd        
                mju = Top[i, j]
                mil = Left[i, j]
                mir = Right[i, j]
                mjd = Bottom[i, j]
                out += max(0, min(mju , (mir ) // 2) + min(mir , (mju ) // 2) - 2)
                out += max(0, min(mju , (mil ) // 2) + min(mil , (mju ) // 2) - 2)
                out += max(0, min(mjd , (mir ) // 2) + min(mir , (mjd ) // 2) - 2)
                out += max(0, min(mjd , (mil ) // 2) + min(mil , (mjd ) // 2) - 2)
            j += 1
        j = 0
        i += 1
    print('Case #', k0 - k + 1, ': ', out, sep='')
    k -= 1
