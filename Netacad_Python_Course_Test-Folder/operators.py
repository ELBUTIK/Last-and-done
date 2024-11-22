


start_h = int(input('start time:'))
start_m = int(input('start minute:'))
dur = int(input('duration in minutes:'))



# start_m = ((start_m+dur) % 60)
start_m = start_m + dur
start_h = start_h + start_m // 60

print(start_h % 24,":",start_m % 60, sep='')


print(4%1)