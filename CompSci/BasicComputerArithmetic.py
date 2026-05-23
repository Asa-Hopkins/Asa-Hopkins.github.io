import math

def sqrt(x):
    #use binary search to find sqrt(x)
    if x < 1:
        bounds = [x,1]
    else:
        bounds = [1,x]
        
    #Keep track of how much bounds changed since last iteration
    prev = max(bounds)
    while (bounds[1] - bounds[0]) < prev:
        prev = bounds[1] - bounds[0]
        y = (bounds[0] + bounds[1]) / 2
        if y*y > x:
            bounds[1] = y
        else:
            bounds[0] = y
    if abs(bounds[0]*bounds[0] - x) < abs(bounds[1]*bounds[1] - x):
        return bounds[0]
    else:
        return bounds[1]

def exp(x, n):
    #Use exponentiation by squaring
    #Also square rooting if necessary
    
    if n < 0:
        n = -n
        x = 1/x
    
    fraction = n % 1
    int_part = int(n - fraction)

    ans = 1

    temp = x
    while fraction > 0:
        fraction *= 2
        temp = sqrt(temp)
        if fraction >= 1:
            ans *= temp
            fraction -= 1

    while int_part > 0:
        if int_part & 1:
            ans *= x
        x *= x
        int_part //= 2
    return ans

def trig_table():
    #We know sin and cos of 360, 180, 90, and 45 degrees exactly
    sin = [0, 0, 1, 1/sqrt(2)]
    cos = [1,-1,0,1/sqrt(2)]
    while sin[-1] > 1e-10:
        sin.append(sqrt((1 - cos[-1])/2))
        cos.append(sqrt((1 + cos[-1])/2))
    return sin, cos

sin_table, cos_table = trig_table()

def sin_cos(x):
    #Input in degrees
    x /= 360
    x = x % 1.0 #Shift to range [0,1]
    i = 0
    #Start at an angle of 0
    s = 0
    c = 1
    while x > 0 and i < 30:
        x *= 2
        i += 1
        if x > 1:
            x = x - 1
            old_sin = s
            s = s*cos_table[i] + c*sin_table[i]
            c = cos_table[i]*c - old_sin*sin_table[i]
    return s, c

def log(b,x):
    if x < 0:
        return "Can't do log of negative number"
    
    
