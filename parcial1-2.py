temperatura = float (input ("ingrese temperatura:"))
escala = input("Es Fahrenheit(F)) o es celsius(C)?:"). lower()

if escala == "f":
    celcius = (temperatura - 32) * 5/9
    print(celcius)

elif escala == "c":
    Fahrenheit = temperatura * 1.8 + 32
    print(Fahrenheit)
else:
    print("escala incorrecta")