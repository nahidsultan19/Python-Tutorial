def Exam(nahidScore, mamunScore, passed):
    if nahidScore >= passed and mamunScore >= passed:
        print('Both Students are Passed')
    elif nahidScore >= passed or mamunScore >= passed:
        print('Only one student passed')
        if nahidScore >= mamunScore:
            print(f'And it is Nahid with {nahidScore} points')
        else:
            print(f' and it is Mamun with {mamunScore} points')
    else:
        print('Both students failed')

Exam(80, 50, 60)