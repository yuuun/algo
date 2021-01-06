def solution(phone_book):
    for idx1, phone in enumerate(phone_book):
        for idx2, phone_ in enumerate(phone_book):
            #접두어이기 때문에 phone == phone_[:len(phone)]
            if idx1 != idx2 and phone == phone_[:len(phone)]:
                return False
    return True

#hash map을 이용하여 작성하는 방법(코드 참조)
def solution2(phone_book):
    answer = True
    hash_map = {}
    #hash_map: 접두어로 하기 위함?
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            #자기자신과 겹치는 경우는 pass
            if temp in hash_map and temp != phone_number:
                 return False
    return answer


print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution2(['12','123','1235','567','88']))