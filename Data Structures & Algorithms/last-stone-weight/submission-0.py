class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            print(1, stones)
            heaviest1 = heapq.heappop(stones)
            heaviest2 = heapq.heappop(stones)
            print(2, stones)
            print(heaviest1, heaviest2)

            if heaviest2 > heaviest1:
                heapq.heappush(stones, heaviest1 - heaviest2)
                print(3, stones)
            
        if len(stones) > 0:
            return abs(stones[0])
        else:
            return 0
        
            




