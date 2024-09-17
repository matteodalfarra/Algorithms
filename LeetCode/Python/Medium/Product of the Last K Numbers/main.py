class ProductOfNumbers(object):
    def __init__(self):
        self.numbers = [1]
    
    def add(self, num):
        if num == 0:
            self.numbers = [1]
        else:
            self.numbers.append(self.numbers[-1] * num)

    def getProduct(self, k):
        if k >= len(self.numbers):
            return 0
        else:
            return self.numbers[-1] // self.numbers[-1 - k]