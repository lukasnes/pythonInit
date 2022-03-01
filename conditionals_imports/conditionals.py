temperature = int(input("What's the temperature?\n"))

if temperature >= 100:
    print('Pool time!')
elif temperature < 100 and temperature >= 85:
    print('Great day for a walk in the park.')
elif temperature < 85 and temperature >= 50:
    print("It's chilly! Take a jacket.")
elif temperature < 50:
    print("It's freezing! Bundle up!")