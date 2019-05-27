def pretty(func):
    def inner():
        print ("I am ordinary")
        func("I am decorated")
    return inner

#@pretty
def ordinary(msg):
    print (msg)

pretty = pretty(ordinary)
pretty()
