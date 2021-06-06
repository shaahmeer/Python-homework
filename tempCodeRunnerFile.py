def tochkanapryamoy():
    k,b = map(float, input().split('x'))    
    x,y = map(float, input().split(';'))    
    if k*x+b==y:
        print(True)
    else:
        print(False)

tochkanapryamoy()

