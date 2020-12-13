(my_time_str, times_str) = open("data", "r").read().split('\n')
times = times_str.split(',')


data_mod = []
data_off = []

for (offset, time) in zip(range(1000), times):
    if time == 'x':
        continue
    data_mod.append(int(time))
    data_off.append(offset)

M = 1
for m in data_mod:
    M *= m

result = 0
for (i, m, o) in zip(range(100), data_mod, data_off):
    print(f"Processing {i} (m = {m}, o = {o})...")
    base = int(M / m)
    this_val = base
    supposed_to = 0
    if o > 0:
        supposed_to = m - o%m

    while this_val % m != supposed_to:
        this_val += base
        #print(f"\tthis_val = {this_val}")

    result += this_val

result %= M

print(result)

