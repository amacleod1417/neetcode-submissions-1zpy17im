class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [] 
        index = 0
        biggest = 9999999999999999
        zero = [0, 0]

        for i in range (len(points)):
            distance = math.dist(zero, points[i])
            print(distance)

            distances.append([distance, i])
            
        heapq.heapify(distances)
        print(distances)
        smallest = heapq.nsmallest(k, distances)
        
        print(smallest)
        indexes = [row[1] for row in smallest]
        print(indexes)
        sp = []
        for i in indexes:
            sp.append(points[i])


        return sp