import math
def my_quad_equation():
    #make so if a or b are equal to 1, they are not printed
    if valA ==1 and valB == 1:
        print("\nEquation is: f(x)=x**2+x+"+str(valC))
    elif valA ==1 and valB!= 1:
        if valB < 0 and valC < 0:
            print("\nEquation is: f(x)=x**2-"+str(abs(valB))+"x-"+str(abs(valC)))
        elif valB == -1 and valC < 0:
            print("\nEquation is: f(x)=x**2-x-"+str(abs(valC)))
        elif valB == -1 and valC > 0:
            print("\nEquation is: f(x)=x**2-x+"+str(valC))
        elif valB < 0 and valC > 0:
            print("\nEquation is: f(x)=x**2-"+str(abs(valB))+"x+"+str(valC))
        elif valB > 0 and valC < 0:
            print("\nEquation is: f(x)=x**2+"+str(valB)+"x-"+str(abs(valC)))
        else:  
            print("\nEquation is: f(x)=x**2+"+str(valB)+"x+"+str(valC))
    elif valB == 1:
        if valC < 0:
            print("\nEquation is: f(x)="+str(valA)+"x**2+x-"+str(abs(valC)))
        else:
            print("\nEquation is: f(x)="+str(valA)+"x**2+x+"+str(valC))    
    #make so if a or b are equal to -1, they are not printed but signs are changed
    elif valA ==-1 and valB == -1 and valC ==-1:
        print("\nEquation is: f(x)=-x**2-x-1")
    elif valA ==-1 and valB == -1:
        print("\nEquation is: f(x)=-x**2-x+"+str(valC))
    elif valA ==-1 and valB!= -1:
        if valB<0 and valC <0:
            print("\nEquation is: f(x)=-x**2-"+str(abs(valB))+"x-"+str(abs(valC)))
        elif valB<0:
            print("\nEquation is: f(x)=-x**2-"+str(abs(valB))+"x+"+str(valC))
        elif valC <0:
            print("\nEquation is: f(x)=-x**2+"+str(valB)+"x-"+str(abs(valC)))
        else:
            print("\nEquation is: f(x)=-x**2+"+str(valB)+"x+"+str(valC))
    elif valB == -1:
        if valC <0:
            print("\nEquation is: f(x)=-x**2+"+str(valB)+"x-"+str(abs(valC)))
        else:
            print("\nEquation is: f(x)="+str(valA)+"x**2-x+"+str(valC))
    #check if b,c is negative, fix equation
    elif valB < 0 and valC < 0:
        print("\nEquation is: f(x)="+str(valA)+"x**2-"+str(abs(valB))+"x-"+str(abs(valC)))
    elif valB < 0 and valC > 0:
        print("\nEquation is: f(x)="+str(valA)+"x**2-"+str(abs(valB))+"x+"+str(valC))
    elif valB > 0 and valC < 0:
        print("\nEquation is: f(x)="+str(valA)+"x**2+"+str(valB)+"x-"+str(abs(valC)))
    else:
        print("\nEquation is: f(x)="+str(valA)+"x**2+"+str(valB)+"x+"+str(valC)) #normal equation
    temp=input("\nPress Enter to continue...")#wait

def evaluate_quad_equation():
    x=float(input("Enter value for x: "))
    y=valA*(x)**2+valB*x+valC #calculate function with value x
    print("f("+str(x)+")= "+ str(y))
    temp=input("\nPress Enter to continue...")#wait
    #decide if minimum or maximum
    if valA<0:
        print("f(x) has maximum at x0="+str(x0)+" with value f(x0)="+str(y0))
    else:
        print("f(x) has minimum at x0="+str(x0)+" with value f(x0)="+str(y0))
    temp=input("\nPress Enter to continue...")#wait

def compute_discriminant():
    print("Solving for f(x)=0")
    print("Discriminant is",d)
    if d>0:
        print("Two real solutions:",x1,"and",x2)
    elif d==0:
        print("One real solution:",x0)
    elif d<0:
        print("No real solutions")
        #task 8, calculate and print complex solutions
        jx1=(-valB+1j*math.sqrt(abs(d)))/(2*valA)
        jx2=(-valB-1j*math.sqrt(abs(d)))/(2*valA)
        print("Complex solutions are ",jx1,"and",jx2)

def factorize_form():
    if d>0: #there are two solutions, x1 and x2
        if x1<0 and x2<0:
            #checking for sign issues
            if valA ==1:
                print("Factorize form is: f(x)=(x+"+str(abs(x1))+")(x+"+str(abs(x2))+")")
            else:
                print("Factorize form is: f(x)="+str(valA)+"*(x+"+str(abs(x1))+")(x+"+str(abs(x2))+")")
        elif x1<0:
            if valA ==1:
                print("Factorize form is: f(x)=(x+"+str(abs(x1))+")(x-"+str(x2)+")")
            else:
                print("Factorize form is: f(x)="+str(valA)+"*(x+"+str(abs(x1))+")(x-"+str(x2)+")")
        elif x2<0:
            if valA ==1:
                print("Factorize form is: f(x)=(x-"+str(x1)+")(x+"+str(abs(x2))+")")
            else:
                print("Factorize form is: f(x)="+str(valA)+"*(x-"+str(x1)+")(x+"+str(abs(x2))+")")
        else:
            if valA ==1:
                print("Factorize form is: f(x)=(x-"+str(x1)+")(x-"+str(x2)+")")
            else:
                print("Factorize form is: f(x)="+str(valA)+"*(x-"+str(x1)+")(x-"+str(x2)+")")
    elif d==0: #only solution is x0
        if x0<0:
            if valA==1:
                print("Factorize form is: f(x)=(x+"+str(abs(x0))+")**2")
            else:
                print("Factorize form is: f(x)="+str(valA)+"*(x+"+str(abs(x0))+")**2")
        else:
            if valA==1:
                print("Factorize form is: f(x)=(x-"+str(abs(x0))+")**2")
            else:
                print("Factorize form is: f(x)="+str(valA)+"*(x-"+str(abs(x0))+")**2")


print("Welcome to Quadratic Solver for f(x)=ax**2+bx+c\n")

#defining variables needed between functions
valA=float(input("Enter value for a: "))
valB=float(input("Enter value for b: "))
valC=float(input("Enter value for c: "))
x0=float(-valB/(2*valA)) #calculate extremum x0
y0=valA*(x0)**2+valB*x0+valC #calculate function value of extremum
d=(valB**2)-(4*valA*valC)
if d>0:#x1 and x2 cannot be calculated if d is less than zero, negative sqrt
    x1=(-valB+math.sqrt(d))/(2*valA)
    x2=(-valB-math.sqrt(d))/(2*valA)
if d > -1.0e-14 and d < 1.0e-14: #task 9, if d between +-1*10^-14, then it is equal to 0
    d=0.0

#run the functions
my_quad_equation()
evaluate_quad_equation()
compute_discriminant()
factorize_form()
print("\nThanks for using Quadratic solver!, come back soon")
 




        
