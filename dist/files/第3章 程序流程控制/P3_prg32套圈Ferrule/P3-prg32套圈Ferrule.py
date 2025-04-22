import turtle
r =10
head = 90
for i  in range (4):
   turtle.seth(head)
   turtle.circle(r) 
   r = r + 40
turtle.done()