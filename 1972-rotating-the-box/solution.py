class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid[0]) #no of cols
        n = len(boxGrid) #no of rows

        for i in range (n):
            current = m-1
            mover = current-1
            while mover >=0:
                if boxGrid[i][current] == '.':
                    if boxGrid[i][mover] == '#':
                        boxGrid[i][current], boxGrid[i][mover] = boxGrid[i][mover], boxGrid[i][current]
                        current -=1
                        mover-=1
                    elif boxGrid[i][mover] == '*':
                        current = mover-1
                        mover-=2
                    else:
                        mover-=1
                else:
                    current -=1
                    mover = current-1

        ans = [['.' for _ in range (n)] for _ in range (m)]

        for i in range(n):
            for j in range(m):
                
                ans[j][n - 1 - i] = boxGrid[i][j]
        return ans
