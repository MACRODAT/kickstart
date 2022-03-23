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
    j = 0
    i = 0
    while (i < R):
        while (j < C):
            if Rows[i][j] != 0:
                mjd, mju, mir, mil = maxGoodSegment(i, j, 1, 0),maxGoodSegment(i, j, -1, 0),maxGoodSegment(i, j, 0, 1),maxGoodSegment(i, j, 0, -1)      
                # mju += mjd
                # mir += mil
                # mju, mir = min(mju, mir), max(mju, mir)
                out += max(0, min(mju + 1, (mir + 1) // 2) + min(mir + 1, (mju + 1) // 2) - 2)
                out += max(0, min(mju + 1, (mil + 1) // 2) + min(mil + 1, (mju + 1) // 2) - 2)
                out += max(0, min(mjd + 1, (mir + 1) // 2) + min(mir + 1, (mjd + 1) // 2) - 2)
                out += max(0, min(mjd + 1, (mil + 1) // 2) + min(mil + 1, (mjd + 1) // 2) - 2)
                # if diff > 0:
                #     print((i,j), '  -  ', diff)
            j += 1
        j = 0
        i += 1
    print('Case #', k0 - k + 1, ': ', out, sep='')
    k -= 1