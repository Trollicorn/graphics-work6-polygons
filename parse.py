from transform import *
from matrix import *
from draw import *
from curve import *
from solid import *

def argify(line):
    args = line.split()
    for i in range(len(args)):
        try:
            args[i] = int(args[i])
        except ValueError:
    #        print(args[0])
            pass
    return args

def parse(fname, edge, orders, screen, color):
    transform = {
        "scale": dilate,
        "move": translate,
        "rotate": rotate
    }
    shape = {
        "line": add_edge,
        "circle": circle,
        "hermite": hermite,
        "bezier": bezier,
        "box": box,
        "sphere": sphere,
        "torus": torus
    }
    f = open(fname, 'r')

    for line in f:
#        print(type(line))
        line = line[:len(line)-1]
    #    print("[" + line + "]")
        if line in transform:
            args = f.next()
            #print(args)
            args = argify(args)
            transform[line](orders,args)
        elif line in shape:
            args = f.next()
            args = argify(args)
            shape[line](edge,args)
        elif line == "apply":
            matrix_mult(orders,edge)
            clear_screen(screen)
            draw_lines(edge,screen,color)
        elif line == "ident":
            orders = new_matrix()
            ident(orders)
        elif line == "save":
    #        print_matrix(edge)
            name = f.next()
            name = name[:len(name)-1]
            save_extension(screen,name)
        elif line == "display":
            clear_screen(screen)
            draw_lines(edge,screen,color)
#            print_matrix(edge)
            display(screen)
        elif line == "clear":
            edge = []
        else:
            print line
    f.close()
