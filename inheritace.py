class A:
    def __init__(self):
        print("in init A")

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")


class B:
    def __init__(self):
        print("init in B")


    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")
class C(A,B):
    def __init__(self):

        print("init in C")


    def feature5(self):
        print("feature5 is working")
        super().feature3()

    def feature6(self):
        print("feature6 is working")



c = C()

c.feature5()