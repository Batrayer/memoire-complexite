class Condition:
    def __init__(self, left = None, right = None, operator = ""):
        self.left = left
        self.right =  right
        self.operator = operator

    def __str__(self):
        return "\n Left: " + str(self.left) +"\n Right: " + str(self.right) + "\n Operator: " + str(self.operator) + "\n"
