def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        sample=s[0:i]
        compressed_word=""
        count=1
        for j in range(i,len(s)+i,i):
            if sample==s[j:j+i]:
                count+=1
            else:
                if count>=2:
                    compressed_word+=str(count)+sample
                else:
                    compressed_word+=sample
                sample=s[j:j+i]
                count=1
        answer=min(len(compressed_word),answer)
    return answer