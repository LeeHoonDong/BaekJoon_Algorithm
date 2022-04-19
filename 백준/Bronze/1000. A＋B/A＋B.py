import sys
data= sys.stdin.readline().rstrip().split()
a=list(data)
sum=0
for i in a:
    sum+=int(i)
print(sum)
