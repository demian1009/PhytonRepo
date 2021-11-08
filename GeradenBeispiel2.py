
def computeIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    
    print("Computing intersection of 2 straights...")
    
    print("\nBegin and end point of 1. straight:")
    print("point 1: {}/{}".format(x1,y1))
    print("point 2: {}/{}".format(x2,y2))
       
    g1 = (y2-y1)/(x2-x1)
    print("Gradient1: {}".format(g1))
    
    m1 = y1-g1*x1
    print("y value: {}".format(m1))
   
    print("\nBegin and end point of 2. straight:")
    print("point 3: {}/{}".format(x3,y3))
    print("point 4: {}/{}".format(x4,y4))
   
    g2 = (y4-y3)/(x4-x3)
    print("Gradient2: {}".format(g2))
    
    m2 = y3-g2*x3
    print("y value: {}".format(m2))
      

    print("\nCompute intersection of 1. and 2. straight:")
 
    if g1==g2:
        print("No intersection found due both straights are parallel!")
        return False
        
        
    x = (m2-m1)/(g1-g2);
    y = g1*x+m1;
    
    
    a1 = min(x1,x2) 
    a2 = max(x1,x2)
    
    a3 = min(x3,x4) 
    a4 = max(x3,x4)
    
    b1 = min(y1,y2) 
    b2 = max(y1,y2)
    
    b3 = min(y3,y4) 
    b4 = max(y3,y4)
      
 
    if a1<=x and x<=a2 and a3<=x and x<=a4 and b1<=y and y<=b2 and b3<=y and y<=b4:
        print("Intersection found in point {}/{}!".format(round(x,2),round(y,2)))
        return True
    
    print("No intersection found!")
    return False



print("\n1. example:")    
computeIntersection(0,0,1,1,0,1,1,0)


print("\n2. example:")   
computeIntersection(0,-0.5,1,1,0,-1,0.5,1)
    
    
print("\n3. example:")   
computeIntersection(0,0,1,1,-1,1,0.5,-1)


print("\n4. example:")   
computeIntersection(-1,-1,1,1,-1,1,1,-1)


print("\n5. example:")   
computeIntersection(-1,1,0.5,-1,0,-1,1,1)
