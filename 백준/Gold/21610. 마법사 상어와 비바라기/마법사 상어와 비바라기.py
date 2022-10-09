dx=[0,0,-1,-1,-1,0,1,1,1]
dy=[0,-1,-1,0,1,1,1,0,-1]
#대각선 위치 확인
cx=[-1,-1,+1,+1]
cy=[-1,+1,+1,-1]
def solution(N,M,arr,moves):
    answer=0
    cloud=[[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

    for d,s in moves:
        visited = [[False] * N for _ in range(N)]
        new_cloud = []
        # 구름 이동
        for r,c in cloud:
            new_r=(N+r+dx[d]*s)%N
            new_c=(N+c+dy[d]*s)%N
            new_cloud.append([new_r,new_c])
        #비뿌려
        for r,c in new_cloud:
            arr[r][c]+=1
            visited[r][c]=True
        #비 뿌린 칸의 대각선 위치 확인해서 0이 아닌 것의 갯수만큼 값 증가
        for r,c in new_cloud:
            count=0
            for index in range(4):
                new_r=r+cx[index]
                new_c=c+cy[index]
                if 0<=new_r<N and 0<=new_c<N:
                    if arr[new_r][new_c]!=0:
                        count+=1
            arr[r][c]+=count
        #구름 위치= 이전 구름 위치가 아닌 것 중에 2 이상인 것
        cloud=[]
        for i in range(N):
            for j in range(N):
                if arr[i][j]>=2 and visited[i][j]==False:
                    cloud.append([i,j])
                    arr[i][j]-=2
    for i in range(N):
        answer+=sum(arr[i])
    return answer
if __name__ == '__main__':
    N,M=map(int,input().split())
    arr=[]
    for i in range(N):
        arr.append(list(map(int,input().split())))
    moves=[]
    for i in range(M):
        moves.append(list(map(int,input().split())))
    print(solution(N,M,arr,moves))