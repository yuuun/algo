#https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3974/
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        stext = []
        selse, sloc = [], []
        for idx, st in enumerate(s):
            if (ord(st) >= 97 and ord(st) <= 122) or (ord(st) >= 65 and ord(st) <= 90):
                stext.append(st)
            else:
                selse.append(st)
                sloc.append(idx)
        stext = stext[::-1]
        print(stext)
        tidx = 0
        eidx = 0
        ans = ''
        for i in range(len(s)):
            if eidx < len(sloc):
                if i == sloc[eidx]:
                    ans += selse[eidx]
                    eidx += 1
                else:
                    ans += stext[tidx]
                    tidx += 1
            else:
                ans += stext[tidx]
                tidx += 1
        return ans