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
			#use visited not to go for numbers already seen since they are seen before means their generation is better earlier
                if coin+i not in visited and coin+i <= amount:
                    visited.add(coin+i)
                    queue.append(coin+i)
            if counter == 0:
                generation += 1
                counter = len(queue)
            if amount in visited:
			#if amount is found in new generation just return the generaion 
                if counter == len(queue):
                    return generation
				#if amount is in generation not yet counted add one to generation count
                return generation+1
        return -1
        
        
        
