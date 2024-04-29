def f():
    t = [1, 2, 3]
    for i in t:
        print(i)
        yield i

print(f())