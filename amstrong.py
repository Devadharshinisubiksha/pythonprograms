b,c=map(int,input().split())
for d in range(b+1,c):
    sum=0
    num=d
    while num>0:
        dig=num%10
        sum+=dig**3
        num//=10
        if(d==sum):
            print(d)
