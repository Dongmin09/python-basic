# 홀/짝을 입력하시오
# 나: 홀
# 컴 : 짝
# 결과 승리
from random import random

# user = input("홀짝을 입력하시오")
#
#
# com = int(random())
#
# comRan = range(0,1+1)
#
# if user == "홀" :
#     user = 0
# else :
#     user = 1
#
# if com < 0.5:
#     print("홀")
# else :
#     print("짝")
#
#
# if user == com:
#     print("승리")  
#
# else:
#     print("패배")  
    

# 선생님 풀이
mine = input("홀/짝을 입력하시오")    
com = ""
result = ""

rnd = random()
if rnd>0.5 :
    com = "홀"
else :
    com = "짝"

if com == mine:
    result = "승리"
else :
    result = "패배"
    
print("mine",mine)
print("com",com)
print("result",result)
