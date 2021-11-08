# Beispiel für die Berechnung des Schnittpunktes 2-er Geraden mittels Itaration 
def computeIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    
    print("Computing intersection of 2 straights...")
    
    print("\nBegin and end point of 1. straight:")
    print("point 1: {}/{}".format(x1,y1))
    print("point 2: {}/{}".format(x2,y2))
    
    
    gradient1 = (y2-y1)/(x2-x1)
    print("Gradient1: {}".format(gradient1))
     
    print("\nComputed x/y values of 1. straight:")
    x = x1
    y0 = y1-gradient1*x1
    while x<=x2:
       y = round(y0+gradient1*x,2)
       print("x1/y1={}/{}".format(x,y))
       x = round(x+0.1,2)
    
    print("\nBegin and end point of 2. straight:")
    print("point 3: {}/{}".format(x3,y3))
    print("point 4: {}/{}".format(x4,y4))
    gradient2 = (y4-y3)/(x4-x3)
    print("Gradient2: {}".format(gradient2))
    
    print("\nComputed x/y values of 2. straight:")
    x= x3
    y0 = y3-gradient2*x3
    while x<=x4:
       y = round(y0+gradient2*x,2)
       print("x2/y2={}/{}".format(x,y))
       x = round(x+0.1,2)
       
       
    print("\nTrying to find intersection of 1. and 2. straight:")
    if gradient1==gradient2:
        print("No intersection found due both straights are parallel!")
        return False

    x = min(x1,x3)
    found = False
    m1 = y1-gradient1*x1
    m2 = y3-gradient2*x3
    
        
    while x<=max(x2,x4):
        if x1<=x and x<=x2 and x3<=x and x<=x4:
           y5 = round(m1+gradient1*x,2)
           y6 = round(m2+gradient2*x,2)
           print("x/y1/y2: {}/{}/{}".format(x,y5,y6))
           if (y5==y6):
              print("Found intersection in point: {}/{}".format(x,y5))
              found = True
              break
        x = round(x+0.01,2)
    if found:   
        print("Intersection found!")
    else:
        print("Intersection not found!")
    return found
    
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
