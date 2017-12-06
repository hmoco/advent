banks = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
past = []
it = 0
def done():
    now = '-'.join([str(b) for b in banks])
    print now
    if now in past:
        return len(past) - past.index(now) 
    past.append(now)
    return False
count = 0
done_ = False
while not done_:
    big = banks.index(max(banks))
    to_dis = banks[big]
    banks[big] = 0
    n = big + 1
    while to_dis > 0:
        if n > 15:
            n = 0
        banks[n] = banks[n] + 1
        n += 1
        to_dis -= 1
    count += 1
    done_ = done()

print done_
print count

print count - done_
