__author__ = 'Sreenivas narne'


class addition2nums:
    def adding(self,i,j):
        print(i+j)


class addition3nums:
    def adding(self,i,**j):

        for i,k in j.items():
            print(i,k)





a =addition3nums()
a.adding(2,mar1=3,mar2=5,mar3=6)