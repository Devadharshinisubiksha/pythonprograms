d1=int (input())
sum=0
c=d1
while c>0:
  digit=c%10
  sum+=digit**3
  c//=10
if d1==sum:
    print("yes")
else:
    print("no")      
