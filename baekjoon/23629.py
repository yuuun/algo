s = input()
s = s.replace('ZERO', '0')
s = s.replace('ONE', '1')
s = s.replace('TWO', '2')
s = s.replace('THREE', '3')
s = s.replace('FOUR', '4')
s = s.replace('FIVE', '5')
s = s.replace('SIX', '6')
s = s.replace('SEVEN', '7')
s = s.replace('EIGHT', '8')
s = s.replace('NINE', '9')

print(s)
from string import digits
sign_str = s.translate(None, digits)
