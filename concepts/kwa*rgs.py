def greet(name, nationality):
    print('Name is', name)
    print('From', nationality)

#here comes in kwargs
greet(nationality='Italy', name='Kayeem')    #the order placed doesn't matter
greet(name='NINE', nationality='mexico')

#another example
def employee(**kwargs):
    print(kwargs)

employee(name='Jack', age='22', nationality='cuban')   