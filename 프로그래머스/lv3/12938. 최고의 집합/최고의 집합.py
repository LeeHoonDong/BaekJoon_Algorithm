def solution(n, s):
    answer = []
    if n>s:
        answer.append(-1)
        return answer
    p, q = divmod(s, n)
    answer = [p] * n
    for i in range(q):
        answer[i]+=1
    answer.sort()
    return answer