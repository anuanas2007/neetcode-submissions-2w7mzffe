class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new = []
        for i in range(len(speed)):
            new.append([position[i],speed[i]])
        
        new.sort(reverse=True)

        fleets = 1
        prevt = (target - new[0][0])/new[0][1]

        for i in range(1, len(new)):
            curt = (target - new[i][0])/new[i][1]
            if curt > prevt:
                fleets += 1
                prevt = curt
        
        return fleets
            
        
