ni6= []
def drime(o):
    z6 = 0
    for x in range(2,o-1):
        if o%x == 0:
            z6 =1
            break
    if not z6:
        ni6.append(o)

a6 ,yt6 = map(int,input().split())

for e6 in range(a6,yt6+1):
    drime(e6)
print(len(ni6))
