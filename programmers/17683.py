import math
dic = {'A#': '0', 'C#': '1', 'D#': '2', 
        'F#': '4', 'G#': '5'}
    
def convert_str(val):
    for key, value in dic.items():
        val = val.replace(key, value)
    return val

def solution(m, musicinfos):
    m = convert_str(m)
    ans = ["(None)", None]
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        sx, sy = map(int, start.split(':'))
        ex, ey = map(int, end.split(':'))
        time_lap = (ex - sx) * 60 + (ey - sy)
        music = convert_str(music)
        music = music * (time_lap // len(music)) + music[:time_lap % len(music)]
        
        if m in music:
            if ans[1] == None or time_lap > ans[1]:
                ans = (title, time_lap)
    return ans[0]
    
print(solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]),	"HELLO")
print(solution("CC#BCC#BCC#BCC#B",	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]),	"FOO")
print(solution("ABC",	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]),	"WORLD")
print(solution("CDEFGAC", ["12:00,12:06,HELLO,CDEFGA"]), '(None)')
print(solution('CCB', ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]), 'FOO')