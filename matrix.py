"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    bucket = []
    for r in matrix[0]:
        bucket.append("")
    for c in matrix:
        for r in range(len(c)):
            #print(str(c[r]))
            bucket[r] += str(c[r]) + " "
    for i in range(len(bucket)):
        print(bucket[i])

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    n = len(matrix)
    for c in range(n):
        for r in range(n):
            if  c == r:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
#ASSUMING SQUARE MATRIX
def matrix_mult( m1, m2 ):
    cols = len(m2) #num cols of m2
    rows = len(m1) #num rows of m2 same as num cols of m1

    #list to store values of current column as temp holder
    curr_col = []
    for r in range(rows):
        curr_col.append(0)

    for c in range(cols): #for each col
        for r in range(rows):
            #store values of col in temp holder
            curr_col[r] = m2[c][r]
        #    print(curr_col[r])
        #print("done")
        for r in range(rows):
            m2[c][r] = 0 #set new value to zero
            for i in range(rows):
            #    print(str(temp[r]) + "*" + str(m1[r][i]) + ", ")
            #    print(str(m2[c][r])+"+"+str(curr_col[i])+"*"+str(m1[c][i]))


                #add product of corresponding values
                m2[c][r]+= curr_col[i] * m1[i][r]
            #    print("="+str(m2[c][r]))
            #    print_matrix(m2)
            #    print("")


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def mag(v): #magnitude of vector
    s = 0
    for i in v:
        s += i * i
    return math.sqrt(s)

def normal(v): #normal vector
    s = mag(v)
    for i in range(len(v)):
        if v[i]!=0:
            v[i] = v[i] / s
    return v

def dot(v1,v2):
    s = 0
    for i in range(len(v1)):
        s += v1[i]*v2[i]
    return s

def cross(v1,v2): #cross product of 3d vectors
    x = v1[1]*v2[2] - v1[2]*v2[1]
    y = v1[2]*v2[0] - v1[0]*v2[2]
    z = v1[0]*v2[1] - v1[1]*v2[0]
    return [x,y,z]

def surf(polygon,index):
    a = polygon[index]
    b = polygon[index+1]
    c = polygon[index+2]
    d = [0,0,0]
    e = [0,0,0]
    for i in range(3):
        d[i] = b[i]-a[i]
        e[i] = c[i]-a[i]
    return normal(cross(d,e))
