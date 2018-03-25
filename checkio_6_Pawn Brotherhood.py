
def checkio(game_result):
    
    judge_result=""
    str=""
    
    for x in game_result:
        str += x
    print(str)
    
    #yoko
    x6 = str[0]+str[1]+str[2]
    x7 = str[3]+str[4]+str[5]
    x8 = str[6]+str[7]+str[8]
    #tate
    x1 = str[0]+str[3]+str[6]
    x2 = str[1]+str[4]+str[7]
    x3 = str[2]+str[5]+str[8]
    #naname
    x4 = str[0]+str[4]+str[8]
    x5 = str[2]+str[4]+str[6]

    if (x6 == "XXX" or x7 == "XXX" or x8 == "XXX") or (x1 == "XXX" or x2 == "XXX" or x3 == "XXX") or (x4 == "XXX" or x5 == "XXX"):
        judge_result="X"
    elif (x6 == "OOO" or x7 == "OOO" or x8 == "OOO") or (x1 == "OOO" or x2 == "OOO" or x3 == "OOO") or (x4 == "OOO" or x5 == "OOO"):
        judge_result="O"
    else:
        judge_result="D"

    return judge_result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

