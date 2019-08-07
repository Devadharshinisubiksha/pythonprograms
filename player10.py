b6,re6=map(str,input().split())
b6=list(b6)
re6=list(re6)
cnt=0
for f in range(0,len(b6)):
        if(b6[f]!=re6[f]):
            cnt=cnt+1
if(cnt==1):
    print("yes")
else:
    print("no")
