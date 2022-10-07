def move_east(dice):
    new_dice=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(4):
        for j in range(3):
            new_dice[i][j]=dice[i][j]
    new_dice[1][0]=dice[3][1]
    new_dice[1][1]=dice[1][0]
    new_dice[1][2]=dice[1][1]
    new_dice[3][1]=dice[1][2]
    return new_dice

def move_west(dice):
    new_dice=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(4):
        for j in range(3):
            new_dice[i][j]=dice[i][j]
    new_dice[1][0]=dice[1][1]
    new_dice[1][1]=dice[1][2]
    new_dice[1][2]=dice[3][1]
    new_dice[3][1]=dice[1][0]
    return new_dice

def move_south(dice):
    new_dice=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(4):
        for j in range(3):
            new_dice[i][j]=dice[i][j]
    new_dice[0][1]=dice[3][1]
    new_dice[1][1]=dice[0][1]
    new_dice[2][1]=dice[1][1]
    new_dice[3][1]=dice[2][1]
    return new_dice

def move_north(dice):
    new_dice=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(4):
        for j in range(3):
            new_dice[i][j]=dice[i][j]
    new_dice[0][1]=dice[1][1]
    new_dice[1][1]=dice[2][1]
    new_dice[2][1]=dice[3][1]
    new_dice[3][1]=dice[0][1]
    return new_dice

def find_direction(A,B,flag):
    if A>B: #시계방향 90도 회전
        if flag==0:#동쪽
            flag=2#남쪽
        elif flag==1:#서쪽
            flag=3
        elif flag==2:
            flag=1
        elif flag==3:
            flag=0
    elif A<B:
        if flag==0:#동쪽
            flag=3 #북쪽
        elif flag==1:#서쪽
            flag=2 #남쪽
        elif flag==2: #남쪽
            flag=0 #동쪽
        else: #북쪽
            flag=1
    else:
        flag=flag 
    return flag

def dfs(graph,x,y,target,visited):
    global cnt
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if graph[x][y]==target:
        if visited[x][y]==False:
            visited[x][y]=True
            cnt+=1
            for i in range(4):
                dfs(graph,x+dx[i],y+dy[i],target,visited)
            return True
    return False

def solution(N,M,K,graph):
    answer=0
    x=0
    y=0
    dice=[[0,2,0],[4,1,3],[0,5,0],[0,6,0]]
    flag=0
    for i in range(K):
        global cnt
        cnt=0
        visited=[[False]*M for i in range(N)]
        if flag==0: #동쪽으로 이동
            if y+1>=M: #현재 위치에서 동쪽으로 더 이상 갈 수 없다면
                y-=1 #현재 위치에서 서쪽으로 가야하니깐 하나 줄여주고
                dice=move_west(dice)
                flag=1
                flag=find_direction(dice[3][1],graph[x][y],flag)
            else: #현재 위치에서 동쪽으로 갈 수 있음
                y+=1 #현재 위치에서 동쪽으로 가고
                dice=move_east(dice) #주사위 굴려주고
                flag=find_direction(dice[3][1],graph[x][y],flag)
        elif flag==1: #서쪽으로 이동
            if y-1<0: #현재위치에서 서쪽으로 못감
                y+=1
                dice=move_east(dice)
                flag=0
                flag=find_direction(dice[3][1],graph[x][y],flag)
            else:
                y-=1
                dice=move_west(dice)
                flag=find_direction(dice[3][1],graph[x][y],flag)
        elif flag==2: #남쪽으로 이동
            if x+1>=N:#현재 위치에서 남쪽으로 더 이상 갈 수 없다면
                x-=1 #북쪽으로 가야함
                flag=3
                dice=move_north(dice)
                flag=find_direction(dice[3][1],graph[x][y],flag)
            else:
                x+=1
                dice=move_south(dice)
                flag=find_direction(dice[3][1],graph[x][y],flag)
        else: #북쪽으로 이동
            if x-1<0:#현재 위치에서 북쪽으로 더 이상 갈 수 없다면
                x+=1
                dice=move_south(dice)
                flag=2
                flag=find_direction(dice[3][1],graph[x][y],flag)
            else:
                x-=1
                dice=move_north(dice)
                flag=find_direction(dice[3][1],graph[x][y],flag)
        #점수구해야함
        dfs(graph,x,y,graph[x][y],visited)
        answer+=cnt*graph[x][y]
    print(answer)
cnt=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]   
N,M,K=map(int,input().split())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))
solution(N,M,K,graph)