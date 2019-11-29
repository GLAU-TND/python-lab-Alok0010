class MyException(Exception):
    def __init__(self,v):
        self.v=v

    def __str__(self):
        print(v)

a=int(input())
b=int(input())
def xyz(a,b):
    return a+b

if xyz(a,b)>150:
    print(a+b)
    
else:
    raise MyException('Custom Exception Occured')

