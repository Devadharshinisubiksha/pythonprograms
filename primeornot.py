b=int(input())
if b>1:
  for i in range(2,b):
   if(b%i)==0:
    print("yes")
    break
  else:
      print("no")
