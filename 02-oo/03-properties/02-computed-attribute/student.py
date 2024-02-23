# Write your code here
class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m) -> None:
        self.__weight_in_kg = weight_in_kg
        self.__height_in_m = height_in_m
    
    @property
    def bmi(self):
        return (self.__weight_in_kg / (self.__height_in_m**2))
    
    def category(self):
        if self.bmi() < 18.5:
            return ("underweight")
        elif 18.5 <= self.bmi() <= 25:
            return ("normal")
        elif self.bmi() > 25:
            return ("overweight")