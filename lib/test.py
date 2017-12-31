#!/user/bin/python

import random

class test(object):
    def __init__(self):
        print("calling __init__")

    def dothis(self):
        self.randomValue = random.randint(1,10)


i = test()

i.dothis()

#print(i.randomValue)

#names = ('s', 'o','l','l')


#names[1]='y'

print (names)
