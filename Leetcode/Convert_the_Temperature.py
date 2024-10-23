class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:    
       Fahrenheit = celsius * 1.80 + 32.00
       Kelvin = celsius + 273.15
       return[Kelvin,Fahrenheit]
