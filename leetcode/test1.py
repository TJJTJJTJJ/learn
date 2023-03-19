class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges)+1
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        guesses = set( (x, y) for x, y in guesses)
        cnt = 0
        def dfs(x, fa):
            nonlocal cnt 
            for y in graph[x]:
                if y!=fa:
                    if (x, y) in guesses:
                        cnt+=1
                    dfs(y, x)
        
        dfs(0, -1)
        print("cnt: ", cnt)
        res = 0
        def reroot(x, fa, cnt):
            nonlocal res
            # cnt: 表示以x为根节点时的命中数量
            print("reroot: ", x, cnt) 
            if cnt>=k:
                res+=1
            for y in graph[x]:
                if y!=fa:
                    if (x, y) in guesses:
                        cnt-=1
                    if (y, x) in guesses:
                        cnt+=1
                    reroot(y, x, cnt)
        reroot(0, -1, cnt)
        return res
            
cnt:  1
reroot:  0 1
reroot:  1 0
reroot:  7 0
reroot:  2 0
reroot:  4 0
reroot:  10 0
reroot:  16 1
reroot:  8 1
reroot:  13 1
reroot:  9 1
reroot:  11 1
reroot:  14 1
reroot:  15 1
reroot:  3 0
reroot:  5 0
reroot:  12 1
reroot:  6 0

cnt0:  1
reroot:  0 1
reroot:  1 0
reroot:  7 0
reroot:  2 1
reroot:  4 1
reroot:  10 1
reroot:  16 2
reroot:  8 2
reroot:  13 2
reroot:  9 1
reroot:  11 1
reroot:  14 1
reroot:  15 1
reroot:  3 1
reroot:  5 1
reroot:  12 2
reroot:  6 1