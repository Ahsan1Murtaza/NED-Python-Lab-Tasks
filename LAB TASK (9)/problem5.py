# 5.   Write a program which will compare two sets, Set A and Set B. Both the sets have some students who love to play one is hockey and other one is cricket. 10 of them play both. Now using sets find how many of them are playing cricket only, if universal set is 40, students who play hockey are 21.


universal_set = set(range(1, 41))  # Universal set with 40 students
hockey_players = set(range(1, 22))  # 21 students play hockey
both_players = set(range(1, 11))    # 10 students play both hockey and cricket

# only hockey players
only_hockey_players=hockey_players-both_players

# cricket players
cricket_players=universal_set-only_hockey_players

# only cricket players
only_cricket_players=cricket_players-both_players
print(len(only_cricket_players))

