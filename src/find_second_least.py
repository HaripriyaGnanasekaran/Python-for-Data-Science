if __name__ == '__main__':
    pythonstudents = []
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pythonstudents.append([name, score])
        names.append(name)
        scores.append(score)

    for twice in range(1):
        minscore = min(scores)
        ids = [i for i in range(len(scores)) if scores[i]==minscore]
        counter=0
        for loop in ids:
            temp = loop-counter
            del scores[temp]
            del names[temp]
            counter+=1

    minscore=min(scores)
    ids = [i for i in range(len(scores)) if scores[i]==minscore]
    newnames=[]
    for loop in ids:
        newnames.append(names[loop])
    newnames = sorted(newnames)
    for nam in newnames:
        print(nam)
