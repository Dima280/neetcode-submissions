import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width = None):
        if width is not None:
            return length * width
        
        result = math.pi * length ** 2
        return round(result, 2)

    
        
    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
