N=int(input())
group_word=0
for i in range(N):
	word=input().lower()
	cnt=0
	for i in range(len(word)-1):
		if word[i]!=word[i+1]:
			new_word=word[i+1:]
			if new_word.count(word[i])>0:
				cnt +=1
	if cnt==0:
			group_word+=1
print(group_word)