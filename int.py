x,y = input().split()
a = int(x)
b = int(y)
d = input().split()
sum = 0
for i in range(0,b,1):
  sum += int(d[i])
print(sum)
