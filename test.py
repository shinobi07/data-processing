def print_temperature_line(day, month, temp):
    print(day + "." + month + " ", end = "")
    print("   "*(temp + 5) + "-", end = "")
    print()

def print_temperature_axis():
    print("      ", end="")
    for i in range(-5,16):
        print("{:02d} ".format(i), end="")
    print()

while True:

    choice = input("ACME WEATHER DATA APP\n1) Choose weather data file\n2) See data for selected day\n3) Calculate average statistics for the data\n4) Print a scatterplot of the average temperatures\n0) Quit program\nChoose what to do: ")

    if choice == "0":
        break

    else:
        if choice == "1":
            namefile = input("Give name of the file: ")
            dot = namefile.index(".")
            print("Loaded weather data from", namefile[:dot].capitalize())

        else:
            with open(namefile, "r") as readfile:
                readfile.readline()

                if choice == "2":
                    original = input("Give a date (dd.mm): ")
                    user_input = original.split(".")
                    date = user_input[1] + "-" + user_input[0]
                    for row in readfile:
                        row = row.strip()
                        details = row.split(";")
                        if date == (details[0])[6:11]:
                            print("The weather on %s was on average %s centigrade" % (original, details[2]))
                            print("The lowest temperature was %s and the highest temperature was %s" % (details[3], details[4]))
                            print("There was %s mm rain" % details[1])

                elif choice == "3":
                    mean_temps = []
                    high_temps = []
                    low_temps = []
                    for row in readfile:
                        row = row.strip()
                        details = row.split(";")
                        mean_temps.append(float(details[2]))
                        low_temps.append(float(details[3]))
                        high_temps.append(float(details[4]))
                    print("The average temperature for the 25 day period was", round(sum(mean_temps) / 25, 1))
                    print("The average lowest temperature was", round(sum(low_temps) / 25, 1))
                    print("The average highest temperature was", round(sum(high_temps) / 25, 1))

                elif choice == "4":
                    for row in readfile:
                        row = row.strip()
                        details = row.split(";")
                        day = (details[0])[-3:-1]
                        month = (details[0])[-6:-4]
                        temp = int(round(float(details[2]), 0))
                        print_temperature_line(day, month, temp)
                    print_temperature_axis()

    print("")
