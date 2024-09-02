# 0 0 0
# 0 0 0
# 0 0 0
# A -> B

# f(x,y)=f(x-1,y)+f(x,y-1)
x=0
y=0
a=2
b=2
route=0
for i in range(3,3):
    print(i)
# x走1步或者y走1步
def f(x,y):
    if y==1:
        return 1
    if x==1:
        return 1
    return f(x-1,y)+f(x,y-1)
print(f(3,3))


