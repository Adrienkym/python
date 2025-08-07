def greet(*args):
    for name in args:
        print('I am', name)
greet('Kayeem', 'Den', 'Foreign')      


def sum(*args):
    ans=0
    for n in args:
        print(f'{ans}={ans} + {n}')
        ans=ans+n

        print('Ans is', ans)
        

sum(100,50,123)        