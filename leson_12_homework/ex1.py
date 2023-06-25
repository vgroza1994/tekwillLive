def convert_temperature(temperature, unit):
    if unit == "C":
        converted_temperature = (temperature * 9/5) + 32
        converted_unit = "F"
    elif unit == "F":
        converted_temperature = (temperature - 32) * 5/9
        converted_unit = "C"
    else:
        print("Unitatea introdusă nu este validă.")
        return

    return converted_temperature, converted_unit


temperature = float(input("Introduceți temperatura: "))
unit = input("Introduceți unitatea curentă (C/F): ")


converted_temperature, converted_unit = convert_temperature(temperature, unit)


print("Temperatura convertită:", converted_temperature, converted_unit)