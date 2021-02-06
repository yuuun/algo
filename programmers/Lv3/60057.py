def solution(value):
    if len(value) == 1:
        return 1
    cut_list = [i for i in range(1, int(len(value)/2) + 1)]
    ans_list = []
    for cut in cut_list:
        value_list = []
        for idx in range(0, len(value), cut):
            value_list.append(value[idx:idx + cut])
        init = value_list[0]
        cnt = 1
        string = ''
        for val in value_list[1:]:
            if init == val:
                cnt += 1
            else:
                if cnt != 1:
                    string += str(cnt)
                string += init
                init = val
                cnt = 1
        if cnt != 1:
            string += str(cnt)
        string += init
        ans_list.append(len(string))
    return min(ans_list)
