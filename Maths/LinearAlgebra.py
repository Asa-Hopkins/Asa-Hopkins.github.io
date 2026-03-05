import numpy as np
from matplotlib import pyplot as plt


##ignore this bit, it's just some formatting to make the graphs look nicer
import seaborn as sns
sns.set_palette("bright")
#plt.rc('text', usetex=True)
plt.rcParams["svg.fonttype"] = 'none'
plt.rcParams['font.size'] = 14
plt.rcParams.update({'errorbar.capsize': 1.5})
plt.rcParams.update({'lines.markeredgewidth': 0.5})


#We'll use numpy to give us a more convenient array type
def eliminate(A):
    size = A.shape[0]
    #Step 1. Python uses 0 as the first row/column in arrays
    n = 0
    while n != size - 1:
        #Step 2, make sure we have a nonzero entry
        if A[n,n] == 0:
            #Check all rows to find a nonzero entry
            for i in range(1, size - n):
                if A[n+i,n] != 0:
                    #We found a row, swap it with the n'th row
                    A[[n,n+i]] = A[[n+i,n]]
                    break
                
            #If we failed to find a row, we go to step 10 and exit as a failure
            if A[n,n] == 0:
                return "Gaussian Elimination Failed"

        #Step 3, add a multiple of row n to the rows below it to make their n'th entry 0
        for i in range(1, size - n):
            A[n + i] += -A[n + i,n]/A[n,n] * A[n]
        #Step 4, add 1 to n and return to Step 2 unless we're at the bottom
        n += 1

    while n != 0:
        #Step 6, scale the row
        A[n] /= A[n,n]

        #Step 7, add a multiple of row n to the rows above it to make their n'th entry 0
        for i in range(0,n):
            A[i] += -A[i,n] * A[n]

        #Step 8, decrease n by 1 and go to step 6 unless we're at the top
        n -= 1
    return A
        

def augment(A,v):
    #Attach v to the right hand side of A
    return np.concat([A,v.reshape(-1,1)], axis=1)

#Set up our system of equations
x = np.array([-1,0,1])
A = np.vander(x)
v = np.sin(x)

print(f"Fitting degree 2 polynomial to sin(x)...\n")

A = augment(A,v)
print(f"The solved system is {eliminate(A)}, the same as by hand")

#Let's plot the two functions
x = np.linspace(-1.5,1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, np.sin(x), label='y = sin(x)')
plt.plot(x, x*np.sin(1), label='y = p(x)')
plt.legend()
plt.savefig('LinearAlgebraFig1.png', bbox_inches='tight', dpi=300)
plt.cla()

#Set up our system of equations
x = np.array([0,1,2,3,4,5,6])
A = np.vander(x)
v = np.cos(np.sqrt(x))

#Check our solution against numpy to be sure
solution = np.linalg.solve(A, v)

print(f"Fitting degree 6 polynomial to cos(sqrt(x))...\n")

A = augment(A,v)
A = eliminate(A)
print(f"Our solution is {A[:,-1]}")
if np.allclose(solution,A[:,-1]):
    print(f"and matches numpy!")

p = np.poly1d(A[:,-1])

x = np.linspace(0,6, 200)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, np.cos(np.sqrt(x)) - p(x), label='y = cos(sqrt(x)) - p(x)')

#Set up our system of equations again, but with different x positions
x = np.array([0,1,2,3,4,5,6])
x = np.cos((x + 0.5)*np.pi/7)

A = np.vander(x)

v = np.cos(np.sqrt((x+1)*3))

#Check our solution against numpy to be sure
solution = np.linalg.solve(A, v)

print(f"Fitting degree 6 polynomial to cos(sqrt(x))...\n")

A = augment(A,v)
A = eliminate(A)
print(f"Our solution is {A[:,-1]}, which is clearly completely wrong.")
print("The error is not with the algorithm per-se, but rather that computers are imprecise. It keeps dividing by nearly-0 numbers until the result is so large it runs out of digits and just says 'inf'")
print(f"This can be fixed, and numpy correctly gives {solution} as the solution, but that will be discussed later")
p = np.poly1d(solution)

x = np.linspace(0,6,200)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, np.cos(np.sqrt(x)) - p(x/3 - 1), label='y = cos(sqrt(x)) - best(x)')
plt.legend(loc='upper left')
plt.savefig('LinearAlgebraFig2.png', bbox_inches='tight', dpi=300)


