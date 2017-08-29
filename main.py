

def args_demo():

    """Function arguments (written args by convention) and keyword arguments 
    (written kwargs by convention) can be packed implicitly using the * 
    operator."""
    def func(*args, **kwargs):     
        for arg in args:
            print arg
        for kwarg in kwargs:
            print kwargs[kwarg]

    func(1, 2, 3, a=4, b=5, c=6)    # prints 1\n2\n3\n4\n5\n6

    """We can instead store our arguments in collections: lists for ordinary 
    args, and dictionaries for kwargs."""
    list_args = [1, 2, 3]
    dict_args = {'a' : 4, 'b' : 5, 'c' : 6}

    """ We can then execute the same code by *unpacking* the collections (after 
    which they are repacked implicitly)."""
    func(*list_args, **dict_args)   # prints 1\n2\n3\n4\n5\n6


def iterator_demo():

    """A generator is a function containing the yield keyword. This allows us to 
    generate a sequence of values on demand."""
    def natural_range(n):
        for i in range(n):
            yield i + 1

    for i in natural_range(3):  # 1, 2, 3
        print i

    """To implement an iterator, we must implement the __iter__() and next() 
    methods in a class. Thus, we may use a for-in loop on a custom type."""
    class iterator:
        def __init__(self, items):
            self.index = 0
            self.items = items
        def __iter__(self):
            return self
        def next(self):
            if self.index < len(self.items):
                ret = self.items[self.index]
                self.index += 1
                return ret
            else:
                raise StopIteration()
        def generator(self):
            for item in self.items:
                yield item

    iterable = iterator([1, 2, 3])

    for val in iterable:    # 1, 2, 3
        print val

def closure_demo():

    """Closures are possible in languages supporting first-class functions, that 
    is, where functions are treated as first-class citizens (i.e. as any other 
    object). A closure is a record/struct of a function and environment. This is
    achieved by returning a function defined within another function, in which 
    variables are specified."""
    def encloser(x):
        def enclosed(y):
            return x + y
        return enclosed

    closure1 = encloser(1)  # bind function object to identifier closure1
    print closure1(1)       # prints 2

    closure2 = encloser(2)  # bind function object to identifier closure2
    print closure2(1)       # prints 3

    """The enclosed function will have access to the ``free variables'' defined 
    in the enclosing scope. In so doing, the same function can be initialised 
    with different parameters. Note the above could also be shorthanded to:"""
    def encloser(x):
        return lambda y : x + y

    """We can use closures to create decorated functions."""
    def get_text(name):
        return 'Hello, %s!' % name

    def decorator(func):
        def get_text_with_tags(name):
            return '<h1>%s</h1>' % func(name)
        return get_text_with_tags

    get_text = decorator(get_text)  # create decorated function
    print get_text('Joe')           # prints '<h1>Hello, Joe!</h1>'

    """Python provides syntactic sugar to automate the above"""
    @decorator
    def get_text(name):
        return 'Hello, %s!' % name

    print get_text('Joe')           # prints '<h1>Hello, Joe!</h1>'

    """Decoraters may be nested repeatedly:"""
    @decorator
    @decorator
    def get_text(name):
        return 'Hello, %s!' % name

    print get_text('Joe')           # prints '<h1>Hello, Joe!</h1>'

    """Memoisation is a useful application of decorators. We first define a 
    memoisation function."""
    def memoise(f):
        memo = {}
        def memoised_function(x):
            if x not in memo:
                memo[x] = f(x)
            return memo[x]
        return memoised_function

    @memoise
    def fibonnaci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonnaci(n-1) + fibonnaci(n-2)

    # fast execution--extremely slow without memoisation
    assert fibonnaci(100) == 354224848179261915075


if __name__ == '__main__':
    args_demo()
    iterator_demo()
    closure_demo()
