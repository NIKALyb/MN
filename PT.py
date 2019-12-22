def pt():
    import math
    a = int(input("Введите а--> ")) 
    b = int(input("Введите b--> ")) 
    c = int(input("Введите c--> "))
    p =(a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
pt()
