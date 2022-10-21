def f1():
    s = ['Ilove GeeksforGeeks']
    def f2():
        s[0] = 'Me too'
        print(s)

    f2()
    print(s)

f1()