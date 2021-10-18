tempincelsius = input("Please enter a temperature in Celcius... ")
tempinfahrenheit = float(tempincelsius) * 1.8 + 32
tempinfahrenheit = round(tempinfahrenheit, 2)
# round() is a method for limiting the number of decimal places
print(str(tempincelsius) + "° Celsius is " + str(tempinfahrenheit) + "° Fahrenheit.")
