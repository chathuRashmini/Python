class getSum:
    num = 0

    def _init_(self):
        #constructor
        print('I am constructed')
        print('So far sum = ', self.num)

    def getSumFunc(self):
        self.num = self.num + 1
        print('So far sum = ', self.num)

    def _del_(self):
        print('I am distructed')
        print('Sum = ', self.num)

tot = getSum()

tot.getSumFunc()
tot.getSumFunc()
tot.getSumFunc()
tot = 100
