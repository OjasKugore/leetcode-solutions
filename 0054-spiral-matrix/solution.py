class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m
        left = 0
        right = n
        ans = []

        while top<bottom and left<right:
            for j in range (left, right):
                ans.append(matrix[top][j])
            top+=1
            for i in range (top, bottom):
                ans.append(matrix[i][right-1])
            right-=1
            if left>=right or top>=bottom:
                break
            for j in range (right-1, left-1, -1):
                ans.append(matrix[bottom-1][j])
            bottom -=1
            for i in range (bottom-1, top-1, -1):
                ans.append(matrix[i][left])
            left+=1
            
        return ans
