from collections import deque

start = [0,1]
end = [9, 5]
arr = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]

def bfs(root):
    visited = [[0] * 10 for _ in range(10)]
    queue = deque([root])
    route_q = deque([[root]])
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    visited[start[0]][start[1]] = 1

    while queue:
        now = queue.popleft()
        route = route_q.popleft()
        if now[0] == end[0] and now[1] == end[1]: #end에 도착하면 끝내기
            return route
        for i in range(4):
            route_tmp = []
            for tmp in route:
                route_tmp.append(tmp)
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
                continue
            if arr[nx][ny] == 1 or visited[nx][ny] == 1:
                continue
            route_tmp.append([nx, ny])
            route_q.append(route_tmp)
            queue.append([nx, ny])        
            visited[nx][ny] = 1        

res = bfs(start)
print(res)
                 
