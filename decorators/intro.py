# decorators 


def my_deco(func):
    def wrapper():
        print('Before function runs')
        func()
        print('After function runs')

    return wrapper 

@my_deco
def hello():
    print('Hello World')

hello()

def greet():
    print('greetings')

greet()   
        