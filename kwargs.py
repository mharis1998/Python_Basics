def name(**kwargs):
    print(kwargs)

def price_nicely(**kwargs):
    name(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')


price_nicely(name='Bob',age=25)

## Both Arguements

def both(*args,**kwargs):
    print(args)
    print(kwargs)

both(1,2,4,name='bob')