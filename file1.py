class ArithmeticOperations:
    def __init__(self):
        self.sum = 0
        self.product = 0
        self.difference = 0
        self.quotient = 0

    def get_sum(self, num1, num2):
        self.sum = num1 + num2
        return self.sum

    def get_difference(self, num1, num2):
        self.difference = num1 - num2
        return self.difference

    def get_product(self, num1, num2):
        self.product = num1 * num2
        return self.product

    def get_quotient(self, num1, num2):
        self.quotient = num1 / num2
        return self.quotient