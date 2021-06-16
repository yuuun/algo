#undone
def solution(number, k):
    number = list(number)
    num_list = sorted(range(len(number)), key=lambda k : number[k], reverse=True)
    print(number)
    idx = 0
    answer = ''
    ans_list = []
    while k > num_list[idx]:
        ans_list.append(idx)
        answer += number[num_list[idx]]
        print(answer)

        idx += 1

if __name__=='__main__':
    solution("19242", 2)