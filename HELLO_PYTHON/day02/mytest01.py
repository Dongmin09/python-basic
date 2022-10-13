# 첫 수를 넣으세요
# 끝 수를 넣으세요
# 1에서 4 까지의 합은 10입니다.



a= input("첫수를 넣으세요")
b= input(" 끝 수를 넣으세요")

aa = int(a)
bb = int(b)

sum = 0
for i in range(aa,bb+1):
        sum += i

print(aa,"에서",b,"까지의 합은",sum,"입니다.")
print("{}에서 {}까지의 합은 {} 입니다".format(aa, bb, sum))