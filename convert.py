from os import system

n=int(input("choisie un nombre à convertir --> "))
b=int(input("choisie une base (min 2 et max 10 pour l'instantcar ça ira jusqu'a 16 max) --> "))
a=int(input("sur 4 ou 8 bits -->"))

def convert(n,b):

    l=[]
    
    while n > 0:
        m=n%b
        n=n//b
        l = l + [m]
        st=''
        j=0

        for i in range(len(l)):

            st = str(l[0+i]) + st
            i=i+1
            j=j+1
            
            if a==8 and j == 8:
                st = ' ' + st
                j=0
            elif a == 4 and j==4:
                st = ' ' + st
                j=0

    
    print(st)


convert(n,b)
system("pause")
