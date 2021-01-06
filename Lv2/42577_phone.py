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

def solution3(phoneBook):
    #x의 길이로 sort하게 된다면 시간복잡도가 O(n^2)까지는 안 감
    phoneBook.sort(key=lambda x: len(x))
    for a in range(len(phoneBook)):
        for b in range(a+1, len(phoneBook)):
            if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
                return False
    return True


print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution2(['12','123','1235','567','88']))