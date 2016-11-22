seconds = int(input())

# 1 hr = 60 * 60 seconds
# 1 min = 60 seconds
HR  = 60 * 60 
MIN = 60
SEC = 1

hr = 0
mn = 0
sc = 0


while(seconds >= HR):
	hr = hr + 1
	seconds = seconds - HR

while(seconds >= MIN):
        mn = mn + 1
        seconds = seconds - MIN

while(seconds >= SEC):
        sc = sc + 1
        seconds = seconds - SEC

print("%i:%i:%i" % (hr,mn,sc))
	
