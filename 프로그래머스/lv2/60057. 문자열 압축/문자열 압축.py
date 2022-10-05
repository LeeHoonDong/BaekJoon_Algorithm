def solution(s):
    answer=len(s)
    for i in range(1,len(s)//2+1):
        sample=s[0:i]
        compression=""
        count=1
        for j in range(i,len(s),i):
            if sample==s[j:j+i]:
                count+=1
            else:
                if count>=2:
                    compression+=str(count)+sample
                else:
                    compression+=sample  
                sample=s[j:j+i]
                count=1
        if count>=2:
            compression+=str(count)+sample
        else:
            compression+=sample
        answer=min(answer,len(compression))
    return answer