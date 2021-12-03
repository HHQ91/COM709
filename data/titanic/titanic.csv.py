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

except IOError:
  print("Error returned")