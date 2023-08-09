a=[8,7,6,9,13,23,42,77]
def sumsquare (a):
    odd=0
    even=0
    for i in a:
        if i%2==0:
           even=even+i**2
        else:
           odd=odd+i**2
    a=[odd, even]
    return (a)
print(sumsquare(a))
