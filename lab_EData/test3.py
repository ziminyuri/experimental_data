

class Pidor():
    def __init__(self,c):
        self.x = 1
        self.v = c

def main():
    p = Pidor(2)
    m = Pidor(3)
    s = Pidor(4)

    a = []
    a.append(p)

    for obf in a:
        print(obf.x)



if __name__=="__main__":
    main()