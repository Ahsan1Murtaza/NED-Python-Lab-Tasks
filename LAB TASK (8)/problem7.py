# 7.   Implement function cheer() that takes as input a team name (as a string) and prints a cheer as shown:

# >>> cheer('uitians')
# How do you spell winner? 
# I know, I know!
# U I T I A N S !
# And that's how you spell winner! 
# Go Uitians!

def cheer(team_name):
    team_name_upper=team_name.upper()
    print("How do you spell winner?\nI know, I know!")
    print(" ".join(team_name))
    print(f"And that's how you spell winner!\nGo {team_name.capitalize()}!")

cheer("uitians")