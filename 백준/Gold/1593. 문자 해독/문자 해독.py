import sys
def check_dict(dict_W):
    for key in dict_W.keys():
        if dict_W[key]!=0:
            return False
    return True
def solution(W,S,g,s):
    answer=0
    dict_W={}
    for i in W:
        if i in dict_W.keys():
            dict_W[i]+=1
        else:
            dict_W[i]=1
    #딕셔너리 만들었고
    start=0
    compare_word=S[start:start+g]
    for cw in compare_word:
        if cw in dict_W.keys():
            dict_W[cw]-=1
    if check_dict(dict_W)==True:
        answer+=1
    while start+g<s:
        if S[start] in dict_W.keys():
            dict_W[S[start]]+=1
        if S[start+g] in dict_W.keys():
            dict_W[S[start+g]]-=1
        start+=1
        if check_dict(dict_W)==True:
            answer+=1
    print(answer)

input=sys.stdin.readline
g, s=map(int,input().split())
W=input().rstrip()
S=input().rstrip()
solution(W,S,g,s)