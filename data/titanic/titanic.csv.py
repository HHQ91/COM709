import  csv

file_path = "titanic.csv"
records = []
try:
    print("Loading data....", end="")
    with open(file_path) as file:
        csv_reading = csv.reader(file)
        heading = next(csv_reading)
        count = 0
        for line in csv_reading:
            records.append(line)
        print("Done!")
        print(f"Successfully loaded {len(records)} records.")
        selection = int(input("""
          [1] Display the names of all passengers
          [2] Display the number of passengers that survived
          [3] Display the number of passengers per gender
          [4] Display the number of passengers per age group
          [5] Display the number of survivors per age group
                         """))

        print(f"You have selected the option {selection}")


        if selection == 1:
            print("The names of the passengers are...")
            for record in records:
                print(record[3])
        elif selection == 2:
            num_survived = 0
            for record in records:
                if record[1] == '1':
                    num_survived +=1

            print(f"{num_survived} passengers survived")
        elif selection == 3:
            females = 0
            males = 0
            for record in records:
                females += 1 if record[4] == "female" else 0
                males += 1 if record[4] == "male" else 0

            print(f"Females: {females}, males: {males}")

except IOError:
  print("Error returned")