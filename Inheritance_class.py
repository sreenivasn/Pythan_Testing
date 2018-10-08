__author__ = 'Sreenivas narne'

class A:

    def __init__(self):
        print("this is super class initialization method")

    def feature1(self):
        print("feature1 is implemented in A class")

    def feature2(self):
        print("feature2 is implemented in A class")


class B(A):


    def feature3(self):
        super()
        print("feature3 is implemented")



b=B()
b.feature3()


