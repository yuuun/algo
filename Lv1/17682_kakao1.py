def solution(dartResult):
    dartResult = list(dartResult)
    area = ['', 'S', 'D', 'T']
    score = []
    val = 0
    for dart in dartResult:
        if dart == '0' and val == 1:    #점수가 0-10이기 때문
            val = 10 
        elif dart.isdigit():
            val = int(dart)
        elif dart in area:
            score.append(val ** area.index(dart))
        elif dart == '*':
            score[-1] *= 2
            if len(score) >  1:
                score[-2] *= 2
        elif dart == '#':
            score[-1] *= -1

    return sum(score)



st = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
for s in st:
    print(solution(s))

