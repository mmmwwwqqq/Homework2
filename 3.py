n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
p=int(input())
q=int(input())
print(sum(num[p-1:q]))
