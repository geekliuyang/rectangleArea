class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        rectangleOne = rectangle()
        rectangleTwo = rectangle()
        
        rectangleOne.bottomX = A
        rectangleOne.bottomY = B
        rectangleOne.topX = C
        rectangleOne.topY = D
        
        rectangleTwo.bottomX = E
        rectangleTwo.bottomY = F
        rectangleTwo.topX = G
        rectangleTwo.topY = H
        
        length = 0
        height = 0
        result = 0
        intersert = 0
        
        oneArea = (rectangleOne.topX-rectangleOne.bottomX)*(rectangleOne.topY-rectangleOne.bottomY)
        twoArea = (rectangleTwo.topX-rectangleTwo.bottomX)*(rectangleTwo.topY-rectangleTwo.bottomY)
        
        topX = min(rectangleTwo.topX, rectangleOne.topX)  
        bottomX = max(rectangleTwo.bottomX, rectangleOne.bottomX)
        topY = min(rectangleTwo.topY, rectangleOne.topY)
        bottomY = max(rectangleTwo.bottomY, rectangleOne.bottomY)
        
        if bottomX < topX and bottomY < topY:
            intersert = (topX-bottomX)*(topY-bottomY)
        result = oneArea+twoArea -intersert
        return result
        
class rectangle():
    def __init__(self):
        self.bottomX = 0
        self.bottomY = 0
        self.topX = 0
        self.topY = 0

s = Solution()
result = s.computeArea(-1,-1,1,1,-1,-1,1,1)
print result