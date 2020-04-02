info = []

def print_temperature_line(day, month, temp):
    print(day + "." + month + " ", end = "")
    print("   "*(temp + 5) + "-", end = "")
    print()

def print_temperature_axis():
    print("      ", end="")
    for i in range(-5,16):
        print("{:02d} ".format(i), end="")
    print()

def number1(data):
    data.clear()

    inputfile = input("Give name of the file: ")

    with open(inputfile, "r") as readfile:
        readfile.readline()
        for row in readfile:
            row = row.strip()
            details = row.split(";")
            data.append(details)

    dot = inputfile.index(".")
    print("Loaded weather data from", inputfile[:dot].capitalize())

def number2(data):
    original = input("Give a date (dd.mm): ")
    user_input = original.split(".")
    date = user_input[1] + "-" + user_input[0]
    for details in data:
        if date == (details[0])[6:11]:
            print("The weather on %s was on average %s centigrade" % (original, details[2]))
            print("The lowest temperature was %s and the highest temperature was %s" % (details[3], details[4]))
            print("There was %s mm rain" % details[1])

def number3(data):
    mean_temps = []
    high_temps = []
    low_temps = []

    for details in data:
        mean_temps.append(float(details[2]))
        low_temps.append(float(details[3]))
        high_temps.append(float(details[4]))

    print("The average temperature for the 25 day period was", round(sum(mean_temps) / 25, 1))
    print("The average lowest temperature was", round(sum(low_temps) / 25, 1))
    print("The average highest temperature was", round(sum(high_temps) / 25, 1))

def number4(data):
    for details in data:
        day = (details[0])[-3:-1]
        month = (details[0])[-6:-4]
        temp = int(round(float(details[2]), 0))

        print_temperature_line(day, month, temp)

    print_temperature_axis()

while True:

    choice = input("ACME WEATHER DATA APP\n1) Choose weather data file\n2) See data for selected day\n3) Calculate average statistics for the data\n4) Print a scatterplot of the average temperatures\n0) Quit program\nChoose what to do: ")

    if choice == "0":
        break

    else:
        if choice == "1":
            number1(info)

        elif choice == "2":
            number2(info)

        elif choice == "3":
            number3(info)

        elif choice == "4":
            number4(info)

    print("")
