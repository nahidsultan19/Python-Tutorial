passUni = 80
passColl = 70

def passExam(name, score):
    if score >= passUni:
        print(f'{name} Has enrolled in university with {score}  points')
    elif score >= passColl:
        print(f'{name} Has enrolled in college with {score} points')
    else:
        print(f'{name} has failed!')


def calcScore(quize, written):
    score = quize + written
    return score

passExam('Nahid', calcScore(40, 45))
passExam('Mahmud', calcScore(40, 50))
passExam('Tahan', calcScore(30, 40))