#makes my math look neater 
sq = lambda x : x*x
c = lambda x, y: sq(x) + sq(y) #x^2 + y^2
def testCoord(max_iter, x, y):
     #a,b = original coords
     a, b, iteration = float(x), float(y), 1
     while c(x,y) < 4 and iteration < max_iter:
         chekpntx=x ; x = ( sq(x) - sq(y) ) + a
         y = (2*chekpntx*y) + b
         iteration += 1
     return iteration 
        
