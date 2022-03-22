class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, a):
            # if we get to the target amount return 1
            if a == amount:
                return 1
            # if we go over the amount return 0
            if a > amount:
                return 0
            # if we go out of bounds
            if i == len(coins):
                return 0
            # if we have already computed
            if (i, a) in cache:
                return cache[(i, a)]
            # case 1: choosing a coin at index i
            # case 2: skipped a coin at index i
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            # put the result in the cache
            return cache[(i, a)]
        
        return dfs(0, 0)