from matrix import *
from draw import *
from math import cos,sin,pi


def add_poly(polygon,x0,y0,z0,x1,y1,z1,x2,y2,z2):
    add_point(polygon,x0,y0,z0)
    add_point(polygon,x1,y1,z1)
    add_point(polygon,x2,y2,z2)

def box(polygon, args): #[x,y,z,w,h,d]
    x = args[0]
    y = args[1]
    z = args[2]
    w = args[3] #width
    h = args[4] #height
    d = args[5] #depth
    ex = x + w
    ey = y - h
    ez = z - d

    #parallel xy plane
    add_poly(polygon,ex, y, z, x, y, z, x,ey, z)
    add_poly(polygon, x,ey, z,ex,ey, z,ex, y, z)
    add_poly(polygon, x, y,ez, x,ey,ez,ex,ey,ez)
    add_poly(polygon,ex,ey,ez,ex, y,ez, x, y,ez)
    #parallel yz plane
    add_poly(polygon, x,ey, z, x, y, z, x,ey, z)
    add_poly(polygon, x,ey, z,ex,ey, z,ex, y, z)
    add_poly(polygon, x, y,ez, x,ey,ez,ex,ey,ez)
    add_poly(polygon,ex,ey,ez,ex, y,ez, x, y,ez)

    add_edge(edge,[x,y,z,x+w,y,z]) #front top
    add_edge(edge,[x,y,z,x,y-h,z]) #front left
    add_edge(edge,[x,y-h,z,x+w,y-h,z]) #front bottom
    add_edge(edge,[x+w,y,z,x+w,y-h,z]) #front right
    add_edge(edge,[x,y,z-d,x+w,y,z-d]) #back top
    add_edge(edge,[x,y,z-d,x,y-h,z-d]) #back left
    add_edge(edge,[x,y-h,z-d,x+w,y-h,z-d]) #back bottom
    add_edge(edge,[x+w,y,z-d,x+w,y-h,z-d]) #back right
    add_edge(edge,[x,y,z,x,y,z-d]) #top left
    add_edge(edge,[x,y-h,z,x,y-h,z-d]) #bottom left
    add_edge(edge,[x+w,y,z,x+w,y,z-d]) #top right
    add_edge(edge,[x+w,y-h,z,x+w,y-h,z-d]) #bottom right

def sphere(edge,args): #[x,y,z,r]
    x = args[0]
    y = args[1]
    z = args[2]
    r = args[3]
    points = p_sphere(x,y,z,r)
#    print(points)
    for i in range(len(points)):
        px = points[i][0]
        py = points[i][1]
        pz = points[i][2]
        add_edge(edge,[px,py,pz,px+1,py,pz])

def torus(edge,args): #[x,y,z,r1,r2]
    x = args[0]
    y = args[1]
    z = args[2]
    r1 = args[3] #small circles
    r2 = args[4] #big circle
    points = p_torus(x,y,z,r1,r2)
    for i in range(len(points)):
        px = points[i][0]
        py = points[i][1]
        pz = points[i][2]
        add_edge(edge,[px,py,pz,px+1,py,pz])

def p_sphere(x,y,z,r):
    points = []
    num = 25.0
    for i in range(int(num)):
        phi = 2*pi*i/num
        cosphi = cos(phi)
        sinphi = sin(phi)
        for j in range(int(num)):
            theta = pi*j/num
            sintheta = sin(theta)
            costheta = cos(theta)
            points.append([int(r*costheta)+x, int(r*sintheta*cosphi)+y, int(r*sintheta*sinphi)+z])
    return points

def p_torus(x,y,z,r1,r2):
    points = []
    num = 25.0
    for i in range(int(num)):
        phi = 2*pi*i/num
        cosphi = cos(phi)
        sinphi = sin(phi)
        for j in range(int(num)):
            theta = 2*pi*j/num
            sintheta = sin(theta)
            costheta = cos(theta)
            points.append([int(cosphi*(r1*costheta+r2))+x, int(r1*sintheta)+y, int(sinphi*(r1*costheta+r2))+z])
    return points
