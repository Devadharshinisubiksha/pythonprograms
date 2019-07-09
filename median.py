n1=int(input())
s1=list(map(int,input().split()))[:n1]
a1=s1.sort()
middleIndex =int( (len(s1))/2)
print(s1[middleIndex])
