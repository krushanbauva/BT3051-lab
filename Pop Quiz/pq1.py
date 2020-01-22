# Pop quiz BT3051
# Krushan Bauva
# BE17B037

class BinaryNumber:
    def __init__(self, A = [0]):
        for i in A:
            if ((i>1) or (i<0)):
                raise ValueError("Check your input!")
        self.A = A
    
    def value(self):
        val = 0
        j = 0
        for i in self.A:
            val = val + i*(2**j)
            j = j+1
        return val
    
    def __str__(self):
        A_string = ""
        for i in self.A:
            A_string = A_string + "{}".format(i)
        A_string = A_string[ : : -1]
        return "[{}]_2".format(A_string)