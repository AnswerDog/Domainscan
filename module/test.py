from itertools import chain
a =[]
b = []
a=['asas','sasa','qwer']
b=['cccc','vvvv','bbbb']
f = []
c = []
c=chain(a,b,f)
for i in c:
    print i
print c