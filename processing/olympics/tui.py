def started(msg=""):
    for x in range(85):
        print('_', end='')
    print(f"operation started: {msg}...\n")
    print ("Reading data from athlete_events.csv")
started("athlete_events")

def complete():
    print("operation complete")
    for x in range(85):
        print('_', end='')

def error(msg):
    print(f"Error!{msg}")

def menu():
    sel = input ("""
    please select one from the following options:
    [Years]       list unique years
    [tally]      Tally up medals
    [ctally]    Tally up medals for each team
    [exit]       Exit the program """)

    print (f"Your selection:{sel:10}")
menu()
def display_medal_tally(tally):


