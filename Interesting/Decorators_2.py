# Decorators

def outer_function(msg):
    def inner_function(msg2):
        print(msg)


greeting = outer_function('Hey hows it going')
greeting()

# outer_function(msg) basically = inter_function and to execute the function you have to add the closure.

hi_function = outer_function('Hi')
bye_function = outer_function('Bye')

hi_function()
bye_function()
