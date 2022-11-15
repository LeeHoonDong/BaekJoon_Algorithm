def solution(n):
    answer = ''
    dict_num={0:1,1:2,2:4}
    i=1 #자릿수
    while True: #i가 최대 16
        if n<=3*(3**i-1)//2:
            print(i)
            break
        i+=1
    arr=[]
    cnt=0
    start=3*(3**(i-1)-1)//2+1
    m=n-start #n=2 start=1 m=1 i=1
    # if i==0
    while True:
        if m==0:
            if cnt==i:
                break
            arr.append(dict_num[m])
            cnt+=1
        else:
            remain=m%3
            m=m//3
            arr.append(dict_num[remain])
            cnt+=1
    arr.reverse()
    for ele in arr:
        answer+=str(ele)
    return answer