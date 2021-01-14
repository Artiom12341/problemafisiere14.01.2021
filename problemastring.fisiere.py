with open ('input.2.txt','r') as f:
    s=f.readline()
c="""QWERTYUIOPĂÎÂASDFGHJKLȘȚZXCVBNM"""
d="""0123456789"""
e="""+-*/"""
j="""qwertyuiopasdfghjklzxcvbnm"""
v=''
for i in s:
    if i in c:
        v=v+str(i)
        with open ('litereA.txt','w') as f:
            f.write(v)
b=''
for a in s:
    if a in d:
        b=b+str(a)
        with open ('cifre.txt','w') as f:
            f.write(b)
n=''
for k in s:
    if k in j:
        n=n+str(k)
        with open ('litereB.txt','w') as f:
            f.write(n) 
m=''
for f in s:
    if f in e:
        m=m+str(f)
        with open ('operatori.txt','w') as f:
            f.write(m)
