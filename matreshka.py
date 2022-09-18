def matreshka(n):
    if n == 1:
        print("Matreshechka")
    else:
        print("Top of matreshka n=", n)
        matreshka(n-1)
        print("Botton matreshki n=", n)

matreshka(5)