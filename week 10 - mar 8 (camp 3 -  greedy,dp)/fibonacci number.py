class Solution:
    def fib(self, n: int) -> int:
        visited = {0:0,1:1}
        def recursion(val,n):
            if n in visited:
                return visited[n]
            visited[n] =  recursion(val,n-1)+recursion(val,n-2)
            return visited[n]
        return recursion(0,n)