"""
Class variables:
1. Defined inside a class, but outside any method.
2. Shared by all objects (instances) of the class.
3. If one object changes a class variable (and it’s not shadowed by an instance variable),
   that change is visible to all other objects.
4. Accessible at class level and instance level (through ClassName.var or self.var).

Instance variables:
1. Defined inside methods (usually __init__) using self.
2. Each object (instance) has its own separate copy.
3. Accessible only through that specific object (instance level).
"""

class RateOfInterest:
    interest = 0.06     # Class variable
    def __init__(self, name, loan):
        self.name = name    # instance variable
        self.loan = loan    # instance variable

    def calc_interest(self):
        # print("Total interest", self.loan*self.interest) # Used self.interest so it will be changeable.
        print("Total interest", self.loan * RateOfInterest.interest) # Used RateOfInterest.interest so it is not changeable.
p1 = RateOfInterest("Manish", 400000)
p1.interest = 0.08
p1.calc_interest()

p2 = RateOfInterest("Joe", 400000)
p2.calc_interest()