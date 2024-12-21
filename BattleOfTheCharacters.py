def battle(x, y):
    score_x = sum(ord(char) - ord('A') + 1 for char in x)
    score_y = sum(ord(char) - ord('A') + 1 for char in y)
        
    if score_x > score_y:
        return x
    elif score_y > score_x:
        return y
    else:
        return "Tie!"