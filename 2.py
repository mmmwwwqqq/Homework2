a=[]
n=int(input())
for i in range(n):
    im=input()
    if im.startswith('%%'):
         im=im.replace('%%','', 1)
    if '###' not in im: #По условиям '####', а в примере '###'
        a.append(im)
print(a)
