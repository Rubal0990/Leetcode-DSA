class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        m = int(math.ceil(n/(2*numRows-1)))
        col = m*n
        a = [[0 for i in range(col)] for j in range(numRows)]
        i = 0
        j = 0
        si = 0
        up = False
        down = True

        if len(s) == 1 or numRows == 1:
            return s

        while si < n:
            for _ in range(numRows):
                if down and si < n:
                    a[i][j] = s[si]
                    i += 1
                    si += 1

                    if i == numRows:
                        i = numRows - 2
                        j += 1
                        if si < n:
                            up = True
                        down = False

            for _ in range(numRows):
                if up:
                    if i == 0:
                        i = 0
                        up = False
                        if(si<n):
                            down = True

                    else:
                        if si < n:
                            a[i][j] = s[si]
                            si += 1
                            i -= 1
                            j += 1       

        s = ""
        for i in range(numRows):
            for j in range(col):
                if a[i][j] != 0:
                    s = s + a[i][j]

        return s