's'
def f():
    global s
    s += 'GFG'
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)


s = "Python is great!"
f()
print(s)