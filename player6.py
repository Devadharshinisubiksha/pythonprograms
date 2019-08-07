b16,b26=map(str,input().split())
for u in b16:
    p=b16.count(u)
for y in b26:
    q=b26.count(y)
if(p==q):
    print("yes")
else:
    print("no")
