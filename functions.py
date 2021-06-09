'''
def hai():
    print('ourfirst function')
    print('ourfirst function statement12')

def bye():
    print('bye function')
    print('bye function statement12')
    
#print(hai)#we can print the address of the function
bye()
hai()
bye()
hai()
bye()
hai()

def add(a,b):
    print(a)
    print(b)
    print(a+b)

add(20,45)


def add(a=45,b=90):
    print(a)
    print(b)
    print(a+b)

#add(20,45)
#add(89)
add()


def add(a,b=99):
    print(a)
    print(b)
    print(a+b)

#add(20,45)
#add(89)
add(56,67,89)

def add(*args):
    #print(args)
    summ=0
    for i in args:
        summ+=i
    print(summ)

add(20,45)
add(89)
add(56,67,89)
add()


def add(**kwargs):
    #print(kwargs)
    summ=0
    for i in kwargs:
        summ+=kwargs[i]
    print(summ)

add(a=10,b=89,c=809)


def display(a,b=78,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

display(45,67,9,8,7,90,x=9,v=90)


def add():
    return 67+89

#print(add())
result=add()
print(result)



def add(a,b):
    return a+b

#print(add(78,89))
result=add(67,89)
print(result)
'''
'''def add(*args):
    #print(args)
    summ=0
    for i in args:
        summ+=i
    return summ

print(add(20,45))'''

def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
    
def primenumbers(l,u):
    for i in range(l,u+1):
        if isprime(i):
            print(i)
primenumbers(2,34)





        



































