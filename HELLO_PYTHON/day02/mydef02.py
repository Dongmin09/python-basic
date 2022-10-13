#
# def dan(a):
#     return a
#
# def su(a,dan):
#     return a*dan




# print("{}*{}={}".format(2,1,2*1))
# print("{}*{}={}".format(2,1,2*2))
# print("{}*{}={}".format(2,1,2*3))
# print("{}*{}={}".format(2,1,2*4))
# print("{}*{}={}".format(2,1,2*5))
# print("{}*{}={}".format(2,1,2*6))
# print("{}*{}={}".format(2,1,2*7))
# print("{}*{}={}".format(2,1,2*8))
# print("{}*{}={}".format(2,1,2*9))

for i in range(2,9+1):
    if i%2==1:
        continue
    for j in range(1,9+1):
        # if i%2==0 :
            print("{}*{}={}".format(i,j,i*j))