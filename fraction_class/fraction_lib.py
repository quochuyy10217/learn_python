import os
os.system("clear")

class fraction():
    def __init__(self, numerator,denominator):  #numerator: Tu so, denominator: Mau so
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return "("+str(self.numerator)+"/"+str(self.denominator)+")"
    def __add__(self,other):
        tempOfNumerator = self.denominator*other.numerator + self.numerator*other.denominator
        tempOfDenominator = self.denominator * other.denominator 
        return tempOfNumerator,tempOfDenominator
    def __sub__(self,other):
        tempOfNumerator = self.numerator*other.denominator - self.denominator*other.numerator
        tempOfDenominator = self.denominator * other.denominator
        return tempOfNumerator,tempOfDenominator
    def __mul__(self,other):
        tempOfNumerator = self.numerator*other.numerator
        tempOfDenominator = self.denominator * other.denominator
        return tempOfNumerator,tempOfDenominator
    def __truediv__(self,other):
        tempOfNumerator = self.numerator*other.denominator
        tempOfDenominator = self.denominator * other.numerator
        return tempOfNumerator,tempOfDenominator
    def fraction_reduction(self):
        x = self.numerator
        y = self.denominator
        i = 2
        if x>y:
            while i in range(2,y+1):
                if (self.numerator%i==0)&(self.denominator%i==0):
                    self.numerator=self.numerator//i
                    self.denominator=self.denominator//i
                else:
                    i+=1
        elif x<y:
            for i in range(2,x+1):
                if (self.numerator%i==0)&(self.denominator%i==0):
                    self.numerator=self.numerator//i
                    self.denominator=self.denominator//i
                else:
                    i+=1
        else:
            self.numerator=1
            self.denominator=1
        return self.numerator,self.denominator
