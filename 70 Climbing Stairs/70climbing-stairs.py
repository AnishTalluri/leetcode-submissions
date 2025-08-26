class Solution:
    def climbStairs(self, n: int) -> int:
        stored_instances = {1:1, 2:2}

        def climb(n):
            if n in stored_instances:
                return stored_instances[n]
            else:
                stored_instances[n] = climb(n-1) + climb(n-2)
                return stored_instances[n]
        
        return climb(n)