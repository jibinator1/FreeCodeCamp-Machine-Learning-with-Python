plays = {}

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    
    n = 3

    current = opponent_history
    guess = "R"

    if len(current) > n:
        recent = "".join(current[-(n):])
        if "".join(current[-(n+1):]) in plays.keys():
            plays["".join(current[-(n+1):])]+=1
        else:
            plays["".join(current[-(n+1):])] = 1

        for i in [(recent + "R"), (recent + "P"), (recent + "S")]:
            if i not in plays.keys():
                plays[i] = 0
        predict = max([(recent + "R"), (recent + "P"), (recent + "S")], key=lambda k: plays[k])
        if len(current) > 510 and len(current)< 512:
            print(plays)
        

        if predict[-1] == "P":
            guess = "S"
        elif predict[-1] == "R":
            guess = "P"
        elif predict[-1] == "S":
            guess = "R"

    return guess
