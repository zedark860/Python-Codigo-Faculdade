
class ConversorTemperatura:

    @staticmethod
    def converter_Fahrenheit(temp:float) -> float:
        calc = ((temp * 1.8) + 32)
        return calc
    
    @staticmethod
    def converter_Celsius(temp:float) -> float:
        calc = ((temp - 32) / 1.8)
        return calc

if __name__ == "__main__":
    converter_temp = ConversorTemperatura()
    print(f"{converter_temp.converter_Fahrenheit(15):.1f} ºF")
    print(f"{converter_temp.converter_Celsius(40):.1f} ºC")


