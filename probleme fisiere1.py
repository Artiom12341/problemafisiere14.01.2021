with open('globulete.txt','r') as f:
    a=f.readline()
x=int(a)*3
y=(int(a)+x)-2
c=int(a)+x+y
with open('bradut.txt','w') as f:
    f.write(str(c))
