
# найти сркдний бал и вывыести с точности до 10
bals = "3 3 2 4 4 5 4 3 2"
bals = bals.split()

#s = 0

#for x in bals:
#    s+= int(x)
#avg = s/ len(bals)

bals = [int(x) for x in bals]
print(sum(bals)/len(bals))

balls = " один один  два три"
balls = balls.split()
new_balls = []

for ball in balls:
    if ball == "один":
        new_balls.append(1)
    elif ball =="два":
        new_balls.append(2)
print(new_balls)

# +7(xxx)xxx-xx-xx
# +7(912)123-45-67

#сделать список (посимвольно) затем удалять первый + число 7 и заменит на 8 и убрать дефисф

tlf = "+7(913)123-45-67"
tlf = tlf.replace("+7","8").replace("-","")
tlf = list(tlf)
print(tlf)
tlf = "".join(tlf)

