__author__ = 'Sreenivas narne'
def sum(a,*b):
    for i in b:
       a=a+i

    print(a)


sum(6,7,2,2,1,2)


def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b



fib(2000)
