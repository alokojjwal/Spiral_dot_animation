from random import randint
import turtle
turtle.bgcolor("black") #background colour
disp=turtle.Turtle()
width=5
height=7
dot_distance=25
disp.setpos(-250,250) #position of the graphics
disp.penup()
colours=["white","blue","orange","pink","yellow","green","violet","red","brown","grey","cyan"]
def Traversal_graphics(m,n):
    k=0
    l=0
    f=0
    col=randint(0,10)
    disp.color(colours[col])
    while (k<m and l<n):
        if(f==1):
            disp.right(90)
        for i in range(l,n):
            disp.dot()
            disp.forward(dot_distance)
        k+=1
        f=1
        
        disp.right(90)
        col=randint(0,10)
        disp.color(colours[col])
        for i in range(k,m):
            disp.dot()
            disp.forward(dot_distance)
        n-=1
        
        disp.right(90)
        col=randint(0,10)
        disp.color(colours[col])        
        if(k<m):
            for i in range(n-1,l-1,-1):
                disp.dot()
                disp.forward(dot_distance)
            m-=1
        disp.right(90)
        col=randint(0,10)
        disp.color(colours[col])
        if(l<n):
            for i in range(m-1,k-1,-1):
                disp.dot()
                disp.forward(dot_distance)
            l+=1
    turtle.done()

R=int(input("Enter the height factor (max 20): "))
C=int(input("Enter the width factor (max 20): "))


    
Traversal_graphics(R,C)