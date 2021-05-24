def fun(ls):
    diction={}
    for i in ls:
        #print(diction)
        if str(type(i)) in diction:
            diction[str(type(i))].append(i)
            
        else:
            diction[str(type(i))]=[i]
    return diction
ls=[1,1.3,7,4.4,'hi',[0,1],'45']
print(fun(ls))
