a=lambda x:x+5
print(a(2))

b=lambda x,y : x + y
print(b(5,10))

grt=lambda x,y: x if(x>y) else y
print(grt(5,10))

sqr=lambda a:a*a
print(sqr(2))

lst=[1,2,3,4,5,6,7,8,9]
l=list(map(lambda x:x+5,lst))
print(l)

lst1=[1,2,3,4,5,6,7,8]
r=list(filter(lambda x:x%2,lst1))
print(r)

lst2=[1,2,3,4,5,6,7,8]
t=list(filter(lambda x:x%2==0,lst2))
print(t)



from functools import reduce
lst=[1,2,3,4,5,6,7,8,9]
y=reduce(lambda x,y:x+y,lst)
print(y)

from functools import reduce
lst1=[1,3,4,6,8,9]
y=reduce(lambda x,y:x if(x>y) else y,lst1)
print(y)

