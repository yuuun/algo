import re
def cal(op_p, values, ops):
    vals = [v for v in values]
    ops_list = [op for op in ops]
    print(op_p)
    for op_v in op_p:
        a = 0
        length = len(ops_list)
        for i in range(length):
            i -= a
            o = ops_list[i]
            print(op_v, "\t", o, "\t", i, "\t", ops_list)
            if op_v is o:
                #print(op_v, "\tbefore\t",vals, "\t", ops_list)
                vals[i+1] = cal_val(o, vals[i], vals[i+1])
                del ops_list[i]
                del vals[i]
                a += 1
                
                print(op_v, '\tafter\t', vals, "\t", ops_list)
            
    
    '''
    if len(vals) > 1:
        vals[0] = cal_val(ops_list[0], vals[0], vals[1])
        del vals[1]
    '''
    return vals[0]

        
def cal_val(op, val1, val2):
    if op is '+':
        return val1 + val2
    elif op is '-':
        return val1 - val2
    else:
        return val1 * val2
    
def solution(expression):
    print(expression)
    values = re.split('[*+\-]', expression)
    vals = []
    for v in values:
        vals.append(int(v))
    ops = re.split('[0-9]', expression)
    ops = [v for v in ops if v]
    
    op_list = ['*+-','*-+', '+*-', '+-*', '-*+', '-+*']
    ans_list = []
    for op_p in op_list:
        ans_list.append(abs(cal(op_p, vals, ops)))
    
    answer = max(ans_list)
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))