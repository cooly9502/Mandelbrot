#makes math look neater
sq = lambda x : x * x 

def testCoord(max_iter, x_in, y_in):
    #Stores original coordinates
    a, b, iteration = float(x_in), float(y_in), 1
    #Iteration 1 is easier just to do this math...
    c = sq(x_in) + sq(y_in)
    if c >= 4:
        return iteration
    else:
        max_iter -= 1
        while max_iter != 0:
            iteration += 1
            z = {'x' : sq(a) - sq(b), 'y' : 2*a*b}
            a, b = z['x'] + x_in, z['y'] + y_in
            if sq(a) + sq(b) >= 4:
                return iteration
                max_iter = 0
            elif max_iter == 1:
                return iteration
            else:
                max_iter -= 1
                pass #(move on to next iteration)
            


        
