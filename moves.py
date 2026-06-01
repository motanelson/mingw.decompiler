a="hello world\n"
b="#############\n"


_v=vars()
_v.update({'hello':1})
print(hello)
_a=dict(_v)

counter=0
for _b in _a:
    if len(_b)>0:
        
        
        if _b[0:1]!="_":
            print(_b+"#",end="")
            print(_a[_b])
    counter=counter+1