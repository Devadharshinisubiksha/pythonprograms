d1=int (input())
sum=0
b=d1
while b>0:
  digit=b%10
  sum+=digit**3
  b//=10
if d1==sum:
    print("yes")
else:
    print("no")      
