# car X has 60 km/h
# car Y has 90 km/h
# distance = posY - posX
# distance = speedY * time - speedX * time
# time = distance / (speedY - speedX)
# time has units in hours
# so time = time * 60
# calculations complete here.

dist = int(input())

time = dist / (90-60)
time = time * 60
time = int(time)

print(str(time) + " minutos")

