class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = set()
        queue = deque()
        generation = 0
        if amount == 0:
            return generation
        for i in coins:
            visited.add(i)
            queue.append(i)
        generation += 1
        if amount in visited:
            return generation
        counter = len(queue)
        while queue:
            coin = queue.popleft()
            counter -=1
            for i in coins:
                if coin+i not in visited and coin+i <= amount:
                    visited.add(coin+i)
                    queue.append(coin+i)
            # print(queue,generation)
            if counter == 0:
                generation += 1
                counter = len(queue)
            if amount in visited:
                if counter == len(queue):
                    return generation
                return generation+1
        return -1
        
        
        