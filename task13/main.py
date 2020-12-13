(my_time_str, times_str) = open("data", "r").read().split('\n')
my_time = int(my_time_str)
times = list(map(int, times_str.replace(",x", "").split(',')))

def calculate_wait_time(time):
    t = 0
    while t < my_time:
        t += time
    
    return t - my_time

lowest_wait_time = 1000000000
bus_nr = -1
for time in times:
    wait_time = calculate_wait_time(time)
    if wait_time < lowest_wait_time:
        lowest_wait_time = wait_time
        bus_nr = time

print(lowest_wait_time, bus_nr, lowest_wait_time * bus_nr)