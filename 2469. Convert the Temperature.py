class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        l=[]
        Kelvin = celsius +273.15
        l.append(Kelvin)
        Farenheit = celsius * 1.80 + 32.00
        l.append(Farenheit)
        return l
    
