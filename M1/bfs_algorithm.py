from collections import deque

start = [0, 4]
end = [9, 2]
# 
arr = [[1,1,1,1,0,1,1,1,1,1],
       [1,0,0,0,0,1,1,1,1,1],
       [1,0,1,1,0,0,0,0,0,1],
       [1,0,1,1,0,1,0,1,0,1],
       [1,0,1,1,0,1,0,0,0,1],
       [1,0,1,0,0,1,0,1,1,1],
       [1,0,1,0,1,1,0,0,1,1],
       [1,0,1,0,1,1,1,0,1,1],
       [1,1,0,0,0,0,0,0,1,1],
       [1,1,0,1,1,1,1,1,1,1]]

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
        print(now)
        print("is now")
        if now[0] == end[0] and now[1] == end[1]: #end에 도착하면 끝내기
            return route
        for i in range(4):
            route_tmp = []
            for tmp in route:
                route_tmp.append(tmp)
            print(now)
            print("is now")
            print(now[0])
            print("is now_row")
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
            
def optimize(path):
    result = [path[0]]
    index, cur = 1, 0
    row_change, col_change = False, False
    while index < len(path):
        if path[cur][0] != path[index][0]:
            row_change = True
        else:
            col_change = True
        if row_change and col_change:
            result.append(path[cur])
            if path[cur][0] != path[index][0]:
                col_change = False
            else:
                row_change = False
        cur+=1
        index+=1
    result.append(path[cur])
    return result

res = bfs(start)
print(res)
print("is bfs")
res = optimize(res)
print(res)     
print("is aptimize")           
