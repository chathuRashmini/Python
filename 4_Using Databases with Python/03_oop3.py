class getSum:
    num = 10

    def _init_(self):
        #constructor
        print('I am constructed')
        print('So far sum = ', self.num)

    def getSumFunc(self, input):
        prevsum = self.num
        self.num = self.num + input
        print('Previous sum = ', prevsum, ' | input = ', input, ' | total = ', self.num)

    def _del_(self):
        print('I am distructed')
        print('Sum = ', self.num)

tot = getSum()

tot.getSumFunc(10)
tot.getSumFunc(20)
tot.getSumFunc(500)
tot = 100
