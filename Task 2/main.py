file = 'data_prog_contest_problem_2.txt'
with open(file) as f: 
    f.readline()
    ids = f.readline().split()
    codes = [int(ind) for ind in ids]
    alph = set()
    i = 0
    for code in codes: 
        if code >= 1 and code <= 26: 
            alph.add(code)
        print(f"итерация = {i}, множество {alph}")
        if len(alph) == 26:
            break
        i += 1
    print(f'Длина префикса: {i+1}')