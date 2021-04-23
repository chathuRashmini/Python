class getName:
    points = 0
    name = ""

    def _init_(self, inputName):
        #constructor
        self.name = inputName
        print(self.name, ' is constructed')

    def incPoints(self):
        prevsum = self.points
        self.points = self.points + 1
        print('Previous points = ', prevsum, ' | inputName = ', inputName, ' | total = ', self.points)

    def _del_(self):
        print('I am distructed')
        print('Sum = ', self.points)

class getPoints(getName):
    points = 0
    def countPoints(self):
        prevsum = self.points
        self.points = self.points + 10
        print('Previous points = ', prevsum, ' | inputName = ', inputName, ' | total = ', self.points)

e = getName("Edward")
e.incPoints()

b = getPoints("Bella")
b.incPoints()
b.countPoints()
