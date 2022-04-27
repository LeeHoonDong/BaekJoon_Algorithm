def solution(a):
    answer="yes"
    len_a=len(a)
    i=0
    while i<len_a//2:
        if a[i]!=a[-1-i]:
            answer="no"
            break
        i+=1
    return answer
while True:
    T=input()
    if T=="0":
        break
    print(solution(T))