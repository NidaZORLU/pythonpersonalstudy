class a:
    def m(self):
        print("m() from class a...")
class b(a):
    def m(self):
        print("m() from class b...")
class c(a):
    def m(self):
        print("m() from class b...")
class d(b,c):
    def m(self):
        print("m() from class d...")
        b.m(self)
        c.m(self)
        a.m(self)
def main():
    obj1=d()
    obj1.m()

if __name__=="__main__":
    main()