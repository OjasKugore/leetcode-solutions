class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        sum=0
        countright,countleft = 0,0
        res=[]
        for i in range(len(boxes)):
            if boxes[i] == '1':
                sum+=i
                countright+=1
        
        for i in range (len(boxes)):
            if i == 0:
                if boxes[i] == '1':
                    countright-=1
                    countleft+=1
                res.append(sum)
                continue
            
            sum = sum - countright + countleft
            if boxes[i] == '1':
                countright-=1
                countleft+=1
            res.append(sum)
        return res
            
                
                
