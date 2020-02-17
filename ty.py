import turtle as t

def circle(x,y,r):
     p=1-r
     print(p)
     while(x!=y):
          if p<0:
               x=x+1
               y=y
               print(x,' ', y)
               p=p+4*x+1
               print(p)
          else:
               p>0
               x=x+1
               y=y-1
               p=p+4*(x-y)+1
               print(x,' ',y)
               print(p)
          t.pd()
          t.goto(x,y)
          t.goto(y,x)
          t.goto(y,-x)
          t.goto(x,-y)
          t.goto(-x,-y)
          t.goto(-y,-x)
          t.goto(-y,x)
          t.goto(-x,y)
         
         
     
          
     
circle(0,30,30)  
