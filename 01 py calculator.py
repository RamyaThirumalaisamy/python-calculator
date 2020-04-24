print("py calc")
print("operators")
options=["add","sub","mul","div"]
print("1    add")
print("2    subtraction")
print("3    multiplication")
print("4    division")
while True:
    option=input(print("enter ur operator"))
    if option not in options:
        print("invalid")
    if option=="exit":
        break
    if option in options:
        a=input(print("enter 1 no"))
        b=input(print("entre 2 no"))
        a=float(a)
        print(a)
        b=float(b)
        print(b)
        if option=="add":
            c=a+b
            print("result is",c)
        elif option=="sub":
                c=a-b
                print("result is",c)
        elif option=="mul":
                    c=a*b
                    print("result is",c)
        elif option=="div":
            c=a/b
            print("result is",c)
       # else:
            #print("invalid")
        #else:
            #c=a/b
           # print("result is",c)


