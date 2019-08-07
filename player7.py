b16=list(input())
t16=len(b16)
new=''
for l in range (0,t16,2):
    b16[l],b16[l+1]=b16[l+1],b16[l]
print(*b16,sep='')
