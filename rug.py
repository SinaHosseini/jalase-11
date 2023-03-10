
# class Rug:
def rug(len):
    if len % 2 == 1:
        s = 1
        x = 0
        f = 2
        print(" ", end="")
        for i in range(len):
            if s == len:
                for i in range(s):
                    print(x, end=" ")
                break
            else:
                s += 2
                x += 1
        f = 2
        d = 1
        g = 0
        h = 1
        for i in range(x):
            print("\n", x, end=" ")
            for i in range(h-1):
                print(x-g, end=" ")
            for i in range(len - f):
                print(x-d, end=" ")
            for i in range(h-1):
                print(x-g, end=" ")
            print(x, end=" ")
            f += 2
            d += 1
            g += 1
            h += 1
        g = 1
        d = 2
        f = 8
        for i in range(x-1):
            print("\n", x, end=" ")
            for i in range(h-2):
                print(x-g, end=" ")
                g += 1
            for i in range(f - len):
                print(x - d, end=" ")
            for i in range(h-2):
                print(x-d, end=" ")
                d -= 1
            print(x, end=" ")
            f += 2
            d += 1
            g -= 2
            h -= 1
        s = 1
        x = 0
        f = 2
        print("\n", "", end="")
        for i in range(len):
            if s == len:
                for i in range(s):
                    print(x, end=" ")
                break
            else:
                s += 2
                x += 1


rug(7)
